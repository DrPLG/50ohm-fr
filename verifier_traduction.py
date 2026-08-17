#!/usr/bin/env python3
r"""
verifier_traduction.py — Mécanise les huit contrôles du §5 de CLAUDE.md.

Le §5 impose, avant toute compilation, huit contrôles sur une section traduite
face à son original allemand. Ils étaient jusqu'ici passés à l'œil, section par
section. Sur 22 sections resynchronisées le 16/08/2026, c'est ingérable — et
c'est précisément à ce moment qu'un défaut passe.

CE QUE LE SCRIPT A TROUVÉ LE JOUR OÙ IL A ÉTÉ ÉCRIT. `digital_analog_umsetzer`
annonçait un pas de quantification de 6,25 mV au lieu de 67 mV environ, avait
perdu la phrase d'avertissement de l'amont (« avec 16 échelons, il n'y a que
15 pas intermédiaires ») et traduisait *Zwischenschritte* par « échelons ». La
section était dans le livre A depuis des semaines et avait été relue.

LES HUIT CONTRÔLES, dans l'ordre du tableau du §5 :

  1. marqueurs DARCdown  — nombre, nature ET ORDRE identiques à l'amont ;
  2. formules $…$        — verbatim, SAUF les mots allemands qui s'y trouvent ;
  3. séparateurs ---     — même nombre ;
  4. puces et tableaux   — même nombre de lignes ;
  5. commentaires %      — même nombre, préservés verbatim ;
  6. légendes            — aucun « : », qui ferait disparaître la figure ;
  7. accents             — aucun accent NU en mode mathématique ;
  8. germanismes         — sonde sur le texte français.

TROIS PRÉCAUTIONS, chacune payée par un faux positif :

  - les blocs <france>…</france> sont RETIRÉS avant toute comparaison : ce sont
    des compléments nationaux ajoutés (§7), sans équivalent amont par
    construction ;
  - les LÉGENDES de [picture:], [photo:] et [table:], ainsi que le contenu de
    [index:], sont du texte destiné au lecteur : ils DOIVENT être traduits, et
    ne sont donc pas comparés ;
  - les formules sont comparées après neutralisation du contenu de \text{},
    \mathrm{} et consorts — le §5 autorise explicitement d'y traduire les mots
    allemands.

TROIS LIMITES, à connaître avant de se fier à un rc=0 :

  - **le script ne voit pas une prose périmée.** Si l'amont réécrit un
    paragraphe sans toucher aux marqueurs ni aux formules, la section passe au
    vert alors que la traduction est en retard. Sur les 21 sections en retard
    du 16/08, il en a signalé 19 ; `kabeldaempfung_2`, dont l'amont n'avait
    changé que deux phrases, lui était invisible. C'est `verifier_amont.py` qui
    détecte ce cas, par empreinte — les deux outils sont complémentaires, aucun
    ne remplace l'autre ;
  - **un ajout français hors encart `<france>` est signalé comme un écart.**
    Deux cas connus au dépôt, tous deux légitimes : un <tip> dans
    `elektrische_geaete_oeffnen_2` et un <indepth> dans `transverter_2`. Ils
    figurent au §9 de CLAUDE.md comme à regarder un jour ;
  - **une GLOSE allemande volontaire est prise pour un germanisme.** Le corpus
    cite délibérément le terme allemand entre parenthèses — « le circuit
    bouchon (Sperrkreis) », « bloqueur d'ondes de gaine (Mantelwellensperre) ».
    Dans `q_schluessel`, le mot allemand porte même le moyen mnémotechnique :
    « grande puissance (gr*o*ße Leistung) » explique le O de QRO, et le
    retirer détruirait l'astuce. Ces cas sont à confirmer à l'œil, pas à
    corriger d'office.

Les DÉROGATIONS assumées sont listées plus bas et rapportées comme telles :
elles s'affichent, mais n'influencent pas le code de retour.

ÉTAT DU CORPUS AU 17/08/2026, mesuré : sur 386 sections, **345 conformes,
2 dérogations, 39 écarts**. Les 39 sont PRÉEXISTANTS et n'ont pas été
analysés — 25 en classe N, 7 en E, 7 en A. Ils relèvent pour l'essentiel des
trois limites ci-dessus, mais pas tous : `antennen` (N) a bel et bien perdu un
commentaire amont, ce que le §6 interdit. Le script sort donc en rc=1 sur le
dépôt entier ; c'est un état de fait à réduire, pas un défaut de l'outil.

Usage :
    python verifier_traduction.py --amont <chemin>/50ohm-contents-dl-main A
    python verifier_traduction.py --amont <chemin> A swr_meter_2 traps
    python verifier_traduction.py --amont <chemin> --tout

Code de retour : 1 si au moins un contrôle échoue, 0 sinon — même convention
que verifier_amont.py et sonde_dessins.py.

Licence des contenus : CC BY 4.0 — 50ohm.de-Autorenteam / DARC e. V.

Version : v0.1 (17/08/2026) — écrit pendant la resynchronisation amont
(feuille d'arbitrage nº 5), versé au dépôt sur décision de Pierre.
"""
import argparse
import pathlib
import re
import sys
import unicodedata

