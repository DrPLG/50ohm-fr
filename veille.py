#!/usr/bin/env python3
"""
veille.py — Veille des mises à jour : amont DARC et retours des relecteurs.

Passe en UNE commande tout ce que le §10 de CLAUDE.md demandait de lancer à la
main en début de session, et classe chaque changement selon le tableau des
réponses de docs/PROTOCOLE-MISES-A-JOUR.md (codes R0 à R9, L1 à L3).

Pourquoi un script de plus. Trois trous constatés :

  - verifier_amont.py compare à l'INSTANTANÉ LOCAL et rend rc=0 pendant que
    l'amont avance (16/08 : 28 commits ; 19/08 : 18 commits) ;
  - le contrôle réseau du §10 se lisait à l'œil et ne disait pas ce que les
    fichiers changés représentent pour NOUS — le 21/10/2026, 28 commits
    d'écart ne touchaient que contents/solutions/, que le livre n'emploie pas ;
  - les relectures arrivent en fichiers dans Fichierstravail/Relectures/ et
    rien ne disait lesquels avaient déjà donné lieu à une feuille d'arbitrage.

Usage :
    python veille.py                       # rapport complet (réseau compris)
    python veille.py --hors-ligne          # sans réseau : relectures + local
    python veille.py --rapport veille.md   # recopie le rapport dans un fichier

    # une relecture vient d'être inventoriée dans la feuille nº 12
    python veille.py relecture-traitee --feuille 12 "Pauline F4LDR/Chap 13.pdf"

    # un nouvel instantané amont vient d'être extrait, contrôlé et intégré
    python veille.py amont-integre --depot contenus --sha <sha complet>

Codes de retour — un contrôle qui ne peut pas rendre son verdict ne contrôle
rien, il doit donc se distinguer d'un « rien à signaler » :
    0  rien de neuf à traiter
    1  au moins un élément à traiter (dérive amont ou relecture en attente)
    2  verdict INCOMPLET : réseau, gh, instantané ou état introuvable.
       Le rapport affiche quand même ce qui a pu être mesuré.

Ce script n'écrit RIEN hors de ses deux fichiers d'état, et seulement par les
deux sous-commandes explicites. Le rapport ne marque jamais rien comme vu :
« avoir vu » n'est pas « avoir traité ».

États :
    veille-amont.json                               versionné ; sha intégrés
    Fichierstravail/Relectures/veille-relectures.json  local ; fichiers reçus

Version du script : v0.1 (21/10/2026).
"""
import argparse
import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

# Même précaution que les quatre scripts de contrôle (CLAUDE.md §11) : la
# console Windows est en cp1252 et le corpus ne l'est pas.
for _flux in (sys.stdout, sys.stderr):
    try:
        _flux.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

RACINE = Path(__file__).resolve().parent
ETAT_AMONT = RACINE / "veille-amont.json"
DOSSIER_RELECTURES = RACINE / "Fichierstravail" / "Relectures"
ETAT_RELECTURES = DOSSIER_RELECTURES / "veille-relectures.json"
CLASSES = ("N", "E", "A", "SWL")
CATALOGUES = ("contents/questions/fragenkatalog3b.json",
              "contents/questions/fragenkatalog_swl.json")
# La compare de GitHub plafonne la liste des fichiers à 300 : au-delà, la
# liste est tronquée SANS erreur. Il faut alors comparer deux instantanés.
PLAFOND_FICHIERS = 300

# Réponses types — le détail est au §3 de docs/PROTOCOLE-MISES-A-JOUR.md.
REPONSES = {
    "R0": "hors périmètre du livre — consigner, rien à faire",
    "R1": "section traduite modifiée — resynchroniser la traduction",
    "R2": "section au sommaire SANS traduction — traduire",
    "R3": "dessin forké modifié — reporter le changement dans le fork",
    "R4": "dessin non forké employé — sort tel quel ; sonder à la recompilation",
    "R5": "question modifiée — revoir l'énoncé traduit",
    "R6": "sommaire modifié — mesurer l'effet sur la structure des livres",
    "R7": "LaTeX amont modifié — document réduit avant toute compilation",
    "R8": "photo — sort telle quelle",
    "R9": "générateur modifié — régénérer et comparer les arbres",
}
DECISION_PIERRE = {"R1", "R2", "R5", "R6", "R7", "R9"}


