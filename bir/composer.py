#!/usr/bin/env python3
r"""Compose en PDF les documents d'accompagnement du BIR écrits en Markdown.

    python composer.py                  tout composer
    python composer.py formateur        un seul document (voir DOCUMENTS)
    python composer.py --sans-compiler  n'écrire que les .tex

Sources : formateur/seance-NN.md, fiches/seance-NN-eleve.md,
fiches/seance-NN-encadrant.md, MODE-EMPLOI.md.
Sorties : pdf/livre-du-formateur.pdf, pdf/fiches-eleve.pdf,
pdf/fiches-encadrant.pdf, pdf/mode-emploi.pdf. Les .tex et les fichiers
auxiliaires vont dans build-docs/ ; ni l'un ni l'autre n'est suivi par git.

La mise en forme est celle de maquettes/BIRdoc.cls. Le Markdown reste la
SEULE source du texte : on ne retouche jamais les .tex produits.

Ce que le convertisseur comprend — et rien d'autre : titres # à ####,
paragraphes, listes à puces et numérotées (avec lignes de suite indentées),
tableaux, blocs de code, **gras**, *italique*, `code`, filets ---.
Conventions propres aux fiches : « ☐ » devient une case à cocher, une suite
de « … » une ligne pointillée à remplir, un bloc de code vide un cadre où
dessiner. Une construction non prévue ARRÊTE la conversion : mieux vaut une
erreur qu'une page fausse.

Version : v0.1 (30/09/2026).
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ICI = Path(__file__).resolve().parent
BUILD = ICI / "build-docs"
PDF = ICI / "pdf"

# Titres de niveau 2 dont le contenu va dans un encadré.
ENCADRES = {"Ce que l'élève doit emporter", "À retenir",
            "Savoir-faire à valider dans le livret"}
# Paragraphes en gras d'ouverture qui deviennent une alerte.
ALERTES = re.compile(
    r"^\*\*(Règles? du jour|Sécurité|Important|Aucune émission[^*]*|"
    r"Réception seulement|Ce qu'on écoute[^*]*)\s*[:.]?\*\*\s*")

SPECIAUX = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}
SYMBOLES = {
    "Ω": r"\ensuremath{\Omega}", "λ": r"\ensuremath{\lambda}",
    "≈": r"\ensuremath{\approx}", "÷": r"\ensuremath{\div}",
    "×": r"\ensuremath{\times}", "−": r"\ensuremath{-}",
    "→": r"\ensuremath{\rightarrow}", "↔": r"\ensuremath{\leftrightarrow}",
    "√": r"\ensuremath{\surd}", "²": r"\textsuperscript{2}",
    "›": r"\guilsinglright{}", "⎓": r"\BIRcontinu{}", "☐": r"\BIRcase{}",
}


class Erreur(SystemExit):
    pass


def echapper(s):
    return "".join(SPECIAUX.get(c, c) for c in s)


def code_en_ligne(s):
    """`code` : chasse fixe, coupures permises après / \\ . _ -"""
    out = []
    for c in s:
        # Les symboles absents de la police à chasse fixe (☐, Ω…) passent
        # par leur macro, comme dans le texte courant.
        out.append(SPECIAUX.get(c) or SYMBOLES.get(c, c))
        if c in "/\\._-":
            out.append(r"\allowbreak{}")
    return r"\BIRcode{" + "".join(out) + "}"


def pointilles(texte, en_cellule):
    """Suites de « … » -> lignes à remplir."""
    def une(m):
        n = len(m.group(0))
        fin = m.end() == len(texte.rstrip())
        # En fin de texte, la ligne va jusqu'à la marge : c'est là qu'on
        # écrit le plus. Ailleurs, sa longueur suit celle de la source.
        if en_cellule or fin:
            return r"\BIRfin{}"
        return r"\BIRligne[%dmm]" % min(110, max(16, round(n * 2.6)))
    return re.sub(r"…{3,}", une, texte)


def en_ligne(s, en_cellule=False):
    """Markdown en ligne -> LaTeX."""
    # Ce qui est déjà du LaTeX (code en ligne, lignes pointillées) est mis de
    # côté sous forme de jetons, pour échapper à l'échappement — et pour
    # qu'un gras puisse enjamber un `code`.
    jetons = []

    def jeton(tex):
        jetons.append(tex)
        return "\x00%d\x00" % (len(jetons) - 1)

    m = re.sub(r"`([^`]*)`", lambda x: jeton(code_en_ligne(x.group(1))), s)
    if "`" in m:
        raise Erreur(f"!! accent grave non apparié : {s[:80]}")
    m = pointilles(m, en_cellule)
    m = re.sub(r"\\BIRligne\[\d+mm\]|\\BIRfin\{\}", lambda x: jeton(x.group(0)), m)
    m = echapper(m)
    m = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", m)
    m = re.sub(r"(?<![*\w])\*([^*\s][^*]*?)\*(?![*\w])", r"\\emph{\1}", m)
    if "*" in m:
        raise Erreur(f"!! astérisque non apparié : {s[:80]}")
    for car, tex in SYMBOLES.items():
        m = m.replace(car, tex)
    return re.sub("\x00(\\d+)\x00", lambda x: jetons[int(x.group(1))], m)


def texte_nu(s):
    """Longueur utile d'une cellule : sans balisage."""
    s = re.sub(r"[`*]", "", s)
    return re.sub(r"…{3,}", "", s).strip()