CLASSES = ("N", "E", "A")

# Balises DARCdown reconnues par le parseur amont (renderer/tag.py), plus
# <france>, qui est notre ajout.
BALISES = ("margin|indepth|webmargin|warning|attention|tip|webtip|webindepth|"
           "person|fullwidth|unit|danger|webonly|latexonly|wordorigin|note|"
           "fragment|left|right|qso|france")

MARQUEUR = re.compile(r"\[(\w+):([^\]]*)\]|</?(" + BALISES + r")>")
FORMULE = re.compile(r"(?<!\$)\$([^$]+)\$(?!\$)")
LIGNE_COMMENTEE = re.compile(r"^\s*%")
PUCE = re.compile(r"^\s*[*-]\s+")
LIGNE_TABLEAU = re.compile(r"^\s*\|")
# Le contenu de ces macros est du texte : il a le droit de changer.
TEXTE_EN_MATHS = re.compile(r"\\(mathrm|text|textrm|mathit|operatorname)\{[^{}]*\}")

# Sonde anti-germanisme. Tout mot également français en est EXCLU — « des » y
# figurait et produisait un faux positif sur chaque section. Même raison que
# les retraits de « Signal », « Filter » et « Band » dans sonde_dessins.py :
# un mot commun aux deux langues ne mesure rien.
ALLEMAND = re.compile(
    r"\b(?:der|die|das|dem|den|ein|eine|einer|einem|einen|und|oder|aber|"
    r"nicht|auch|noch|schon|wird|werden|wurde|kann|können|muss|müssen|ist|"
    r"sind|war|waren|hat|haben|sich|beim|zum|zur|vom|durch|über|unter|"
    r"zwischen|Spannung|Strom|Widerstand|Leistung|Frequenz|Welle|Wellen|"
    r"Leitung|Schaltung|Antenne[nr]|Abbildung|Beispiel|Klasse)\b")

# Écarts VOULUS, décidés et documentés. Affichés, mais sans effet sur le rc.
# Les retirer d'ici si la raison disparaît — ce n'est pas une liste d'excuses.
DEROGATIONS = {
    ("A", "elektrische_verlaengerung_verkuerzung"):
        "légende du dessin 650 écrite \\frac{5}{8} là où l'amont écrit "
        "\\qty{5}{8}, qui compose « 58λ » (defauts-amont.md §6)",
    ("A", "strom_spannung_speisung_2"):
        "renvoi a_stromverteilungen adopté avec la figure ; l'amont n'a "
        "renommé que la figure et son renvoi pend en classe A "
        "(defauts-amont.md §10)",
    ("A", "mantelwellen_2"):
        "$m$ au lieu de $ü$ : un accent nu en mode mathématique disparaît du "
        "PDF (CLAUDE.md §6)",
    ("A", "antennenformen_3"): "idem $ü$ -> $m$",
    ("A", "brueckengleichrichter"): "idem $ü$ -> $m$",
}


def sans_commentaires(lignes):
    return [l for l in lignes if not LIGNE_COMMENTEE.match(l)]


def sans_encarts_france(texte):
    """Retire les blocs <france>…</france>, compléments nationaux du §7."""
    return re.sub(r"<france>.*?</france>", "", texte, flags=re.S)


