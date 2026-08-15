#!/usr/bin/env python3
"""
sonde_dessins.py — Sonde anti-germanisme sur les DESSINS composés dans les livres.

Les sections traduites passent la sonde anti-germanisme du §5 de CLAUDE.md.
Les dessins, eux, n'avaient aucun contrôle équivalent : un dessin forké
(traductions/<CLASSE>/dessins/<id>.tex) peut être traduit à 90 % et afficher
encore « Höhe » ou « Raumwelle » dans le livre livré, sans qu'aucune étape de
la chaîne ne le signale. C'est exactement ce qui a été constaté le 14/08/2026
par Pierre, sur épreuve papier : classe N figure 2.24 (« Höhe », dessin 731) et
figure 2.28 (« Raumwelle », dessins 732 et 741), tous trois FORKÉS — donc
traduits, mais incomplètement.

DEUX POPULATIONS, à ne jamais confondre dans le compte rendu :

  - dessin FORKÉ portant encore de l'allemand  -> DÉFAUT de traduction ;
  - dessin NON forké                           -> sort tel quel de l'amont,
    c'est l'état du chantier de francisation (§9 de CLAUDE.md), pas un défaut.

Seuls les dessins RÉELLEMENT UTILISÉS par le livre sont examinés : l'amont en
compte 885, dont une partie n'est référencée par aucune section.

DEUX DÉTECTIONS COMPLÉMENTAIRES, et leurs limites :

  1. umlaut et eszett (ä ö ü Ä Ö Ü ß) — ces caractères n'existent pas en
     français, donc aucun faux positif possible. Mais cette détection ne voit
     ni « Bodenwelle », ni « Langwelle », ni « Frequenz », ni « Leistung » ;
  2. liste de mots allemands du corpus technique, PURGÉE des mots identiques ou
     quasi identiques en français. « Antenne », « Masse », « des », « Quelle »,
     « Last », « Ton » y figuraient dans une première version et produisaient
     du bruit : trois dessins parfaitement traduits étaient signalés à tort.

LIMITE ASSUMÉE. Cette sonde donne un PLANCHER, jamais un compte exhaustif : un
mot allemand absent de la liste et dépourvu d'umlaut passe au travers. Elle lit
par ailleurs le source TikZ et non le PDF — un mot présent dans le fichier mais
non composé (branche inactive, macro non appelée) serait compté à tort. Un
retour à zéro ne prouve donc pas l'absence d'allemand : il prouve l'absence de
ce que la sonde sait reconnaître. Les commentaires « % » sont exclus, comme le
veut le §6 (blocs commentés allemands préservés verbatim).

Usage :
    python sonde_dessins.py                 # les trois classes
    python sonde_dessins.py N E             # classes choisies
    python sonde_dessins.py --racine <dir>  # autre racine que celle du script

Code de retour : 1 si au moins un dessin FORKÉ porte encore de l'allemand
(même convention que verifier_amont.py) ; 0 sinon. Les dessins non forkés
n'influencent jamais le code de retour : ce n'est pas un défaut.

Licence des contenus : CC BY 4.0 — 50ohm.de-Autorenteam / DARC e. V.

Version : v0.1 (14/08/2026)
"""
import argparse
import pathlib
import re
import sys

# Mots allemands du corpus technique. Tout mot également français en est EXCLU.
MOTS_ALLEMANDS = """
Höhe Welle Wellen Raumwelle Bodenwelle Langwelle Mittelwelle Kurzwelle
Ultrakurzwelle Grenzwelle Frequenz Frequenzen Spannung Strom Widerstand
Leistung Länge Erde Erdboden Boden Sender Empfänger Abstand Winkel Ausbreitung
Reichweite Schicht Ionosphäre Entfernung Richtung Leitung Schaltung Wirkung
Dämpfung Verstärkung Sendung Empfang Spule Kondensator Zeichen Träger Bereich
Ebene Achse Fläche Knoten Zweig Kennlinie Verlauf Anstieg Abfall Feldstärke
Zeit Strahlung Erdung Abschirmung Speisung Anpassung Rückkopplung
und mit für von zum zur der die das dem den ein eine einer einem oder aber
auch nicht bei aus nach über unter durch gegen ohne
""".split()

