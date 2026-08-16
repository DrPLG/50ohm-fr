#!/usr/bin/env python3
# Docstring en chaîne brute (r"""...) : elle cite abondamment des macros LaTeX
# (\qty, \lambda, \drawings...) que Python interpréterait sinon comme des
# séquences d'échappement — SyntaxWarning à chaque exécution.
r"""
build_book.py — Génère un livre PDF (via LaTeX/LuaLaTeX) à partir des contenus 50ohm.de.

Ce script est le « chef d'orchestre » manquant du dépôt public : il assemble les
sections DARCdown en un document maître LaTeX basé sur la classe FiftyOhm du
dépôt de contenus, puis le compile avec latexmk (LuaLaTeX).

Usage :
    python3 build_book.py --edition N --input /chemin/50ohm-contents-dl \
                          --output build-book [--no-compile] [--limit-chapters 2]

Licence des contenus : CC BY 4.0 — 50ohm.de-Autorenteam / DARC e. V.

Version du script : v0.20
    v0.20 — Page de titre des éditions combinées : filigrane EMPILÉ.

            Le bandeau de droite fait 0,34 de la largeur du papier, soit 71 mm
            en A4. La v0.9 réduisait le corps du filigrane à mesure que le
            nombre de lettres augmentait — 220 pt pour une, 150 pour deux,
            105 pour trois. Mesuré sur épreuve par Pierre : « NEA » à 105 pt
            débordait ENCORE, le N mordant sur la zone blanche à gauche et le A
            se faisant couper au bord droit de la page.

            Dès deux lettres, elles sont désormais empilées une par ligne,
            centrées sur l'axe du bandeau et calées en haut. Chaque lettre
            garde un corps de 150 pt et reste lisible à l'endroit. Une lettre
            seule ne change pas : 220 pt, à sa place d'origine.

            Trois dispositions ont été composées et comparées sur épreuve —
            à plat, pivotée à 90°, empilée — avant la décision.

    v0.19 — Version a.2, feuille d'arbitrage nº 4 (B1). Une seule ligne, mais
            elle répare un défaut qui touchait UN ÉNONCÉ SUR QUATRE.

            L'amont demande déjà le gras mathématique pour les énoncés de
            question (\\newkomafont{questiontext}{\\bfseries\\boldmath}). Mais
            settings.tex charge unicode-math sans déclarer de version
            mathématique grasse : sous unicode-math, \\boldmath est alors sans
            effet, et SANS AUCUN AVERTISSEMENT. Tout nombre composé en mode
            mathématique restait donc maigre au milieu d'un énoncé gras.

            Le parseur amont rendant « 230 V » par « $230$\\,V », le défaut
            touchait 418 énoncés — N 102, E 122, A 194. Relevé par Pierre sur
            trois questions du livre E, puis compté sur les trois classes.

            Correctif : \\setmathfont[version=bold, FakeBold=2]{Libertinus Math}
            après \\input{settings.tex}. Libertinus Math n'ayant pas de fonte
            grasse compagne, le gras est synthétique.

            *Piège rencontré :* le premier diagnostic visait la définition de
            \\Question. Elle était hors de cause — l'amont fait déjà ce qu'il
            faut, et c'est la CONFIGURATION DES POLICES qui rendait sa demande
            inopérante. Vérifié sur document réduit : sans la ligne le nombre
            reste maigre, avec elle il suit l'énoncé.

    v0.18 — Version a.2, feuille d'arbitrage nº 2 (B1, B6). Suite directe de la
            v0.17 : une fois les 950 figures des trois livres ramenées dans leur
            gabarit par le clamp d'images, il restait 180 débordements
            horizontaux. Leur inventaire, cause par cause, donne :

              tableau en marge            123    figure en marge          11
              formule hors texte en marge  25    texte courant (marge)     4
              texte courant (corps)        14    tableau (corps)           3

            B1 — CLAMP DES BLOCS INSÉCABLES. 151 des 180 cas sont du contenu
            qui ne se coupe jamais — un « tabular » est une hbox, une formule
            hors texte aussi — placé dans la colonne de marge, large de 52 mm.
            Pires cas : 168,9 pt (59 mm) pour un tableau de sender_messungen,
            97,2 pt pour une formule de modulatoren. Le clamp mesure le bloc
            composé et ne réduit que ce qui dépasse vraiment. Étendu aux
            formules sur décision de Pierre : sur la classe A, elles sont la
            famille dominante (18 cas sur 33).

            B6 — CONTRÔLE EXACT DES QUESTIONS COUPÉES. La vérification par
            extraction du texte du PDF est bruitée : le contenu des figures de
            marge s'intercale en début de ligne et masque les lettres de
            réponse, ce qui produisait douze faux positifs sur la classe N.
            Chaque question porte désormais deux \label — un à l'énoncé, un
            après le tableau des réponses. Comparer leurs pages est exact, et
            se lit directement dans le .aux, sans code LaTeX de comparaison :
            verifier_questions.py s'en charge.
    v0.17 — Version a.2, feuille d'arbitrage nº 1 (A1 à A4). Quatre corrections
            de CLASSE, décidées après mesure, qui remplacent une quarantaine de
            retouches page à page.

            A1 — TYPOGRAPHIE FRANÇAISE. Le .sty amont fait
            \PassOptionsToPackage{ngerman}{babel} : les trois livres français
            étaient composés avec la césure et les espacements ALLEMANDS.
            Mesuré par \showhyphens : « ali-men-ta-ti-on », « ray-onne-ment »
            (coupures allemandes, fautives en français) contre
            « ali-men-ta-tion », « rayon-ne-ment » sous french.
            Corrigé par \babelprovide[import, main, transforms=punctuation.space],
            c'est-à-dire le mode MODERNE de babel, propre à LuaTeX : les espaces
            fines avant « : ; ! ? » sont insérées par transformation de NŒUDS,
            sans rendre aucun caractère actif — contrairement à french.ldf
            (frenchb), dont les catcodes actifs entrent en conflit avec la
            syntaxe à deux-points de siunitx, tcolorbox, circuitikz et pgfplots,
            tous massivement présents dans le corpus.
            Chaque règle du transform insère « penalty = 10000 » AVANT l'espace :
            la ponctuation haute ne peut plus se retrouver en début de ligne.
            Effet mesuré sur « alpha : beta ; gamma ! delta ? » :
            128,39 pt en allemand contre 124,89 pt en français.
            Le transform est attaché à la locale : le contenu allemand résiduel
            conserve sa typographie correcte.
            Conventions françaises complètes ajoutées explicitement (décision de
            Pierre) : puces en tiret cadratin, listes resserrées, séparateur de
            légende « Fig. 1 -- ». Elles sont écrites ici plutôt qu'héritées de
            frenchb, ce qui évite d'embarquer ses redéfinitions intrusives.

            A2 — CLAMP DE \DARCimage. Le clamp v0.12 ne « bornait pas seulement
            la largeur » comme le disait le CHANGELOG : il ne bornait RIEN, et
            par-dessus il rapetissait.
              (a) Aveugle. Il mesurait \wd d'une boîte contenant déjà le
                  \makebox[\linewidth] final de la macro amont : sa mesure valait
                  donc TOUJOURS \linewidth. Mesuré sur quatre dessins d'essai, du
                  minuscule au démesuré : 147,95 pt en marge et 335,74 pt dans le
                  corps, sans une seule variation. C'est aussi pourquoi la
                  tentative « adjustbox/max size » notée en v0.12 était
                  inopérante : elle s'appliquait par-dessus le makebox.
              (b) Actif à tort. Dès que la cible est inférieure à \linewidth, la
                  condition est vraie par construction et \resizebox réduit une
                  figure qui ne débordait pas — au CARRÉ du facteur : 0.5 donnait
                  25 % au lieu de 50 %. 242 appels concernés (N 27, E 111, A 104).
                  Cause des « colonnes écrasées » et des « figures trop petites »
                  de la relecture.
              (c) Sans plafond de hauteur. Un dessin de 1567 pt (553 mm) passait
                  intact dans une page utile de 711 pt.
            Ampleur réelle, mesurée dessin par dessin sur la classe N et croisée
            avec le placement effectif : 50 des 67 images de NOTE DE MARGE
            débordent, jusqu'à +27,9 mm sur une colonne de 52 mm ; 7 des 89
            images de corps, au plus +4,5 mm.
            Corrigé en mesurant la boîte que produit l'autoscale amont
            (\l_ptxcd_image_box) AVANT tout \makebox, puis en bornant largeur ET
            hauteur.

            A3 — REMPLISSAGE VERTICAL. Le livre composait en \flushbottom
            (mesuré : \@textbottom = \relax), alors que la classe amont
            FiftyOhm.cls fait \raggedbottom — BOOK_CLASS ne l'avait pas repris.
            En \flushbottom, le blanc laissé par un objet insécable renvoyé à la
            page suivante est DISTRIBUÉ entre les paragraphes au lieu d'être
            rassemblé en bas de page : 93 pages « Underfull \vbox » en N (dont 78
            au badness maximal de 10000), 41 en E, 172 en A. Ce sont les « grandes
            zones de vide » de la relecture.

            A4 — QUESTIONS COUPÉES DE LEURS RÉPONSES. Dans le .sty amont,
            l'énoncé est composé en paragraphe et les quatre réponses dans un
            « tabular » — un bloc insécable. La DARCQuestionBox étant
            « breakable », la jointure énoncé/tableau est le SEUL point de
            coupure de toute la boîte : d'où la régularité du défaut (au moins 19
            occurrences relevées en classe N, non recensées au-delà de la p. 100).
            Corrigé par une pénalité infranchissable à cette jointure.
    v0.16 — fix_latex() : \qty{0.05}{\lambda} -> \num{0.05}\,\lambda.
            Symétrique du correctif v0.14, mais la macro est ici dans l'UNITÉ
            et non dans le nombre. \lambda n'étant pas une unité siunitx, elle
            est composée dans la police de texte droite, où le glyphe U+1D706
            manque à Libertinus Serif : le lambda disparaît du PDF SANS erreur
            de compilation (simple « Missing character » dans le journal), et
            le lecteur lit « au moins 0,05 » sans unité. Idiome amont, présent
            dans antennenformen_3 depuis une évolution amont de l'été 2026 ;
            la source n'est pas touchée. \num{} est conservé pour garder la
            virgule décimale française.
    v0.15 — Fork optionnel des dessins côté français. Un dessin amont
            (contents/drawings/<id>.tex) est du TikZ/pgfplots : le texte
            allemand qu'il affiche (légendes d'axes, libellés de nœuds) est
            du texte LaTeX, mais contrairement aux sections, rien ne
            permettait jusqu'ici de lui substituer une version française —
            le script copiait toujours l'amont sans jamais regarder
            --translations. Ajout d'un sous-dossier dessins/ à côté de
            sections/ dans chaque répertoire --translations, avec la MÊME
            priorité que pour les sections (premier répertoire cité
            l'emporte en cas de doublon). Un dessin non forké continue de
            sortir tel quel depuis l'amont, sans avertissement : c'est le
            cas par défaut, aucune traduction de dessin n'existe encore.
            cf. docs/ANALYSE-DESSINS.md pour l'inventaire et la méthode de
            suivi de la dérive amont (hors du périmètre de ce script).
    v0.14 — fix_latex() : \\qty{120\\pi}{\\ohm} -> 120\\pi\\,\\unit{\\ohm}. siunitx v3
            rejette un nombre contenant une macro (« Invalid number '120\\mitpi' »)
            puis part en runaway argument : la compilation de la classe A échouait
            (rc=12) sur nahfeld et naeherungsformel_2. Idiome présent dans la source
            amont ; correction côté script, la source n'est pas touchée.
    v0.13 — BOOK_CLASS : garde-fou sur la hauteur des notes de marge. La classe A
            ne produisait aucun PDF (« Float too large for page », puis
            « Package marginfix Error: lost some margin notes »).
            CAUSE : dans latex.ltx, \\marginpar se termine par \\end@float
            (via \\@xympar) et subit donc \\@largefloatcheck — une note de marge
            EST un flottant pour LaTeX, d'où un message parlant de flottant alors
            qu'aucun n'apparaît dans le contenu rendu. \\@largefloatcheck n'écrête
            qu'une COPIE (\\@currbox) ; la boîte placée (\\@marbox) garde sa
            hauteur, et marginfix ne peut jamais loger une note plus haute que sa
            colonne : il la conserve puis lève l'erreur fatale. Les dessins 1096
            et 687 étaient hors de cause : le coupable est le <indepth> unique et
            volumineux qui les englobe (fehlerkorrektur : 911,49 pt mesurés pour
            \\textheight = 711,32 pt).
            PARADE : \\DARCmarginpar mesure la note à \\marginparwidth, sans effet
            de bord (compteurs restaurés via \\cl@@ckpt, \\protected@write
            neutralisé, \\label et \\index désactivés le temps de la mesure) ;
            au-delà de \\DARCmarginmaxheight (= \\textheight par défaut), la note
            est composée dans le corps du texte en tcolorbox sécable, comptée
            (DARCmargindemoted) et signalée nominativement dans le journal.
            Ce garde-fou couvre aussi, de façon générique, la classe de défauts
            traitée au cas par cas en v0.12 (dessin 202).
    v0.12 — Précompilation des dessins dont l'axe pgfplots fixe ses propres
            dimensions (202 : 21 x 29 cm). L'autoscale DARC ne les atteint pas et
            le clamp de \\DARCimage ne contrôle que la largeur : en note de marge,
            la figure devenait inplaçable, marginfix perdait cette note et toutes
            les suivantes, et la classe E ne compilait plus du tout
            (« lost some margin notes », aucun PDF produit). Le dessin est
            désormais compilé isolément à 52 mm et remplacé par un
            \\includegraphics. Échec de précompilation : avertissement, dessin
            laissé tel quel, chaîne poursuivie.
    v0.11 — Localisation du paquet « renderer », qui vient du dépôt GÉNÉRATEUR
            et non du dépôt de contenus. Le script le cherche désormais dans son
            propre dossier, le dossier courant, leurs parents et leurs
            sous-dossiers immédiats, et place le dossier trouvé en tête de
            sys.path — ce qui neutralise au passage un paquet homonyme installé
            dans site-packages. La variable OHM_RENDERER force l'emplacement.
            À défaut, diagnostic explicite en rc=2 au lieu d'un Traceback :
            distingue paquet absent et paquet incomplet, compte les fichiers,
            nomme les manquants, repère un dossier imbriqué, et signale un
            homonyme servi depuis l'extérieur.
    v0.10 — 1. --translations devient répétable. Les éditions combinées NE, EA
              et NEA tirent leurs sections de plusieurs classes : un seul
              répertoire ne pouvait pas les couvrir. En cas de doublon, le
              premier répertoire cité l'emporte ; titles.json et questions.json
              sont fusionnés selon la même priorité.
           2. Rapport de couverture : une section sans fichier français sortait
              EN ALLEMAND sans un mot. Le script compte désormais les manquantes
              et le signale — défaut invisible autrement sur une édition
              combinée, le livre compilant sans erreur.
           3. Filigrane de la page de titre : corps adapté au nombre de lettres.
              « NEA » à 220 pt débordait de la page.
    v0.9 — 1. --front-matter : pièces liminaires DARCdown rendues en chapitre non
              numéroté et inscrit au sommaire (avant-propos, remerciements,
              avertissement). Option répétable, syntaxe « TITRE=fichier » ;
              l'ordre des options fixe l'ordre des pages. Les intertitres passent
              en variantes étoilées : sous un \\chapter* le compteur de chapitre
              vaut 0 et ils se numéroteraient « 0.0.1 ».
           2. \\cleardoublepage en fin de document : pagination PAIRE garantie,
              exigée par tout imprimeur pour un dos carré collé. La classe N
              tombait sur 253 pages.
           Sans --front-matter, la sortie est identique à celle de la v0.8.
    v0.8 — Liens vers contents/photos : repli Windows. La création d'un lien
           symbolique y est refusée hors mode développeur ou session
           administrateur (OSError WinError 1314). Le script tente désormais,
           dans l'ordre : lien symbolique, jonction de répertoire (mklink /J,
           sans privilège requis), puis copie en dernier recours.
    v0.7 — Contrôle des chemins --input et --translations avant tout traitement.
           Un --input erroné échouait trente lignes plus loin sur un
           FileNotFoundError « settings.tex » qui ne désignait pas la cause : le
           glob sur latex/ renvoyait une liste vide sans rien signaler. Le
           contrôle nomme le fichier attendu manquant et, si la racine du dépôt
           se trouve dans un sous-dossier (décompression ZIP imbriquée de
           GitHub), propose le bon chemin.
    v0.6 — Correctif du parasite « „, » imprimé avant CHAQUE liste à puces.
           Cause : contents/latex/settings.tex fait `\\let\\empty\\relax` juste
           après le chargement de circuitikz (contournement amont d'une double
           définition). Un paquet chargé ensuite teste `\\ifx…\\empty` ; le test
           échoue et trois virgules sont émises, que la ligature TeX transforme
           en « „ » suivi d'une virgule. Le défaut touche toutes les éditions et
           les deux langues, et passe inaperçu car il ressemble à un guillemet
           allemand. Correctif chirurgical par crochets d'environnement
           (itemize/enumerate/description) : `\\empty` retrouve sa valeur LaTeX
           dans le groupe de la liste seulement, circuitikz n'est pas touché.
    v0.5 — Balise DARCdown <france> … </france> : encart « En France » destiné aux
           compléments nationaux français ajoutés AU CONTENU ALLEMAND (aucun retrait,
           aucune réécriture du texte amont ; le complément s'ajoute, il ne remplace
           rien). Trois pièces :
             1. renderer.tag.captures : ajout de « france » à la liste blanche des
                balises reconnues par le parseur amont (sinon la balise ressort en
                texte brut « <france> » dans le PDF). Patch local, côté FR uniquement,
                le dépôt amont n'est pas modifié.
             2. BookLaTeXRenderer.render_tag() : rend la balise en environnement
                \\begin{DARCFranceBox}…\\end{DARCFranceBox}. Si le premier élément du
                bloc est un titre de niveau 1 (« # … »), il devient le sous-titre de
                l'encart.
             3. FiftyOhmBook.cls : définition de l'encart (tcolorbox sécable, bandeau
                de titre bleu, filet gauche, fond clair — lisible en niveaux de gris).
           NB : ne jamais placer de [question:…] dans un encart <france> — le renderer
           produirait une tcolorbox sécable imbriquée, que tcolorbox refuse.
    v0.4 — 1. validate_output() : garde-fou à la génération (marqueurs DARCdown non
              rendus, \\ref orphelines, clés de titles.json["sections"] qui ne sont
              pas des idents). Ces défauts ne se voyaient qu'après compilation.
           2. fix_latex() : les \\ref subissent la même normalisation d'ident que les
              \\label (sinon « figure ?? » sur les idents non-ASCII).
           3. settings.tex : clamp de largeur sur \\DARCimage — une figure plus large
              que la place demandée est réduite (l'autoscale ne pilote pas les
              width/height pgfplots). Supprime la cause racine des pertes de notes
              de marge (img/202include.tex : 21x29 cm, inplaçable).
           4. settings-pre.tex : \\extrafloats{400} ajouté automatiquement.
    v0.3 — render_unit() : prise en compte de token.prefix. En v0.2, le préfixe SI
           était perdu (« 145 MHz » était rendu « $145$\\,Hz », « 1,2 μH » -> « 1,2 H »),
           ce qui faussait les énoncés d'examen. Touchait toutes les éditions (N/E/A)
           et les deux langues.
    v0.2 — version précédente (gelée).
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import mistletoe

# v0.11 — Localisation du paquet « renderer ».
#
# Ce paquet vient du dépôt GÉNÉRATEUR (DARC-e-V/50ohm) et non du dépôt de
# contenus, confusion fréquente : 50ohm-contents-dl ne contient ni ne peut
# contenir de « renderer ». Plutôt que d'exiger une copie à côté du script, on
# le cherche aux endroits plausibles et on place le dossier trouvé EN TÊTE de
# sys.path — ce qui neutralise au passage un éventuel paquet homonyme installé
# dans site-packages, qui serait sinon servi à sa place.
#
# La variable d'environnement OHM_RENDERER l'emporte sur tout le reste. Elle
# accepte indifféremment le dossier « renderer » lui-même ou son parent.
def _localiser_renderer():
    ici = Path(__file__).resolve().parent
    candidats = []
    env = os.environ.get("OHM_RENDERER")
    if env:
        e = Path(env).expanduser()
        candidats += [e.parent if e.name == "renderer" else e]
    candidats += [ici, Path.cwd()]
    for base in (ici, ici.parent, ici.parent.parent, Path.cwd(), Path.cwd().parent):
        candidats += [base, base / "50ohm-main", base / "50ohm",
                      base / "50ohm-contents-dl-main", base / "50ohm-contents-dl"]
    vus = set()
    def _essai(c):
        try:
            c = c.resolve()
        except OSError:
            return None
        if c in vus or not c.is_dir():
            return None
        vus.add(c)
        return c if (c / "renderer" / "document.py").is_file() else None

    for c in candidats:
        if _essai(c):
            sys.path.insert(0, str(c.resolve()))
            return c.resolve()
    # Second tour, un cran plus bas : les dépôts sont souvent rangés dans un
    # dossier fourre-tout (C:\50ohm\50ohm-main\renderer), et le ZIP GitHub
    # ajoute lui-même un niveau. On explore donc les sous-dossiers immédiats
    # des racines candidates, sans jamais descendre au-delà.
    for c in list(candidats):
        try:
            enfants = sorted(p for p in c.iterdir() if p.is_dir()) if c.is_dir() else []
        except OSError:
            continue
        for enfant in enfants:
            if _essai(enfant):
                sys.path.insert(0, str(enfant.resolve()))
                return enfant.resolve()
    return None

_RENDERER_TROUVE = _localiser_renderer()

try:
    from renderer.document import Document
except ModuleNotFoundError as _e:
    _ici = Path(__file__).resolve().parent
    _pkg = _ici / "renderer"
    print("!! Le paquet Python « renderer » est introuvable ou incomplet.\n"
          f"   Erreur d'origine : {_e}", file=sys.stderr)
    print("   Rappel : « renderer » appartient au dépôt GÉNÉRATEUR\n"
          "   github.com/DARC-e-V/50ohm, et non au dépôt de contenus\n"
          "   50ohm-contents-dl, qui n'en contient pas.", file=sys.stderr)
    if _pkg.is_dir():
        _py = sorted(p.name for p in _pkg.glob("*.py"))
        print(f"   Un dossier « renderer » existe pourtant : {_pkg}\n"
              f"   Il contient {len(_py)} fichier(s) .py, alors que le paquet complet"
              f" en compte 25.", file=sys.stderr)
        for _manquant in ("__init__.py", "document.py", "fifty_ohm_latex_renderer.py"):
            if _manquant not in _py:
                print(f"   absent : renderer/{_manquant}", file=sys.stderr)
        for _sous in _pkg.iterdir():
            if _sous.is_dir() and (_sous / "document.py").exists():
                print(f"   -> le paquet réel semble être : {_sous}\n"
                      f"      (dossier imbriqué : remonter son contenu d'un niveau)",
                      file=sys.stderr)
    else:
        print(f"   Aucun dossier « renderer » ici : {_ici}", file=sys.stderr)
    # Cas le plus déroutant : un paquet HOMONYME, sans rapport avec le projet,
    # installé dans site-packages — typiquement par un « pip install renderer »
    # tenté pour réparer une erreur précédente.
    try:
        import renderer as _r
        _trouve = Path(getattr(_r, "__file__", "") or "").resolve().parent
        if _trouve and _trouve.parent != _ici:
            print(f"\n   ATTENTION : Python a servi un paquet « renderer » situé\n"
                  f"   hors du dossier de travail :\n     {_trouve}\n"
                  f"   Ce n'est pas celui du projet. S'il vient de site-packages,\n"
                  f"   c'est un homonyme sans rapport : le désinstaller\n"
                  f"   (« pip uninstall renderer ») évitera qu'il masque le bon.",
                  file=sys.stderr)
    except Exception:
        pass
    print("\n   Deux remèdes, au choix :\n"
          "     1. copier le dossier « renderer » du dépôt DARC-e-V/50ohm\n"
          "        à côté de ce script ;\n"
          "     2. indiquer son emplacement par la variable d'environnement\n"
          "        OHM_RENDERER, par exemple :\n"
          "        set OHM_RENDERER=C:\\50ohm\\50ohm-main", file=sys.stderr)
    sys.exit(2)

from renderer.fifty_ohm_latex_renderer import FiftyOhmLaTeXRenderer
from renderer.formula import Formula
from renderer.include import Include
from renderer.morse import Morse
from renderer.qso import Qso
from renderer.reference import Reference
from renderer.unit import Unit

# ---------------------------------------------------------------------------
# v0.5 — Balise <france> : liste blanche du parseur amont
# renderer.tag.Tag.start() ne reconnaît que les balises listées dans
# renderer.tag.captures ; une balise inconnue n'est pas tokenisée et ressort
# telle quelle dans le PDF. On étend la liste ICI (patch local côté FR), sans
# toucher au dépôt amont. La liste est relue à chaque appel de Tag.start(),
# l'ajout à l'import suffit donc.
# ---------------------------------------------------------------------------
import renderer.tag as _renderer_tag

if "france" not in _renderer_tag.captures:
    _renderer_tag.captures.append("france")

# ---------------------------------------------------------------------------
# Renderer LaTeX étendu (le renderer public ne couvre pas tous les tokens)
# ---------------------------------------------------------------------------

UNIT_MAP = {"Ohm": "\\textOmega{}"}


UI_LANG = "de"  # habillage : renseigné depuis --lang dans main()


class BookLaTeXRenderer(FiftyOhmLaTeXRenderer):
    """FiftyOhmLaTeXRenderer + tokens manquants (Unit, Morse, Reference, Qso,
    Include, Formula) pour couvrir toute la syntaxe DARCdown des sections."""

    def __init__(self, question_renderer=None):
        # On reproduit la liste de tokens du renderer LaTeX public et on la
        # complète avec ceux du renderer HTML.
        from renderer.comment import BlockComment
        from renderer.dash import Dash
        from renderer.halfwidth_spaces import HalfwidthSpaces
        from renderer.image import Image
        from renderer.index import Index
        from renderer.nonbreaking_spaces import NonbreakingSpaces, NonbreakingSpacesDots
        from renderer.question import Question
        from renderer.quote import Quote
        from renderer.table import Table, TableBody, TableCell, TableHeader, TableRow
        from renderer.tag import Tag
        from renderer.underline import Underline

        # NB : on n'appelle PAS super().__init__ pour contrôler l'ordre des tokens
        from mistletoe.latex_renderer import LaTeXRenderer

        LaTeXRenderer.__init__(
            self,
            Dash,
            BlockComment,
            Quote,
            Unit,
            Underline,
            Morse,
            Tag,
            HalfwidthSpaces,
            NonbreakingSpaces,
            NonbreakingSpacesDots,
            Reference,
            Question,
            Image,
            Table,
            TableBody,
            TableRow,
            TableHeader,
            TableCell,
            Qso,
            Include,
            Formula,
            Index,
        )
        self.question_renderer = question_renderer

    # Images dont l'encre TikZ excède la boîte que \DARCimage leur alloue
    # (ex. 713 : cadre débordant ~6 mm à gauche dans la gouttière). Pour
    # celles-ci, on court-circuite l'autoscale : \resizebox produit une boîte
    # exactement ajustée à l'encre, ramenée à la largeur de colonne et calée
    # à gauche — placement déterministe.
    RESIZEBOX_IMAGES = {"713"}

    def render_image(self, token):
        if getattr(token, "kind", None) == "picture" and token.id in self.RESIZEBOX_IMAGES:
            return (
                f"\\resizebox{{\\linewidth}}{{!}}{{\\input{{img/{token.id}include}}}}\n"
                f"\\captionof{{figure}}{{{token.text}}}\n"
                f"\\label{{{token.marker}}}"
            )
        return super().render_image(token)

    def render_question(self, token):
        # Chaque question d'examen est placée dans une boîte à fond clair.
        inner = self.question_renderer(token.question_number)
        return f"\\begin{{DARCQuestionBox}}\n{inner}\\end{{DARCQuestionBox}}\n"

    # --- v0.5 : encart « En France » --------------------------------------

    def render_tag(self, token):
        if getattr(token, "tagtype", None) != "france":
            return super().render_tag(token)
        children = list(token.children)
        subtitle = ""
        # Un « # Titre » en tête de bloc devient le sous-titre de l'encart
        # (sinon render_heading en ferait un \subsection à l'intérieur de la boîte).
        if children and type(children[0]).__name__ == "Heading" and children[0].level == 1:
            subtitle = self.render_inner(children.pop(0)).strip()
        inner = "".join(
            x for x in (self.render(child) for child in children) if x is not None
        )
        opt = f"[{subtitle}]" if subtitle else ""
        return f"\\begin{{DARCFranceBox}}{opt}\n{inner}\n\\end{{DARCFranceBox}}\n"

    # --- tokens supplémentaires ------------------------------------------

    def render_unit(self, token):
        unit = UNIT_MAP.get(token.unit, token.unit)
        value = token.value.replace(",", "{,}")  # virgule décimale allemande
        # v0.3 — renderer.unit.Unit sépare « 145 MHz » en value=145, prefix='M',
        # unit='Hz'. Sans reprise de token.prefix, le préfixe SI disparaissait
        # silencieusement (« 2 kHz » rendu « 2 Hz ») et faussait les énoncés.
        prefix = getattr(token, "prefix", "") or ""
        if token.unit in ("°", "%"):  # jamais de préfixe SI sur ° et %
            unit = unit.replace("%", "\\%")
            return f"${value}${unit}"
        return f"${value}$\\,{prefix}{unit}"

    def render_morse(self, token):
        chars = Morse.convert_to_morse_code(token.content)
        out = []
        for char in chars:
            sym = ""
            for c in char:
                if c == 1:
                    sym += "\\MorseDit{}"
                elif c == 2:
                    sym += "\\MorseDah{}"
                else:
                    sym += "\\MorseWordSep{}"
            out.append(sym)
        return "\\mbox{" + "\\MorseCharSep{}".join(out) + "}"

    def render_reference(self, token):
        return f"\\ref{{{token.marker}}}"

    def render_qso(self, token):
        qso = ""
        for child in token.children:
            macro = "QSOother" if child.received else "QSOown"
            qso += f"\\{macro}{{{self.render_inner(child)}}}\n"
        return qso

    def render_qso_line(self, token):
        return self.render_inner(token)

    def render_include(self, token):
        # Applets interactifs web : remplacés par un renvoi vers le site.
        if UI_LANG == "fr":
            return (
                "\\WebTip{Un élément interactif accompagne cette section "
                "sur \\mbox{50ohm.de}.}\n"
            )
        return (
            "\\WebTip{Zu diesem Abschnitt gibt es ein interaktives "
            "Element auf \\mbox{50ohm.de}.}\n"
        )

    def render_formula(self, token):
        f = token.formula.strip()
        # Certaines formules du contenu sont déjà des environnements
        # d'affichage complets (align*, equation*...) : ne pas les emballer.
        if f.startswith(("\\begin{split}", "\\begin{aligned}", "\\begin{gathered}")):
            return f"\\begin{{equation*}}{f}\\end{{equation*}}\n"
        if f.startswith("\\begin{"):
            return f + "\n"
        return f"\\begin{{displaymath}}{f}\\end{{displaymath}}\n"

    def render_table_header(self, token):
        # La syntaxe DARCdown autorise des colonnes sans préfixe d'alignement
        # (None) ; le renderer public plante dessus. Par défaut : gauche.
        align = "".join(a if a else "l" for a in token.alignment)
        return f"{{{align}}}\n{self.render_table_row(token)}"

    # --- ajustements ------------------------------------------------------

    def render_heading(self, token):
        # Les titres internes des sections descendent d'un niveau sous \section
        inner = self.render_inner(token)
        level = {1: "subsection", 2: "subsubsection"}.get(token.level, "paragraph")
        return f"\n\\{level}{{{inner}}}\n"

    def render_link(self, token):
        inner = self.render_inner(token)
        return f"\\href{{{self.escape_url(token.target)}}}{{{inner}}}"

    def render_document(self, token):
        # Pas de préambule ni de \begin{document} : fragment inclus via \input
        self.footnotes.update(token.footnotes)
        return self.render_inner(token)


# ---------------------------------------------------------------------------
# Rendu des questions d'examen
# ---------------------------------------------------------------------------


class QuestionBuilder:
    """Produit le code \\Question* pour un numéro de question BNetzA."""

    LAYOUT_FALLBACK = {
        # Macros absentes des fichiers LaTeX publics -> alias raisonnables
        "QuestionPictureLeft": "QuestionMD",
        "QuestionPictureTwo": "QuestionTwoCol",
        "QuestionFourCol": "QuestionTwoCol",
        "QuestionPictureSmall": "QuestionMD",
    }

    def __init__(self, contents: Path, renderer_factory, translations: dict | None = None):
        katalog = json.loads(
            (contents / "contents/questions/fragenkatalog3b.json").read_text(encoding="utf-8")
        )
        self.metadata = json.loads(
            (contents / "contents/questions/metadata3b.json").read_text(encoding="utf-8")
        )
        layout_file = contents / "contents/metadata/question_layout.json"
        self.layouts = json.loads(layout_file.read_text(encoding="utf-8")) if layout_file.exists() else {}
        self.renderer_factory = renderer_factory
        self.translations = translations or {}  # {numéro: {question, answer_a..d}}
        self.missing = set()
        self.n_translated_q = 0

        self.questions = {}
        for exampart in katalog["sections"]:
            for chapter in exampart["sections"]:
                for q in chapter.get("questions", []):
                    self.questions[q["number"]] = q
                for section in chapter.get("sections", []):
                    for q in section.get("questions", []):
                        self.questions[q["number"]] = q

    def _inline(self, text: str) -> str:
        """Markdown -> LaTeX pour un fragment (texte de question/réponse)."""
        # Math display \[...\] du catalogue officiel : mistletoe le prendrait
        # pour des échappements ; on le convertit en math inline protégé.
        text = text.replace("\\[", "$").replace("\\]", "$").replace("30 Ohm\\cdot", "\\qty{30}{\\ohm}\\cdot")
        with self.renderer_factory() as renderer:
            out = renderer.render(Document([text]))
        # \newline casse les cellules de questiontabular ; \par y est sûr.
        return fix_latex(out.strip().replace("\\newline", "\\par "))

    def _answer(self, question, metadata, letter, ascale):
        pic = metadata.get(f"picture_{letter}", "")
        if pic:
            return f"\\DARCimage{{{ascale}\\linewidth}}{{{pic}include}}"
        return self._inline(question.get(f"answer_{letter}", ""))

    def build(self, number: str) -> str:
        question = self.questions.get(number)
        metadata = self.metadata.get(number)
        if question is None or metadata is None:
            self.missing.add(number)
            return f"% Frage {number} nicht gefunden\n"

        # Traduction française : remplace le texte allemand quand disponible.
        tr = self.translations.get(number)
        if tr:
            question = {**question, **{k: v for k, v in tr.items() if v}}
            self.n_translated_q += 1

        layout = self.layouts.get(number, {})
        macro = layout.get("type") or ("QuestionMD" if metadata.get("picture_a") else "Question")
        macro = self.LAYOUT_FALLBACK.get(macro, macro)
        qscale = layout.get("qscale", 0.5)
        ascale = layout.get("ascale", 0.5)

        qtext = self._inline(question["question"])
        qpic = ""
        if metadata.get("picture_question"):
            qpic = (
                f"\\par\\DARCimage{{{qscale}\\linewidth}}"
                f"{{{metadata['picture_question']}include}}"
            )

        answers = [self._answer(question, metadata, letter, ascale) for letter in "abcd"]

        return (
            f"\\{macro}{{{number}}}{{{qtext}}}{{{qpic}}}"
            f"{{{answers[0]}}}{{{answers[1]}}}{{{answers[2]}}}{{{answers[3]}}}\n"
        )


# ---------------------------------------------------------------------------
# LaTeX auxiliaire : classe livre + compatibilité
# ---------------------------------------------------------------------------

BOOK_CLASS = r"""\ProvidesClass{FiftyOhmBook}
% Classe « livre » dérivée de FiftyOhm.cls (une colonne, marges identiques).
\disable@package@load{physics}{}
\LoadClass[ngerman,10pt,twoside,open=right,twocolumn=false,fontsize=10pt,parskip=half-,listof=leveldown,bibliography=leveldown]{scrreprt}