def marqueurs(texte):
    """Suite ORDONNÉE des marqueurs, hors lignes commentées.

    Seule l'identité de l'objet est retenue : la légende d'une figure ou d'un
    tableau, comme le libellé d'une entrée d'index, est du texte à traduire.
    """
    suite = []
    for ligne in sans_commentaires(texte.splitlines()):
        for m in MARQUEUR.finditer(ligne):
            if m.group(3):
                suite.append(f"<{m.group(3)}>")
                continue
            typ, arg = m.group(1), m.group(2)
            if typ in ("picture", "photo"):
                arg = ":".join(arg.split(":")[:2])
            elif typ == "table":
                arg = arg.split(":")[0]
            elif typ == "index":
                arg = ""
            suite.append(f"[{typ}:{arg}]")
    return suite


def formules(texte):
    """Formules d'un texte, normalisées pour la comparaison.

    Deux normalisations, et deux seulement :

      - le contenu de \\text{}, \\mathrm{} et consorts est neutralisé : le §5
        autorise explicitement d'y traduire les mots allemands ;
      - « ü » devient « m ». C'est le rapport de transformation d'un
        transformateur (*Übersetzungsverhältnis*), que l'amont note « ü ». Un
        accent NU en mode mathématique disparaît du PDF (§6) : le lecteur
        allemand lit « = 1:7 », sans symbole. Décision de Pierre du 15/08/2026,
        appliquée à tout le corpus — d'où sa place ici plutôt que dans la liste
        des dérogations, qu'elle remplirait de vingt entrées identiques.
    """
    return [TEXTE_EN_MATHS.sub(r"\\\1{}", m.group(1)).replace("ü", "m")
            for l in sans_commentaires(texte.splitlines())
            for m in FORMULE.finditer(l)]