# --------------------------------------------------------------------------
# Blocs
# --------------------------------------------------------------------------

def lire_blocs(lignes, fichier):
    """Découpe en blocs : (genre, contenu)."""
    blocs, i, n = [], 0, len(lignes)
    while i < n:
        l = lignes[i]
        if not l.strip():
            i += 1
            continue
        if l.startswith("```"):
            j = i + 1
            while j < n and not lignes[j].startswith("```"):
                j += 1
            if j >= n:
                raise Erreur(f"!! {fichier} : bloc de code non fermé, ligne {i + 1}")
            blocs.append(("code", lignes[i + 1:j]))
            i = j + 1
            continue
        m = re.match(r"^(#{1,4}) (.*)$", l)
        if m:
            blocs.append(("h%d" % len(m.group(1)), m.group(2).strip()))
            i += 1
            continue
        if re.match(r"^---+\s*$", l):
            blocs.append(("filet", None))
            i += 1
            continue
        if l.startswith("|"):
            j = i
            while j < n and lignes[j].startswith("|"):
                j += 1
            blocs.append(("tableau", lignes[i:j]))
            i = j
            continue
        m = re.match(r"^([-*]|\d+\.) ", l)
        if m:
            ordonnee = m.group(1)[0].isdigit()
            motif = r"^\d+\. " if ordonnee else r"^[-*] "
            items = []
            while i < n:
                if re.match(motif, lignes[i]):
                    items.append([re.sub(motif, "", lignes[i])])
                    i += 1
                elif lignes[i].startswith("  ") and lignes[i].strip():
                    items[-1].append(lignes[i].strip())
                    i += 1
                elif (not lignes[i].strip() and i + 1 < n
                      and (re.match(motif, lignes[i + 1])
                           or (lignes[i + 1].startswith("  ") and lignes[i + 1].strip()))):
                    # ligne vide à l'intérieur de la liste
                    if lignes[i + 1].startswith("  "):
                        items[-1].append("")
                    i += 1
                else:
                    break
            blocs.append(("liste-num" if ordonnee else "liste", items))
            continue
        if l.startswith(">") or l.startswith("<") or l.startswith("    "):
            raise Erreur(f"!! {fichier} : construction non prévue, ligne {i + 1} : {l[:60]}")
        j = i
        while (j < n and lignes[j].strip()
               and not re.match(r"^(#{1,4} |```|\||[-*] |\d+\. |---+\s*$)", lignes[j])):
            j += 1
        blocs.append(("para", " ".join(x.strip() for x in lignes[i:j])))
        i = j
    return blocs


def rendre_liste(items, ordonnee):
    env = "enumerate" if ordonnee else "itemize"
    out = [r"\begin{%s}" % env]
    for it in items:
        paras, cour = [], []
        for ligne in it:
            if ligne == "":
                paras.append(" ".join(cour))
                cour = []
            else:
                cour.append(ligne)
        paras.append(" ".join(cour))
        out.append(r"\item " + "\n\n".join(en_ligne(p) for p in paras if p))
    out.append(r"\end{%s}" % env)
    return "\n".join(out)