\input{settings-pre.tex}

\RequirePackage{DARC-ausbildungsmaterialien}
\RequirePackage{csquotes}
\providecolor{DARClightgray}{cmyk}{0,0,0,.1}

% ---------------------------------------------------------------------------
% v0.17 (A1) — Typographie française.
%
% Le .sty ci-dessus fait \PassOptionsToPackage{ngerman}{babel} : sans ce qui
% suit, tout le livre français est coupé selon les règles ALLEMANDES.
% Mesuré : « ali-men-ta-ti-on » et « ray-onne-ment » au lieu de
% « ali-men-ta-tion » et « rayon-ne-ment ».
%
% On emploie le mode MODERNE de babel plutôt que french.ldf (frenchb) : sous
% LuaTeX, les espaces fines avant « : ; ! ? » sont insérées par transformation
% de NŒUDS, et non en rendant ces caractères actifs. Le corpus est saturé de
% siunitx, tcolorbox, circuitikz et pgfplots, dont la syntaxe de clés repose
% sur le deux-points : un « : » actif y serait une source de conflits.
%
% Chaque règle du transform insère « penalty = 10000 » avant l'espace : la
% ponctuation haute ne peut plus basculer en début de ligne.
% Le transform est attaché à la LOCALE : le contenu allemand résiduel garde
% ses espacements corrects.
% ---------------------------------------------------------------------------
\babelprovide[import, main, transforms = punctuation.space]{french}

