#!/usr/bin/env python3
"""
verifier_amont.py — Suivi de la dérive amont pour les dessins forkés ET les
sections traduites côté français.

Un dessin forké (traductions/<CLASSE>/dessins/<id>.tex) comme une section
traduite (traductions/<CLASSE>/sections/<ident>.md) sortent définitivement du
pipeline amont : si le DARC modifie l'original allemand ensuite, la version
française ne le sait jamais toute seule — build_book.py utilise la version
française sans jamais recomparer à l'amont. Ce script journalise l'empreinte
SHA-256 de l'amont au moment de la traduction ou du fork, puis permet de la
recomparer à l'amont courant, en début de session.

Le besoin a été démontré le 14/08/2026 : quatre sections de la classe A
(antennenformen_3, photovoltaik, polarisation_3, remote_station) avaient pris
du retard sur l'amont sans qu'aucun signal ne le révèle — le contenu allemand
ajouté depuis était simplement absent du livre français. Il a fallu comparer
deux instantanés amont pour s'en apercevoir. Un manifeste rend ce diagnostic
possible sans conserver d'ancien instantané.

Usage :
    # dessins : enregistrer un fork qui vient d'etre cree
    python verifier_amont.py enregistrer --type dessins --edition N \\
        --input <chemin>/50ohm-contents-dl-main --id 357

    # sections : constituer la ligne de base pour tout ce qui est deja traduit
    python verifier_amont.py initialiser --type sections \\
        --input <chemin>/50ohm-contents-dl-main

    # a chaque session, detecter la derive (les deux types, les trois classes)
    python verifier_amont.py verifier --input <chemin>/50ohm-contents-dl-main

ATTENTION à « initialiser » : la commande affirme que tout ce qu'elle
enregistre est à jour vis-à-vis de l'amont du jour. C'est vrai au moment où on
la lance sur du contenu qu'on vient de resynchroniser ; ça ne l'est pas sur du
contenu dont on ignore l'état. En cas de doute, utiliser --note pour inscrire
la réserve dans le manifeste plutôt que de laisser croire à une vérification.

Licence des contenus : CC BY 4.0 — 50ohm.de-Autorenteam / DARC e. V.

TROIS ÉTATS SONT RAPPORTÉS, et le troisième est le plus insidieux :

  - dérive détectée      : l'amont a changé depuis le fork ;
  - introuvable          : l'amont a disparu ou été renommé ;
  - FORKÉ MAIS NON SUIVI : le fichier existe côté français mais n'a aucune
    entrée au manifeste. Il ne sera donc JAMAIS signalé en dérive — le script
    ne comparait que ce que le manifeste connaissait déjà, si bien qu'un fork
    oublié lui était entièrement invisible. Constaté le 15/08/2026 sur trois
    dessins de la classe A (260, 303, 315), forkés après un « initialiser » :
    « verifier » répondait « 261 éléments suivis, 0 dérive » sans rien dire.

Version du script : v0.3 — détection des forks absents du manifeste
(v0.2 : généralisation aux sections ; v0.1 : dessins seuls).
"""
import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent
CLASSES = ("N", "E", "A")

# Tout ce qui distingue un type de suivi de l'autre. Ajouter un type revient a
# ajouter une entree ici : le reste du script n'en sait rien.
TYPES = {
    "dessins": {
        "amont": ("contents", "drawings"),
        "suffixe": ".tex",
        "fork": "dessins",
        "manifeste": "dessins-manifest.json",
        "cle_date": "date_fork",
        "libelle": "dessin",
        # les dessins sont identifies par un entier, on trie en consequence
        "tri": lambda k: (0, int(k)) if k.isdigit() else (1, k),
    },
    "sections": {
        "amont": ("contents", "sections"),
        "suffixe": ".md",
        "fork": "sections",
        "manifeste": "sections-manifest.json",
        "cle_date": "date_traduction",
        "libelle": "section",
        "tri": lambda k: (0, k),
    },
}


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def chemin_amont(contents: Path, type_: str, ident: str) -> Path:
    cfg = TYPES[type_]
    return contents.joinpath(*cfg["amont"], ident + cfg["suffixe"])


def chemin_fork(edition: str, type_: str, ident: str) -> Path:
    cfg = TYPES[type_]
    return RACINE / "traductions" / edition / cfg["fork"] / (ident + cfg["suffixe"])