def rendre_tableau(lignes, fichier):
    rangs = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lignes]
    if len(rangs) < 2 or not re.match(r"^[-: ]+$", "".join(rangs[1])):
        raise Erreur(f"!! {fichier} : tableau sans ligne de séparation : {lignes[0][:60]}")
    tete, corps = rangs[0], rangs[2:]
    nc = len(tete)
    for r in corps:
        if len(r) != nc:
            raise Erreur(f"!! {fichier} : tableau à {nc} colonnes, ligne à {len(r)} : {r}")
    cellules = sum(len(r) for r in corps) or 1
    vides = sum(1 for r in corps for c in r if not texte_nu(c))
    a_remplir = vides / cellules >= 0.25

    # Largeur utile de chaque colonne, en caractères.
    besoin, moyenne = [], []
    for k in range(nc):
        donnees = [len(texte_nu(r[k])) for r in corps]
        mot = max((len(w) for w in texte_nu(tete[k]).split()), default=0)
        besoin.append(max(max(donnees, default=0), mot))
        moyenne.append(sum(donnees) / max(1, len(donnees)))
    pleines = [any(texte_nu(r[k]) for r in corps) for k in range(nc)]
    if a_remplir and not all(pleines):
        # Tableau à remplir : les colonnes déjà écrites (les libellés) prennent
        # la place qu'il leur faut, les colonnes vides se partagent le reste.
        etroites = list(pleines)
        besoin = [min(b, 30) for b in besoin]
    else:
        etroites = [b <= 15 and p for b, p in zip(besoin, pleines)]
    if all(etroites):
        etroites[besoin.index(max(besoin))] = False
    poids = [max(10.0, min(60.0, m if m else 25.0)) for m in moyenne]
    somme = sum(p for p, e in zip(poids, etroites) if not e)
    nx = etroites.count(False)
    cols = []
    for k in range(nc):
        if etroites[k]:
            cols.append("P{%dmm}" % round(besoin[k] * 1.75 + 3))
        else:
            cols.append(r">{\hsize=%.3f\hsize\raggedright\arraybackslash}X" % (poids[k] * nx / somme))
    if a_remplir:
        spec = "|" + "|".join(cols) + "|"
        fin_rang, debut_rang = r" \\ \hline", r"\BIRhaut "
        tete_tex = r"\hline\BIRentete "
    else:
        spec = "".join(cols)
        fin_rang, debut_rang = r" \\", ""
        tete_tex = r"\BIRentete "

    def cap(s):
        return s[:1].upper() + s[1:]
    out = [r"{\small\begin{tabularx}{\linewidth}{%s}" % spec,
           tete_tex + " & ".join(r"\BIRth{%s}" % en_ligne(cap(c), True) for c in tete) + fin_rang]
    for r in corps:
        out.append(debut_rang + " & ".join(en_ligne(c, True) for c in r) + fin_rang)
    if not a_remplir:
        out.append(r"\bottomrule")
    out.append(r"\end{tabularx}}\par\vspace{3pt}")
    return "\n".join(out)


def rendre_code(corps):
    if all(not x.strip() for x in corps):
        return r"\BIRcadrevide{%dmm}" % (7 * max(3, len(corps)))
    largeur = max(len(x) for x in corps)
    taille = r"\footnotesize" if largeur <= 100 else r"\scriptsize"
    if any("\\end{Verbatim}" in x for x in corps):
        raise Erreur("!! bloc de code contenant \\end{Verbatim}")
    return ("\\begin{Verbatim}[fontsize=%s,frame=leftline,framerule=1.5pt,"
            "rulecolor=\\color{BIRbleu},framesep=6pt]\n%s\n\\end{Verbatim}"
            % (taille, "\n".join(corps)))