def controler(racine, classe, ident, amont):
    """Renvoie la liste des anomalies ; vide = tout va bien."""
    f_fr = racine / "traductions" / classe / "sections" / f"{ident}.md"
    f_de = amont / "contents" / "sections" / f"{ident}.md"
    if not f_fr.is_file():
        return [f"traduction absente : {f_fr}"]
    if not f_de.is_file():
        return [f"amont absent (section supprimée en amont ?) : {f_de}"]

    fr = sans_encarts_france(f_fr.read_text(encoding="utf-8"))
    de = f_de.read_text(encoding="utf-8")
    pb = []

    m_fr, m_de = marqueurs(fr), marqueurs(de)
    if m_fr != m_de:
        pb.append("marqueurs DARCdown différents")
        for i in range(max(len(m_fr), len(m_de))):
            a = m_de[i] if i < len(m_de) else "—"
            b = m_fr[i] if i < len(m_fr) else "—"
            if a != b:
                pb.append(f"    rang {i} : amont {a!r} / français {b!r}")

    f_de_l, f_fr_l = formules(de), formules(fr)
    if f_de_l != f_fr_l:
        for x in [x for x in f_de_l if x not in f_fr_l]:
            pb.append(f"formule perdue  : ${x}$")
        for x in [x for x in f_fr_l if x not in f_de_l]:
            pb.append(f"formule ajoutée : ${x}$")

    n_de = sum(1 for l in sans_commentaires(de.splitlines()) if l.strip() == "---")
    n_fr = sum(1 for l in sans_commentaires(fr.splitlines()) if l.strip() == "---")
    if n_de != n_fr:
        pb.append(f"séparateurs --- : amont {n_de}, français {n_fr}")

    for nom, motif in (("puces", PUCE), ("lignes de tableau", LIGNE_TABLEAU)):
        a = sum(1 for l in sans_commentaires(de.splitlines()) if motif.match(l))
        b = sum(1 for l in sans_commentaires(fr.splitlines()) if motif.match(l))
        if a != b:
            pb.append(f"{nom} : amont {a}, français {b}")

    # Les blocs commentés allemands sont préservés VERBATIM (§6), %TODO
    # compris. On montre lesquels diffèrent : un compte seul n'est pas
    # actionnable, et le cas « même nombre, contenu changé » existe.
    c_de = [l.strip() for l in de.splitlines() if LIGNE_COMMENTEE.match(l)]
    c_fr = [l.strip() for l in fr.splitlines() if LIGNE_COMMENTEE.match(l)]
    if c_de != c_fr:
        pb.append(f"commentaires % : amont {len(c_de)}, français {len(c_fr)}"
                  f" — préservés verbatim (§6)")
        for x in [c for c in c_de if c not in c_fr]:
            pb.append(f"    perdu   : {x[:110]}")
        for x in [c for c in c_fr if c not in c_de]:
            pb.append(f"    ajouté  : {x[:110]}")

    for l in sans_commentaires(fr.splitlines()):
        for m in re.finditer(r"\[(?:picture|photo):([^\]]*)\]", l):
            parts = m.group(1).split(":", 2)
            if len(parts) == 3 and ":" in parts[2]:
                pb.append(f"légende avec « : » (figure {parts[0]}) — la figure "
                          f"disparaîtrait sans erreur : {parts[2]!r}")

    # Un accent NU en mode mathématique disparaît du PDF (§6) ; dans \text{} ou
    # \mathrm{}, il passe sans dommage — établi le 14/08/2026 par extraction.
    for l in sans_commentaires(fr.splitlines()):
        for m in FORMULE.finditer(l):
            reste = TEXTE_EN_MATHS.sub("", m.group(1))
            nus = {c for c in reste
                   if ord(c) > 127 and unicodedata.category(c).startswith("L")}
            if nus:
                pb.append(f"accent NU en mode mathématique ({''.join(sorted(nus))})"
                          f" — disparaît du PDF sans erreur : ${m.group(1)}$")

    # Formules retirées avant la sonde : sans cela, le « hat » de \hat{U} est
    # compté comme allemand.
    nu = FORMULE.sub(" ", MARQUEUR.sub("", "\n".join(sans_commentaires(fr.splitlines()))))
    restes = sorted(set(ALLEMAND.findall(nu)))
    if restes:
        pb.append(f"germanismes possibles : {', '.join(restes)}")

    return pb


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classe", nargs="?", choices=CLASSES,
                    help="classe à vérifier (omise avec --tout)")
    ap.add_argument("idents", nargs="*",
                    help="sections à vérifier (défaut : toutes celles de la classe)")
    ap.add_argument("--amont", required=True,
                    help="racine de 50ohm-contents-dl (amont).")
    ap.add_argument("--racine", default=None,
                    help="racine du dépôt (défaut : le répertoire de ce script)")
    ap.add_argument("--tout", action="store_true",
                    help="les trois classes, toutes leurs sections")
    args = ap.parse_args()

    racine = pathlib.Path(args.racine).resolve() if args.racine \
        else pathlib.Path(__file__).resolve().parent
    amont = pathlib.Path(args.amont)
    if not (amont / "contents" / "sections").is_dir():
        sys.exit(f"amont introuvable : {amont}\\contents\\sections")

    if args.tout:
        travail = [(c, p.stem)
                   for c in CLASSES
                   for p in sorted((racine / "traductions" / c / "sections").glob("*.md"))]
    elif not args.classe:
        ap.error("préciser une classe, ou --tout")
    else:
        idents = args.idents or [
            p.stem for p in
            sorted((racine / "traductions" / args.classe / "sections").glob("*.md"))]
        travail = [(args.classe, i) for i in idents]

    echecs = derogations = ok = 0
    for classe, ident in travail:
        pb = controler(racine, classe, ident, amont)
        if not pb:
            ok += 1
            if len(travail) <= 20:
                print(f"[  OK  ] {classe}/{ident}")
        elif (classe, ident) in DEROGATIONS:
            derogations += 1
            print(f"[DÉROG.] {classe}/{ident} — {DEROGATIONS[(classe, ident)]}")
        else:
            echecs += 1
            print(f"[ÉCHEC] {classe}/{ident}")
            for x in pb:
                print(f"  {x}")

    print(f"\n{len(travail)} section(s) : {ok} conforme(s), "
          f"{derogations} dérogation(s) assumée(s), {echecs} écart(s).")
    if echecs:
        print("Rappel : un ajout français hors encart <france> est compté ici "
              "comme un écart, et le script NE VOIT PAS une prose périmée.")
    sys.exit(1 if echecs else 0)


if __name__ == "__main__":
    main()