def manifeste_path(edition: str, type_: str) -> Path:
    return RACINE / "traductions" / edition / TYPES[type_]["manifeste"]


def charger_manifeste(edition: str, type_: str) -> dict:
    p = manifeste_path(edition, type_)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def sauver_manifeste(edition: str, type_: str, data: dict):
    p = manifeste_path(edition, type_)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def cmd_enregistrer(args):
    contents = Path(args.input).resolve()
    cfg = TYPES[args.type]
    amont = chemin_amont(contents, args.type, args.id)
    if not amont.is_file():
        print(f"!! {cfg['libelle']} amont introuvable : {amont}", file=sys.stderr)
        sys.exit(2)
    fork = chemin_fork(args.edition, args.type, args.id)
    if not fork.is_file():
        print(f"!! aucune version française trouvée : {fork}", file=sys.stderr)
        sys.exit(2)
    data = charger_manifeste(args.edition, args.type)
    data[args.id] = {
        "sha256_amont": empreinte(amont),
        cfg["cle_date"]: date.today().isoformat(),
        "note": args.note or "",
    }
    sauver_manifeste(args.edition, args.type, data)
    print(f"OK : {cfg['libelle']} {args.id} enregistré dans "
          f"traductions/{args.edition}/{cfg['manifeste']}")


def cmd_initialiser(args):
    """Ligne de base en masse : enregistre tout ce qui est deja traduit.

    Refuse par defaut d'ecraser une entree existante — sans cela, un
    « initialiser » lance par megarde effacerait la memoire d'une derive
    detectee mais pas encore traitee, ce qui est exactement ce que le
    manifeste doit empecher.
    """
    contents = Path(args.input).resolve()
    cfg = TYPES[args.type]
    editions = [args.edition] if args.edition else list(CLASSES)
    for edition in editions:
        data = charger_manifeste(edition, args.type)
        dossier = RACINE / "traductions" / edition / cfg["fork"]
        if not dossier.is_dir():
            print(f"   {edition} : aucun dossier {cfg['fork']}/, ignoré")
            continue
        ajouts, deja, absents = 0, 0, 0
        for f in sorted(dossier.glob("*" + cfg["suffixe"])):
            ident = f.name[: -len(cfg["suffixe"])]
            if ident in data and not args.forcer:
                deja += 1
                continue
            amont = chemin_amont(contents, args.type, ident)
            if not amont.is_file():
                absents += 1
                print(f"?? {edition}/{ident} : pas d'équivalent amont "
                      f"({amont.name}) — non enregistré.")
                continue
            data[ident] = {
                "sha256_amont": empreinte(amont),
                cfg["cle_date"]: date.today().isoformat(),
                "note": args.note or "ligne de base",
            }
            ajouts += 1
        sauver_manifeste(edition, args.type, data)
        print(f"   {edition} : {ajouts} enregistrée(s), {deja} déjà suivie(s), "
              f"{absents} sans équivalent amont.")
    print(f"\nLigne de base écrite. Elle affirme que ces {cfg['libelle']}s sont "
          f"à jour\nvis-à-vis de l'amont du {date.today().isoformat()}.")


def forks_non_suivis(edition: str, type_: str, data: dict) -> list:
    """Idents forkés côté français qui n'ont AUCUNE entrée au manifeste.

    Trou constaté le 15/08/2026 : le script comparait l'amont aux entrées du
    manifeste, et rien d'autre. Un fork créé sans « enregistrer » lui était donc
    entièrement invisible — il ne serait JAMAIS signalé en dérive, même si le
    DARC modifiait son original. Trois dessins de la classe A (260, 303, 315)
    étaient dans ce cas ; « verifier » répondait « 261 éléments suivis, 0
    dérive » sans rien dire. C'est une question de Pierre qui les a rattrapés,
    pas l'outillage.

    On compte les fichiers réellement présents, et non l'inverse : c'est le
    dossier qui fait foi, le manifeste n'étant que sa mémoire.
    """
    cfg = TYPES[type_]
    dossier = RACINE / "traductions" / edition / cfg["fork"]
    if not dossier.is_dir():
        return []
    presents = {f.name[: -len(cfg["suffixe"])]
                for f in dossier.glob("*" + cfg["suffixe"])}
    return sorted(presents - set(data), key=cfg["tri"])


