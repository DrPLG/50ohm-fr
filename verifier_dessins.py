#!/usr/bin/env python3
"""
verifier_dessins.py — Suivi de la dérive amont pour les dessins forkés côté français.

Un dessin forké (traductions/<CLASSE>/dessins/<id>.tex, cf. build_book.py v0.15
et docs/ANALYSE-DESSINS.md) sort définitivement du pipeline amont : si le DARC
modifie l'original allemand ensuite, le fork français ne le sait jamais tout
seul — build_book.py copie le fork sans jamais recomparer à l'amont. Ce script
journalise l'empreinte SHA-256 de l'amont au moment du fork
(traductions/<CLASSE>/dessins-manifest.json, un par classe) et permet de la
recomparer à l'amont courant, en début de session.

Usage :
    # au moment de créer un fork, une fois traductions/<CLASSE>/dessins/<id>.tex
    # en place :
    python verifier_dessins.py enregistrer --edition N \\
        --input <chemin>/50ohm-contents-dl-main --id 357

    # à chaque session, pour détecter une dérive sur tous les dessins déjà
    # forkés (les trois classes par défaut) :
    python verifier_dessins.py verifier --input <chemin>/50ohm-contents-dl-main

Licence des contenus : CC BY 4.0 — 50ohm.de-Autorenteam / DARC e. V.

Version du script : v0.1 — première version, aucun dessin forké à ce jour.
"""
import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parent
CLASSES = ("N", "E", "A")


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def manifeste_path(edition: str) -> Path:
    return RACINE / "traductions" / edition / "dessins-manifest.json"


def charger_manifeste(edition: str) -> dict:
    p = manifeste_path(edition)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def sauver_manifeste(edition: str, data: dict):
    p = manifeste_path(edition)
    p.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def cmd_enregistrer(args):
    contents = Path(args.input).resolve()
    amont = contents / "contents" / "drawings" / f"{args.id}.tex"
    if not amont.is_file():
        print(f"!! dessin amont introuvable : {amont}", file=sys.stderr)
        sys.exit(2)
    fork = RACINE / "traductions" / args.edition / "dessins" / f"{args.id}.tex"
    if not fork.is_file():
        print(f"!! aucun fork trouvé : {fork}\n"
              f"   créer traductions/{args.edition}/dessins/{args.id}.tex d'abord.",
              file=sys.stderr)
        sys.exit(2)
    data = charger_manifeste(args.edition)
    data[args.id] = {
        "sha256_amont": empreinte(amont),
        "date_fork": date.today().isoformat(),
        "note": args.note or "",
    }
    sauver_manifeste(args.edition, data)
    print(f"OK : dessin {args.id} enregistré dans "
          f"traductions/{args.edition}/dessins-manifest.json")


def cmd_verifier(args):
    contents = Path(args.input).resolve()
    editions = [args.edition] if args.edition else list(CLASSES)
    total, derives, absents = 0, 0, 0
    for edition in editions:
        data = charger_manifeste(edition)
        if not data:
            continue
        for ident, info in sorted(data.items(), key=lambda kv: int(kv[0])):
            total += 1
            amont = contents / "contents" / "drawings" / f"{ident}.tex"
            if not amont.is_file():
                absents += 1
                print(f"?? {edition}/{ident} : dessin amont introuvable "
                      f"({amont}) — a-t-il été renommé ou supprimé côté DARC ?")
                continue
            actuelle = empreinte(amont)
            if actuelle != info["sha256_amont"]:
                derives += 1
                print(f"!! {edition}/{ident} : L'AMONT A CHANGÉ depuis le fork "
                      f"du {info['date_fork']} — revérifier "
                      f"traductions/{edition}/dessins/{ident}.tex face au nouvel "
                      f"original allemand.")
            else:
                print(f"   {edition}/{ident} : inchangé depuis le {info['date_fork']}")
    if total == 0:
        print("Aucun dessin forké enregistré — rien à vérifier "
              "(cf. « verifier_dessins.py enregistrer »).")
        return
    print(f"\n{total} dessin(s) forké(s) suivi(s), {derives} dérive(s) détectée(s), "
          f"{absents} introuvable(s) côté amont.")
    if derives or absents:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sous = ap.add_subparsers(dest="commande", required=True)

    p_enr = sous.add_parser(
        "enregistrer",
        help="Journaliser l'empreinte amont d'un dessin qui vient d'être forké.")
    p_enr.add_argument("--edition", required=True, choices=CLASSES)
    p_enr.add_argument("--input", required=True,
                        help="Racine de 50ohm-contents-dl (amont).")
    p_enr.add_argument("--id", required=True,
                        help="Identifiant numérique du dessin, ex. 357.")
    p_enr.add_argument("--note", default="", help="Raison du fork (facultatif).")
    p_enr.set_defaults(func=cmd_enregistrer)

    p_ver = sous.add_parser(
        "verifier",
        help="Comparer l'empreinte enregistrée de chaque dessin forké à l'amont actuel.")
    p_ver.add_argument("--input", required=True,
                        help="Racine de 50ohm-contents-dl (amont).")
    p_ver.add_argument("--edition", choices=CLASSES, default=None,
                        help="Limiter à une classe (par défaut : les trois).")
    p_ver.set_defaults(func=cmd_verifier)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
