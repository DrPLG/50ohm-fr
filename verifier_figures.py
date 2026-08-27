#!/usr/bin/env python3
"""
verifier_figures.py — Une figure et sa légende sont-elles sur la même page ?

Le défaut est le pendant exact de celui que traite `verifier_questions.py` : la
page s'achève sur l'image, et la légende « Fig. 2.29 – … » ouvre seule la page
suivante. Le lecteur voit un graphique sans titre, puis un titre sans graphique.

ORIGINE. Signalé par Sylvain F6DBI sur la a.2 (« P.57 ET 58 : la mention de la
figure 2.29 située en page 57 se trouve rejetée à la page suivante »), une seule
occurrence relevée. Pierre a demandé d'en faire une règle plutôt qu'une retouche,
le format 20 × 24 devant de toute façon redistribuer tous les points de coupure.

CAUSE, et elle était de notre fait. L'amont protégeait déjà le couple :
`\\WebMargin` valait `\\noindent\\parbox{\\linewidth}{#1}`, et un `\\parbox` ne se
coupe pas. Le patch du `.sty` l'a rendu sécable pour qu'un grand tableau cesse de
déborder — retirant du même coup la protection des figures. `build_book.py` v0.26
la rétablit pour les seules IMAGES, via `\\DARCfigbloc` ; les tableaux restent
sécables, décision de Pierre du 26/08/2026.

POURQUOI CE SCRIPT PLUTÔT QU'UNE LECTURE DU PDF — et la leçon a été payée deux
fois. Un premier contrôle comptait les légendes ouvrant une page dans le texte
extrait. Il annonçait 8 cas. Plusieurs étaient FAUX : une photographie ne
contient aucun texte extractible, si bien que sa légende apparaît comme première
ligne de la page alors que l'image est juste au-dessus, sur la même page. C'est
mot pour mot l'erreur déjà décrite dans la docstring de `verifier_questions.py`,
commise à nouveau sur les figures.

La mesure exacte est donnée par LaTeX. `build_book.py` v0.26 pose deux `\\label`
autour de chaque figure ; LaTeX résout leur page au shipout, donc sans le
décalage qu'aurait un `\\thepage` lu pendant la composition. Les deux atterrissent
dans le `.aux` sous la forme :

    \\newlabel{DARCfig:debut:n_ionosphaere_sonnenflecken}{{}{57}{}{...}{}}
    \\newlabel{DARCfig:fin:n_ionosphaere_sonnenflecken}{{}{58}{}{...}{}}

Il suffit de comparer les deux numéros de page.

Le séparateur est « : » et non « @ » comme pour les questions : les repères de
figure passent par `fix_latex()`, dont la sanitisation des `\\label` remplace tout
caractère hors `[A-Za-z0-9_:.-]`. Le marqueur lui-même la subit — un ident à
umlaut voit son « ä » devenir « - » — mais les deux repères d'une même figure la
subissent à l'identique, et l'appariement se fait sur la forme trouvée dans le
`.aux`, jamais sur une forme reconstruite.

LIMITE CONNUE. Le script ne voit que ce qui a été compilé : un livre absent de
l'arbre n'est pas contrôlé, et il le dit. Il ne juge pas non plus les TABLEAUX,
qui restent volontairement sécables.

Usage :
    python verifier_figures.py                 # tous les livres présents
    python verifier_figures.py N E             # livres choisis
    python verifier_figures.py --racine <dir>

Code de retour : 1 si au moins une figure est séparée de sa légende, 0 sinon.

Licence des contenus : CC BY 4.0 — 50ohm.de-Autorenteam / DARC e. V.

Version : v0.1 (26/08/2026)
"""
import argparse
import io
import pathlib
import re
import sys

# La console Windows est en cp1252 et le corpus cite des idents à umlaut : sans
# cette reconfiguration, le script plante AU MILIEU de son verdict et rend un
# code de retour indiscernable d'un rc=1 légitime (cf. CLAUDE.md §11).
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

LIVRES = ["N", "E", "A", "NEA", "SWL"]

# \newlabel{DARCfig:debut:<ident>}{{<num>}{<page>}...}
MOTIF = re.compile(
    r"\\newlabel\{DARCfig:(debut|fin):([^}]+)\}\{\{[^}]*\}\{(\d+)\}"
)


def pages_des_reperes(aux: pathlib.Path):
    """Rend {ident: {'debut': page, 'fin': page}} pour un fichier .aux."""
    reperes = {}
    for bout, ident, page in MOTIF.findall(aux.read_text(encoding="utf-8", errors="replace")):
        reperes.setdefault(ident, {})[bout] = int(page)
    return reperes


def controler(racine: pathlib.Path, livres):
    total_figures = 0
    coupees = []
    examines = []

    for livre in livres:
        aux = racine / f"build-{livre}" / f"book-{livre}.aux"
        if not aux.exists():
            print(f"=== livre {livre} : pas de .aux, non contrôlé ===")
            continue
        reperes = pages_des_reperes(aux)
        if not reperes:
            print(f"=== livre {livre} : aucun repère de figure ===")
            print("    (compilé par une version antérieure à build_book.py v0.26 ?)")
            continue

        examines.append(livre)
        incomplets = [i for i, p in reperes.items() if "debut" not in p or "fin" not in p]
        rompues = [
            (i, p["debut"], p["fin"])
            for i, p in sorted(reperes.items())
            if "debut" in p and "fin" in p and p["debut"] != p["fin"]
        ]
        total_figures += len(reperes)
        coupees.extend((livre, *r) for r in rompues)

        print(f"=== livre {livre} : {len(reperes)} figures repérées ===")
        print(f"  figures coupées : {len(rompues)}")
        if incomplets:
            # Un repère isolé signale une figure dont l'un des deux \label n'a
            # pas été écrit : ce n'est pas une coupure, mais ce n'est pas normal.
            print(f"  repères incomplets : {len(incomplets)} -> {', '.join(incomplets[:5])}")
        for ident, d, f in rompues:
            print(f"    {ident} : image p.{d}, légende p.{f}")
        print()

    if not examines:
        # rc=2, et surtout PAS rc=0. Un contrôle qui n'a rien pu mesurer ne
        # contrôle rien : rendre « tout va bien » serait exactement le piège
        # décrit au §12 du CLAUDE.md, où sonde_dessins.py rendait rc=0 en toute
        # bonne foi pendant que 39 dessins étaient fautifs.
        print("Aucun livre contrôlé — AUCUN VERDICT RENDU.")
        print("Compiler d'abord (build_book.py v0.26 ou plus récent), puis relancer.")
        return 2

    if coupees:
        print(f"{len(coupees)} figure(s) séparée(s) de leur légende, sur {total_figures} :")
        for livre, ident, d, f in coupees:
            print(f"  {livre}/{ident} : image p.{d}, légende p.{f}")
        return 1

    print(f"Aucune figure n'est séparée de sa légende ({total_figures} contrôlées).")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("livres", nargs="*", default=None,
                    help=f"livres à contrôler (défaut : {' '.join(LIVRES)})")
    ap.add_argument("--racine", default=".", help="racine du dépôt")
    args = ap.parse_args()

    livres = args.livres if args.livres else LIVRES
    inconnus = [c for c in livres if c not in LIVRES]
    if inconnus:
        print(f"Livre(s) inconnu(s) : {', '.join(inconnus)}")
        print(f"Attendu : {', '.join(LIVRES)}")
        return 2

    return controler(pathlib.Path(args.racine), livres)


if __name__ == "__main__":
    sys.exit(main())
