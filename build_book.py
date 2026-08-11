#!/usr/bin/env python3
"""
build_book.py — Génère un livre PDF (via LaTeX/LuaLaTeX) à partir des contenus 50ohm.de.

Ce script est le « chef d'orchestre » manquant du dépôt public : il assemble les
sections DARCdown en un document maître LaTeX basé sur la classe FiftyOhm du
dépôt de contenus, puis le compile avec latexmk (LuaLaTeX).

Usage :
    python3 build_book.py --edition N --input /chemin/50ohm-contents-dl \
                          --output build-book [--no-compile] [--limit-chapters 2]

Licence des contenus : CC BY 4.0 — 50ohm.de-Autorenteam / DARC e. V.

Version du script : v0.14
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
\input{settings.tex}

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

% Environnement tabulaire émis par le renderer LaTeX (grab du corps avec +b
% pour rester compatible avec le scan de tabularx) :
\ExplSyntaxOn
\NewDocumentEnvironment{DARCtabular}{m +b}{
	\par\medskip\noindent
	\str_if_in:nnTF {#1} {X}
		{\begin{tabularx}{\linewidth}{#1}#2\end{tabularx}}
		{\begin{tabular}{#1}#2\end{tabular}}
	\par\medskip
}{}
\ExplSyntaxOff

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
\renewcaptionname{ngerman}{\contentsname}{Table des matières}
\renewcaptionname{ngerman}{\chaptername}{Chapitre}
\renewcaptionname{ngerman}{\figurename}{Fig.}
\renewcaptionname{ngerman}{\tablename}{Tab.}
\renewcaptionname{ngerman}{\indexname}{Index alphabétique}
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
	% Lettre de classe, énorme, en réserve claire dans le bandeau
	\node[anchor=east, text=white!22, font=\fontsize{@CLASSSIZE@}{@CLASSSIZE@}\selectfont\bfseries]
		at ($(current page.east)+(-0.02\paperwidth,3.5cm)$) {@CLASS@};
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
% Clamp de \DARCimage — largeur ET hauteur (v0.12).
%
% v0.4 ne bornait que la LARGEUR : une figure trop HAUTE passait au travers.
% Trois cas l'ont montré — le 202 de la classe E (axe pgfplots de 21 x 29 cm),
% puis les 1096 et 687 de la classe A. Une figure trop haute produit
% « Float too large for page », marginfix perd la note ET toutes les suivantes,
% puis la compilation s'arrête sur « lost some margin notes » sans produire de
% PDF.
%
% adjustbox/max size réduit la boîte à proportions constantes UNIQUEMENT si elle
% déborde de l'une des deux limites : les figures conformes ne bougent pas, et
% aucune n'est agrandie. La limite de hauteur est prudente — beaucoup de figures
% partagent leur page avec du texte, et une figure occupant 80 % de la hauteur
% utile est déjà généreuse.
% ---------------------------------------------------------------------------
% LIMITE CONNUE (v0.12) : ce clamp ne borne que la LARGEUR. Une figure trop
% HAUTE passe au travers, provoque « Float too large for page », puis fait
% perdre à marginfix cette note de marge ET toutes les suivantes, jusqu'à
% l'erreur fatale « lost some margin notes » sans production de PDF.
% Cas connus : dessin 202 (classe E), traité par précompilation ; dessins 1096
% et 687 (classe A), non résolus à ce jour. Une tentative de bornage par
% adjustbox/max size s'est révélée inopérante sur ces deux derniers et n'a pas
% été retenue.
% ---------------------------------------------------------------------------
\newsavebox{\DARCfitbox}
\NewCommandCopy{\DARCimageUnclamped}{\DARCimage}
\RenewDocumentCommand{\DARCimage}{sO{Bild~zur~Prüfungsfrage~\l_ptxcd_question_tl}mm}{%
  \sbox{\DARCfitbox}{%
    \IfBooleanTF{#1}%
      {\DARCimageUnclamped*[#2]{#3}{#4}}%
      {\DARCimageUnclamped[#2]{#3}{#4}}%
  }%
  \ifdim\wd\DARCfitbox>\dimexpr#3\relax
    \resizebox{#3}{!}{\usebox{\DARCfitbox}}%
  \else
    \usebox{\DARCfitbox}%
  \fi
}
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

    # 1. Fichiers LaTeX du dépôt de contenus
    for f in (contents / "latex").glob("*"):
        shutil.copy(f, out / f.name)

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
    for f in (contents / "contents/drawings").glob("*.tex"):
        shutil.copy(f, out / "img" / f"{f.stem}include.tex")

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
    tr_dirs = [Path(x).resolve() for x in args.translations]
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
        # Le filigrane est calibré pour UNE lettre. « NE » ou « NEA » à 220 pt
        # déborderait de la page : on réduit le corps à mesure.
        header = header.replace("@CLASS@", lettres)
        header = header.replace("@CLASSSIZE@", {1: "220", 2: "150"}.get(len(lettres), "105"))
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
          + (f", {qb.n_translated_q} questions traduites" if q_translations else ""))
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