MOTIF_MOTS = re.compile(r"\b(" + "|".join(MOTS_ALLEMANDS) + r")\b")
MOTIF_LETTRES = re.compile(r"\b\w*[äöüÄÖÜß]\w*\b")
# Un « % » précédé d'une contre-oblique est un vrai pourcent, pas un commentaire.
MOTIF_COMMENTAIRE = re.compile(r"(?<!\\)%.*")


def germanismes(source: str) -> list:
    """Mots allemands d'un dessin, commentaires exclus."""
    net = MOTIF_COMMENTAIRE.sub("", source)
    return sorted(set(MOTIF_MOTS.findall(net)) | set(MOTIF_LETTRES.findall(net)))


def dessins_utilises(build: pathlib.Path) -> set:
    """Idents des dessins référencés par au moins une section du livre."""
    utilises = set()
    for f in (build / "sections").glob("*.tex"):
        utilises |= set(re.findall(r"\{(\d+)include\}", f.read_text(encoding="utf-8")))
    return utilises


def analyser(racine, classe):
    """Renvoie le bilan d'une classe, ou None si son arbre n'est pas compilé.

    Sans annotation « dict | None » : cette syntaxe exige Python 3.10, alors que
    la sonde doit rester lançable avec le python du PATH, qui peut être plus
    ancien (le venv 3.12 du générateur n'est requis que par build_book.py).
    """
    build = racine / f"build-{classe}"
    if not (build / "sections").is_dir():
        return None
    forks = racine / "traductions" / classe / "dessins"
    res = {
        "utilises": 0, "forke_propre": 0, "forke_sale": [], "non_forke_sale": [],
        "forkes": len(list(forks.glob("*.tex"))) if forks.is_dir() else 0,
    }
    utilises = dessins_utilises(build)
    res["utilises"] = len(utilises)
    for ident in sorted(utilises, key=int):
        fichier = build / "img" / f"{ident}include.tex"
        if not fichier.is_file():
            continue
        mots = germanismes(fichier.read_text(encoding="utf-8", errors="replace"))
        est_forke = (forks / f"{ident}.tex").is_file()
        if mots:
            cle = "forke_sale" if est_forke else "non_forke_sale"
            res[cle].append((ident, mots))
        elif est_forke:
            res["forke_propre"] += 1
    return res


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*", default=["N", "E", "A"],
                    help="classes à sonder (défaut : N E A)")
    ap.add_argument("--racine", default=None,
                    help="racine du dépôt (défaut : le répertoire de ce script)")
    ap.add_argument("--tout", action="store_true",
                    help="lister aussi tous les dessins non forkés, sans troncature")
    args = ap.parse_args()

    racine = pathlib.Path(args.racine).resolve() if args.racine \
        else pathlib.Path(__file__).resolve().parent
    defauts = 0

    for classe in args.classes:
        r = analyser(racine, classe)
        if r is None:
            print(f"=== classe {classe} : build-{classe}/sections absent — "
                  f"compiler d'abord, la sonde lit l'arbre de compilation ===\n")
            continue
        print(f"=== classe {classe} : {r['utilises']} dessins utilisés, "
              f"{r['forkes']} forkés au total ===")
        print(f"  forkés et propres              : {r['forke_propre']}")
        print(f"  FORKÉS avec allemand résiduel  : {len(r['forke_sale'])}"
              f"   <- défauts de traduction")
        for ident, mots in r["forke_sale"]:
            print(f"      {ident:>5} : {', '.join(mots[:6])}")
        print(f"  non forkés avec allemand       : {len(r['non_forke_sale'])}"
              f"   <- chantier de francisation (§9), pas un défaut")
        limite = None if args.tout else 10
        for ident, mots in r["non_forke_sale"][:limite]:
            print(f"      {ident:>5} : {', '.join(mots[:6])}")
        if limite and len(r["non_forke_sale"]) > limite:
            print(f"      … et {len(r['non_forke_sale']) - limite} autres (--tout pour la liste)")
        print()
        defauts += len(r["forke_sale"])

    if defauts:
        print(f"{defauts} dessin(s) forké(s) portent encore de l'allemand.")
        sys.exit(1)
    print("Aucun dessin forké ne porte d'allemand reconnaissable par la sonde.")


if __name__ == "__main__":
    main()