def rendre_corps(blocs, fichier):
    """Blocs (hors titre de niveau 1) -> LaTeX."""
    out, i, n = [], 0, len(blocs)
    while i < n:
        genre, c = blocs[i]
        if genre == "h2":
            if c in ENCADRES:
                j = i + 1
                while j < n and blocs[j][0] not in ("h1", "h2"):
                    j += 1
                out.append(r"\begin{BIRencadre}{%s}" % en_ligne(c))
                out.append(rendre_corps(blocs[i + 1:j], fichier))
                out.append(r"\end{BIRencadre}")
                i = j
                continue
            out.append(r"\section*{%s}" % en_ligne(c))
        elif genre == "h3":
            out.append(r"\subsection*{%s}" % en_ligne(c))
        elif genre == "h4":
            out.append(r"\paragraph{%s}" % en_ligne(c))
        elif genre == "h1":
            raise Erreur(f"!! {fichier} : second titre de niveau 1 : {c}")
        elif genre == "para":
            m = ALERTES.match(c)
            if m:
                reste = c[m.end():]
                out.append(r"\begin{BIRalerte}{%s}" % en_ligne(m.group(1)))
                if reste:
                    out.append(en_ligne(reste[:1].upper() + reste[1:]))
                if (reste.rstrip().endswith(":") or not reste) and i + 1 < n \
                        and blocs[i + 1][0] in ("liste", "liste-num"):
                    out.append(rendre_liste(blocs[i + 1][1], blocs[i + 1][0] == "liste-num"))
                    i += 1
                out.append(r"\end{BIRalerte}")
            else:
                out.append(en_ligne(c) + "\n")
        elif genre in ("liste", "liste-num"):
            out.append(rendre_liste(c, genre == "liste-num"))
        elif genre == "tableau":
            out.append(rendre_tableau(c, fichier))
        elif genre == "code":
            out.append(rendre_code(c))
        elif genre == "filet":
            out.append(r"\par\medskip{\color{BIRbleu!40}\hrule}\medskip")
        i += 1
    return "\n\n".join(out)


def convertir(chemin):
    """Un fichier Markdown -> (titre, sous-titre, corps LaTeX)."""
    blocs = lire_blocs(chemin.read_text(encoding="utf-8").splitlines(), chemin.name)
    if not blocs or blocs[0][0] != "h1":
        raise Erreur(f"!! {chemin.name} : le fichier doit commencer par un titre « # »")
    titre = blocs[0][1]
    reste = blocs[1:]
    sous_titre = ""
    if reste and reste[0][0] == "para" and len(reste[0][1]) <= 110 \
            and not reste[0][1].startswith("**"):
        sous_titre = reste[0][1]
        reste = reste[1:]
    return titre, sous_titre, rendre_corps(reste, chemin.name)


# --------------------------------------------------------------------------
# Documents
# --------------------------------------------------------------------------

def court(titre):
    """« Séance 8 — Le spectre et les bandes » -> la partie après le tiret."""
    return titre.split(" — ", 1)[1] if " — " in titre else titre


def couverture(titre, sous_titre, lignes):
    return "\n".join([
        r"\thispagestyle{empty}", r"\vspace*{35mm}",
        r"{\sffamily\bfseries\fontsize{30}{36}\selectfont\color{BIRbleu}Brevet d'Initiation\\ à la Radio\par}",
        r"\vspace{3mm}{\color{BIRrouge}\rule{50mm}{1.2pt}\par}\vspace{6mm}",
        r"{\sffamily\fontsize{20}{24}\selectfont %s\par}" % en_ligne(titre),
        r"\vspace{4mm}{\sffamily\large %s\par}" % en_ligne(sous_titre),
        r"\vfill", lignes, r"\clearpage",
    ])


def assembler(nom, type_doc, fichiers, titre_couv=None, sous_titre_couv="", feuille=False):
    """Écrit build-docs/<nom>.tex.

    feuille=True : chaque fichier commence sur une NOUVELLE FEUILLE (page
    impaire), pour que des fiches imprimées recto verso restent séparables.
    """
    parties = [r"\documentclass{BIRdoc}", r"\begin{document}"]
    if titre_couv:
        parties.append(r"\BIRdocument{%s}{}" % en_ligne(type_doc))
        parties.append(couverture(titre_couv, sous_titre_couv,
                                  r"{\small\tableofcontents}"))
    for k, f in enumerate(fichiers):
        titre, sous_titre, corps = convertir(f)
        if f.name.endswith("-encadrant.md"):
            # « Fiche nº 4 — côté encadrant » : on reprend le nom de
            # l'activité dans la fiche de l'élève, plus parlant.
            eleve = f.with_name(f.name.replace("-encadrant.md", "-eleve.md"))
            nom_activite = court(convertir(eleve)[0])
            titre = titre.split(" — ")[0] + " — " + nom_activite
            sous_titre = "Côté encadrant · " + sous_titre
        if k or titre_couv:
            parties.append(r"\BIRfeuille" if feuille else r"\clearpage")
        entete = type_doc
        m = re.match(r"^Fiche nº (\d+)", titre)
        if m:
            entete = "%s nº %s" % (type_doc, m.group(1))
        parties.append(r"\BIRdocument{%s}{%s}" % (en_ligne(entete), en_ligne(court(titre) if len(fichiers) > 1 else "")))
        if titre_couv:
            parties.append(r"\addcontentsline{toc}{subsection}{%s}" % en_ligne(titre))
        parties.append(r"\BIRtitre{%s}{%s}" % (en_ligne(court(titre) if m else titre), en_ligne(sous_titre)))
        parties.append(corps)
    parties.append(r"\end{document}")
    BUILD.mkdir(exist_ok=True)
    (BUILD / f"{nom}.tex").write_bytes(("\n\n".join(parties) + "\n").encode("utf-8"))
    return len(fichiers)