% ---------------------------------------------------------------------------
% v0.17 (A1) — Le transform et les dessins TikZ ne s'entendent pas.
%
% Sur un nœud pgf sans police résolue, le moteur de transforms casse :
%   babel-transforms.lua:462: attempt to index a nil value (local 'base_font')
% La compilation de la classe N s'arrêtait au dessin 587 (circuitikz), sans
% produire de PDF. Reproduit isolément sur ce seul dessin ; 579 dessins du
% corpus emploient circuitikz, l'exposition est donc générale.
%
% \disablelocaletransform agit par ATTRIBUT, donc localement au groupe de
% l'environnement : le texte courant garde ses espaces fines. Vérifié par
% mesure — hors dessin, « alpha : beta ; gamma ! delta ? » fait toujours
% 124,89 pt (contre 128,39 pt sans transform).
%
% La garde \@ifundefined est indispensable : babel lève une erreur
% « transform-not-available » si le transform n'est pas défini pour la langue
% courante, et un dessin peut être composé sous ngerman.
% ---------------------------------------------------------------------------
\makeatletter
\newcommand{\DARCnotransform}{%
	\@ifundefined{bbl@ATR@punctuation.space@\languagename @}%
		{}{\disablelocaletransform{punctuation.space}}%
}
\makeatother
\AddToHook{env/tikzpicture/begin}{\DARCnotransform}
\AddToHook{env/circuitikz/begin}{\DARCnotransform}

