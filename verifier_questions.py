#!/usr/bin/env python3
"""
verifier_questions.py — Une question et ses réponses sont-elles sur la même page ?

Le défaut est visible et pénalisant : la page s'achève sur l'énoncé, les quatre
réponses A/B/C/D sont sur la page suivante. Dix-neuf cas avaient été relevés à
la main sur la classe N en version a.1, non recensés au-delà de la page 100.

POURQUOI CE SCRIPT PLUTÔT QU'UNE LECTURE DU PDF. La première vérification
extrayait le texte du PDF et cherchait les lettres A/B/C/D après le numéro de
question. Elle était bruitée : le contenu des figures de marge s'intercale en
début de ligne (« B VeryHighFrequency… ») et masque les lettres. Elle a produit
douze faux positifs sur la classe N, dont huit dus au seul format
\\QuestionTwoCol, où A et B partagent une ligne. Aucun n'était une vraie coupure.

La mesure exacte est donnée par LaTeX lui-même : build_book.py v0.18 (B6) pose
deux \\label par question, l'un à l'énoncé, l'autre après le tableau des
réponses. LaTeX résout leurs pages au shipout, donc sans le décalage qu'aurait
un \\thepage lu pendant la composition. Les deux atterrissent dans le .aux sous
la forme :

    \\newlabel{DARCq@debut@NA103}{{}{12}{}{...}{}}
    \\newlabel{DARCq@fin@NA103}{{}{13}{}{...}{}}

Il suffit de comparer les deux numéros de page.

Usage :
    python verifier_questions.py            # les trois classes
    python verifier_questions.py N E        # classes choisies
    python verifier_questions.py --racine <dir>

Code de retour : 1 si au moins une question est coupée, 0 sinon.

Licence des contenus : CC BY 4.0 — 50ohm.de-Autorenteam / DARC e. V.

Version : v0.1 (14/08/2026)
"""
import argparse
import pathlib
import re
import sys

# \newlabel{NOM}{{numero}{page}{...}...} — on ne veut que le 2e groupe.
MOTIF_LABEL = re.compile(r"\\newlabel\{DARCq@(debut|fin)@([^}]+)\}\{\{[^}]*\}\{([^}]*)\}")


def pages_des_questions(aux: pathlib.Path) -> dict:
    """{numero: {'debut': page, 'fin': page}} d'après le .aux."""
    out = {}
    for m in MOTIF_LABEL.finditer(aux.read_text(encoding="utf-8", errors="replace")):
        bout, numero, page = m.group(1), m.group(2), m.group(3)
        out.setdefault(numero, {})[bout] = page
    return out


def analyser(racine: pathlib.Path, classe: str):
    aux = racine / f"build-{classe}" / f"book-{classe}.aux"
    if not aux.is_file():
        return None
    pages = pages_des_questions(aux)
    coupees, incompletes = [], []
    for numero, bouts in sorted(pages.items()):
        if "debut" not in bouts or "fin" not in bouts:
            incompletes.append(numero)
        elif bouts["debut"] != bouts["fin"]:
            coupees.append((numero, bouts["debut"], bouts["fin"]))
    return {"total": len(pages), "coupees": coupees, "incompletes": incompletes}


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*", default=["N", "E", "A"])
    ap.add_argument("--racine", default=None,
                    help="racine du dépôt (défaut : le répertoire de ce script)")
    args = ap.parse_args()

    racine = pathlib.Path(args.racine).resolve() if args.racine \
        else pathlib.Path(__file__).resolve().parent
    total_coupees = 0

    for classe in args.classes:
        r = analyser(racine, classe)
        if r is None:
            print(f"=== classe {classe} : book-{classe}.aux absent — compiler d'abord ===\n")
            continue
        if r["total"] == 0:
            print(f"=== classe {classe} : aucun repère de question dans le .aux.")
            print("    Le livre a-t-il été compilé avec build_book.py v0.18 ou plus ?\n")
            continue
        print(f"=== classe {classe} : {r['total']} questions repérées ===")
        print(f"  questions coupées : {len(r['coupees'])}")
        for numero, d, f in r["coupees"]:
            print(f"      {numero:>8} : énoncé page {d}, réponses page {f}")
        if r["incompletes"]:
            print(f"  repères incomplets : {len(r['incompletes'])} "
                  f"({', '.join(r['incompletes'][:5])}…)")
            print("      (une seule des deux bornes trouvée — .aux tronqué ?)")
        print()
        total_coupees += len(r["coupees"])

    if total_coupees:
        print(f"{total_coupees} question(s) séparée(s) de leurs réponses.")
        sys.exit(1)
    print("Aucune question n'est séparée de ses réponses.")


if __name__ == "__main__":
    main()
