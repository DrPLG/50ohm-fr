#!/usr/bin/env python3
"""Exporte la banque de questions du BIR au format GIFT (Moodle, éléa).

    python exporter_moodle.py            -> bir/moodle/bir-questions.gift.txt

Dans Moodle ou éléa : Banque de questions > Importer > format GIFT.

Le catalogue (questions/*.json) est au format des catalogues amont : la bonne
réponse y est toujours la réponse A. GIFT la marque d'un « = », les trois
autres d'un « ~ » ; c'est la plateforme qui mélange l'ordre à l'affichage.

Les formules LaTeX du catalogue sont réécrites en texte simple :
$\\qty{145}{\\mega\\hertz}$ devient « 145 MHz ». Une formule que ce script ne
sait pas réécrire ARRÊTE l'export : mieux vaut une erreur qu'un énoncé
illisible dans un examen.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ICI = Path(__file__).resolve().parent
PREFIXES = {"kilo": "k", "mega": "M", "giga": "G", "milli": "m", "centi": "c",
            "micro": "µ", "nano": "n", "pico": "p"}
UNITES = {"hertz": "Hz", "meter": "m", "metre": "m", "volt": "V", "ampere": "A",
          "ohm": "Ω", "watt": "W", "second": "s", "hour": "h"}
INSECABLE = " "


def unite(code):
    """\\mega\\hertz -> MHz. Lève KeyError sur un nom inconnu."""
    noms = re.findall(r"\\([A-Za-z]+)", code)
    if not noms or "".join("\\" + n for n in noms) != code.replace(" ", ""):
        raise KeyError(code)
    return "".join(PREFIXES[n] if n in PREFIXES else UNITES[n] for n in noms)


def texte_simple(s, numero):
    """LaTeX du catalogue -> texte pour la plateforme."""
    s = re.sub(r"\$\\qty\{([^{}]*)\}\{([^{}]*)\}\$",
               lambda m: m.group(1) + INSECABLE + unite(m.group(2)), s)
    s = re.sub(r"\$\\qtyrange\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}\$",
               lambda m: "{} à {}{}{}".format(m.group(1), m.group(2), INSECABLE,
                                              unite(m.group(3))), s)
    if "$" in s or "\\" in s:
        raise SystemExit(f"!! {numero} : formule non réécrite — {s}")
    return s


def gift(s):
    """Échappe les caractères que GIFT réserve."""
    return re.sub(r"([~=#{}:])", r"\\\1", s)


def main():
    lignes, total = ["// Banque de questions du BIR — export GIFT", ""], 0
    for fichier in sorted((ICI / "questions").glob("*.json")):
        for domaine in json.loads(fichier.read_text(encoding="utf-8"))["sections"]:
            for seance in domaine["sections"]:
                lignes += ["$CATEGORY: BIR/{}/{}".format(
                    domaine["title"].replace("/", "-"), seance["title"].replace("/", "-")), ""]
                for q in seance["questions"]:
                    n = q["number"]
                    lignes.append("::{}::{} {{".format(n, gift(texte_simple(q["question"], n))))
                    for lettre in "abcd":
                        lignes.append("\t{}{}".format(
                            "=" if lettre == "a" else "~",
                            gift(texte_simple(q["answer_" + lettre], n))))
                    lignes += ["}", ""]
                    total += 1
    sortie = ICI / "moodle" / "bir-questions.gift.txt"
    sortie.parent.mkdir(exist_ok=True)
    sortie.write_text("\n".join(lignes), encoding="utf-8")
    print(f"{total} question(s) exportée(s) : {sortie}")
    return 0 if total else 1


if __name__ == "__main__":
    sys.exit(main())