% Conventions françaises complètes (décision de Pierre, arbitrage nº 1).
% Écrites ici plutôt qu'héritées de frenchb : on obtient l'aspect voulu sans
% embarquer ses redéfinitions de notes, de \@ et de captions.
\AddToHook{begindocument}{%
	% Puces en tiret cadratin, à tous les niveaux.
	\renewcommand{\labelitemi}{\textemdash}%
	\renewcommand{\labelitemii}{\textemdash}%
	\renewcommand{\labelitemiii}{\textemdash}%
	\renewcommand{\labelitemiv}{\textemdash}%
	% Séparateur de légende : « Fig. 1 -- légende » au lieu de « Fig. 1: ».
	\renewcommand*{\captionformat}{~\textendash~}%
}
% Listes resserrées, à la française. Réglé par crochet d'environnement plutôt
% qu'avec enumitem : le corpus place beaucoup de listes DANS des tcolorbox,
% où un paquet de listes supplémentaire ajouterait un facteur de risque.
\AddToHook{env/itemize/begin}{\setlength{\itemsep}{0pt}\setlength{\parsep}{0pt}}
\AddToHook{env/enumerate/begin}{\setlength{\itemsep}{0pt}\setlength{\parsep}{0pt}}
\AddToHook{env/description/begin}{\setlength{\itemsep}{0pt}\setlength{\parsep}{0pt}}

% v0.17 (A2) — requis par le clamp de \DARCimage, ajouté en queue de
% settings.tex ; chargé ici pour être disponible avant l'\input.
\RequirePackage{adjustbox}

\input{settings.tex}

% ---------------------------------------------------------------------------
% v0.19 (B1) — Nombres gras dans les énoncés de question.
%
% L'amont demande DÉJÀ le gras mathématique pour la police des énoncés :
%     \newkomafont{questiontext}{\bfseries\boldmath}
% (DARC-ausbildungsmaterialien.sty, l. 42). Mais settings.tex charge
% unicode-math avec \setmathfont{Libertinus Math} et ne déclare AUCUNE version
% mathématique grasse. Sous unicode-math, \boldmath est alors sans effet, et
% sans le moindre avertissement.
%
% Conséquence mesurée : tout nombre composé en mode mathématique restait maigre
% au milieu d'un énoncé gras. Le parseur amont produit « $230$\,V » pour
% « 230 V », si bien que 418 énoncés étaient concernés — N 102, E 122, A 194,
% soit un sur quatre. Relevé par Pierre sur les questions EJ109, EJ116 et
% EJ119 du livre E, puis compté sur les trois classes.
%
% Libertinus Math n'a pas de fonte grasse compagne : le gras est donc
% SYNTHÉTIQUE (FakeBold). Vérifié sur document réduit avant application — sans
% cette ligne le nombre reste maigre, avec elle il suit le gras de l'énoncé.
%
% Placé après \input{settings.tex} : unicode-math doit être chargé et la police
% mathématique normale déjà fixée.
% ---------------------------------------------------------------------------
\setmathfont[version=bold, FakeBold=2]{Libertinus Math}

% ---------------------------------------------------------------------------
% v0.17 (A3) — Remplissage vertical.
%
% La classe amont FiftyOhm.cls fait \raggedbottom ; cette classe-ci ne l'avait
% pas repris et composait donc en \flushbottom (mesuré : \@textbottom = \relax).
% Conséquence : le blanc laissé par un objet insécable renvoyé à la page
% suivante était DISTRIBUÉ entre les paragraphes au lieu d'être rassemblé en
% bas de page — 93 pages « Underfull \vbox » en N, 41 en E, 172 en A.
% ---------------------------------------------------------------------------
\raggedbottom

% Maquette A4 : 2/3 texte, 1/3 marge (notes, photos, encadrés).
% 18 + 118 (texte) + 7 (sép.) + 52 (marge) + 15 = 210 mm
\usepackage{geometry}
% twoside : « inner » = côté reliure ; la colonne de marge (marginpar) bascule
% automatiquement côté extérieur (droite sur page impaire, gauche sur page paire).
\geometry{a4paper,twoside,inner=18mm,textwidth=118mm,top=25mm,bottom=22mm,%
	marginparsep=7mm,marginparwidth=52mm}
\setlength{\marginparpush}{6pt}
% Comme dans kaobook : marginfix réordonne les \marginpar de chaque page
% pour qu'aucune note/figure de marge ne déborde sous le bas de page ;
% les notes trop basses sont remontées ou reportées à la page suivante.
\RequirePackage{marginfix}
% Folio centré sur le PAPIER (et non sur le bloc texte, décentré de 28 mm) :
% \cfoot centre sur le bloc texte ; l'espace fantôme de 56 mm déplace le centre
% optique de +28 mm (page impaire) ou -28 mm (page paire) vers le milieu du papier.
\RequirePackage[automark]{scrlayer-scrpage}
\clearpairofpagestyles
\cfoot*{\Ifthispageodd{\hspace*{56mm}}{\hspace*{-56mm}}\pagemark}
\pagestyle{scrheadings}
% Les grands schémas/tableaux peuvent déborder dans la colonne de marge,
% toujours côté EXTÉRIEUR (droite sur page impaire, gauche sur page paire) :
\AddToHook{begindocument}{%
	\renewcommand{\FullWidth}[1]{%
		\par\noindent
		\Ifthispageodd{}{\hspace*{-\dimexpr\marginparsep+\marginparwidth\relax}}%
		\begin{minipage}{\dimexpr\textwidth+\marginparsep+\marginparwidth\relax}
			#1%
		\end{minipage}\par
	}%
}

\RequirePackage{imakeidx}
\makeindex[intoc]

% ---------------------------------------------------------------------------
% Boîte des questions d'examen : fond clair, lisible aussi en niveaux de gris.
% Les couleurs sont définies pour bien contraster une fois converties en gris
% (impression N&B) : fond très clair, filet et bandeau nettement plus foncés.
% ---------------------------------------------------------------------------
\definecolor{QuestionBack}{gray}{0.955}   % fond de la boîte (gris très clair)
\definecolor{QuestionFrame}{cmyk}{.8,.15,0,.35} % filet (bleu foncé -> gris moyen)
\definecolor{QuestionRule}{gray}{0.75}    % filet séparateur question/réponses

\tcbuselibrary{skins,breakable}
\tcbset{
	questionboxstyle/.style={
		enhanced, breakable,
		colback=QuestionBack, colframe=QuestionFrame,
		boxrule=0.4pt, leftrule=2.2pt,
		arc=1.2pt, outer arc=1.2pt,
		left=6pt, right=6pt, top=5pt, bottom=5pt,
		boxsep=2pt,
		before skip=8pt, after skip=8pt,
	},
}

% Étiquette du numéro de question, en gras, contrastée en gris aussi.
\definecolor{QuestionLabel}{cmyk}{.8,.15,0,.4}
\addtokomafont{questionlabel}{\color{QuestionLabel}}

% Enveloppe de boîte pour les questions : le renderer Python entoure chaque
% bloc question de \begin{DARCQuestionBox} ... \end{DARCQuestionBox}.
% ---------------------------------------------------------------------------
% v0.6 — Parasite « „, » avant chaque liste à puces.
% settings.tex (dépôt de contenus) fait \let\empty\relax juste après circuitikz.
% Un paquet chargé ensuite compare \ifx…\empty ; le test échoue et émet trois
% virgules, que la ligature TeX rend « „ » + « , ». Résultat : un faux guillemet
% allemand devant CHAQUE itemize, dans les deux langues et toutes les éditions.
% On rend à \empty sa valeur LaTeX dans le seul groupe de la liste : circuitikz
% conserve le contournement dont il a besoin partout ailleurs.
% ---------------------------------------------------------------------------
\makeatletter
\AddToHook{env/itemize/before}{\let\empty\@empty}
\AddToHook{env/enumerate/before}{\let\empty\@empty}
\AddToHook{env/description/before}{\let\empty\@empty}
\makeatother

\newtcolorbox{DARCQuestionBox}{questionboxstyle}