def cmd_verifier(args):
    contents = Path(args.input).resolve()
    editions = [args.edition] if args.edition else list(CLASSES)
    types = [args.type] if args.type else list(TYPES)
    total, derives, absents, non_suivis = 0, 0, 0, 0
    for type_ in types:
        cfg = TYPES[type_]
        for edition in editions:
            data = charger_manifeste(edition, type_)
            # Contrôle mené AVANT la comparaison des empreintes, et même quand
            # le manifeste est vide : un dossier de forks sans manifeste du tout
            # est le pire des cas, pas un cas neutre.
            for ident in forks_non_suivis(edition, type_, data):
                non_suivis += 1
                print(f"!! {type_} {edition}/{ident} : FORKÉ MAIS NON SUIVI — "
                      f"aucune entrée au manifeste, donc aucune dérive amont ne "
                      f"sera jamais signalée. Lancer « enregistrer » ou "
                      f"« initialiser ».")
            if not data:
                continue
            for ident, info in sorted(data.items(), key=lambda kv: cfg["tri"](kv[0])):
                total += 1
                amont = chemin_amont(contents, type_, ident)
                if not amont.is_file():
                    absents += 1
                    print(f"?? {type_} {edition}/{ident} : amont introuvable — "
                          f"renommé ou supprimé côté DARC ?")
                    continue
                if empreinte(amont) != info["sha256_amont"]:
                    derives += 1
                    quand = info.get(cfg["cle_date"], "?")
                    print(f"!! {type_} {edition}/{ident} : L'AMONT A CHANGÉ "
                          f"depuis le {quand} — revérifier la version française "
                          f"face au nouvel original allemand.")
                elif args.verbeux:
                    print(f"   {type_} {edition}/{ident} : inchangé")
    if total == 0 and non_suivis == 0:
        print("Aucun manifeste renseigné — rien à vérifier "
              "(cf. « initialiser »).")
        return
    print(f"\n{total} élément(s) suivi(s), {derives} dérive(s) détectée(s), "
          f"{absents} introuvable(s) côté amont, "
          f"{non_suivis} forké(s) non suivi(s).")
    if derives or absents or non_suivis:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sous = ap.add_subparsers(dest="commande", required=True)

    p_enr = sous.add_parser(
        "enregistrer",
        help="Journaliser l'empreinte amont d'un élément qui vient d'être "
             "forké ou traduit.")
    p_enr.add_argument("--type", required=True, choices=list(TYPES))
    p_enr.add_argument("--edition", required=True, choices=CLASSES)
    p_enr.add_argument("--input", required=True,
                       help="Racine de 50ohm-contents-dl (amont).")
    p_enr.add_argument("--id", required=True,
                       help="Identifiant : numéro pour un dessin (357), "
                            "nom de fichier sans extension pour une section.")
    p_enr.add_argument("--note", default="", help="Raison (facultatif).")
    p_enr.set_defaults(func=cmd_enregistrer)

    p_ini = sous.add_parser(
        "initialiser",
        help="Constituer la ligne de base pour tout ce qui est déjà traduit.")
    p_ini.add_argument("--type", required=True, choices=list(TYPES))
    p_ini.add_argument("--input", required=True,
                       help="Racine de 50ohm-contents-dl (amont).")
    p_ini.add_argument("--edition", choices=CLASSES, default=None,
                       help="Limiter à une classe (par défaut : les trois).")
    p_ini.add_argument("--note", default="",
                       help="Note portée sur chaque entrée créée.")
    p_ini.add_argument("--forcer", action="store_true",
                       help="Réécrire les entrées existantes. À éviter : "
                            "efface la trace d'une dérive non traitée.")
    p_ini.set_defaults(func=cmd_initialiser)

    p_ver = sous.add_parser(
        "verifier",
        help="Comparer chaque empreinte enregistrée à l'amont actuel.")
    p_ver.add_argument("--input", required=True,
                       help="Racine de 50ohm-contents-dl (amont).")
    p_ver.add_argument("--type", choices=list(TYPES), default=None,
                       help="Limiter à un type (par défaut : les deux).")
    p_ver.add_argument("--edition", choices=CLASSES, default=None,
                       help="Limiter à une classe (par défaut : les trois).")
    p_ver.add_argument("--verbeux", action="store_true",
                       help="Lister aussi les éléments inchangés.")
    p_ver.set_defaults(func=cmd_verifier)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