class Incomplet(Exception):
    """Mesure impossible : le verdict doit sortir en rc=2."""


# --------------------------------------------------------------------------
# Outils
# --------------------------------------------------------------------------

def gh(*args, brut=False):
    """Appelle gh et rend sa sortie ; lève Incomplet au moindre échec."""
    try:
        r = subprocess.run(["gh", *args], capture_output=True, timeout=120)
    except FileNotFoundError:
        raise Incomplet("gh introuvable dans le PATH")
    except subprocess.TimeoutExpired:
        raise Incomplet(f"gh {' '.join(args[:2])} : délai dépassé")
    if r.returncode != 0:
        err = r.stderr.decode("utf-8", "replace").strip().splitlines()
        raise Incomplet(f"gh {' '.join(args[:2])} : "
                        f"{err[-1] if err else 'rc=' + str(r.returncode)}")
    return r.stdout if brut else r.stdout.decode("utf-8", "replace")


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def charger(chemin: Path, defaut):
    if not chemin.exists():
        return defaut
    return json.loads(chemin.read_text(encoding="utf-8"))


def sauver(chemin: Path, data):
    chemin.write_text(json.dumps(data, ensure_ascii=False, indent=2,
                                 sort_keys=True) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------
# Ce que nous employons de l'amont
# --------------------------------------------------------------------------

def index_local(instantane: Path):
    """Sections traduites, dessins forkés et employés, questions traduites."""
    traduites, forkes, employes, questions = {}, {}, {}, {}
    for c in CLASSES:
        d = RACINE / "traductions" / c
        for f in (d / "sections").glob("*.md"):
            traduites.setdefault(f.stem, []).append(c)
            for ligne in f.read_text(encoding="utf-8").splitlines():
                if ligne.lstrip().startswith("%"):  # commentaire amont repris
                    continue
                # [picture:<numéro>:<label>:<légende>] — DARCdown
                debut = ligne.find("[picture:")
                while debut != -1:
                    num = ligne[debut + 9:].split(":", 1)[0]
                    employes.setdefault(num, set()).add(c)
                    debut = ligne.find("[picture:", debut + 1)
        for f in (d / "dessins").glob("*.tex"):
            forkes.setdefault(f.stem, []).append(c)
        q = d / "questions.json"
        if q.exists():
            for num in json.loads(q.read_text(encoding="utf-8")):
                questions.setdefault(num, []).append(c)
    sommaires = {}
    for toc in sorted((instantane / "toc").glob("*.json")):
        data = json.loads(toc.read_text(encoding="utf-8"))
        for chap in data.get("chapters", []):
            for s in chap.get("sections", []):
                sommaires.setdefault(s["ident"], []).append(toc.stem)
    return traduites, forkes, employes, questions, sommaires


def classer_contenu(chemin: str, idx):
    """Rend (code, précision) pour un fichier du dépôt de contenus."""
    traduites, forkes, employes, _questions, sommaires = idx
    nom = Path(chemin)
    if chemin.startswith("contents/sections/") and nom.suffix == ".md":
        ident = nom.stem
        if ident in traduites:
            return "R1", "traduite en " + ", ".join(traduites[ident])
        if ident in sommaires:
            return "R2", "au sommaire de " + ", ".join(sommaires[ident])
        return "R0", "section hors de tout sommaire (à l'instantané local)"
    if chemin.startswith("contents/drawings/") and nom.suffix == ".tex":
        num = nom.stem
        if num in forkes:
            return "R3", "forké en " + ", ".join(forkes[num])
        if num in employes:
            return "R4", "appelé en " + ", ".join(sorted(employes[num]))
        return "R0", "dessin appelé par aucune section traduite"
    if chemin in CATALOGUES:
        return "R5", "catalogue — détail par question ci-dessous"
    if chemin.startswith("contents/questions/"):
        return "R5", "métadonnées du catalogue"
    if chemin.startswith("toc/"):
        return "R6", "sommaire " + nom.stem
    if chemin.startswith("latex/") or chemin == "latexmkrc":
        return "R7", ""
    if chemin.startswith("contents/photos/"):
        return "R8", ""
    return "R0", ""


def classer_generateur(chemin: str):
    if chemin.startswith("renderer/"):
        return "R9", ""
    return "R0", ""


# --------------------------------------------------------------------------
# Amont
# --------------------------------------------------------------------------

def comparer(depot: str, sha: str):
    """Commits et fichiers entre le sha intégré et main."""
    data = json.loads(gh("api", f"repos/{depot}/compare/{sha}...main"))
    commits = [(c["sha"][:8], c["commit"]["committer"]["date"][:10],
                c["commit"]["message"].splitlines()[0])
               for c in data.get("commits", [])]
    fichiers = [(f["status"], f["filename"], f.get("previous_filename", ""))
                for f in data.get("files", [])]
    return data.get("status"), data.get("ahead_by", 0), commits, fichiers


def questions_par_numero(octets: bytes) -> dict:
    out = {}

    def parcourir(x):
        if isinstance(x, dict):
            if "number" in x:
                out[x["number"]] = x
                return
            for v in x.values():
                parcourir(v)
        elif isinstance(x, list):
            for v in x:
                parcourir(v)
    parcourir(json.loads(octets.decode("utf-8")))
    return out


def detail_questions(depot, instantane, chemin, questions_traduites, lignes):
    """Compare le catalogue de main à celui de l'instantané, question par
    question : c'est le numéro qui dit si une traduction est concernée."""
    local = instantane / chemin
    if not local.exists():
        raise Incomplet(f"{chemin} absent de l'instantané local")
    distant = gh("api", "-H", "Accept: application/vnd.github.raw",
                 f"repos/{depot}/contents/{chemin}?ref=main", brut=True)
    avant = questions_par_numero(local.read_bytes())
    apres = questions_par_numero(distant)
    for num in sorted(set(avant) | set(apres)):
        if avant.get(num) == apres.get(num):
            continue
        quoi = ("nouvelle" if num not in avant else
                "retirée" if num not in apres else "modifiée")
        trad = questions_traduites.get(num)
        champs = ""
        if quoi == "modifiée":
            champs = " (" + ", ".join(sorted(
                k for k in set(avant[num]) | set(apres[num])
                if avant[num].get(k) != apres[num].get(k))) + ")"
        lignes.append(f"      {num} {quoi}{champs} — "
                      + ("traduite en " + ", ".join(trad) if trad
                         else "non traduite"))


def veille_amont(etat, lignes, a_traiter):
    instantane = Path(etat["contenus"]["instantane"])
    if not (instantane / "toc").is_dir():
        raise Incomplet(f"instantané introuvable : {instantane}")
    idx = index_local(instantane)
    for cle, classer in (("contenus", None), ("generateur", None)):
        e = etat[cle]
        lignes.append(f"\n## Amont — {e['depot']}")
        lignes.append(f"   intégré : {e['sha'][:8]} (le {e['date_integration']})")
        statut, avance, commits, fichiers = comparer(e["depot"], e["sha"])
        if statut not in ("ahead", "identical"):
            lignes.append(f"!! comparaison « {statut} » : le sha intégré n'est "
                          f"plus un ancêtre de main (historique réécrit ?)")
            a_traiter.append(f"{cle} : historique divergent")
        if avance == 0:
            lignes.append("   à jour : main = sha intégré.")
            continue
        lignes.append(f"   {avance} commit(s) d'écart, {len(fichiers)} fichier(s)")
        if len(fichiers) >= PLAFOND_FICHIERS:
            lignes.append(f"!! liste plafonnée à {PLAFOND_FICHIERS} par GitHub : "
                          f"comparer deux instantanés (`diff -rq`).")
        for sha, quand, msg in commits[-15:]:
            lignes.append(f"     {sha} {quand} {msg[:70]}")
        if len(commits) > 15:
            lignes.append(f"     … et {len(commits) - 15} plus anciens")
        par_code = {}
        for statut_f, chemin, ancien in fichiers:
            if cle == "contenus":
                code, prec = classer_contenu(chemin, idx)
            else:
                code, prec = classer_generateur(chemin)
            if statut_f in ("removed", "renamed") and code != "R0":
                prec = (prec + " ; " if prec else "") + (
                    "SUPPRIMÉ" if statut_f == "removed" else f"RENOMMÉ depuis {ancien}")
            par_code.setdefault(code, []).append((statut_f, chemin, prec))
        for code in sorted(par_code):
            elems = par_code[code]
            marque = "!!" if code != "R0" else "  "
            qui = " [décision de Pierre]" if code in DECISION_PIERRE else ""
            lignes.append(f"{marque} {code} {REPONSES[code]}{qui} — "
                          f"{len(elems)} fichier(s)")
            montrer = elems if code != "R0" else elems[:5]
            for statut_f, chemin, prec in montrer:
                lignes.append(f"     {statut_f:8} {chemin}"
                              + (f" — {prec}" if prec else ""))
            if len(montrer) < len(elems):
                lignes.append(f"     … et {len(elems) - len(montrer)} autres")
            if code != "R0":
                a_traiter.append(f"{cle} : {code} × {len(elems)}")
            if code == "R5":
                for _s, chemin, _p in elems:
                    if chemin in CATALOGUES:
                        detail_questions(e["depot"], instantane, chemin,
                                         idx[3], lignes)


def verifier_local(etat, lignes, a_traiter):
    """verifier_amont.py : nos forks face à l'instantané LOCAL."""
    lignes.append("\n## Forks face à l'instantané local (verifier_amont.py)")
    r = subprocess.run([sys.executable, str(RACINE / "verifier_amont.py"),
                        "verifier", "--input", etat["contenus"]["instantane"]],
                       capture_output=True, timeout=600)
    sortie = r.stdout.decode("utf-8", "replace").strip().splitlines()
    for l in sortie:
        if l.startswith(("!!", "??")) or "élément(s) suivi(s)" in l:
            lignes.append("   " + l.strip())
    if r.returncode == 1:
        a_traiter.append("forks : dérive face à l'instantané local")
    elif r.returncode != 0:
        raise Incomplet(f"verifier_amont.py rc={r.returncode}")


# --------------------------------------------------------------------------
# Relectures
# --------------------------------------------------------------------------

def fichiers_relecture():
    if not DOSSIER_RELECTURES.is_dir():
        return {}
    out = {}
    for f in sorted(DOSSIER_RELECTURES.rglob("*")):
        if f.is_file() and f != ETAT_RELECTURES:
            out[f.relative_to(DOSSIER_RELECTURES).as_posix()] = f
    return out


def veille_relectures(lignes, a_traiter, hors_ligne):
    lignes.append("\n## Relectures — Fichierstravail/Relectures/")
    if not DOSSIER_RELECTURES.is_dir():
        raise Incomplet(f"dossier introuvable : {DOSSIER_RELECTURES}")
    etat = charger(ETAT_RELECTURES, {})
    presents = fichiers_relecture()
    attente = 0
    for rel, f in presents.items():
        e = etat.get(rel)
        if e is None:
            lignes.append(f"!! L1 NOUVEAU     {rel}")
            attente += 1
        elif e.get("sha256") != empreinte(f):
            lignes.append(f"!! L1 MODIFIÉ     {rel} (rattaché à la feuille "
                          f"nº {e.get('feuille')} avant modification)")
            attente += 1
        elif not e.get("feuille"):
            lignes.append(f"!! L2 EN ATTENTE  {rel} (reçu, sans feuille)")
            attente += 1
    for rel in sorted(set(etat) - set(presents)):
        # Une pièce reçue qui disparaît est une source perdue, pas un non-événement.
        lignes.append(f"?? disparu        {rel} (feuille nº {etat[rel].get('feuille')})")
        attente += 1
    if attente:
        a_traiter.append(f"relectures : {attente} fichier(s)")
    else:
        lignes.append(f"   {len(presents)} fichier(s), tous rattachés à une feuille.")
    if hors_ligne:
        return
    lignes.append("\n## Relectures — issues GitHub ouvertes")
    issues = json.loads(gh("issue", "list", "--state", "open", "--limit", "100",
                           "--json", "number,title,createdAt,labels"))
    if not issues:
        lignes.append("   aucune.")
    for i in issues:
        etiq = ", ".join(l["name"] for l in i["labels"])
        lignes.append(f"!! L3 #{i['number']} {i['createdAt'][:10]} {i['title']}"
                      + (f" [{etiq}]" if etiq else ""))
    if issues:
        a_traiter.append(f"issues : {len(issues)} ouverte(s)")


# --------------------------------------------------------------------------
# Commandes
# --------------------------------------------------------------------------

def cmd_rapport(args):
    lignes = [f"# Veille du {date.today().isoformat()}"
              + (" — HORS LIGNE" if args.hors_ligne else "")]
    a_traiter, incomplets = [], []
    etat = charger(ETAT_AMONT, None)
    etapes = []
    if etat is None:
        incomplets.append(f"état amont introuvable : {ETAT_AMONT.name}")
    else:
        if not args.hors_ligne:
            etapes.append(lambda: veille_amont(etat, lignes, a_traiter))
        etapes.append(lambda: verifier_local(etat, lignes, a_traiter))
    etapes.append(lambda: veille_relectures(lignes, a_traiter, args.hors_ligne))
    # Chaque étape est indépendante : l'échec de l'une n'empêche pas de
    # rapporter ce que les autres ont mesuré.
    for etape in etapes:
        try:
            etape()
        except Incomplet as e:
            lignes.append(f"\n?? MESURE IMPOSSIBLE : {e}")
            incomplets.append(str(e))
    lignes.append("\n## Verdict")
    for t in a_traiter:
        lignes.append(f"   à traiter : {t}")
    for t in incomplets:
        lignes.append(f"   NON MESURÉ : {t}")
    if args.hors_ligne:
        lignes.append("   NON MESURÉ : amont distant et issues (--hors-ligne)")
    rc = 2 if (incomplets or args.hors_ligne) else (1 if a_traiter else 0)
    lignes.append({0: "   rc=0 — rien de neuf à traiter.",
                   1: "   rc=1 — des éléments sont à traiter (protocole §2).",
                   2: "   rc=2 — verdict INCOMPLET : ce qui précède n'est pas "
                      "un « rien à signaler »."}[rc])
    texte = "\n".join(lignes)
    print(texte)
    if args.rapport:
        Path(args.rapport).write_text(texte + "\n", encoding="utf-8")
    sys.exit(rc)


def cmd_relecture_traitee(args):
    etat = charger(ETAT_RELECTURES, {})
    presents = fichiers_relecture()
    for rel in args.fichiers:
        rel = rel.replace("\\", "/")
        if rel not in presents:
            sys.exit(f"!! {rel} : introuvable sous {DOSSIER_RELECTURES}")
        etat[rel] = {"sha256": empreinte(presents[rel]),
                     "feuille": args.feuille,
                     "date": date.today().isoformat()}
        print(f"   {rel} → feuille nº {args.feuille}")
    sauver(ETAT_RELECTURES, etat)


def cmd_amont_integre(args):
    etat = charger(ETAT_AMONT, None)
    if etat is None:
        sys.exit(f"!! {ETAT_AMONT.name} introuvable")
    e = etat[args.depot]
    if len(args.sha) != 40:
        sys.exit("!! donner le sha COMPLET (40 caractères) : un sha court "
                 "peut devenir ambigu")
    # Le sha doit exister chez GitHub : on n'inscrit pas une faute de frappe.
    gh("api", f"repos/{e['depot']}/commits/{args.sha}", "--jq", ".sha")
    ancien = e["sha"]
    e.update(sha=args.sha, date_integration=date.today().isoformat())
    if args.instantane:
        e["instantane"] = args.instantane
    # Écart tout en R0 : on solde sans renouveler l'instantané, et on le dit.
    e["note"] = args.note
    sauver(ETAT_AMONT, etat)
    print(f"   {args.depot} : {ancien[:8]} → {args.sha[:8]}")


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hors-ligne", action="store_true",
                    help="Ne pas interroger GitHub (rc=2 d'office).")
    ap.add_argument("--rapport", help="Recopier le rapport dans ce fichier.")
    ap.set_defaults(func=cmd_rapport)
    sous = ap.add_subparsers(dest="commande")

    p = sous.add_parser("relecture-traitee",
                        help="Rattacher des fichiers de relecture à une feuille.")
    p.add_argument("--feuille", required=True,
                   help="Numéro de la feuille d'arbitrage (ex. 12).")
    p.add_argument("fichiers", nargs="+",
                   help="Chemins relatifs à Fichierstravail/Relectures/.")
    p.set_defaults(func=cmd_relecture_traitee)

    p = sous.add_parser("amont-integre",
                        help="Inscrire le sha d'un amont intégré.")
    p.add_argument("--depot", required=True, choices=("contenus", "generateur"))
    p.add_argument("--sha", required=True, help="sha complet, 40 caractères.")
    p.add_argument("--instantane", help="Nouveau chemin de l'instantané local.")
    p.add_argument("--note", default="",
                   help="Ex. « écart R0 seul, instantané 48e18bf4 conservé ».")
    p.set_defaults(func=cmd_amont_integre)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
