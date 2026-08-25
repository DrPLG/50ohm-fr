#!/usr/bin/env python3
r"""
slides_beamer.py — PROTOTYPE : rend un fichier de slides DARCdown en Beamer.

POURQUOI CE PROTOTYPE. Le dépôt amont porte un dossier `contents/slides/` que
nous n'avions jamais exploité : 381 fichiers, un par section, écrits dans le
même DARCdown que les sections, pour 2 924 séparateurs de slide, 1 746
questions, 490 dessins, 442 notes de présentateur et 402 fragments. L'amont
les rend en HTML (reveal.js) via `renderer/fifty_ohm_html_slide_renderer.py`.
Aucun rendu Beamer n'existe.

CE QU'IL DÉMONTRE, ET SES LIMITES. Il traite UN fichier, pour répondre à une
seule question : le rendu Beamer vaut-il la peine ? Il ne gère pas les
sommaires, ni les éditions combinées, ni le fork de dessins — il emprunte
l'arbre d'un `build-<CLASSE>` déjà généré, qui contient déjà les dessins
francisés, les photos et les .sty amont. Ce n'est PAS un outil de production.

CE QU'IL RÉUTILISE, et c'est l'essentiel de la démonstration :
  - le parseur DARCdown amont (mistletoe + les tokens de `renderer/`) ;
  - notre BookLaTeXRenderer, donc les quatre correctifs de fix_latex(), les
    questions traduites, les unités, le morse, les liens ;
  - les dessins forkés et francisés, via l'arbre de build emprunté.

La correspondance DARCdown -> Beamer est presque terme à terme :
    ---            -> \begin{frame} ... \end{frame}
    <left>/<right> -> \begin{columns}
    <fragment>     -> \pause
    <note>         -> \note{}         (mode présentateur de Beamer)
    [question:XX]  -> notre \Question existant

Usage :
    python slides_beamer.py <ident> --build build-N --output slides-<ident>
"""
import argparse
import pathlib
import re
import shutil
import subprocess
import sys

for _flux in (sys.stdout, sys.stderr):
    try:
        _flux.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

import build_book  # noqa: E402  — localise le paquet `renderer` au chargement

from mistletoe import block_token  # noqa: E402
# Document vient du paquet amont, PAS de mistletoe : renderer/document.py
# définit `references` AVANT que super().__init__ ne tokenise, parce que
# ReferencedToken le lit sur _root_node pendant la tokenisation. Avec le
# Document de mistletoe, la première image rencontrée lève
# « 'Document' object has no attribute 'references' ».
from renderer.document import Document  # noqa: E402
from renderer.slide_break import SlideBreak  # noqa: E402


class BeamerRenderer(build_book.BookLaTeXRenderer):
    """BookLaTeXRenderer + le token SlideBreak, rendu en frames Beamer."""

    def __init__(self, question_renderer=None):
        super().__init__(question_renderer=question_renderer)
        # SlideBreak est un BlockToken amont. On l'enregistre à la main, parce
        # que BookLaTeXRenderer.__init__ fixe sa propre liste de tokens et
        # n'accepte pas d'extras — c'est exactement ce que fait
        # BaseRenderer.__init__ pour ses *extras.
        #
        # position=0 est INDISPENSABLE : « --- » est aussi un ThematicBreak du
        # Markdown standard. Sans la priorité, chaque séparateur de slide
        # serait lu comme un filet horizontal et le découpage en frames
        # n'aurait tout simplement pas lieu.
        block_token.add_token(SlideBreak, position=0)
        self.render_map["SlideBreak"] = self.render_slide_break

    # -- une frame par slide ------------------------------------------------
    def render_slide_break(self, token):
        inner = self.render_inner(token).strip()
        if not inner:
            return ""
        # L'attribut amont est du CSS (« style="font-size: 0.7em;" ») : il n'a
        # pas d'équivalent Beamer. On en retient la seule intention qui compte,
        # « ce contenu est dense », et on laisse Beamer réduire le corps.
        petit = token.attribute and "font-size" in token.attribute
        options = "[shrink=15]" if petit else ""
        return (f"\\begin{{frame}}{options}{{\\insertsectionhead}}\n"
                f"{inner}\n\\end{{frame}}\n\n")

    # -- le contenu de tête est une slide, lui aussi ------------------------
    def render_document(self, token):
        # Un fichier de slides commence par du contenu AVANT le premier « --- »
        # : c'est la première slide, comme sous reveal.js. Sans ce traitement,
        # ces tokens ne sont enveloppés dans aucune frame — Beamer les compose
        # alors hors frame, et la liste d'introduction de `bandbreite` sortait
        # en tête de PDF précédée d'un guillemet parasite.
        self.footnotes.update(token.footnotes)
        enfants = list(token.children)
        tete, reste = [], enfants
        for i, enfant in enumerate(enfants):
            if type(enfant).__name__ == "SlideBreak":
                tete, reste = enfants[:i], enfants[i:]
                break
        else:
            tete, reste = enfants, []
        sortie = ""
        if tete:
            inner = "".join(x for x in (self.render(c) for c in tete)
                            if x is not None).strip()
            if inner:
                sortie += (f"\\begin{{frame}}{{\\insertsectionhead}}\n{inner}\n"
                           f"\\end{{frame}}\n\n")
        sortie += "".join(x for x in (self.render(c) for c in reste)
                          if x is not None)
        return sortie

    # -- colonnes, note du présentateur, fragment ---------------------------
    def render_tag(self, token):
        # L'attribut porte le nom `tagtype` (renderer/tag.py), et le token amont
        # capture DÉJÀ note, fragment, left et right : les balises de slides
        # sont reconnues sans rien ajouter au parseur.
        nom = getattr(token, "tagtype", None)
        inner = "".join(x for x in (self.render(c) for c in token.children)
                        if x is not None)
        if nom == "left":
            return ("\\begin{columns}[T]\n\\begin{column}{0.48\\textwidth}\n"
                    f"{inner}\\end{{column}}\n")
        if nom == "right":
            return (f"\\begin{{column}}{{0.48\\textwidth}}\n{inner}"
                    "\\end{column}\n\\end{columns}\n")
        if nom == "note":
            # \note prend le texte du présentateur ; il ne s'imprime que dans
            # la sortie « notes on second screen ».
            return f"\\note{{{inner.strip()}}}\n"
        if nom == "fragment":
            # Révélation progressive : Beamer avance d'un overlay.
            return f"\\pause\n{inner}"
        return super().render_tag(token)

    # -- une image de slide n'est pas un flottant ---------------------------
    def render_image(self, token):
        # Dans un livre, \DARCimage place un flottant en marge. Dans une frame,
        # il n'y a ni marge ni flottant : on compose l'image à la largeur de la
        # colonne, légende dessous, sans numérotation.
        if getattr(token, "kind", None) in ("picture", "photo"):
            corps = (f"\\includegraphics[width=\\linewidth]"
                     f"{{{token.id}}}" if token.kind == "photo"
                     else f"\\resizebox{{\\linewidth}}{{!}}"
                          f"{{\\input{{img/{token.id}include}}}}")
            return (f"\\begin{{center}}\n{corps}\\\\[2pt]\n"
                    f"{{\\small {token.text}}}\n\\end{{center}}\n")
        return super().render_image(token)