% ---------------------------------------------------------------------------
% v0.5 — Encart « En France » : compléments nationaux français ajoutés au
% contenu allemand. Le repère visuel doit être IMMÉDIAT (le lecteur doit savoir
% en un coup d'œil qu'il quitte le droit allemand) et rester lisible en niveaux
% de gris : bandeau de titre foncé à texte blanc, filet gauche épais, fond clair
% distinct de celui des boîtes de questions (0,955).
% ---------------------------------------------------------------------------
\RequirePackage{etoolbox}
\definecolor{FranceBlue}{cmyk}{1,.72,0,.28}   % bleu -> gris foncé en N&B
\definecolor{FranceRed}{cmyk}{0,.85,.8,.12}   % rouge -> gris moyen en N&B
\definecolor{FranceBack}{gray}{0.985}         % fond très clair
\newcommand{\DARCFranceTitle}{En France}
\newcommand{\DARCFranceSub}[1]{\ifstrempty{#1}{}{\space\textbar\space #1}}
\newtcolorbox{DARCFranceBox}[1][]{%
	enhanced, breakable,
	colback=FranceBack, colframe=FranceBlue,
	boxrule=0.4pt, leftrule=2.6pt,
	arc=1.2pt, outer arc=1.2pt,
	left=6pt, right=6pt, top=5pt, bottom=5pt,
	boxsep=2pt,
	before skip=9pt, after skip=9pt,
	fonttitle=\sffamily\bfseries\small,
	coltitle=white, colbacktitle=FranceBlue,
	toptitle=2pt, bottomtitle=2pt,
	titlerule=1.2pt, titlerule style=FranceRed,
	title={\DARCFranceTitle\DARCFranceSub{#1}},
}
\RequirePackage{collcell}
% Décalage vertical constant entre la lettre de réponse (sans-serif gras) et le
% texte de réponse (serif), dû à la différence de métrique des polices.
\newcommand{\ptxcdLetterRaise}{8.3pt}

% Alignement des lettres de réponse (A/B/C/D) avec les réponses. La colonne
% « q » reste en fer à droite (comme d'origine) ; le décalage vertical vient
% de ce que la cellule-lettre et la cellule-réponse ne partagent pas la même
% ligne de base. On force les deux à s'aligner par le haut avec un même
% réglage \p[t] et une origine de ligne de base commune.
\AddToHook{begindocument}{%
	\expandafter\let\csname NC@find@q\endcsname\relax
	\expandafter\let\csname NC@rewrite@q\endcsname\relax
	\newcolumntype{q}{>{\raggedleft\usekomafont{questionlabel}\vspace*{-\ptxcdLetterRaise}}p{0.15\linewidth}<{\hspace*{1ex}}}%
	\expandafter\let\csname NC@find@t\endcsname\relax
	\expandafter\let\csname NC@rewrite@t\endcsname\relax
	\newcolumntype{t}{>{\RaggedRight\let\newline\\\arraybackslash\hspace{0pt}}p{0.85\linewidth}}%
}

% Unités du build interne absentes des fichiers publics :
\AddToHook{package/siunitx/after}{%
	\DeclareSIUnit{\dBd}{dBd}%
	\DeclareSIUnit{\oszidiv}{DIV}%
	\DeclareSIUnit{\milliOhm}{\milli\ohm}%
	\DeclareSIUnit{\mOhm}{\milli\ohm}%
	\DeclareSIUnit{\kiloOhm}{\kilo\ohm}%
	\DeclareSIUnit{\dBuV}{dBµV}%
	\DeclareSIUnit{\sps}{Sps}%
}
% Le contenu utilise parfois siunitx de façon non stricte (préfixe seul,
% nombres comme 10^3...) : on dégrade ces erreurs en avertissements.
\ExplSyntaxOn
\msg_redirect_module:nnn {siunitx} {error} {warning}
\ExplSyntaxOff

% Robustesse : image manquante -> encadré au lieu d'une erreur fatale.
\RequirePackage{cancel}
\RequirePackage{letltxmacro}
\AddToHook{begindocument}{%
	\providecommand{\MarginWarning}[1]{\MarginAttention{#1}}%
	\LetLtxMacro\ptxcdRealIncludegraphics\includegraphics
	\RenewDocumentCommand{\includegraphics}{O{}m}{%
		\IfFileExists{#2}{\ptxcdRealIncludegraphics[#1]{#2}}{%
		\IfFileExists{#2.png}{\ptxcdRealIncludegraphics[#1]{#2}}{%
		\IfFileExists{#2.jpg}{\ptxcdRealIncludegraphics[#1]{#2}}{%
		\IfFileExists{#2.jpeg}{\ptxcdRealIncludegraphics[#1]{#2}}{%
			\fbox{\ttfamily fehlendes~Bild:~\detokenize{#2}}}}}}%
	}%
}

% ---------------------------------------------------------------------------
% v0.18 (B1) — Clamp des BLOCS INSÉCABLES : tableaux et formules hors texte.
%
% CONSTAT, mesuré sur les trois livres a.2 après réparation du clamp d'images :
% 180 débordements horizontaux subsistent, dont 151 sont du contenu insécable
% placé dans la COLONNE DE MARGE, large de 52 mm seulement :
%
%   tableau en marge            123     tableau dans le corps         3
%   formule hors texte en marge  25     figure en marge              11
%
% Un « tabular » est une hbox : il prend sa largeur naturelle et ne se coupe
% jamais. Une formule hors texte non plus. Dans 52 mm, les plus larges sortent
% du gabarit — jusqu'à 168,9 pt (59 mm) pour un tableau de sender_messungen,
% 97,2 pt pour une formule de modulatoren.
%
% Le clamp mesure le bloc composé et ne le réduit QUE s'il dépasse réellement
% la largeur disponible. Un tableau conforme n'est pas touché. Comme pour les
% images (A2), la réduction est proportionnelle : elle diminue la taille
% apparente de la police, ce qui est le compromis accepté — un tableau lisible
% en petit vaut mieux qu'un tableau qui sort de la page.
%
% LIMITE CONNUE, mesurée : les tableaux à colonne « X » échappent au clamp.
% tabularx fixe la largeur du tableau à \linewidth par construction ; \wd vaut
% donc exactement \linewidth même quand le contenu déborde, et la comparaison
% est toujours fausse. C'est le même aveuglement que celui de l'ancien clamp
% d'images, dont la mesure était constante — ici il ne concerne qu'une forme de
% tableau.
% Un tel tableau se corrige à la SOURCE, pas ici : c'est sa colonne rigide qui
% est trop large. Cas rencontré et résolu (B2, 14/08/2026) —
% widerstand_materialien (classe E) débordait de 28 pt avec un {lX}, parce que
% « Résistances à couche d'oxyde métallique » (39 caractères) ne tient pas dans
% une colonne « l » de la marge, là où l'allemand « Metalloxidschicht-
% widerstände » (28) passait. Passer la première colonne en « X » a suffi, sans
% toucher au texte.
% ---------------------------------------------------------------------------
\newsavebox{\DARCblocbox}
\newcounter{DARCtabreduit}
\newcounter{DARCmathreduit}

% Environnement tabulaire émis par le renderer LaTeX (grab du corps avec +b
% pour rester compatible avec le scan de tabularx) :
\ExplSyntaxOn
\NewDocumentEnvironment{DARCtabular}{m +b}{
	\par\medskip\noindent
	\sbox\DARCblocbox{
		\str_if_in:nnTF {#1} {X}
			{\begin{tabularx}{\linewidth}{#1}#2\end{tabularx}}
			{\begin{tabular}{#1}#2\end{tabular}}
	}
	\ifdim\wd\DARCblocbox>\linewidth
		\stepcounter{DARCtabreduit}
		\resizebox{\linewidth}{!}{\usebox\DARCblocbox}
	\else
		\usebox\DARCblocbox
	\fi
	\par\medskip
}{}
\ExplSyntaxOff

% Formules hors texte. Le contenu est composé en \displaystyle dans une hbox,
% mesuré, puis réduit s'il déborde. displaymath n'étant pas numéroté, rien
% n'est perdu au passage. Les formules conformes sont simplement centrées,
% comme avant.
% La redéfinition est posée dans « begindocument » et NON ici : amsmath est
% chargé plus loin dans la chaîne et redéfinit displaymath, écrasant
% silencieusement toute redéfinition antérieure. Vérifié par mesure — placée
% dans le corps de la classe, elle ne se déclenchait jamais (compteur à zéro
% alors qu'une formule mesurée à 188,6 pt pour 142,3 pt disponibles aurait dû
% être réduite) ; posée dans le hook, elle agit.
\AddToHook{begindocument}{%
	\renewenvironment{displaymath}
		{\par\addvspace{\abovedisplayskip}%
		 \setbox\DARCblocbox\hbox\bgroup$\displaystyle}
		{$\egroup
		 \noindent
		 \ifdim\wd\DARCblocbox>\linewidth
			 \stepcounter{DARCmathreduit}%
			 \makebox[\linewidth][c]{\resizebox{\linewidth}{!}{\usebox\DARCblocbox}}%
		 \else
			 \makebox[\linewidth][c]{\usebox\DARCblocbox}%
		 \fi
		 \par\addvspace{\belowdisplayskip}}%
}

\makeatletter
\AddToHook{enddocument/afterlastpage}{%
	\ifnum\value{DARCtabreduit}>\z@
		\@latex@warning@no@line{\arabic{DARCtabreduit} tableau(x) reduit(s)
			pour tenir dans la largeur disponible}%
	\fi
	\ifnum\value{DARCmathreduit}>\z@
		\@latex@warning@no@line{\arabic{DARCmathreduit} formule(s) reduite(s)
			pour tenir dans la largeur disponible}%
	\fi}
\makeatother

\AddToHook{begindocument/end}{%
	% Macros du build interne absentes des fichiers publics :
	\providecommand{\MarginWebInDepth}[1]{\WebInDepth{#1}}%
	\providecommand{\QuestionPictureLeft}{\QuestionMD}%
	\providecommand{\QuestionPictureTwo}{\QuestionTwoCol}%
	\providecommand{\QuestionFourCol}{\QuestionTwoCol}%
	\providecommand{\QuestionPictureSmall}{\QuestionMD}%
}

% ---------------------------------------------------------------------------
% v0.13 (build_book.py) — Notes de marge plus hautes que la page.
%
% CAUSE. Dans latex.ltx, \marginpar se termine par \@xympar, qui appelle
% \end@float — donc \@largefloatcheck. Une note de marge est, pour LaTeX, un
% flottant : d'où le message « Float too large for page by ... » alors
% qu'aucun environnement flottant n'apparaît dans le contenu rendu.
% \@largefloatcheck ne fait qu'écrêter \ht\@currbox (une COPIE) ; la boîte
% réellement placée, \@marbox, garde sa hauteur. marginfix, qui gère une
% colonne de marge de \textheight, ne peut alors jamais la placer : il la
% conserve, puis lève « lost some margin notes » à \end{document}.
%
% PARADE. Mesurer la note à \marginparwidth ; si elle dépasse la hauteur
% disponible, la composer dans le CORPS du texte, en boîte sécable, au lieu de
% la marge. La mesure est faite sans effet de bord : compteurs restaurés,
% écritures .aux/.lof/.idx neutralisées, \label et \index désactivés.
% ---------------------------------------------------------------------------
\newsavebox{\DARCmarginfitbox}
\newlength{\DARCmarginmaxheight}
\newcounter{DARCmargindemoted}
\AddToHook{begindocument}{\setlength{\DARCmarginmaxheight}{\textheight}}
\makeatletter
\def\DARC@gobbleopt[#1]#2{}
\newcommand*{\DARC@ctrsave}{%
	\begingroup
		\def\@elt##1{\noexpand\setcounter{##1}{\the\value{##1}}}%
		\xdef\DARC@ctrrestore{\cl@@ckpt}%
	\endgroup}
\renewcommand{\DARCmarginpar}[1]{%
	\DARC@ctrsave
	\begingroup
		\let\label\@gobble
		\renewcommand{\index}{\@ifnextchar[\DARC@gobbleopt\@gobble}%
		\let\protected@write\@gobblethree
		\global\setbox\DARCmarginfitbox\vbox{%
			\hsize\marginparwidth \@parboxrestore \@marginparreset
			\setupDARCmargin #1\par}%
	\endgroup
	\DARC@ctrrestore
	\ifdim\dimexpr\ht\DARCmarginfitbox+\dp\DARCmarginfitbox\relax>\DARCmarginmaxheight
		\stepcounter{DARCmargindemoted}%
		\@latex@warning{Note de marge trop haute pour la colonne
			(\the\dimexpr\ht\DARCmarginfitbox+\dp\DARCmarginfitbox\relax\space>\space
			\the\DARCmarginmaxheight) -- composee dans le corps du texte}%
		\par\addvspace{\medskipamount}%
		\begingroup
			\tcbset{marginboxstyle/.append style={breakable}}%
			\setupDARCmargin #1\par
		\endgroup
		\addvspace{\medskipamount}%
	\else
		\marginpar{\setupDARCmargin #1}%
	\fi}
\AddToHook{enddocument/afterlastpage}{%
	\ifnum\value{DARCmargindemoted}>\z@
		\@latex@warning@no@line{\arabic{DARCmargindemoted} note(s) de marge
			composee(s) dans le corps du texte (trop hautes)}%
	\fi}
\makeatother
"""

MASTER_HEADER_DE = r"""\documentclass{FiftyOhmBook}
\begin{document}
\begin{titlepage}
	\centering
	{\Huge\bfseries 50ohm.de\par}
	\vspace{1cm}
	{\LARGE @TITLE@\par}
	\vspace{2cm}
	{\large Erstellt aus den Inhalten von 50ohm.de\par}
	{\large 50ohm.de-Autorenteam, koordiniert durch das AJW-Referat des DARC e.\,V.\par}
	\vfill
	{\small Lizenz: CC BY 4.0 --- \url{https://github.com/DARC-e-V/50ohm-contents-dl}\par}
	{\small Kompiliert am \today\par}
\end{titlepage}
\tableofcontents
"""

MASTER_HEADER_FR = r"""\documentclass{FiftyOhmBook}
% Habillage du document en français (le contenu pédagogique et les questions
% officielles BNetzA restent en allemand) :
% v0.17 (A1) — la langue principale est désormais « french » (cf. BOOK_CLASS) :
% ces redéfinitions doivent viser french, faute de quoi elles n'ont plus AUCUN
% effet. babel fournit déjà « Table des matières » et « Chapitre » ; on les
% laisse par sécurité, mais « Fig. » et « Tab. » sont de vrais choix éditoriaux
% (babel donnerait « Figure » et « Table »), tout comme l'index.
\renewcaptionname{french}{\contentsname}{Table des matières}
\renewcaptionname{french}{\chaptername}{Chapitre}
\renewcaptionname{french}{\figurename}{Fig.}
\renewcaptionname{french}{\tablename}{Tab.}
\renewcaptionname{french}{\indexname}{Index alphabétique}
\AddToHook{begindocument}{\patchcmd{\setupDARCmargin}{Abb.}{Fig.}{}{}}
% Titres des encadrés : traduits par substitution directe dans le .sty copié.
\usepackage{tikz}
\usetikzlibrary{calc}
% Couleurs de la page de titre, choisies pour rester lisibles en niveaux de gris
% (le bandeau foncé passe en gris soutenu, le texte blanc reste contrasté).
\definecolor{TitleBand}{cmyk}{.9,.55,.1,.35}   % bleu profond
\definecolor{TitleAccent}{cmyk}{.05,.8,1,0}    % rouge DARC (accent fin)
\begin{document}
\begin{titlepage}
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
	% Grand aplat vertical à droite : occupe ~1/3 de la largeur (rappel de la
	% maquette 2/3-1/3), avec la lettre de classe en filigrane.
	\fill[TitleBand] ($(current page.north east)+(0,0)$)
		rectangle ($(current page.south east)+(-0.34\paperwidth,0)$);
	% Filet d'accent à la jonction des deux zones
	\fill[TitleAccent] ($(current page.north east)+(-0.34\paperwidth,0)$)
		rectangle ($(current page.south east)+(-0.345\paperwidth,0)$);
	% Lettre(s) de classe, énorme(s), en réserve claire dans le bandeau.
	% Le nœud entier est construit côté Python : une lettre seule se pose à
	% l'horizontale, plusieurs s'empilent (cf. v0.20).
	@WATERMARK@
	% Bloc-titre dans la zone claire (2/3 gauche)
	\node[anchor=west, align=left, text width=0.55\paperwidth]
		at ($(current page.west)+(0.09\paperwidth,4.2cm)$)
		{{\fontsize{56}{58}\selectfont\bfseries 50\,Ohm}\\[10pt]
		 {\Large\color{TitleBand}\bfseries Préparation à l'examen radioamateur}};
	% Titre de l'ouvrage, sur le bandeau foncé, texte blanc
	\node[anchor=east, align=right, text=white, text width=0.30\paperwidth,
		font=\Large\bfseries]
		at ($(current page.east)+(-0.02\paperwidth,-2cm)$)
		{@TITLE@};
	% Pied de page : source, licence, date (zone claire, bas de page)
	\node[anchor=south west, align=left, font=\small, text=black!70]
		at ($(current page.south west)+(0.09\paperwidth,1.6cm)$)
		{Réalisé à partir des contenus de 50ohm.de (en allemand)\\
		 50ohm.de-Autorenteam, coordonné par le référat AJW du DARC e.\,V.\\
		 Traduit avec l'aide d'une IA par Pierre F4JWI\\[2pt]
		 Licence CC BY 4.0 --- \texttt{github.com/DARC-e-V/50ohm-contents-dl}\\
		 Version @VERSION@ --- compilée le \today};
\end{tikzpicture}
\end{titlepage}
\tableofcontents
"""

FR_TITLES = {
	"N": "Cours complet\\\\Classe N",
	"E": "Cours complet\\\\Classe E",
	"A": "Cours complet\\\\Classe A",
	"NE": "Cours complet\\\\Classes N et E",
	"EA": "Cours complet\\\\Classes E et A",
	"NEA": "Cours complet\\\\Classes N, E et A",
}
FR_CLASS_LETTER = {
	"N": "N", "E": "E", "A": "A", "NE": "NE", "EA": "EA", "NEA": "NEA",
}

MASTER_FOOTER = r"""
\printindex
% v0.9 — Tout imprimeur exige un nombre de pages PAIR pour un dos carré collé.
% \cleardoublepage ajoute une page blanche si le corps finit sur une page impaire.
\cleardoublepage
\end{document}
"""

LATEXMKRC = r"""ensure_path('TEXINPUTS', '.:./img//:');
$pdf_mode = 4;
$MSWin_back_slash = 0;
$makeindex = 'makeindex %O -o %D %S';
"""


CLAMP_DARCIMAGE = r"""

% ---------------------------------------------------------------------------
% Clamp de \DARCimage — v0.17 (A2). Réécriture complète.
%
% CE QUI N'ALLAIT PAS. Le clamp v0.12 mesurait \wd d'une boîte obtenue en
% appelant la macro amont, laquelle se termine par \makebox[\linewidth][r/c].
% Cette mesure valait donc TOUJOURS \linewidth, jamais la taille de la figure.
% Vérifié par compilation sur quatre dessins d'essai, du minuscule au
% démesuré : 147,95 pt en colonne de marge et 335,74 pt dans le corps, sans
% une seule variation. Trois conséquences :
%
%   (a) aucun débordement n'était jamais détecté — le clamp n'a jamais rien
%       clampé, et la tentative « adjustbox/max size » de la v0.12 échouait
%       pour la même raison : elle s'appliquait PAR-DESSUS le makebox ;
%   (b) dès que la cible était inférieure à \linewidth, la comparaison était
%       vraie par construction et \resizebox réduisait une figure qui ne
%       débordait pas — au CARRÉ du facteur demandé. Une figure appelée à
%       0.5\linewidth sortait à 0.25\linewidth. 242 appels concernés
%       (N 27, E 111, A 104) : ce sont les « colonnes écrasées », les « notes
%       de marge illisibles » et les « figures trop petites » de la relecture ;
%   (c) la hauteur n'était comparée à rien. Un dessin de 1567 pt (553 mm)
%       traversait intact une page utile de 711 pt.
%
% CE QUE FAIT CELUI-CI. Il mesure \l_ptxcd_image_box — la boîte que l'autoscale
% amont vient de produire, AVANT tout \makebox — et ne réduit que si elle
% dépasse réellement la largeur demandée ou le plafond de hauteur. adjustbox
% conserve les proportions et n'agrandit jamais. Une figure conforme n'est
% plus touchée du tout.
%
% AMPLEUR MESURÉE (classe N, croisée avec le placement réel de chaque image) :
% 50 des 67 images de note de marge débordaient, jusqu'à +27,9 mm sur une
% colonne de 52 mm ; 7 des 89 images de corps, au plus +4,5 mm.
% ---------------------------------------------------------------------------
\newlength{\DARCimagemaxheight}
\AddToHook{begindocument}{\setlength{\DARCimagemaxheight}{0.8\textheight}}
\newcounter{DARCimagereduite}
\ExplSyntaxOn
\dim_new:N \l__DARCfr_target_dim
\RenewDocumentCommand{\DARCimage}{sO{Bild~zur~Prüfungsfrage~\l_ptxcd_question_tl}mm}{
	\par\smallskip
	\group_begin:
		\ptxcd_image_autoscale_setup:nnn {#1} {#3} {#4}
		\dim_set:Nn \l__DARCfr_target_dim {#3}
		\bool_lazy_or:nnTF
			{ \dim_compare_p:nNn {\box_wd:N \l_ptxcd_image_box} > {\l__DARCfr_target_dim} }
			{ \dim_compare_p:nNn {\box_ht_plus_dp:N \l_ptxcd_image_box} > {\DARCimagemaxheight} }
			{
				\stepcounter{DARCimagereduite}
				\makebox[\linewidth][c]{
					\adjustbox{max~width=\l__DARCfr_target_dim,
						max~totalheight=\DARCimagemaxheight}
						{\box_use:N \l_ptxcd_image_box}
				}
			}
			{
				\dim_compare:nNnTF {\box_wd:N \l_ptxcd_image_box} > {\linewidth}
					{ \makebox[\linewidth][r]{\box_use:N \l_ptxcd_image_box} }
					{ \makebox[\linewidth][c]{\box_use:N \l_ptxcd_image_box} }
			}
	\group_end:
}
\ExplSyntaxOff
\makeatletter
\AddToHook{enddocument/afterlastpage}{%
	\ifnum\value{DARCimagereduite}>\z@
		\@latex@warning@no@line{\arabic{DARCimagereduite} figure(s) ramenee(s)
			dans leur gabarit par le clamp \string\DARCimage}%
	\fi}
\makeatother

% Note : le clamp v0.12 (\DARCfitbox + \DARCimageUnclamped) est SUPPRIMÉ, et non
% commenté. Laissé en place il redéfinissait \DARCimage après celui-ci et
% l'aurait écrasé. Son analyse complète figure ci-dessus et dans la docstring.
"""

def fix_latex(text: str) -> str:
    """Corrige des idiomes du contenu que siunitx v3 rejette."""
    text = text.replace("\\qty{\\infty}", "\\infty\\,\\unit")
    # \qty{10^5} -> \qty{e5} (notation exigée par siunitx v3)
    text = re.sub(r"\\qty\{10\^\{?(\d+)\}?\}", r"\\qty{e\1}", text)
    # v0.14 — \qty{120\pi}{\ohm} : siunitx v3 refuse un « nombre » contenant une
    # macro (« Invalid number '120\mitpi' »), puis part en runaway argument et fait
    # échouer toute la compilation. Idiome amont (nahfeld, naeherungsformel_2).
    text = re.sub(r"\\qty\{(\d*)\\pi\}\{(\\?\w+)\}", r"\1\\pi\\,\\unit{\2}", text)
    # v0.16 — \qty{0.05}{\lambda} : symétrique du cas ci-dessus, la macro est
    # cette fois dans l'UNITÉ. \lambda n'est pas une unité siunitx : passée
    # comme telle, elle est composée dans la police de texte droite, où le
    # glyphe U+1D706 est absent de Libertinus Serif. Le lambda DISPARAÎT du PDF
    # sans la moindre erreur — seulement un « Missing character » dans le
    # journal — et le lecteur lit « au moins 0,05 », sans unité.
    # Idiome amont (antennenformen_3). \num{} est conservé plutôt que le nombre
    # brut : c'est lui qui rend la virgule décimale française.
    text = re.sub(r"\\qty\{([0-9.,]+)\}\{\\lambda\}", r"\\num{\1}\\,\\lambda", text)
    # Coquilles du contenu source (à remonter upstream) :
    text = text.replace("1000 {\\mega\\hertz}", "1000\\,\\unit{\\mega\\hertz}")
    text = re.sub(r"\\qty\{([A-Za-z])\}\{", r"\1\\,\\unit{", text)
    text = text.replace("\\qty{+}{", "+\\,\\unit{")
    text = text.replace("${32}{\\milli\\watt}$", "$\\qty{32}{\\milli\\watt}$")
    # Macros d'unités utilisées brutes dans le texte (hors \unit/\qty) :
    text = re.sub(r" \\(milliOhm|mOhm|kiloOhm|dBuV|dBd)(?![A-Za-z])", r"\\,\\unit{\\\1}", text)
    # Marqueurs de labels contenant maths/espaces : assainir pour l'.aux
    _sanitize_ident = lambda s: re.sub(r"[^A-Za-z0-9_:.-]", "-", s)
    text = re.sub(r"\\label\{((?:[^{}]|\{[^{}]*\})*)\}",
                  lambda m: "\\label{" + _sanitize_ident(m.group(1)) + "}",
                  text)
    # v0.4 — Les \ref doivent subir EXACTEMENT la même normalisation, sinon un
    # ident non-ASCII produit un \label{a_st-rspektrum} orphelin face à un
    # \ref{a_störspektrum} -> « figure ?? » dans le PDF.
    text = re.sub(r"\\ref\{((?:[^{}]|\{[^{}]*\})*)\}",
                  lambda m: "\\ref{" + _sanitize_ident(m.group(1)) + "}",
                  text)
    text = text.replace("pla^it", "pla\\^{\\i}t")
    # Expression complète dans \qty : la sortir de siunitx
    text = re.sub(r"\\qty\{(\\d?frac\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})\}\{(\\?\w+)\}",
                  r"\1\\,\\unit{\2}", text)
    return text


def escape_latex(text: str) -> str:
    for a, b in [("&", "\\&"), ("%", "\\%"), ("#", "\\#"), ("_", "\\_")]:
        text = text.replace(a, b)
    return text


# ---------------------------------------------------------------------------
# Assemblage
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Précompilation des dessins hors gabarit (v0.12)
# ---------------------------------------------------------------------------

# ident du dessin -> largeur cible. La largeur de la colonne de marge est de
# 52 mm (cf. \geometry dans FiftyOhmBook.cls).
PRECOMPILE_DRAWINGS = {
    "202": "52mm",   # classe E : diagramme d'affaiblissement, axe de 21 x 29 cm
}

PRECOMPILE_WRAPPER = r"""\documentclass[border=2pt,varwidth=false]{standalone}
\usepackage{fontspec}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usepackage{siunitx}
\begin{document}
\resizebox{@WIDTH@}{!}{\input{@SOURCE@}}
\end{document}
"""


def precompile_drawing(img_dir: Path, ident: str, largeur: str) -> bool:
    """Compile img/{ident}include.tex isolément et lui substitue le PDF obtenu.

    Renvoie True si la substitution a eu lieu. En cas d'échec — lualatex absent,
    dessin refusant de compiler seul —, le dessin d'origine est laissé en place
    et un avertissement est émis : mieux vaut une figure mal placée qu'une
    chaîne cassée sans explication.
    """
    source = f"{ident}include.tex"
    cible = f"{ident}include-fig"
    wrapper = img_dir / f"{cible}.tex"
    wrapper.write_text(
        PRECOMPILE_WRAPPER.replace("@WIDTH@", largeur).replace("@SOURCE@", source),
        encoding="utf-8")
    try:
        r = subprocess.run(
            ["lualatex", "-interaction=nonstopmode", "-halt-on-error", f"{cible}.tex"],
            cwd=img_dir, capture_output=True, text=True, timeout=600)
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        print(f"!! précompilation du dessin {ident} impossible ({e}) : dessin laissé "
              f"tel quel, la mise en page peut en souffrir.", file=sys.stderr)
        return False
    if r.returncode != 0 or not (img_dir / f"{cible}.pdf").exists():
        print(f"!! précompilation du dessin {ident} en échec (rc={r.returncode}) : "
              f"dessin laissé tel quel. Voir {img_dir / (cible + '.log')}",
              file=sys.stderr)
        return False
    # Substitution : \DARCimage fait \input{img/{ident}include}, qui charge
    # désormais un simple \includegraphics à la largeur allouée.
    (img_dir / source).write_text(
        f"% Dessin précompilé par build_book.py (v0.12) : l'axe pgfplots d'origine\n"
        f"% fixait des dimensions hors gabarit, inplaçables en note de marge.\n"
        f"\\includegraphics[width=\\linewidth]{{{cible}.pdf}}\n",
        encoding="utf-8")
    print(f"   dessin {ident} précompilé à {largeur} -> {cible}.pdf")
    return True


def validate_output(out, toc, tr_titles, tr_dirs):
    """v0.4 — Garde-fou : détecte à la GÉNÉRATION les défauts qui, sinon, ne se
    voient qu'après une compilation complète (voire pas du tout).

    Trois contrôles, tous en avertissement (jamais bloquants) :
      1. Marqueurs DARCdown non rendus, restés en texte brut dans le .tex.
         Cause typique : un « : » dans une légende — le parseur amont impose
         [picture:ID:ident:légende] avec légende = [^:\\]]+ — ou un champ
         surnuméraire dans la source. Sans ce contrôle, le marqueur s'imprime
         tel quel dans le PDF.
      2. \\ref sans \\label correspondant -> « figure ?? » dans le PDF.
      3. Clés de titles.json["sections"] qui ne sont pas des idents valides.
         Piège : les chapitres sont indexés par TITRE allemand et les abstracts
         par TEXTE d'abstract, mais les sections par IDENT. Une clé « titre »
         est ignorée EN SILENCE et la section reste titrée en allemand.
    """
    n_warn = 0
    sec_files = sorted((out / "sections").glob("*.tex"))

    # 1. marqueurs non rendus (on ignore ce qui suit un % non échappé : commentaire)
    marker = re.compile(r"\[(picture|photo|question|include|ref):")
    uncommented = re.compile(r"(?<!\\)%.*$")
    for f in sec_files:
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            code = uncommented.sub("", line)
            m = marker.search(code)
            if m:
                n_warn += 1
                print(f"!! marqueur non rendu : {f.name}:{i} -> {code.strip()[:90]}",
                      file=sys.stderr)

    # 2. références orphelines
    labels, refs = set(), {}
    for f in sec_files:
        txt = f.read_text(encoding="utf-8")
        labels |= set(re.findall(r"\\label\{([^{}]*)\}", txt))
        for r in re.findall(r"\\ref\{([^{}]*)\}", txt):
            refs.setdefault(r, f.name)
    for r, fname in sorted(refs.items()):
        if r not in labels:
            n_warn += 1
            print(f"!! référence orpheline (\\ref sans \\label) : {r} ({fname})",
                  file=sys.stderr)

    # 3. clés de titles.json["sections"] : doivent être des idents du sommaire
    if tr_dirs:
        idents = {s["ident"] for c in toc["chapters"] for s in c["sections"]}
        for key in sorted(tr_titles.get("sections", {})):
            if key not in idents:
                n_warn += 1
                print(f"!! titles.json[\"sections\"] : clé « {key} » n'est pas un "
                      f"ident connu -> titre IGNORÉ (les sections s'indexent par "
                      f"ident, pas par titre allemand)", file=sys.stderr)

    # 4. v0.5 — décompte des encarts « En France » (repère de suivi) et contrôle
    #    qu'aucune question d'examen n'y a été placée (tcolorbox sécable imbriquée).
    n_fr = 0
    for f in sec_files:
        txt = f.read_text(encoding="utf-8")
        n_fr += txt.count("\\begin{DARCFranceBox}")
        for bloc in re.findall(r"\\begin\{DARCFranceBox\}.*?\\end\{DARCFranceBox\}",
                               txt, re.S):
            if "\\begin{DARCQuestionBox}" in bloc:
                n_warn += 1
                print(f"!! encart France contenant une question : {f.name} — "
                      f"tcolorbox sécable imbriquée, la compilation échouera",
                      file=sys.stderr)
    if n_fr:
        print(f"   {n_fr} encart(s) « En France » rendu(s).")

    if n_warn:
        print(f"!! {n_warn} avertissement(s) de validation.", file=sys.stderr)
    return n_warn


def link_dir(link: Path, target: Path):
    """Fait pointer `link` vers le répertoire `target`, sans le copier si possible.

    v0.8 — Windows refuse les liens symboliques aux comptes non administrateurs
    tant que le « mode développeur » n'est pas activé (OSError WinError 1314).
    On se rabat alors sur une *jonction de répertoire* (`mklink /J`), qui ne
    demande aucun privilège et convient parfaitement ici, puis, en tout dernier
    recours, sur une copie — coûteuse : contents/photos pèse près de 500 Mo et
    trois liens sont nécessaires.
    """
    if link.exists() or link.is_symlink():
        return
    link.parent.mkdir(parents=True, exist_ok=True)
    try:
        link.symlink_to(target, target_is_directory=True)
        return
    except OSError as err:
        if sys.platform != "win32":
            raise
        premiere = err

    jonction = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)],
                              capture_output=True, text=True)
    if jonction.returncode == 0 and link.exists():
        return

    print(f"!! lien symbolique refusé ({premiere}) et jonction impossible "
          f"({jonction.stderr.strip() or jonction.stdout.strip()}).\n"
          f"   Copie de {target}\n   vers {link} — patientez.", file=sys.stderr)
    shutil.copytree(target, link)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--edition", default="N", choices=["N", "E", "A", "NE", "EA", "NEA"])
    ap.add_argument("--lang", default="de", choices=["de", "fr"], help="Langue de l'habillage du document")
    ap.add_argument("--translations", action="append", default=[],
                    help="Répertoire de traductions : sections/{ident}.md + titles.json. "
                         "Répétable — indispensable pour les éditions combinées NE, EA et "
                         "NEA, dont les sections proviennent de plusieurs classes. En cas "
                         "de doublon, le premier répertoire cité l'emporte.")
    ap.add_argument("--input", "-i", required=True, help="Chemin du dépôt 50ohm-contents-dl")
    ap.add_argument("--output", "-o", default="build-book")
    ap.add_argument("--version-label", default="0.1",
                    help="numéro de version affiché sur la page de titre (fr)")
    ap.add_argument("--front-matter", action="append", default=[],
                    metavar="TITRE=FICHIER",
                    help="Pièce liminaire DARCdown rendue en chapitre non numéroté. "
                         "Répétable : l'ordre des options fixe l'ordre des pages. "
                         "Sans « TITRE= », le titre est celui de --front-matter-title.")
    ap.add_argument("--front-matter-title", default="Remerciements",
                    help="Titre par défaut d'une pièce liminaire donnée sans « TITRE= »")
    ap.add_argument("--no-compile", action="store_true", help="Générer les .tex sans compiler")
    ap.add_argument("--limit-chapters", type=int, default=0, help="Ne traiter que n chapitres (debug)")
    args = ap.parse_args()
    global UI_LANG
    UI_LANG = args.lang

    contents = Path(args.input).resolve()
    out = Path(args.output).resolve()

    # v0.7 — Contrôle des chemins AVANT tout traitement.
    # Sans ce garde-fou, un --input erroné ne produit aucune erreur à l'étape 1
    # (le glob sur latex/ renvoie simplement une liste vide) et le script échoue
    # trente lignes plus loin sur un FileNotFoundError « settings.tex », message
    # qui ne désigne pas la cause. Piège classique : les archives ZIP de GitHub
    # se décompressent en un dossier imbriqué de même nom
    # (50ohm-contents-dl-main\50ohm-contents-dl-main\).
    attendus = [
        (contents / "latex" / "settings.tex", "fichiers LaTeX du dépôt de contenus"),
        (contents / "toc" / f"{args.edition}.json", f"sommaire de l'édition {args.edition}"),
        (contents / "contents" / "sections", "sections DARCdown"),
        (contents / "contents" / "questions" / "fragenkatalog3b.json", "catalogue de questions"),
    ]
    manquants = [(p, quoi) for p, quoi in attendus if not p.exists()]
    if manquants:
        print(f"!! --input ne désigne pas la racine de 50ohm-contents-dl :\n   {contents}",
              file=sys.stderr)
        for p, quoi in manquants:
            print(f"   absent : {p}  ({quoi})", file=sys.stderr)
        if contents.is_dir():
            enfants = sorted(c.name for c in contents.iterdir() if c.is_dir())[:8]
            print(f"   sous-dossiers présents : {', '.join(enfants) or 'aucun'}",
                  file=sys.stderr)
            for c in contents.iterdir():
                if (c / "latex" / "settings.tex").exists():
                    print(f"   -> le bon chemin est probablement : {c}", file=sys.stderr)
        else:
            print("   ce chemin n'existe pas ou n'est pas un répertoire.", file=sys.stderr)
        sys.exit(2)

    for _tr in args.translations:
        tr_root = Path(_tr).resolve()
        if not (tr_root / "sections").is_dir():
            print(f"!! --translations doit désigner le répertoire contenant sections/ "
                  f"et titles.json :\n   {tr_root}", file=sys.stderr)
            if (tr_root / "N" / "sections").is_dir() or (tr_root / "E" / "sections").is_dir() \
                    or (tr_root / "A" / "sections").is_dir():
                print("   -> il manque le sous-dossier de classe à la fin du chemin "
                      f"(…\\{args.edition}).", file=sys.stderr)
            sys.exit(2)
    (out / "sections").mkdir(parents=True, exist_ok=True)
    (out / "img").mkdir(exist_ok=True)

    # tr_dirs sert dès l'étape 2 (fork des dessins) ; calculé ici plutôt qu'à
    # l'étape 4 (Renderers) où il vivait jusqu'en v0.14.
    tr_dirs = [Path(x).resolve() for x in args.translations]

    # 1. Fichiers LaTeX du dépôt de contenus
    for f in (contents / "latex").glob("*"):
        shutil.copy(f, out / f.name)

    # v0.17 (A4) — Question séparée de ses réponses.
    #
    # CONSTAT, relevé dans le PDF a.1 de la classe N : page 12, la page s'achève
    # sur l'énoncé de NA103 ; les réponses A/B/C/D sont page 13. Au moins 19 cas
    # en classe N, non recensés au-delà de la p. 100.
    #
    # MÉCANISME. \__ptxcd_question_table_head:nnn compose l'énoncé en paragraphe,
    # puis les quatre réponses arrivent dans un « tabular » — une hbox insécable,
    # donc une « ligne » de plus dans le MÊME paragraphe. La DARCQuestionBox étant
    # « breakable », la jointure entre ces deux lignes est le seul endroit où la
    # boîte puisse se rompre. Le « \\* » que pose l'amont à cette jointure ne
    # suffit pas en pratique.
    #
    # PARADE. \samepage porte \interlinepenalty (et ses variantes) à 10000 pour
    # toute la question : la coupure devient impossible entre l'énoncé et le
    # tableau. Une question qui ne tient pas dans le bas de page est reportée
    # ENTIÈRE à la page suivante — c'est A3 (\raggedbottom) qui rend le blanc
    # ainsi laissé acceptable, en le rassemblant en bas de page au lieu de le
    # distribuer entre les paragraphes. Les deux corrections se soutiennent.
    sty_q = out / "DARC-ausbildungsmaterialien.sty"
    txt_q = sty_q.read_text(encoding="utf-8")
    #
    # v0.18 (B6) — Contrôle exact des questions coupées.
    # Deux \label par question : l'un dans l'énoncé, l'autre après le tableau
    # des réponses. Si leurs pages diffèrent, la question est coupée. Cette
    # mesure est EXACTE, là où la lecture du PDF est bruitée : le texte des
    # figures de marge s'y intercale en début de ligne et masque les lettres de
    # réponse (douze faux positifs constatés sur la classe N). Les pages
    # atterrissent dans le .aux, que verifier_questions.py relit ensuite ;
    # aucun code LaTeX de comparaison n'est nécessaire.
    # Les labels ne sont jamais référencés : pas d'avertissement, et rien de
    # visible dans le PDF.
    AVANT = "\t\t\\par\n\t\t\\__ptxcd_question_table_head:nnn"
    APRES = ("\t\t\\par\\samepage\n"
             "\t\t\\label{DARCq@debut@#1}%\n"
             "\t\t\\__ptxcd_question_table_head:nnn")
    n_q = txt_q.count(AVANT)
    # Principe fondamental du projet : échec fatal sur substitution à zéro
    # correspondance. Zéro signifie que l'amont a changé sous la règle.
    if n_q != 3:
        print(f"!! A4 : {n_q} occurrence(s) de la jointure énoncé/réponses au lieu "
              f"de 3 (\\Question, \\QuestionMD, \\QuestionTwoCol).\n"
              f"   L'amont a changé sous la règle — vérifier "
              f"DARC-ausbildungsmaterialien.sty avant de compiler.", file=sys.stderr)
        sys.exit(3)
    txt_q = txt_q.replace(AVANT, APRES)

    # v0.18 (B6) — second \label, après le tableau des réponses. Une occurrence
    # par macro de question (\Question, \QuestionMD, \QuestionTwoCol).
    FIN_AVANT = "\\end{questiontabular}"
    FIN_APRES = "\\end{questiontabular}\\label{DARCq@fin@#1}"
    n_fin = txt_q.count(FIN_AVANT)
    if n_fin != 3:
        print(f"!! B6 : {n_fin} occurrence(s) de \\end{{questiontabular}} au lieu de 3.\n"
              f"   L'amont a changé sous la règle — vérifier "
              f"DARC-ausbildungsmaterialien.sty avant de compiler.", file=sys.stderr)
        sys.exit(3)
    txt_q = txt_q.replace(FIN_AVANT, FIN_APRES)

    sty_q.write_text(txt_q, encoding="utf-8")

    # v0.4 — (a) Clamp de largeur des figures.
    # L'autoscale DARC ne pilote que les unités tikz (\tikzset{x=..cm,y=..cm}) et
    # n'a AUCUN effet sur width/height d'un « axis » pgfplots : de telles figures
    # gardent leurs dimensions propres. Placées en marge (52 mm), les plus larges
    # débordent, et une figure franchement hors gabarit (img/202include.tex :
    # 21x29 cm) devient INPLAÇABLE -> marginfix perd la note ET toutes les
    # suivantes. On ceinture donc \DARCimage : si la boîte produite dépasse la
    # largeur demandée, on la réduit ; sinon on ne touche à rien (aucun changement
    # visuel pour les figures conformes, aucun agrandissement).
    settings = out / "settings.tex"
    settings.write_text(
        settings.read_text(encoding="utf-8") + CLAMP_DARCIMAGE, encoding="utf-8")

    # v0.4 — (b) \extrafloats : les livres dépassent le quota de floats par défaut.
    pre = out / "settings-pre.tex"
    pre.write_text(pre.read_text(encoding="utf-8") + "\n\\extrafloats{400}\n",
                   encoding="utf-8")

    if args.lang == "fr":
        # Titres des encadrés tcolorbox : substitution directe dans la copie
        # du .sty (les \patchcmd échouaient silencieusement).
        sty = out / "DARC-ausbildungsmaterialien.sty"
        txt = sty.read_text(encoding="utf-8")
        for de, fr in [
            ("\\space Gefahr]", "\\space Danger]"),
            ("\\space Achtung]", "\\space Attention]"),
            ("\\space Tipp]", "\\space Astuce]"),
            ("\\space Neue Einheit]", "\\space Nouvelle unité]"),
            ("\\space Vertiefung}", "\\space Approfondissement}"),
        ]:
            txt = txt.replace(de, fr)
        # \WebMargin compose dans le corps du texte via \parbox (insécable) :
        # un grand tableau y débordait sous le bas de page. On le rend sécable.
        txt = txt.replace(
            "\t\\noindent\\parbox{\\linewidth}{#1}\n",
            "\t\\noindent #1\\par\n",
        )
        sty.write_text(txt, encoding="utf-8")
    (out / "FiftyOhmBook.cls").write_text(BOOK_CLASS, encoding="utf-8")
    (out / "latexmkrc").write_text(LATEXMKRC, encoding="utf-8")

    # 2. Dessins TikZ -> img/{id}include.tex (convention \DARCimage)
    #
    # v0.15 — fork optionnel : traductions/<CLASSE>/dessins/<id>.tex prime sur
    # l'amont s'il existe, même priorité que pour sections/ (premier
    # répertoire --translations cité qui contient le fichier l'emporte).
    n_dessins_forkes = 0
    for f in (contents / "contents/drawings").glob("*.tex"):
        src = f
        for d in tr_dirs:
            candidat = d / "dessins" / f.name
            if candidat.exists():
                src = candidat
                n_dessins_forkes += 1
                break
        shutil.copy(src, out / "img" / f"{f.stem}include.tex")

    # v0.12 — Précompilation des dessins hors gabarit.
    #
    # Certains dessins fixent leurs dimensions DANS l'axe pgfplots
    # (« width=21cm, height=29cm » pour le 202, diagramme d'affaiblissement des
    # câbles de la classe E). L'autoscale DARC ne pilote que les unités tikz et
    # n'a aucune prise sur ces clés ; le clamp de \DARCimage, lui, ne compare que
    # la LARGEUR et laisse passer une hauteur de 29 cm. Placée en note de marge,
    # une telle figure est INPLAÇABLE : « Float too large for page », puis
    # marginfix perd cette note ET toutes les suivantes — dont les encadrés
    # « danger de mort » — et la compilation échoue sur « lost some margin notes ».
    #
    # Remède : compiler le dessin isolément, à la largeur de la colonne de marge,
    # et substituer un \includegraphics du PDF obtenu. Les proportions sont
    # conservées, la hauteur devient compatible, et le reste de la chaîne
    # n'y voit que du feu.
    for ident, largeur in PRECOMPILE_DRAWINGS.items():
        src = out / "img" / f"{ident}include.tex"
        if not src.exists():
            continue
        precompile_drawing(out / "img", ident, largeur)

    # 3. Photos (répertoires foto/ et img/foto/ attendus par les macros)
    for link in [out / "foto", out / "img" / "foto", out / "photo"]:
        link_dir(link, contents / "contents/photos")

    # 4. Renderers
    q_translations = {}
    # Fusion en ordre INVERSE : le premier répertoire cité écrase les suivants,
    # ce qui rend la priorité conforme à celle de la recherche des sections.
    for d in reversed(tr_dirs):
        if (d / "questions.json").exists():
            q_translations.update(json.loads((d / "questions.json").read_text(encoding="utf-8")))
    qb = QuestionBuilder(contents, lambda: BookLaTeXRenderer(), translations=q_translations)
    question_renderer = qb.build

    toc = json.loads((contents / "toc" / f"{args.edition}.json").read_text(encoding="utf-8"))

    # Traductions : fichiers parallèles optionnels
    tr_titles = {"chapters": {}, "sections": {}, "abstracts": {}}
    for d in reversed(tr_dirs):
        if (d / "titles.json").exists():
            for cle, valeurs in json.loads((d / "titles.json").read_text(encoding="utf-8")).items():
                tr_titles.setdefault(cle, {}).update(valeurs)
    n_translated = 0

    if args.lang == "fr":
        title = FR_TITLES[args.edition]
        header = MASTER_HEADER_FR.replace("@TITLE@", title)
        lettres = FR_CLASS_LETTER[args.edition]
        # v0.20 — Filigrane de la page de titre : EMPILÉ dès deux lettres.
        #
        # Le bandeau de droite fait 0,34 de la largeur du papier, soit 71 mm en
        # A4. Une lettre seule y tient à 220 pt. Réduire le corps à mesure —
        # ce que faisait la v0.9 — ne suffisait pas : mesuré sur épreuve,
        # « NEA » à 105 pt débordait ENCORE, le N mordant sur la zone blanche
        # à gauche et le A se faisant couper au bord droit de la page.
        #
        # Les lettres sont donc empilées, une par ligne, centrées sur l'axe du
        # bandeau (-0,17 de la largeur depuis le bord droit) et calées en haut.
        # Chaque lettre reste lisible à l'endroit et garde un corps de 150 pt,
        # au lieu des 105 pt illisibles de l'ancienne mise à plat.
        #
        # Décision de Pierre du 15/08/2026, sur épreuve : trois dispositions
        # ont été composées et comparées (à plat, pivotée à 90°, empilée).
        if len(lettres) == 1:
            watermark = (
                r"\node[anchor=east, text=white!22, "
                r"font=\fontsize{220}{220}\selectfont\bfseries]" "\n"
                r"		at ($(current page.east)+(-0.02\paperwidth,3.5cm)$) "
                f"{{{lettres}}};")
        else:
            empilees = r"\\".join(lettres)
            watermark = (
                r"\node[anchor=north, align=center, text=white!22, "
                r"font=\fontsize{150}{140}\selectfont\bfseries]" "\n"
                r"		at ($(current page.north east)+(-0.17\paperwidth,-1.5cm)$) "
                f"{{{empilees}}};")
        header = header.replace("@WATERMARK@", watermark)
        header = header.replace("@VERSION@", args.version_label)
        master = [header]
    else:
        master = [MASTER_HEADER_DE.replace("@TITLE@", escape_latex(toc["title"]))]

    # v0.9 — Pièces liminaires optionnelles : avant-propos, remerciements,
    # avertissement. Rendues par la même chaîne DARCdown que les sections — gras,
    # italique, listes, tableaux et encadrés y fonctionnent à l'identique. Chacune
    # devient un chapitre NON numéroté, inscrit au sommaire, ouvert sur page
    # impaire. L'option est répétable et son ordre d'apparition fixe l'ordre des
    # pages. Ne pas y placer de [question:…], [picture:…] ni [photo:…] : ces
    # marqueurs n'ont pas de sens hors du corps de l'ouvrage.
    for spec in args.front_matter:
        titre, sep, chemin = spec.partition("=")
        if not sep:
            titre, chemin = args.front_matter_title, spec
        fm = Path(chemin).resolve()
        if not fm.is_file():
            print(f"!! --front-matter : fichier introuvable : {fm}", file=sys.stderr)
            sys.exit(1)
        with BookLaTeXRenderer(question_renderer=question_renderer) as renderer:
            fm_latex = renderer.render(
                Document(fm.read_text(encoding="utf-8").splitlines(keepends=True)))
        # Les intertitres d'une pièce liminaire sortent en \subsection. Sous un
        # \chapter* le compteur de chapitre vaut 0 : ils se numéroteraient
        # « 0.0.1 ». On bascule sur les variantes étoilées, qui suppriment à la
        # fois la numérotation et l'entrée au sommaire. Abaisser secnumdepth ne
        # suffirait pas : avec KOMA, un titre non numéroté reste inscrit au
        # sommaire, et la pièce liminaire y ferait doublon avec elle-même.
        fm_latex = re.sub(r"\\(sub)*section\{",
                          lambda m: m.group(0)[:-1] + "*{", fm_latex)
        master.append(f"\\chapter*{{{escape_latex(titre)}}}\n")
        master.append(f"\\addcontentsline{{toc}}{{chapter}}{{{escape_latex(titre)}}}\n")
        master.append(fix_latex(fm_latex))
        master.append("\\cleardoublepage\n")

    chapters = toc["chapters"]
    if args.limit_chapters:
        chapters = chapters[: args.limit_chapters]

    n_sections = 0
    for chapter in chapters:
        ch_title = tr_titles["chapters"].get(chapter["title"], chapter["title"])
        master.append(f"\n\\chapter{{{escape_latex(ch_title)}}}\n")
        abstract = chapter.get("abstract")
        if abstract:
            abstract = tr_titles["abstracts"].get(abstract, abstract)
            master.append(f"\\textit{{{escape_latex(abstract)}}}\n")
        for section in chapter["sections"]:
            ident = section["ident"]
            md_file = contents / "contents/sections" / f"{ident}.md"
            for d in tr_dirs:
                if (d / "sections" / f"{ident}.md").exists():
                    md_file = d / "sections" / f"{ident}.md"
                    n_translated += 1
                    break
            if not md_file.exists():
                print(f"!! section manquante : {ident}", file=sys.stderr)
                continue
            with BookLaTeXRenderer(question_renderer=question_renderer) as renderer:
                latex = renderer.render(Document(md_file.read_text(encoding="utf-8").splitlines(keepends=True)))
            (out / "sections" / f"{ident}.tex").write_text(fix_latex(latex), encoding="utf-8")
            sec_title = tr_titles["sections"].get(ident, section["title"])
            master.append(f"\\section{{{escape_latex(sec_title)}}}\n")
            master.append(f"\\input{{sections/{ident}.tex}}\n")
            n_sections += 1

    master.append(MASTER_FOOTER)
    master_file = out / f"book-{args.edition}.tex"
    master_file.write_text("".join(master), encoding="utf-8")

    n_warn = validate_output(out, toc, tr_titles, tr_dirs)

    print(f"OK : {n_sections} sections rendues dans {out}"
          + (f" ({n_translated} traduites)" if tr_dirs else "")
          + (f", {qb.n_translated_q} questions traduites" if q_translations else "")
          + (f", {n_dessins_forkes} dessin(s) francisé(s)" if n_dessins_forkes else ""))
    # Une section sans fichier français sort EN ALLEMAND sans erreur ni message.
    # Sur une édition combinée, c'est le défaut le plus facile à ne pas voir :
    # le livre compile, il est simplement bilingue par endroits.
    if tr_dirs and n_translated < n_sections:
        manque = n_sections - n_translated
        print(f"!! {manque} section(s) sans traduction française : elles sortiront "
              f"EN ALLEMAND. Vérifier que tous les répertoires de classe sont "
              f"passés à --translations, et que l'arborescence amont n'a pas "
              f"dérivé (sections renommées ou ajoutées).", file=sys.stderr)
    if qb.missing:
        print(f"Questions introuvables ({len(qb.missing)}) : {sorted(qb.missing)[:10]}...")

    if args.no_compile:
        return

    # 5. Compilation
    print("Compilation LuaLaTeX (latexmk)...")
    r = subprocess.run(
        ["latexmk", "-lualatex", "-interaction=nonstopmode", "-halt-on-error", master_file.name],
        cwd=out,
    )
    if r.returncode == 0:
        print(f"PDF généré : {out / master_file.with_suffix('.pdf').name}")
    else:
        print("Échec de compilation — voir le .log", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