def fichiers_tries(dossier, motif):
    return sorted((ICI / dossier).glob(motif))


DOCUMENTS = {
    "formateur": lambda: assembler(
        "livre-du-formateur", "Livre du formateur",
        fichiers_tries("formateur", "seance-*.md"),
        titre_couv="Livre du formateur",
        sous_titre_couv="Les 24 séances, une à une"),
    "fiches-eleve": lambda: assembler(
        "fiches-eleve", "Fiche d'activité",
        fichiers_tries("fiches", "seance-*-eleve.md"),
        titre_couv="Fiches d'activité",
        sous_titre_couv="Fiches de l'élève, à imprimer recto verso",
        feuille=True),
    "fiches-encadrant": lambda: assembler(
        "fiches-encadrant", "Fiche d'activité, côté encadrant",
        fichiers_tries("fiches", "seance-*-encadrant.md"),
        titre_couv="Fiches d'activité",
        sous_titre_couv="Côté encadrant"),
    "mode-emploi": lambda: assembler(
        "mode-emploi", "Mode d'emploi", [ICI / "MODE-EMPLOI.md"]),
    "referentiel": lambda: assembler(
        "referentiel", "Référentiel", [ICI / "referentiel.md"]),
}
SORTIES = {"formateur": "livre-du-formateur", "fiches-eleve": "fiches-eleve",
           "fiches-encadrant": "fiches-encadrant", "mode-emploi": "mode-emploi",
           "referentiel": "referentiel"}


def compiler(nom):
    env_tex = str(ICI / "maquettes") + ";"
    import os
    env = dict(os.environ, TEXINPUTS=env_tex + os.environ.get("TEXINPUTS", ""))
    r = subprocess.run(
        ["latexmk", "-lualatex", "-interaction=nonstopmode", "-halt-on-error", f"{nom}.tex"],
        cwd=BUILD, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (BUILD / f"{nom}-console.txt").write_bytes(r.stdout)
    if r.returncode != 0:
        print(f"!! {nom} : échec de compilation — voir build-docs/{nom}.log", file=sys.stderr)
        return False
    journal = (BUILD / f"{nom}.log").read_text(encoding="utf-8", errors="replace")
    pages = re.search(r"Output written on .*?\((\d+) pages?", journal)
    PDF.mkdir(exist_ok=True)
    (PDF / f"{nom}.pdf").write_bytes((BUILD / f"{nom}.pdf").read_bytes())
    print(f"   {nom}.pdf : {pages.group(1) if pages else '?'} pages"
          f" · débordements {journal.count('Overfull')}"
          f" · caractères manquants {journal.count('Missing character')}")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("documents", nargs="*",
                    help="parmi : " + ", ".join(DOCUMENTS) + " (défaut : tous)")
    ap.add_argument("--sans-compiler", action="store_true")
    args = ap.parse_args()
    inconnus = [d for d in args.documents if d not in DOCUMENTS]
    if inconnus:
        raise Erreur(f"!! document inconnu : {', '.join(inconnus)}")
    ok = True
    for cle in args.documents or list(DOCUMENTS):
        n = DOCUMENTS[cle]()
        print(f"{cle} : {n} fichier(s) convertis -> build-docs/{SORTIES[cle]}.tex")
        if not args.sans_compiler:
            ok = compiler(SORTIES[cle]) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