PREAMBULE = r"""\documentclass[aspectratio=169,10pt]{beamer}
% PROTOTYPE — rendu Beamer d'un fichier de slides amont.
%
% settings.tex amont est INDISPENSABLE : il apporte siunitx, circuitikz,
% pgfplots et les macros \DARCimage dont dépendent les 908 dessins. Il est
% écrit pour scrreprt ; les incompatibilités avec beamer sont neutralisées
% ci-dessous, une par une et commentées.
\usetheme{default}
\usecolortheme{seahorse}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{itemize items}[circle]

% --- KOMA pour une classe qui n'en est pas une ------------------------------
% Le .sty amont est écrit pour scrreprt : il emploie \newkomafont,
% \addtokomafont et \Ifundefinedorrelax. Les remplacer un par un par des
% \providecommand ne tient pas — la première tentative a buté sur
% \Ifundefinedorrelax dès la ligne 39 du .sty, et d'autres auraient suivi.
% scrextend est fait exactement pour ça : il apporte l'API de fontes KOMA aux
% classes qui n'en sont pas.
\usepackage{scrextend}
% \chapter, lui, n'existe pas sous beamer et scrextend ne le fournit pas.
\providecommand{\chapter}[1]{}
% marginpar : sans objet dans une frame.
\providecommand{\marginnote}[1]{}

% --- l'ordre est celui de BOOK_CLASS, et il n'est pas indifférent ------------
% C'est DARC-ausbildungsmaterialien.sty qui charge tcolorbox (l. 226) et babel.
% L'omettre — ce que faisait la première version de ce prototype — donne
% « Environment tcolorbox undefined » sur chaque question.
\input{settings-pre.tex}
\usepackage{DARC-ausbildungsmaterialien}
\usepackage{csquotes}
\providecolor{DARClightgray}{cmyk}{0,0,0,.1}

% Le .sty vient de charger babel avec ngerman. On bascule en français par le
% même mécanisme que le livre (v0.17/v0.22), mais SANS le transform de
% ponctuation : il casse sur les nœuds TikZ, et ce prototype ne vaut pas le
% garde-fou \DARCnotransform.
\babelprovide[import, main]{french}

\usepackage{adjustbox}
\input{settings.tex}

% --- après settings.tex ------------------------------------------------------
% Le gras mathématique de la v0.19, pour les nombres des énoncés.
\setmathfont[version=bold, FakeBold=2]{Libertinus Math}

% Parasite « „, » avant chaque liste à puces — correctif v0.6 de BOOK_CLASS,
% qu'il faut reprendre ici : settings.tex fait \let\empty\relax juste après
% circuitikz, un paquet chargé ensuite compare \ifx…\empty, le test échoue et
% émet trois virgules que la ligature TeX rend « „ » + « , ».
% Constaté sur ce prototype avant d'être reconnu : 6 occurrences dans un
% fichier de 10 frames. C'est la démonstration qu'un générateur de slides
% devra hériter des correctifs de la classe, et non repartir de zéro.
\makeatletter
\AddToHook{env/itemize/before}{\let\empty\@empty}
\AddToHook{env/enumerate/before}{\let\empty\@empty}
\AddToHook{env/description/before}{\let\empty\@empty}
\makeatother

% Les questions d'examen : même boîte que dans le livre, mais elle doit tenir
% dans une frame. tcolorbox est déjà chargé par le .sty amont.
\newenvironment{DARCQuestionBox}%
  {\begin{tcolorbox}[colback=black!4, colframe=black!25, boxrule=0.4pt,
                     left=3pt, right=3pt, top=3pt, bottom=3pt]}%
  {\end{tcolorbox}}

\title{@TITRE@}
\subtitle{Préparation à l'examen radioamateur — classe @CLASSE@}
\date{\today}
\author{50ohm.de / DARC e.\,V. — traduction française F4JWI}

\begin{document}
\begin{frame}[plain]
	\titlepage
\end{frame}
\section{@TITRE@}

"""

PIED = r"""
\end{document}
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ident", help="ident de la section (ex. bandbreite)")
    ap.add_argument("--classe", default="N", choices=["N", "E", "A"])
    ap.add_argument("--build", default="build-N",
                    help="arbre de build à emprunter (dessins, photos, .sty)")
    ap.add_argument("--input", default=r"C:\50ohm\50ohm-contents-dl-main",
                    help="racine de l'instantané amont")
    ap.add_argument("--titre", default=None, help="titre affiché")
    ap.add_argument("--output", default=None)
    ap.add_argument("--no-compile", action="store_true")
    args = ap.parse_args()

    racine = pathlib.Path(__file__).parent
    src = racine / "traductions" / args.classe / "slides" / f"{args.ident}.md"
    if not src.is_file():
        sys.exit(f"!! slides non traduites : {src}")
    emprunt = racine / args.build
    if not (emprunt / "settings.tex").is_file():
        sys.exit(f"!! arbre de build introuvable ou incomplet : {emprunt}\n"
                 f"   Compiler d'abord la classe {args.classe}.")

    out = racine / (args.output or f"slides-{args.ident}")
    out.mkdir(exist_ok=True)

    # On emprunte l'arbre du livre : dessins francisés, photos, .sty amont.
    # Copie et non lien : le prototype doit rester sans effet sur le build.
    for nom in ("settings.tex", "settings-pre.tex",
                "DARC-ausbildungsmaterialien.sty"):
        shutil.copy2(emprunt / nom, out / nom)
    for rep in ("img", "photo", "foto"):
        cible, source = out / rep, emprunt / rep
        if source.exists() and not cible.exists():
            try:
                shutil.copytree(source, cible, symlinks=False,
                                ignore_dangling_symlinks=True)
            except (OSError, shutil.Error) as e:
                print(f"   (copie de {rep} partielle : {e})")

    # Les questions traduites, construites exactement comme dans le livre :
    # QuestionBuilder(racine de l'amont, fabrique de renderer, traductions).
    import json
    contents = pathlib.Path(args.input)
    if not (contents / "toc").is_dir():
        sys.exit(f"!! amont introuvable : {contents}")
    qpath = racine / "traductions" / args.classe / "questions.json"
    q_translations = (json.loads(qpath.read_text(encoding="utf-8"))
                      if qpath.is_file() else {})
    qb = build_book.QuestionBuilder(
        contents, lambda: build_book.BookLaTeXRenderer(),
        translations=q_translations)

    with BeamerRenderer(question_renderer=qb.build) as renderer:
        corps = renderer.render(
            Document(src.read_text(encoding="utf-8").splitlines(keepends=True)))

    titre = args.titre or args.ident.replace("_", " ").capitalize()
    tex = (PREAMBULE.replace("@TITRE@", titre).replace("@CLASSE@", args.classe)
           + build_book.fix_latex(corps) + PIED)
    maitre = out / f"slides-{args.ident}.tex"
    maitre.write_text(tex, encoding="utf-8")

    n_frames = tex.count(r"\begin{frame}")
    print(f"OK : {n_frames} frame(s) rendue(s) dans {maitre}")

    if args.no_compile:
        return
    print("Compilation LuaLaTeX (latexmk)...")
    for ext in (".aux", ".fdb_latexmk", ".fls", ".log", ".out", ".toc",
                ".nav", ".snm", ".vrb"):
        (out / (maitre.stem + ext)).unlink(missing_ok=True)
    r = subprocess.run(
        ["latexmk", "-lualatex", "-interaction=nonstopmode", maitre.name],
        cwd=out)
    if r.returncode == 0:
        print(f"PDF genere : {out / (maitre.stem + '.pdf')}")
    else:
        sys.exit("Echec de compilation — voir le .log")


if __name__ == "__main__":
    main()
