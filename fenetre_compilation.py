#!/usr/bin/env python3
# Docstring en chaîne brute : elle cite des chemins Windows et des macros LaTeX
# que Python interpréterait sinon comme des séquences d'échappement.
r"""
fenetre_compilation.py — lanceur graphique des compilations 50ohm-fr.

Une fenêtre Tkinter pour choisir le tome (N, E, A, NE, EA, NEA, SWL), le format
du papier, la langue, l'étiquette de version et les pièces liminaires, puis
lancer la chaîne complète : purge des auxiliaires, build_book.py, contrôles de
non-régression du § 4 de CLAUDE.md, compression Ghostscript, et — en option —
la couverture dos carré collé pour l'imprimeur (couverture.tex).

    python fenetre_compilation.py

POURQUOI PAS compiler.bat. Le batch reste le point d'entrée en ligne de
commande, mais il ne sait faire que N, E et A : il ne définit VERSION que pour
ces trois classes, et surtout il ne sait pas RÉPÉTER --translations, dont les
éditions combinées (NE, EA, NEA) ont besoin. Le NEA et le SWL se lancent donc
aujourd'hui à la main, contrôles et compression compris. Cette fenêtre couvre
les sept éditions et les trois formats, et passe les contrôles elle-même.

CE QU'ELLE NE FAIT PAS, ET C'EST DÉLIBÉRÉ :

  - elle ne compile jamais sans un clic ET une confirmation récapitulative
    (CLAUDE.md § 2 : aucune compilation sans accord explicite de Pierre) ;
  - elle ne lance qu'un tome à la fois. Le § 4 autorise le parallélisme entre
    classes — chaque build-<ÉDITION> est indépendant — mais la limite est
    matérielle : 1 à 2 Go de mémoire par lualatex. La mémoire disponible et le
    disque libre sont affichés en permanence, à titre d'avertissement ;
  - elle ne restaure aucun auxiliaire. Le gardien, si la case est cochée, se
    contente de SAUVEGARDER (cf. gardien.ps1).

PIÈGES DU DÉPÔT REPRIS ICI, chacun payé au moins une fois :

  - l'interpréteur Python est ESSAYÉ, jamais supposé : le « python » du PATH est
    celui d'Inkscape (3.9.10, sans mistletoe). Un candidat n'est retenu que s'il
    importe réellement mistletoe en 3.12 ou plus (compiler.bat, :essai) ;
  - latexmk est un script Perl et MiKTeX n'en fournit pas : le Perl de Git for
    Windows est ajouté au PATH du sous-processus ;
  - les auxiliaires sont purgés avant chaque compilation, sans quoi latexmk sort
    en rc=12 puis se croit à jour (« Nothing to do ») ;
  - le journal en direct est écrit dans « build-<ÉDITION>-console-<date>.txt ».
    JAMAIS vers *.out, qui appartient à hyperref — et cette forme de nom est
    celle que le .gitignore reconnaît ;
  - Ghostscript s'appelle gswin64c.exe en 64 bits et gswin32c.exe en 32 bits,
    sous deux racines différentes : les quatre combinaisons sont essayées ;
  - PYTHONIOENCODING=UTF-8 dans l'environnement du sous-processus : la console
    Windows est en cp1252 et le corpus est plein de λ, µ et Ω.

HISTORIQUE :

  v0.3 (18/09/2026) — trois ajouts, demandés par Pierre après l'impression de E :
     - « PDF INTÉRIEUR POUR L'IMPRIMEUR », en case à cocher : /prepress
       (300 dpi, jamais /ebook), nommé « -IMPRESSION », avec en option le FOND
       PERDU de 3 mm — pages à l'échelle 1 sur une feuille agrandie, page de
       titre prolongée, TrimBox/BleedBox. Généralise impression/fondperdu-E.tex
       à tout format ;
     - « COMPLÉTER À UN MULTIPLE DE 4 PAGES », en case à cocher : l'imprimeur
       l'exige. Les pages manquantes (0 à 3) sont des pages « Notes »,
       composées avec la classe du livre (polices, marges, folios) puis
       fusionnées au PDF par Ghostscript — SANS recompiler le livre. La
       compression et la couverture partent ensuite du livre complété.
       Même procédé que impression/notes-E.tex, généralisé ;
     - RELIURE de la couverture, en boutons radio : dos carré collé ou
       couverture rigide (\Reliure de couverture.tex). Le dos d'une
       couverture rigide se demande à l'imprimeur : calculé, il est faux.
  v0.2 (16/09/2026) — trois ajouts, demandés après la première compilation du
       NEA en 20 x 24 :
     - COUVERTURE POUR L'IMPRIMEUR, en case à cocher : couverture.tex compilé
       en épreuve ET en fichier d'impression, pagination lue dans le journal
       du livre, contrôle de superposition relu dans le journal de la
       couverture. Le livre peut être laissé tel quel (« ne pas toucher au
       livre ») : la couverture se refait alors en une minute ;
     - les deux VÉRIFICATEURS tournent aussi sur une sortie au nom non
       canonique (build-NEA-20x24-marge...), par une jonction temporaire.
       En v0.1 ils étaient sautés — et le NEA 20 x 24 a ainsi laissé passer
       trois questions séparées de leurs réponses (AD406, AD416, AD502) ;
     - les notes de marge rétrogradées n'ont de valeur de référence qu'en A4.
       En 20 x 24 le seuil suit \textheight (711,3 -> 574,7 pt) : le NEA en
       compte 7, et la v0.1 criait à tort « 7 au lieu de 5 ».
  v0.1 (16/09/2026) — première version.

Licence des contenus : CC BY 4.0 — 50ohm.de-Autorenteam / DARC e. V.
"""

import ctypes
import os
import queue
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from datetime import datetime
from pathlib import Path

try:
    import tkinter as tk
    from tkinter import messagebox, ttk
except ImportError:  # pragma: no cover - dépend de l'installation Python
    sys.stderr.write(
        "Ce lanceur a besoin de tkinter, absent de cet interpréteur.\n"
        "Lancez-le avec un Python complet, par exemple celui du générateur :\n"
        r"  C:\50ohm\50ohm-main\.venv\Scripts\python.exe fenetre_compilation.py" "\n")
    sys.exit(2)


RACINE = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
#  Tables — tout ce qui est propre au projet vit ici, et nulle part ailleurs.
# ---------------------------------------------------------------------------

EDITIONS = ["N", "E", "A", "NE", "EA", "NEA", "SWL"]

# Répertoires --translations, dans l'ORDRE. Décision de Pierre du 15/08/2026 :
# citer la classe la plus avancée en premier, le premier répertoire cité
# l'emportant en cas de doublon. La portée est étroite (une seule section est
# traduite dans plusieurs classes, N_Ende), mais la règle est écrite.
CLASSES_TRADUCTION = {
    "N": ["N"], "E": ["E"], "A": ["A"], "SWL": ["SWL"],
    "NE": ["E", "N"],
    "EA": ["A", "E"],
    "NEA": ["A", "E", "N"],
}

FORMATS = ["a4", "20x24", "20x24-marge"]

# Pièces liminaires. Le « TITRE= » est celui arrêté le 15/08/2026 : « du
# traducteur » distingue ces deux textes, qui sont de Pierre, de ceux du DARC.
# Leur nom de fichier n'a PAS de suffixe de classe : elles servent aux sept
# éditions (B5, 14/08/2026).
PIECES = [
    ("Avant-propos du traducteur", "avant-propos.md"),
    ("Remerciements du traducteur", "remerciements.md"),
]

# Contrôle nº 4 du § 4 de CLAUDE.md. Celui-ci se COMPTE au lieu de se détecter :
# le garde-fou \DARCmarginpar (v0.13) rétrograde légitimement des notes dans le
# corps du texte. Toute dérive par rapport à ces valeurs mesurées se voit.
# NE et EA n'ont jamais été compilées : pas de valeur de référence, donc pas de
# verdict — le compte est affiché tel quel.
#
# Valeurs A4 SEULEMENT. Le seuil de rétrogradation suit \textheight, qui tombe
# de 711,3 à 574,7 pt en 20 x 24 : toute note entre les deux bascule. Mesuré
# le 16/09/2026 sur le NEA 20 x 24 (marge 52 mm) : 7 notes, dont deux neuves
# à 685 et 621 pt. Une seule mesure ne fait pas une référence.
NMARGE_ATTENDU = {"N": 1, "E": 0, "A": 4, "NEA": 5, "SWL": 1}

# verifier_figures.py ne connaît que ces livres (sa liste LIVRES).
FIGURES_LIVRES = {"N", "E", "A", "NEA", "SWL"}

# couverture.tex ne sait pas faire le SWL : sa 4e de couverture parle des
# classes N, E et A, et le texte propre au cursus n'est pas rédigé.
COUVERTURE_EDITIONS = {"N", "E", "A", "NE", "EA", "NEA"}

# Répertoire des auxiliaires de couverture. « build-* » : ignoré par git.
DOSSIER_COUVERTURE = "build-couverture"

# Durées mesurées sur la machine de Pierre (CLAUDE.md § 1 et § 2). Elles ne
# servent qu'à l'avertissement de confirmation : une compilation monopolise la
# machine, et le NEA a été mesuré à 1 h 39, non « ~1 h ».
DUREES = {
    "N": "environ 10 min", "E": "environ 25 min", "A": "environ 50 min",
    "NEA": "environ 1 h 40", "SWL": "quelques minutes",
    "NE": "durée inconnue — jamais compilée",
    "EA": "durée inconnue — jamais compilée",
}

# Le gardien ne connaît que ces classes (ValidateSet de gardien.ps1).
GARDIEN_CLASSES = {"N", "E", "A", "NEA", "SWL"}

AUXILIAIRES = [".aux", ".fdb_latexmk", ".fls", ".toc", ".idx", ".log", ".out"]

# Les trois premiers contrôles se détectent : toute occurrence est une alerte.
# L'explication n'est affichée que si l'alerte tombe — c'est là qu'elle sert.
MOTIFS_FATALS = [
    ("14.63995pt", "14.63995pt",
     "désynchronisation \\DARCimageCache : deux lualatex enchaînés au lieu "
     "de latexmk ?"),
    ("lost some margin notes", "lost some margin notes",
     "des notes de marge ont été perdues à la composition"),
    ("Float too large", "Float too large",
     "un flottant ne tient pas dans la page"),
]


# ---------------------------------------------------------------------------
#  Détection de l'environnement — essayer, ne jamais supposer.
# ---------------------------------------------------------------------------

def trouver_amont():
    """Racine amont : la première où le paquet renderer existe RÉELLEMENT.

    Renvoie (generateur, contenus) ou (None, None). Même ordre que
    compiler.bat : OHM_AMONT d'abord, qui est le point d'entrée pour une
    machine dont la disposition n'est pas listée.
    """
    racines = [os.environ.get("OHM_AMONT", ""), r"D:\50ohm-amont", r"C:\50ohm"]
    for r in racines:
        if not r:
            continue
        base = Path(r)
        if (base / "50ohm-main" / "renderer" / "document.py").exists():
            return base / "50ohm-main", base / "50ohm-contents-dl-main"
    return None, None


def _essai_python(commande):
    """Un candidat n'est retenu que s'il importe mistletoe en 3.12 ou plus.

    Un « if exist » ne prouve rien : le Python d'Inkscape existe et ne sert à
    rien. C'est le test de compiler.bat, transposé.
    """
    try:
        r = subprocess.run(
            commande + ["-c", "import sys, mistletoe; "
                              "assert sys.version_info >= (3, 12)"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            timeout=30, creationflags=_sans_fenetre())
        return r.returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def trouver_python(generateur):
    """Interpréteur capable de faire tourner build_book.py, ou None."""
    candidats = []
    if os.environ.get("OHM_PYTHON"):
        candidats.append([os.environ["OHM_PYTHON"]])
    if generateur:
        candidats.append([str(generateur / ".venv" / "Scripts" / "python.exe")])
        candidats.append([str(generateur / ".venv" / "bin" / "python.exe")])
    # Celui qui fait tourner cette fenêtre convient peut-être déjà.
    candidats.append([sys.executable])
    for v in ("3.14", "3.13", "3.12"):
        candidats.append(["py", "-" + v])
    candidats.append(["python"])

    for c in candidats:
        if c[0] and _essai_python(c):
            return c
    return None


def trouver_ghostscript():
    """gswin64c.exe ou, à défaut, gswin32c.exe — nom d'exécutable différent.

    Les deux dispositions coexistent sur les machines du projet ; le 64 bits est
    préféré quand les deux sont installés.
    """
    trouve32 = None
    for racine in (r"C:\Program Files\gs", r"C:\Program Files (x86)\gs"):
        base = Path(racine)
        if not base.is_dir():
            continue
        for dossier in sorted(base.glob("gs*")):
            exe64 = dossier / "bin" / "gswin64c.exe"
            exe32 = dossier / "bin" / "gswin32c.exe"
            if exe64.exists():
                return exe64
            if exe32.exists() and trouve32 is None:
                trouve32 = exe32
    if trouve32:
        return trouve32
    depuis_path = shutil.which("gswin64c") or shutil.which("gswin32c") \
        or shutil.which("gs")
    return Path(depuis_path) if depuis_path else None


def perl_de_git():
    """MiKTeX ne fournit pas son propre Perl et latexmk en est un script.

    Git for Windows en installe un, mais ne l'ajoute pas au PATH système.
    Sans lui : « MiKTeX could not find the script engine 'perl' ».
    """
    p = Path(r"C:\Program Files\Git\usr\bin\perl.exe")
    return p.parent if p.exists() else None


def _sans_fenetre():
    """CREATE_NO_WINDOW : pas de console noire derrière la fenêtre Tk."""
    return getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0


def _decoder(brut):
    """Décode une ligne de sortie d'un sous-processus.

    errors="replace" : la sortie est pleine de λ, µ et Ω, et un
    UnicodeDecodeError au milieu du verdict ne vaut rien — un contrôle qui ne
    peut pas rendre son verdict ne contrôle rien.

    Le CR de fin est retiré : le journal est réouvert en mode texte, qui
    retraduit \\n en CRLF. Sans cela, chaque ligne s'écrivait en CR-CR-LF et le
    fichier sortait à double interligne.
    """
    return brut.decode("utf-8", errors="replace").replace("\r\n", "\n")


# ---------------------------------------------------------------------------
#  Ressources — mesurées avant de lancer, jamais après (CLAUDE.md § 4).
# ---------------------------------------------------------------------------

class _MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]


def memoire_disponible_go():
    """Mémoire DISPONIBLE, pas RAM totale : c'est elle qui décide."""
    if os.name != "nt":
        return None
    st = _MEMORYSTATUSEX()
    st.dwLength = ctypes.sizeof(st)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(st)):
        return None
    return st.ullAvailPhys / (1024 ** 3)


def disque_libre_go(chemin):
    """Un disque plein a déjà interrompu une compilation (26/08/2026)."""
    try:
        return shutil.disk_usage(str(chemin)).free / (1024 ** 3)
    except OSError:
        return None


# ---------------------------------------------------------------------------
#  Construction de la commande — fonctions pures, testables sans fenêtre.
# ---------------------------------------------------------------------------

def nom_sortie(edition, format_papier):
    """build-N en A4, build-N-20x24 sinon : deux formats ne se mélangent pas
    dans le même répertoire, leurs auxiliaires s'écraseraient."""
    if format_papier == "a4":
        return "build-" + edition
    return "build-{}-{}".format(edition, format_papier)


def nom_pdf_compresse(edition, version, format_papier):
    suffixe = "" if format_papier == "a4" else "-" + format_papier
    return "livre-{}-{}{}.pdf".format(edition, version, suffixe)


def nom_pdf_impression(edition, version, format_papier):
    """livre-E-a.3-20x24-marge-IMPRESSION.pdf (CLAUDE.md § 3, Compression)."""
    return nom_pdf_compresse(edition, version, format_papier)[:-4] + "-IMPRESSION.pdf"


# Format FINI du livre, en mm (largeur, hauteur) — les geometry de build_book.py.
FORMATS_MM = {"a4": (210, 297), "20x24": (200, 240), "20x24-marge": (200, 240)}

# Fond perdu de l'intérieur, en mm. Consigne de l'imprimeur du 17/09/2026 :
# fichier de (largeur + 6 mm) x (hauteur + 6 mm).
FOND_PERDU_MM = 3


def tex_fond_perdu(source, largeur, hauteur, fond=FOND_PERDU_MM):
    r"""Source LaTeX de l'intérieur avec fond perdu, à partir du PDF `source`.

    Chaque page est centrée à l'échelle 1 sur une feuille agrandie de `fond`
    mm de chaque côté ; TrimBox et BleedBox sont déclarées. Seule la page de
    titre touche le bord (bandeau et filet, build_book.py) : ses aplats sont
    prolongés dans le fond perdu, avec 0,2 mm de recouvrement vers
    l'intérieur pour ne laisser aucun filet blanc. Bandeau : 0,34 de la
    largeur à droite ; filet : entre 0,345 et 0,34.
    Généralise impression/fondperdu-E.tex, validé au pixel le 17/09/2026.
    """
    L, H, b = largeur + 2 * fond, hauteur + 2 * fond, fond
    bp = 72 / 25.4
    bande = b + largeur * (1 - 0.34)
    filet = b + largeur * (1 - 0.345)
    ch = lambda v: ("%.4f" % v).rstrip("0").rstrip(".")
    boites = (r"\pdfvariable pageattr{/TrimBox [%.5f %.5f %.5f %.5f] "
              r"/BleedBox [0 0 %.5f %.5f]}"
              % (b * bp, b * bp, (b + largeur) * bp, (b + hauteur) * bp, L * bp, H * bp))
    return "\n".join([
        r"\documentclass{article}",
        r"\usepackage[paperwidth=%smm, paperheight=%smm, margin=0pt]{geometry}"
        % (ch(L), ch(H)),
        r"\usepackage{pdfpages}",
        r"\usepackage{tikz}",
        r"\definecolor{TitleBand}{cmyk}{.9,.55,.1,.35}",
        r"\definecolor{TitleAccent}{cmyk}{.05,.8,1,0}",
        boites,
        r"\begin{document}",
        r"\includepdf[pages=1, noautoscale, pagecommand={%",
        r"	\begin{tikzpicture}[remember picture, overlay, x=1mm, y=1mm, "
        r"shift={(current page.south west)}]",
        r"		\fill[TitleBand]   (%s, 0) rectangle (%s, %s);" % (ch(L - b - 0.2), ch(L), ch(H)),
        r"		\fill[TitleBand]   (%s, %s) rectangle (%s, %s);" % (ch(bande), ch(H - b - 0.2), ch(L), ch(H)),
        r"		\fill[TitleBand]   (%s, 0) rectangle (%s, %s);" % (ch(bande), ch(L), ch(b + 0.2)),
        r"		\fill[TitleAccent] (%s, %s) rectangle (%s, %s);" % (ch(filet), ch(H - b - 0.2), ch(bande), ch(H)),
        r"		\fill[TitleAccent] (%s, 0) rectangle (%s, %s);" % (ch(filet), ch(bande), ch(b + 0.2)),
        r"	\end{tikzpicture}}]{%s}" % source,
        r"\includepdf[pages=2-, noautoscale]{%s}" % source,
        r"\end{document}",
    ]) + "\n"


def construire_commande(python, edition, langue, format_papier, version,
                        contenus, sortie, pieces, compiler_=True):
    """La ligne de commande exacte, sous forme de liste d'arguments.

    `pieces` est une liste de couples (titre, fichier) : l'ordre des options
    --front-matter fixe l'ordre des pages — avant-propos d'abord.
    """
    cmd = list(python) + [str(RACINE / "build_book.py"),
                          "--edition", edition,
                          "--lang", langue,
                          "--format", format_papier]
    for classe in CLASSES_TRADUCTION[edition]:
        cmd += ["--translations", str(RACINE / "traductions" / classe)]
    cmd += ["--input", str(contenus),
            "--output", str(sortie),
            "--version-label", version]
    for titre, fichier in pieces:
        cmd += ["--front-matter", "{}={}".format(titre, fichier)]
    if not compiler_:
        cmd.append("--no-compile")
    return cmd


def nom_couverture(edition, version, format_papier, reliure="souple"):
    """couverture-NEA-a.3-20x24-marge[-rigide] ; épreuve/impression suit.

    Le dos carré collé garde le nom d'avant la v0.3 : aucun fichier existant
    ne change de nom."""
    suffixe = "" if format_papier == "a4" else "-" + format_papier
    if reliure == "rigide":
        suffixe += "-rigide"
    return "couverture-{}-{}{}".format(edition, version, suffixe)


# Reliures de la couverture : valeur passée à \Reliure, libellé de la fenêtre.
RELIURES = [("souple", "dos carré collé"),
            ("rigide", "couverture rigide (reliée)")]

# Titre des pages ajoutées pour atteindre un multiple de 4.
TITRE_NOTES = {"fr": "Notes", "de": "Notizen"}


def pages_a_ajouter(pages, multiple=4):
    """Nombre de pages à ajouter pour que `pages` soit un multiple de 4."""
    return (-pages) % multiple


def tex_pages_notes(premiere, nombre, titre="Notes"):
    r"""Source LaTeX de `nombre` pages « Notes », numérotées dès `premiere`.

    Compilé DANS la sortie du livre, qui contient FiftyOhmBook.cls : polices,
    marges et folios sont ceux du livre. Lignes d'écriture sur toute la
    largeur texte + colonne de marge. La colonne est à droite sur une page
    impaire, à gauche sur une paire (twoside) : on décale alors d'autant.
    open=any : sinon \chapter* ouvrirait sur une page de droite et ajouterait
    une page blanche quand la première page ajoutée est paire.
    Validé au rendu le 17/09/2026 sur E (274 -> 276 p.), cf. notes-E.tex.
    """
    lignes = [
        r"\documentclass{FiftyOhmBook}",
        r"\KOMAoptions{open=any}",
        r"\newlength{\largeurnotes}",
        r"\setlength{\largeurnotes}{\dimexpr\textwidth+\marginparsep+\marginparwidth\relax}",
        r"\newcommand{\lignesnotes}[1]{%",
        r"	\xleaders\vbox to 9mm{\vfil\moveleft#1\hbox{\color{black!35}"
        r"\rule{\largeurnotes}{0.4pt}}}\vfill}",
        r"\begin{document}",
        r"\setcounter{page}{%d}" % premiere,
    ]
    for i in range(nombre):
        page = premiere + i
        decalage = (r"0pt" if page % 2 else
                    r"\dimexpr\marginparsep+\marginparwidth\relax")
        if i == 0:
            lignes.append(r"\chapter*{%s}" % titre)
        else:
            lignes += [r"\newpage", r"\null"]
        lignes.append(r"\lignesnotes{%s}" % decalage)
    lignes.append(r"\end{document}")
    return "\n".join(lignes) + "\n"


def pages_du_journal(log, edition):
    """Pagination du livre, lue dans son journal LaTeX — la DERNIÈRE passe.

    « Output written on book-NEA.pdf (1036 pages, ...) ». Le .log ne garde
    que la dernière exécution de lualatex (CLAUDE.md § 4), mais on prend
    quand même la dernière occurrence, par prudence.
    """
    try:
        texte = Path(log).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    trouves = re.findall(r"Output written on book-{}\.pdf \((\d+) pages?"
                         .format(re.escape(edition)), texte)
    return int(trouves[-1]) if trouves else None


def lignes_journal_tex(texte):
    """Recolle les lignes que TeX coupe à 79 caractères dans son journal.

    Une ligne d'exactement 79 caractères continue sur la suivante. Sans ce
    recollement, un « COUVERTURE-CONTROLE ALERTE ... » long serait lu en deux
    morceaux, dont le second ne commence plus par le mot-clé.

    On ne recolle qu'à partir d'une ligne qui COMMENCE par « COUVERTURE- » :
    un \typeout ouvre toujours une ligne neuve. Recoller partout était faux —
    mesuré le 16/09/2026, « (…/geometry/geometry.cfg)) » fait 79 caractères
    par nature, et la ligne d'avertissement du dos s'y retrouvait accrochée,
    donc invisible au filtre.
    """
    brutes = texte.splitlines()
    lignes, i = [], 0
    while i < len(brutes):
        ligne = brutes[i]
        if ligne.startswith("COUVERTURE-"):
            while len(brutes[i]) == 79 and i + 1 < len(brutes):
                i += 1
                ligne += brutes[i]
        lignes.append(ligne)
        i += 1
    return lignes


def commande_lisible(cmd):
    """La même commande, prête à coller dans un terminal."""
    morceaux = []
    for a in cmd:
        morceaux.append('"{}"'.format(a) if (" " in a or "=" in a) else a)
    return " ".join(morceaux)


# ---------------------------------------------------------------------------
#  La fenêtre
# ---------------------------------------------------------------------------

class Fenetre:

    def __init__(self, racine_tk):
        self.tk = racine_tk
        self.tk.title("50ohm-fr — compilation")
        self.tk.minsize(920, 640)

        self.generateur, self.contenus = trouver_amont()
        self.python = trouver_python(self.generateur)
        self.gs = trouver_ghostscript()

        self.processus = None      # sous-processus en cours, ou None
        self.gardien = None        # processus gardien.ps1, ou None
        self.file = queue.Queue()  # lignes de journal, du thread vers Tk
        self.journal = None        # fichier de journal ouvert
        self.debut = None

        self._variables()
        self._construire()
        self._etat_ressources()
        self._verdict_environnement()
        self.tk.after(100, self._vider_file)
        self.tk.protocol("WM_DELETE_WINDOW", self._fermer)

    # -- widgets ------------------------------------------------------------

    def _variables(self):
        self.v_edition = tk.StringVar(value="N")
        self.v_format = tk.StringVar(value="a4")
        self.v_langue = tk.StringVar(value="fr")
        self.v_version = tk.StringVar(value="a.4")
        self.v_sortie = tk.StringVar()
        self.v_pieces = [tk.BooleanVar(value=True) for _ in PIECES]
        self.v_purger = tk.BooleanVar(value=True)
        # « compiler », « generer » (.tex seuls) ou « rien » (livre déjà là).
        self.v_livre = tk.StringVar(value="compiler")
        self.v_controles = tk.BooleanVar(value=True)
        self.v_compresser = tk.BooleanVar(value=True)
        self.v_gardien = tk.BooleanVar(value=False)
        self.v_couverture = tk.BooleanVar(value=False)
        self.v_multiple4 = tk.BooleanVar(value=False)
        self.v_impression = tk.BooleanVar(value=False)
        self.v_fond_perdu = tk.BooleanVar(value=True)
        self.v_reliure = tk.StringVar(value="souple")
        self.v_etat = tk.StringVar(value="prêt")
        self.v_ressources = tk.StringVar(value="")

        self.v_edition.trace_add("write", lambda *_: self._sur_edition())
        self.v_format.trace_add("write", lambda *_: self._maj_sortie())

    def _construire(self):
        cadre = ttk.Frame(self.tk, padding=10)
        cadre.pack(fill="both", expand=True)
        cadre.columnconfigure(1, weight=1)

        ligne = 0
        # --- Tome
        ttk.Label(cadre, text="Tome").grid(row=ligne, column=0, sticky="w")
        boite = ttk.Frame(cadre)
        boite.grid(row=ligne, column=1, sticky="w")
        for e in EDITIONS:
            ttk.Radiobutton(boite, text=e, value=e,
                            variable=self.v_edition).pack(side="left", padx=(0, 8))
        ligne += 1

        # --- Format
        ttk.Label(cadre, text="Format").grid(row=ligne, column=0, sticky="w",
                                             pady=(8, 0))
        boite = ttk.Frame(cadre)
        boite.grid(row=ligne, column=1, sticky="w", pady=(8, 0))
        libelles = {"a4": "A4 (publié)",
                    "20x24": "20 × 24 (variante C)",
                    "20x24-marge": "20 × 24, marge de 52 mm"}
        for f in FORMATS:
            ttk.Radiobutton(boite, text=libelles[f], value=f,
                            variable=self.v_format).pack(side="left", padx=(0, 12))
        ligne += 1

        # --- Langue et version
        ttk.Label(cadre, text="Langue").grid(row=ligne, column=0, sticky="w",
                                             pady=(8, 0))
        boite = ttk.Frame(cadre)
        boite.grid(row=ligne, column=1, sticky="w", pady=(8, 0))
        ttk.Radiobutton(boite, text="français", value="fr",
                        variable=self.v_langue).pack(side="left", padx=(0, 12))
        ttk.Radiobutton(boite, text="allemand (amont, sans traduction)",
                        value="de",
                        variable=self.v_langue).pack(side="left")
        ligne += 1

        ttk.Label(cadre, text="Version").grid(row=ligne, column=0, sticky="w",
                                              pady=(8, 0))
        boite = ttk.Frame(cadre)
        boite.grid(row=ligne, column=1, sticky="w", pady=(8, 0))
        ttk.Entry(boite, textvariable=self.v_version,
                  width=10).pack(side="left")
        ttk.Label(boite, text="  — étiquette de la page de titre"
                  ).pack(side="left")
        ligne += 1

        # --- Pièces liminaires
        ttk.Label(cadre, text="Pièces\nliminaires").grid(row=ligne, column=0,
                                                         sticky="w", pady=(8, 0))
        boite = ttk.Frame(cadre)
        boite.grid(row=ligne, column=1, sticky="w", pady=(8, 0))
        for i, (titre, fichier) in enumerate(PIECES):
            existe = (RACINE / fichier).exists()
            texte = titre if existe else titre + "  (fichier introuvable)"
            c = ttk.Checkbutton(boite, text=texte, variable=self.v_pieces[i])
            c.pack(anchor="w")
            if not existe:
                self.v_pieces[i].set(False)
                c.state(["disabled"])
        ligne += 1

        # --- Options
        ttk.Label(cadre, text="Étapes").grid(row=ligne, column=0, sticky="w",
                                             pady=(8, 0))
        boite = ttk.Frame(cadre)
        boite.grid(row=ligne, column=1, sticky="w", pady=(8, 0))
        livre = ttk.Frame(boite)
        livre.grid(row=0, column=0, columnspan=2, sticky="w")
        ttk.Label(livre, text="Livre :").pack(side="left", padx=(0, 8))
        for valeur, texte in (("compiler", "compiler"),
                              ("generer", "générer les .tex seuls"),
                              ("rien", "ne pas y toucher (déjà compilé)")):
            ttk.Radiobutton(livre, text=texte, value=valeur,
                            variable=self.v_livre,
                            command=self._sur_livre).pack(side="left", padx=(0, 12))
        self.c_purger = ttk.Checkbutton(boite, text="purger les auxiliaires avant",
                                        variable=self.v_purger)
        self.c_purger.grid(row=1, column=0, sticky="w")
        self.c_gardien = ttk.Checkbutton(
            boite, text="gardien du .aux (compilations longues)",
            variable=self.v_gardien)
        self.c_gardien.grid(row=1, column=1, sticky="w", padx=(16, 0))
        self.c_controles = ttk.Checkbutton(boite, text="contrôles de non-régression",
                                           variable=self.v_controles)
        self.c_controles.grid(row=2, column=0, sticky="w")
        self.c_compresser = ttk.Checkbutton(
            boite, text="compresser (Ghostscript)", variable=self.v_compresser)
        self.c_compresser.grid(row=2, column=1, sticky="w", padx=(16, 0))
        self.c_multiple4 = ttk.Checkbutton(
            boite, text="compléter à un multiple de 4 pages (pages « Notes » "
                        "en fin de livre, sans recompiler)",
            variable=self.v_multiple4)
        self.c_multiple4.grid(row=3, column=0, columnspan=2, sticky="w")
        self.c_impression = ttk.Checkbutton(
            boite, text="PDF intérieur pour l'imprimeur (/prepress, 300 dpi, "
                        "« -IMPRESSION »)",
            variable=self.v_impression, command=self._sur_livre)
        self.c_impression.grid(row=4, column=0, columnspan=2, sticky="w")
        self.c_fond_perdu = ttk.Checkbutton(
            boite, text="avec fond perdu de {} mm (page de titre prolongée, "
                        "boîtes de coupe)".format(FOND_PERDU_MM),
            variable=self.v_fond_perdu)
        self.c_fond_perdu.grid(row=5, column=0, columnspan=2, sticky="w",
                               padx=(22, 0))
        self.c_couverture = ttk.Checkbutton(
            boite, text="couverture pour l'imprimeur (épreuve + impression)",
            variable=self.v_couverture, command=self._sur_livre)
        self.c_couverture.grid(row=6, column=0, columnspan=2, sticky="w")
        reliure = ttk.Frame(boite)
        reliure.grid(row=7, column=0, columnspan=2, sticky="w", padx=(22, 0))
        ttk.Label(reliure, text="Reliure :").pack(side="left", padx=(0, 8))
        self.r_reliure = []
        for valeur, texte in RELIURES:
            r = ttk.Radiobutton(reliure, text=texte, value=valeur,
                                variable=self.v_reliure)
            r.pack(side="left", padx=(0, 12))
            self.r_reliure.append(r)
        self.l_couverture = ttk.Label(boite, foreground="#555")
        self.l_couverture.grid(row=8, column=0, columnspan=2, sticky="w")
        ligne += 1

        # --- Sortie
        ttk.Label(cadre, text="Sortie").grid(row=ligne, column=0, sticky="w",
                                             pady=(8, 0))
        ttk.Entry(cadre, textvariable=self.v_sortie).grid(
            row=ligne, column=1, sticky="ew", pady=(8, 0))
        ligne += 1

        # --- Ressources
        ttk.Label(cadre, textvariable=self.v_ressources,
                  foreground="#555").grid(row=ligne, column=0, columnspan=2,
                                          sticky="w", pady=(10, 0))
        ligne += 1

        # --- Boutons
        boite = ttk.Frame(cadre)
        boite.grid(row=ligne, column=0, columnspan=2, sticky="w", pady=(10, 4))
        self.b_compiler = ttk.Button(boite, text="Lancer",
                                     command=self._demander_compilation)
        self.b_compiler.pack(side="left")
        self.b_arreter = ttk.Button(boite, text="Arrêter", state="disabled",
                                    command=self._arreter)
        self.b_arreter.pack(side="left", padx=(8, 0))
        ttk.Button(boite, text="Copier la commande",
                   command=self._copier_commande).pack(side="left", padx=(8, 0))
        ttk.Button(boite, text="Vider le journal",
                   command=lambda: self._effacer()).pack(side="left", padx=(8, 0))
        ligne += 1

        # --- Journal
        cadre.rowconfigure(ligne, weight=1)
        boite = ttk.Frame(cadre)
        boite.grid(row=ligne, column=0, columnspan=2, sticky="nsew")
        boite.rowconfigure(0, weight=1)
        boite.columnconfigure(0, weight=1)
        self.texte = tk.Text(boite, wrap="none", height=18,
                             font=("Consolas", 9), background="#1e1e1e",
                             foreground="#dcdcdc", insertbackground="#dcdcdc")
        self.texte.grid(row=0, column=0, sticky="nsew")
        barre = ttk.Scrollbar(boite, orient="vertical",
                              command=self.texte.yview)
        barre.grid(row=0, column=1, sticky="ns")
        self.texte.configure(yscrollcommand=barre.set, state="disabled")
        self.texte.tag_configure("ok", foreground="#6ac36a")
        self.texte.tag_configure("alerte", foreground="#ff6b6b")
        self.texte.tag_configure("titre", foreground="#7ec8ff")
        ligne += 1

        ttk.Label(cadre, textvariable=self.v_etat).grid(
            row=ligne, column=0, columnspan=2, sticky="w", pady=(6, 0))

        self._sur_edition()

    # -- réactions ----------------------------------------------------------

    def _sur_edition(self):
        self._maj_sortie()
        self._sur_livre()

    @staticmethod
    def _activer(case, variable, actif):
        """Active ou grise une case, SANS toucher à son état coché.

        Décocher en grisant était un piège : passer par « ne pas y toucher »
        puis revenir à « compiler » laissait la purge décochée — et une
        compilation sans purge sort en rc=12 (CLAUDE.md § 4). Le plan ne
        retient donc que les cases actives (_coche).
        """
        case.state(["!disabled"] if actif else ["disabled"])

    @staticmethod
    def _coche(case, variable):
        return variable.get() and "disabled" not in case.state()

    def _sur_livre(self):
        """Grise ce qui n'a rien à mordre dans la configuration choisie.

        - purge et gardien n'ont de sens que si le livre est compilé ;
        - le gardien ne connaît que N, E, A, NEA et SWL (ValidateSet) ;
        - « générer les .tex seuls » ne produit ni journal à contrôler, ni
          PDF à compresser, ni pagination pour la couverture. « ne pas y
          toucher » travaille, lui, sur le livre déjà présent dans la sortie.
        """
        edition, livre = self.v_edition.get(), self.v_livre.get()
        compile_ = livre == "compiler"
        self._activer(self.c_purger, self.v_purger, compile_)
        self._activer(self.c_gardien, self.v_gardien,
                      compile_ and edition in GARDIEN_CLASSES)
        self._activer(self.c_controles, self.v_controles, livre != "generer")
        self._activer(self.c_compresser, self.v_compresser,
                      livre != "generer" and self.gs is not None)

        pourquoi = ""
        if not (RACINE / "couverture.tex").exists():
            pourquoi = "couverture.tex introuvable à la racine du dépôt"
        elif shutil.which("lualatex") is None:
            pourquoi = "lualatex introuvable dans le PATH"
        elif edition not in COUVERTURE_EDITIONS:
            pourquoi = ("pas de couverture SWL : sa 4e de couverture n'est pas "
                        "rédigée")
        elif livre == "generer":
            pourquoi = "il faut un livre compilé pour connaître la pagination"
        self._activer(self.c_couverture, self.v_couverture, not pourquoi)
        # La reliure n'a de sens que si la couverture est demandée.
        reliure_active = self._coche(self.c_couverture, self.v_couverture)
        for r in self.r_reliure:
            r.state(["!disabled"] if reliure_active else ["disabled"])
        # Compléter les pages : il faut un PDF de livre et Ghostscript.
        self._activer(self.c_multiple4, self.v_multiple4,
                      livre != "generer" and self.gs is not None)
        # PDF d'impression : Ghostscript ; le fond perdu demande en plus
        # lualatex (pdfpages), et n'a de sens que si l'impression est cochée.
        self._activer(self.c_impression, self.v_impression,
                      livre != "generer" and self.gs is not None)
        self._activer(self.c_fond_perdu, self.v_fond_perdu,
                      self._coche(self.c_impression, self.v_impression)
                      and shutil.which("lualatex") is not None)
        if pourquoi:
            self.l_couverture.configure(text="   " + pourquoi)
        elif edition in ("NE", "EA"):
            self.l_couverture.configure(
                text="   NB : la 4e de couverture parle des classes N, E et A")
        else:
            self.l_couverture.configure(text="")

    def _maj_sortie(self):
        self.v_sortie.set(nom_sortie(self.v_edition.get(), self.v_format.get()))

    def _etat_ressources(self):
        mem = memoire_disponible_go()
        disque = disque_libre_go(RACINE)
        bouts = []
        if mem is not None:
            bouts.append("mémoire disponible : {:.1f} Go".format(mem))
        if disque is not None:
            bouts.append("disque libre : {:.1f} Go".format(disque))
        bouts.append("un lualatex tient 1 à 2 Go ; un build complet, 190 à 250 Mo")
        self.v_ressources.set("   ·   ".join(bouts))
        self.tk.after(20000, self._etat_ressources)

    def _verdict_environnement(self):
        self._ecrire("fenetre_compilation.py v0.3\n", "titre")
        if self.generateur:
            self._ecrire("Générateur : {}\n".format(self.generateur))
            self._ecrire("Contenus   : {}\n".format(self.contenus))
        else:
            self._ecrire("ERREUR : aucun dépôt amont trouvé. Racines essayées : "
                         "OHM_AMONT, D:\\50ohm-amont, C:\\50ohm.\n"
                         "Chaque racine doit contenir 50ohm-main\\ et "
                         "50ohm-contents-dl-main\\.\n", "alerte")
        if self.python:
            self._ecrire("Python     : {}\n".format(" ".join(self.python)))
        else:
            self._ecrire("ERREUR : aucun interpréteur Python utilisable "
                         "(3.12 ou plus, avec mistletoe).\n"
                         "Le « python » du PATH ne convient pas forcément : sur "
                         "cette machine c'est celui d'Inkscape.\n", "alerte")
        self._ecrire("Ghostscript: {}\n".format(self.gs or "introuvable — "
                                                "compression indisponible"))
        if self.contenus and not (self.contenus / "contents" / "sections").is_dir():
            self._ecrire("ERREUR : contenu amont introuvable à {}\n"
                         .format(self.contenus), "alerte")
        self._ecrire("\n")
        if not (self.generateur and self.python):
            self.b_compiler.state(["disabled"])

    # -- journal ------------------------------------------------------------

    def _ecrire(self, texte, tag=None):
        self.texte.configure(state="normal")
        self.texte.insert("end", texte, tag or ())
        self.texte.see("end")
        self.texte.configure(state="disabled")

    def _effacer(self):
        self.texte.configure(state="normal")
        self.texte.delete("1.0", "end")
        self.texte.configure(state="disabled")

    def _vider_file(self):
        """Pompe la file remplie par le thread de travail. Tkinter n'est pas
        réentrant : rien ne touche aux widgets depuis un autre thread."""
        try:
            while True:
                tag, texte = self.file.get_nowait()
                if tag == "fin":
                    self._fin_de_travail(texte)
                else:
                    self._ecrire(texte, tag)
        except queue.Empty:
            pass
        if self.debut is not None:
            self.v_etat.set("en cours depuis {}".format(
                _duree(time.time() - self.debut)))
        self.tk.after(100, self._vider_file)

    def _dire(self, texte, tag=None):
        """Appelable depuis le thread de travail."""
        self.file.put((tag, texte))
        if self.journal:
            try:
                self.journal.write(texte)
                self.journal.flush()
            except (OSError, ValueError):
                pass

    # -- lancement ----------------------------------------------------------

    def _pieces_choisies(self):
        return [PIECES[i] for i, v in enumerate(self.v_pieces) if v.get()]

    def _plan(self):
        """Fige les choix de la fenêtre en un dictionnaire ordinaire.

        Tcl n'est pas réentrant : un tk.StringVar lu depuis le thread de travail
        est un plantage qui attend son heure. Tout ce dont le thread a besoin
        est copié ici, une fois, avant qu'il démarre.
        """
        edition = self.v_edition.get()
        plan = {
            "edition": edition,
            "format": self.v_format.get(),
            "langue": self.v_langue.get(),
            "version": self.v_version.get().strip() or "0.1",
            "sortie": RACINE / self.v_sortie.get(),
            "pieces": self._pieces_choisies(),
            "purger": self._coche(self.c_purger, self.v_purger),
            "livre": self.v_livre.get(),
            "controles": self._coche(self.c_controles, self.v_controles),
            "compresser": self._coche(self.c_compresser, self.v_compresser),
            "gardien": self._coche(self.c_gardien, self.v_gardien),
            "couverture": self._coche(self.c_couverture, self.v_couverture),
            "multiple4": self._coche(self.c_multiple4, self.v_multiple4),
            "impression": self._coche(self.c_impression, self.v_impression),
            "fond_perdu": self._coche(self.c_fond_perdu, self.v_fond_perdu),
            "reliure": self.v_reliure.get(),
            # Renseignés par _completer si des pages sont ajoutées : le PDF à
            # compresser et la pagination de la couverture changent alors.
            "pdf_livre": None,
            "sources_livre": None,
            "pages": None,
        }
        plan["commande"] = construire_commande(
            self.python, edition, plan["langue"], plan["format"],
            plan["version"], self.contenus, plan["sortie"], plan["pieces"],
            compiler_=(plan["livre"] == "compiler"))
        return plan

    def _copier_commande(self):
        if not (self.python and self.contenus):
            messagebox.showerror("Environnement incomplet",
                                 "Ni Python ni l'amont n'ont été trouvés : "
                                 "la commande serait fausse.")
            return
        texte = commande_lisible(self._plan()["commande"])
        self.tk.clipboard_clear()
        self.tk.clipboard_append(texte)
        self._ecrire(texte + "\n\n")

    def _demander_compilation(self):
        if self.processus is not None:
            return
        plan = self._plan()
        edition, pieces, livre = plan["edition"], plan["pieces"], plan["livre"]
        if livre == "rien" and not (plan["controles"] or plan["compresser"]
                                    or plan["couverture"] or plan["multiple4"]
                                    or plan["impression"]):
            messagebox.showinfo("Rien à faire",
                                "Le livre n'est pas touché et aucune autre étape "
                                "n'est cochée.")
            return
        if plan["couverture"] and not re.fullmatch(r"[A-Za-z0-9._-]+",
                                                   plan["version"]):
            # La version entre dans une ligne de commande TeX et dans un nom de
            # fichier : pas d'espace, pas d'accolade, pas de backslash.
            messagebox.showerror("Version", "Pour la couverture, la version ne "
                                 "doit contenir que lettres, chiffres, point, "
                                 "tiret et souligné (ex. a.3).")
            return
        if livre == "compiler":
            # CLAUDE.md § 2 : aucune compilation ne part sans un accord
            # explicite. Le clic ne suffit pas, le récapitulatif non plus tant
            # qu'il n'est pas confirmé. La couverture seule (une minute) n'est
            # pas concernée : c'est le document réduit du § 5.
            resume = (
                "Tome {} — format {} — langue {} — version {}\n"
                "Pièces liminaires : {}\n"
                "Multiple de 4 pages : {}\n"
                "PDF intérieur pour l'imprimeur : {}\n"
                "Couverture pour l'imprimeur : {}\n"
                "Sortie : {}\n\n"
                "Durée attendue : {}. La machine sera monopolisée d'autant.\n\n"
                "Lancer la compilation ?"
            ).format(edition, plan["format"], plan["langue"], plan["version"],
                     ", ".join(t for t, _ in pieces) or "aucune",
                     "compléter par des pages « Notes »" if plan["multiple4"]
                     else "non",
                     ("oui, avec fond perdu" if plan["fond_perdu"] else "oui, "
                      "sans fond perdu") if plan["impression"] else "non",
                     dict(RELIURES)[plan["reliure"]] if plan["couverture"]
                     else "non",
                     plan["sortie"].name, DUREES.get(edition, "inconnue"))
            if not messagebox.askokcancel("Compiler ?", resume, default="cancel"):
                return
        self._lancer()

    def _lancer(self):
        plan = self._plan()
        edition = plan["edition"]
        horodatage = datetime.now().strftime("%Y%m%d-%H%M%S")
        # Nom NEUTRE : jamais *.out, qui appartient à hyperref — l'écraser fait
        # relire le journal du terminal comme du code TeX à la passe suivante.
        # La forme « ...console....txt » n'est pas cosmétique : c'est elle que
        # le .gitignore reconnaît (*console*.txt), sans quoi chaque compilation
        # laisserait un fichier non suivi de plus dans git status.
        chemin_journal = RACINE / "build-{}-console-{}.txt".format(
            edition, horodatage)
        try:
            self.journal = open(chemin_journal, "w", encoding="utf-8")
        except OSError as e:
            self.journal = None
            self._ecrire("Journal non ouvert ({}) — la compilation continue.\n"
                         .format(e), "alerte")

        self.debut = time.time()
        self.b_compiler.state(["disabled"])
        self.b_arreter.state(["!disabled"])
        self._ecrire("\n" + "=" * 70 + "\n", "titre")
        self._ecrire("Tome {} — {} — {} — {}\n".format(
            edition, plan["format"], plan["langue"],
            datetime.now().strftime("%d/%m/%Y %H:%M:%S")), "titre")
        self._ecrire("Journal : {}\n".format(chemin_journal.name), "titre")
        self._ecrire("=" * 70 + "\n", "titre")

        fil = threading.Thread(target=self._travail, args=(plan,), daemon=True)
        fil.start()

    # -- le travail, dans son thread ---------------------------------------

    def _travail(self, plan):
        sortie, livre = plan["sortie"], plan["livre"]
        code = 0
        try:
            if livre != "rien":
                if livre == "compiler" and plan["purger"]:
                    self._purger(sortie)
                if livre == "compiler" and plan["gardien"]:
                    self._lancer_gardien(plan)
                code = self._appeler_build(plan)
                if code != 0:
                    self._dire("\nÉCHEC : build_book.py sort en rc={}.\n"
                               .format(code), "alerte")
                    self._dire("Après une compilation interrompue, PURGER — ne "
                               "jamais reprendre un arbre en l'état.\n", "alerte")
                    return
                if livre == "generer":
                    self._dire("\nArbre généré sans compilation (--no-compile).\n")
                    return
            else:
                self._dire("\nLivre non touché : les étapes suivantes portent sur "
                           "{}.\n".format(sortie.name))
            if plan["controles"]:
                self._controles(plan)
            if plan["multiple4"]:
                # Après les contrôles, qui portent sur le livre tel que LaTeX
                # l'a composé ; avant la compression et la couverture, qui
                # doivent partir du livre complété.
                code = self._completer(plan)
                if code != 0:
                    return
            if plan["compresser"]:
                self._compresser(plan)
            if plan["impression"]:
                code = self._impression(plan)
                if code != 0:
                    return
            if plan["couverture"]:
                code = self._couverture(plan)
        except Exception as e:  # le thread ne doit jamais mourir en silence
            self._dire("\nERREUR interne du lanceur : {}\n".format(e), "alerte")
            code = -1
        finally:
            self._arreter_gardien()
            self.file.put(("fin", str(code)))

    def _purger(self, sortie):
        """Sur arbre non purgé, latexmk sort en rc=12 puis se croit à jour."""
        if not sortie.is_dir():
            return
        n = 0
        for f in sortie.iterdir():
            if f.suffix in AUXILIAIRES and f.is_file():
                try:
                    f.unlink()
                    n += 1
                except OSError:
                    pass
        self._dire("Purge des auxiliaires : {} fichier(s) supprimé(s).\n".format(n))

    def _environnement(self):
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "UTF-8"
        perl = perl_de_git()
        if perl:
            env["PATH"] = str(perl) + os.pathsep + env.get("PATH", "")
        return env

    def _appeler_build(self, plan):
        cmd = plan["commande"]
        self._dire("\n" + commande_lisible(cmd) + "\n\n")
        self.processus = subprocess.Popen(
            cmd, cwd=str(RACINE), env=self._environnement(),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            creationflags=_sans_fenetre())
        for brut in iter(self.processus.stdout.readline, b""):
            self._dire(_decoder(brut))
        self.processus.stdout.close()
        code = self.processus.wait()
        self.processus = None
        return code

    def _controles(self, plan):
        """Les quatre contrôles du § 4, plus les deux vérificateurs par .aux."""
        edition, sortie = plan["edition"], plan["sortie"]
        self._dire("\n" + "-" * 70 + "\nContrôles de non-régression\n"
                   + "-" * 70 + "\n", "titre")
        log = sortie / "book-{}.log".format(edition)
        if not log.exists():
            self._dire("[ALERTE] journal {} introuvable — rien contrôlé.\n"
                       .format(log.name), "alerte")
            return
        contenu = log.read_text(encoding="utf-8", errors="replace")

        for motif, quoi, explication in MOTIFS_FATALS:
            n = contenu.count(motif)
            if n == 0:
                self._dire("[OK]      « {} » : 0 occurrence\n".format(quoi), "ok")
            else:
                self._dire("[ALERTE]  « {} » : {} occurrence(s) — {}\n"
                           .format(quoi, n, explication), "alerte")

        nmarge = contenu.count("Note de marge trop haute")
        attendu = NMARGE_ATTENDU.get(edition) if plan["format"] == "a4" else None
        if attendu is None:
            self._dire("[  ?  ]   Note de marge trop haute : {} — aucune valeur "
                       "de référence pour {} en {}.\n"
                       .format(nmarge, edition, plan["format"]))
        elif nmarge == attendu:
            self._dire("[OK]      Note de marge trop haute : {} (attendu {})\n"
                       .format(nmarge, attendu), "ok")
        else:
            self._dire("[ALERTE]  Note de marge trop haute : {} au lieu de {} "
                       "attendu\n".format(nmarge, attendu), "alerte")

        # Les deux vérificateurs cherchent <racine>\build-<ÉDITION>\ (ou -fr).
        # Pour une autre sortie, on leur donne une racine temporaire où une
        # JONCTION build-<ÉDITION> pointe vers la vraie. En v0.1 ils étaient
        # simplement sautés : le NEA 20 x 24 a ainsi laissé passer trois
        # questions séparées de leurs réponses.
        racine, jonction = self._racine_de_verification(edition, sortie)
        try:
            for script in ("verifier_questions.py", "verifier_figures.py"):
                chemin = RACINE / script
                if not chemin.exists():
                    continue
                if script == "verifier_figures.py" and edition not in FIGURES_LIVRES:
                    self._dire("\nverifier_figures.py ne connaît pas le livre {} : "
                               "ignoré.\n".format(edition))
                    continue
                if racine is None:
                    self._dire("\n[ALERTE] {} non lancé : jonction vers {} "
                               "impossible.\n".format(script, sortie.name), "alerte")
                    continue
                cmd = list(self.python) + [str(chemin), edition,
                                           "--racine", str(racine)]
                self._dire("\n$ {} {}{}\n".format(
                    script, edition,
                    "  (jonction build-{} -> {})".format(edition, sortie.name)
                    if jonction else ""))
                r = subprocess.run(cmd, cwd=str(RACINE), env=self._environnement(),
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   creationflags=_sans_fenetre())
                self._dire(_decoder(r.stdout))
                tag = "ok" if r.returncode == 0 else "alerte"
                # rc=2 sur verifier_figures.py veut dire « rien contrôlé », PAS
                # « tout va bien ».
                self._dire("rc={}\n".format(r.returncode), tag)
        finally:
            self._retirer_jonction(racine, jonction)

        self._dire("\nLes références « ?? » se comptent sur le PDF, pas dans le "
                   "journal — et il faut LIRE le contexte de chacune.\n")

    def _racine_de_verification(self, edition, sortie):
        """(racine à passer en --racine, jonction à retirer ou None).

        Même mécanisme que link_dir() dans build_book.py : « mklink /J », qui
        ne demande aucun privilège. Renvoie (None, None) si la jonction échoue.
        """
        if sortie.parent == RACINE and sortie.name in ("build-" + edition,
                                                       "build-" + edition + "-fr"):
            return RACINE, None
        temporaire = Path(tempfile.mkdtemp(prefix="50ohm-verif-"))
        jonction = temporaire / ("build-" + edition)
        r = subprocess.run(["cmd", "/c", "mklink", "/J", str(jonction), str(sortie)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           creationflags=_sans_fenetre())
        if r.returncode != 0 or not jonction.exists():
            self._retirer_jonction(temporaire, None)
            return None, None
        return temporaire, jonction

    @staticmethod
    def _retirer_jonction(racine, jonction):
        """os.rmdir, JAMAIS shutil.rmtree : sur une jonction, rmtree peut
        descendre dans la cible et vider le vrai répertoire de compilation.
        os.rmdir retire le lien seul, et refuse un répertoire non vide."""
        try:
            if jonction is not None:
                os.rmdir(jonction)
            if racine is not None and racine != RACINE:
                os.rmdir(racine)
        except OSError:
            pass

    def _completer(self, plan):
        """Pages « Notes » jusqu'au multiple de 4 exigé par l'imprimeur.

        Rend 0 si le livre est complet (ou l'était déjà), 1 sinon. En cas de
        succès, plan["pdf_livre"] et plan["pages"] désignent le livre complété :
        la compression et la couverture en partent.
        """
        edition, sortie = plan["edition"], plan["sortie"]
        self._dire("\n" + "-" * 70 + "\nMultiple de 4 pages\n" + "-" * 70 + "\n",
                   "titre")
        brut = sortie / "book-{}.pdf".format(edition)
        pages = pages_du_journal(sortie / "book-{}.log".format(edition), edition)
        if pages is None or not brut.exists():
            self._dire("[ALERTE] livre ou pagination introuvable dans {} : rien "
                       "à compléter.\n".format(sortie.name), "alerte")
            return 1
        manque = pages_a_ajouter(pages)
        if manque == 0:
            self._dire("[OK]      {} pages : déjà un multiple de 4, rien à "
                       "ajouter.\n".format(pages), "ok")
            return 0
        self._dire("{} pages : {} page(s) « {} » ajoutée(s), p. {} à {}.\n".format(
            pages, manque, TITRE_NOTES.get(plan["langue"], "Notes"),
            pages + 1, pages + manque))

        # Composées DANS la sortie : FiftyOhmBook.cls y est. Une seule passe :
        # aucune référence croisée, et le décalage de marge est écrit en dur.
        job = "notes-{}".format(edition)
        (sortie / (job + ".tex")).write_text(
            tex_pages_notes(pages + 1, manque,
                            TITRE_NOTES.get(plan["langue"], "Notes")),
            encoding="utf-8")
        self.processus = subprocess.Popen(
            ["lualatex", "-interaction=nonstopmode", "-halt-on-error", job + ".tex"],
            cwd=str(sortie), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            creationflags=_sans_fenetre())
        rc = self.processus.wait()
        self.processus = None
        texte_log = (sortie / (job + ".log")).read_text(encoding="utf-8",
                                                        errors="replace")
        m = re.findall(r"Output written on {}\.pdf \((\d+) pages?".format(job),
                       texte_log)
        obtenues = int(m[-1]) if m else None
        if rc != 0 or obtenues != manque:
            self._dire("[ALERTE] pages « Notes » : lualatex rc={}, {} page(s) "
                       "produite(s) pour {} attendue(s) — voir {}\\{}.log\n"
                       .format(rc, obtenues, manque, sortie.name, job), "alerte")
            return 1

        # Fusion. /prepress et non /ebook : ce fichier est la source de
        # l'impression, il ne doit pas perdre en résolution (300 dpi).
        complet = sortie / "book-{}-complet.pdf".format(edition)
        r = subprocess.run(
            [str(self.gs), "-q", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.5",
             "-dPDFSETTINGS=/prepress", "-dDetectDuplicateImages=true",
             "-dNOPAUSE", "-dBATCH", "-sOutputFile=" + str(complet),
             str(brut), str(sortie / (job + ".pdf"))],
            cwd=str(sortie), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            creationflags=_sans_fenetre())
        if r.returncode != 0 or not complet.exists():
            self._dire("[ALERTE] fusion Ghostscript : rc={}\n{}".format(
                r.returncode, _decoder(r.stdout)), "alerte")
            return 1
        plan["pdf_livre"] = complet
        # La compression repart des SOURCES (livre brut + pages Notes), pas du
        # fichier fusionné : celui-ci est déjà passé en /prepress, et une
        # seconde compression recompresserait les images deux fois.
        plan["sources_livre"] = [brut, sortie / (job + ".pdf")]
        plan["pages"] = pages + manque
        self._dire("[OK]      livre complété : {} ({} pages, {:.1f} Mo)\n".format(
            complet.name, plan["pages"], complet.stat().st_size / 1e6), "ok")
        return 0

    def _impression(self, plan):
        """PDF intérieur pour l'imprimeur : /prepress, avec ou sans fond perdu.

        Source : le livre complété de ses pages « Notes » s'il l'a été (déjà en
        /prepress), sinon le PDF brut converti en /prepress — jamais le PDF
        /ebook, ré-échantillonné à 150 dpi (CLAUDE.md § 3). Rend 0 ou 1.
        """
        edition, sortie = plan["edition"], plan["sortie"]
        self._dire("\n" + "-" * 70 + "\nPDF intérieur pour l'imprimeur\n"
                   + "-" * 70 + "\n", "titre")
        brut = sortie / "book-{}.pdf".format(edition)
        if plan["pdf_livre"]:
            source = plan["pdf_livre"]
        else:
            if not brut.exists():
                self._dire("[ALERTE] {} absent — rien à préparer.\n"
                           .format(brut.name), "alerte")
                return 1
            source = sortie / "book-{}-prepress.pdf".format(edition)
            r = subprocess.run(
                [str(self.gs), "-q", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.5",
                 "-dPDFSETTINGS=/prepress", "-dDetectDuplicateImages=true",
                 "-dNOPAUSE", "-dBATCH", "-sOutputFile=" + str(source), str(brut)],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                creationflags=_sans_fenetre())
            if r.returncode != 0 or not source.exists():
                self._dire("[ALERTE] conversion /prepress : rc={}\n{}".format(
                    r.returncode, _decoder(r.stdout)), "alerte")
                return 1
        pages = plan["pages"] or pages_du_journal(
            sortie / "book-{}.log".format(edition), edition)
        if pages and pages % 4:
            self._dire("[ATTENTION] {} pages : pas un multiple de 4, que "
                       "l'imprimeur exige. Cocher « compléter à un multiple de "
                       "4 pages ».\n".format(pages), "alerte")

        final = source
        if plan["fond_perdu"]:
            largeur, hauteur = FORMATS_MM[plan["format"]]
            job = "fondperdu-{}".format(edition)
            (sortie / (job + ".tex")).write_text(
                tex_fond_perdu(source.name, largeur, hauteur), encoding="utf-8")
            # Deux passes : « remember picture » ne connaît la page qu'à la 2e.
            for passe in (1, 2):
                self.processus = subprocess.Popen(
                    ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
                     job + ".tex"], cwd=str(sortie), stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL, creationflags=_sans_fenetre())
                rc = self.processus.wait()
                self.processus = None
                if rc != 0:
                    self._dire("[ALERTE] fond perdu : lualatex rc={} à la passe "
                               "{} — voir {}\\{}.log\n".format(rc, passe,
                                                            sortie.name, job),
                               "alerte")
                    return 1
            m = re.findall(r"Output written on {}\.pdf \((\d+) pages?".format(job),
                           (sortie / (job + ".log")).read_text(
                               encoding="utf-8", errors="replace"))
            obtenues = int(m[-1]) if m else None
            if pages and obtenues != pages:
                self._dire("[ALERTE] fond perdu : {} pages produites pour {} "
                           "attendues.\n".format(obtenues, pages), "alerte")
                return 1
            final = sortie / (job + ".pdf")
            self._dire("Fond perdu de {} mm : feuille de {} x {} mm, format fini "
                       "{} x {} mm (TrimBox), {} pages.\n".format(
                           FOND_PERDU_MM, largeur + 2 * FOND_PERDU_MM,
                           hauteur + 2 * FOND_PERDU_MM, largeur, hauteur, obtenues))

        cible = RACINE / nom_pdf_impression(edition, plan["version"], plan["format"])
        shutil.copyfile(final, cible)
        self._dire("[OK]      {} ({:.1f} Mo) — c'est CE fichier qui part chez "
                   "l'imprimeur.\n".format(cible.name, cible.stat().st_size / 1e6),
                   "ok")
        self._dire("Couleur : le PDF reste en couleur ; un intérieur noir et blanc "
                   "est converti par l'imprimeur.\n")
        return 0

    def _couverture(self, plan):
        """Couverture, dos carré collé ou rigide : épreuve puis impression.

        Rend 0 si les deux sont produites sans alerte, 1 sinon. La pagination
        vient du journal du livre — donc du livre réellement composé, dans le
        format demandé — et non d'une table ; ou, si des pages « Notes » ont
        été ajoutées, du livre complété.
        """
        edition, sortie = plan["edition"], plan["sortie"]
        reliure = plan["reliure"]
        self._dire("\n" + "-" * 70 + "\nCouverture pour l'imprimeur — {}\n"
                   .format(dict(RELIURES)[reliure]) + "-" * 70 + "\n", "titre")
        log_livre = sortie / "book-{}.log".format(edition)
        pages = plan["pages"] or pages_du_journal(log_livre, edition)
        if pages is None:
            self._dire("[ALERTE] pagination introuvable dans {} : le livre "
                       "n'a pas été compilé dans cette sortie.\n"
                       .format(log_livre), "alerte")
            return 1
        if pages % 2:
            self._dire("[ALERTE] {} pages : un dos carré collé exige un nombre "
                       "PAIR.\n".format(pages), "alerte")
            return 1
        self._dire("Pagination lue dans {} : {} pages.\n".format(
            plan["pdf_livre"].name if plan["pages"] else log_livre.name, pages))

        dossier = RACINE / DOSSIER_COUVERTURE
        dossier.mkdir(exist_ok=True)
        base = nom_couverture(edition, plan["version"], plan["format"], reliure)
        argument = (r"\def\Classe{%s}\def\Format{%s}\def\PagesForcees{%d}"
                    r"\def\VersionForcee{%s}\def\Reliure{%s}"
                    % (edition, plan["format"], pages, plan["version"], reliure))
        resultat = 0
        dos_impose = False
        for reperes, suffixe in (("oui", "epreuve"), ("non", "impression")):
            job = "{}-{}".format(base, suffixe)
            for ext in (".aux", ".log"):
                try:
                    (dossier / (job + ext)).unlink()
                except OSError:
                    pass
            # DEUX passes : le dessin s'ancre sur « current page », connue
            # seulement après la première. Le contrôle ne vaut qu'à la seconde.
            for passe in (1, 2):
                self.processus = subprocess.Popen(
                    ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
                     "-output-directory=" + str(dossier), "-jobname=" + job,
                     argument + r"\def\Reperes{%s}\input{couverture.tex}" % reperes],
                    cwd=str(RACINE), stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL, creationflags=_sans_fenetre())
                rc = self.processus.wait()
                self.processus = None
                if rc != 0:
                    self._dire("[ALERTE] {} : lualatex sort en rc={} à la passe "
                               "{} — voir {}\\{}.log\n"
                               .format(job, rc, passe, DOSSIER_COUVERTURE, job),
                               "alerte")
                    return 1
            texte = (dossier / (job + ".log")).read_text(encoding="utf-8",
                                                         errors="replace")
            lignes = lignes_journal_tex(texte)
            cles = [l for l in lignes if l.startswith("COUVERTURE-")]
            alertes = [l for l in cles if "ALERTE" in l]
            avertis = [l for l in cles if l.startswith("COUVERTURE-AVERTISSEMENT")]
            ok = [l for l in cles if l.startswith("COUVERTURE-CONTROLE OK")]
            bilan = [l for l in cles if l.startswith("COUVERTURE-BILAN")]
            overfull = sum(1 for l in lignes if l.startswith("Overfull \\hbox"))

            cible = RACINE / (job + ".pdf")
            shutil.copyfile(dossier / (job + ".pdf"), cible)
            self._dire("\n{} ({})\n".format(cible.name, suffixe), "titre")
            if not bilan:
                # Pas de bilan = le contrôle n'a pas tourné. Ce n'est PAS un
                # « zéro alerte ».
                self._dire("[ALERTE] aucun bilan dans le journal : le contrôle "
                           "de superposition n'a pas tourné.\n", "alerte")
                resultat = 1
            else:
                self._dire("  " + bilan[-1][len("COUVERTURE-BILAN "):] + "\n")
                dos_impose = "(imposee)" in bilan[-1]
            for l in avertis:
                self._dire("  [ATTENTION] " + l[len("COUVERTURE-AVERTISSEMENT "):]
                           + "\n", "alerte")
            for l in alertes:
                self._dire("  [ALERTE] " + l[len("COUVERTURE-CONTROLE ALERTE "):]
                           + "\n", "alerte")
            if bilan and not alertes:
                self._dire("  [OK]     superposition : {} contrôles, 0 alerte\n"
                           .format(len(ok)), "ok")
            if overfull:
                self._dire("  [ALERTE] {} ligne(s) trop longue(s) (Overfull "
                           "\\hbox) dans un bloc\n".format(overfull), "alerte")
            if alertes or overfull:
                resultat = 1

        if dos_impose:
            self._dire("\nLe dos est IMPOSÉ par l'imprimeur pour cette pagination, "
                       "ce format et cette reliure (couverture.tex).\n", "ok")
        elif reliure == "rigide":
            self._dire("\n[ATTENTION] Dos CALCULÉ pour une couverture rigide : le "
                       "calcul suppose le papier du dos carré collé (90 g). "
                       "Demander l'épaisseur à l'imprimeur et la porter dans "
                       "couverture.tex (\\DosImpose...) avant tout tirage.\n",
                       "alerte")
        else:
            self._dire("\nLe dos est CALCULÉ avec une main de 1,206 déduite du "
                       "seul chiffre de CoolLibri pour N (258 p.) : estimation à "
                       "faire confirmer par l'imprimeur avant tout tirage.\n")
        if edition in ("NE", "EA"):
            self._dire("La 4e de couverture parle des classes N, E et A : à "
                       "relire pour l'édition {}.\n".format(edition))
        return resultat

    def _compresser(self, plan):
        """La compression se décide seule depuis le 20/08/2026 : quelques
        dizaines de secondes, là où une compilation coûte des dizaines de
        minutes. C'est ce qui sépare les deux règles."""
        edition, sortie = plan["edition"], plan["sortie"]
        brut = sortie / "book-{}.pdf".format(edition)
        # Livre complété de pages « Notes » : ses deux sources, dans l'ordre.
        sources = plan["sources_livre"] or [brut]
        if not brut.exists():
            self._dire("\n[ALERTE] {} absent — rien à compresser.\n"
                       .format(brut.name), "alerte")
            return
        cible = RACINE / nom_pdf_compresse(edition, plan["version"],
                                           plan["format"])
        self._dire("\n" + "-" * 70 + "\nCompression Ghostscript ({:.0f} Mo en "
                   "entrée)\n".format(brut.stat().st_size / 1e6)
                   + "-" * 70 + "\n", "titre")
        cmd = [str(self.gs), "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.5",
               "-dPDFSETTINGS=/ebook", "-dDetectDuplicateImages=true",
               "-dNOPAUSE", "-dBATCH",
               "-sOutputFile=" + str(cible)] + [str(s) for s in sources]
        self.processus = subprocess.Popen(
            cmd, cwd=str(RACINE), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, creationflags=_sans_fenetre())
        for ligne in iter(self.processus.stdout.readline, b""):
            self._dire(_decoder(ligne))
        self.processus.stdout.close()
        code = self.processus.wait()
        self.processus = None
        if code == 0 and cible.exists():
            self._dire("PDF compressé : {} ({:.2f} Mo)\n".format(
                cible.name, cible.stat().st_size / 1e6), "ok")
        else:
            self._dire("[ALERTE] Ghostscript sort en rc={}.\n".format(code),
                       "alerte")

    # -- gardien ------------------------------------------------------------

    def _lancer_gardien(self, plan):
        edition = plan["edition"]
        script = RACINE / "gardien.ps1"
        if not script.exists():
            self._dire("gardien.ps1 introuvable — gardien ignoré.\n", "alerte")
            return
        try:
            self.gardien = subprocess.Popen(
                ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
                 "-File", str(script), "-Classe", edition],
                cwd=str(RACINE), stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL, creationflags=_sans_fenetre())
            # gardien.ps1 déduit lui-même build-<CLASSE> : il ne suit donc pas
            # une sortie au nom non canonique (format 20 x 24, par exemple).
            self._dire("Gardien lancé : il SAUVEGARDE le .aux des passes "
                       "achevées dans build-{}\\gardien\\. Il ne restaure "
                       "jamais rien tout seul.\n".format(edition))
            if plan["sortie"].name != "build-" + edition:
                self._dire("[ALERTE] la sortie est {} : le gardien surveillera "
                           "build-{} et ne verra rien.\n"
                           .format(plan["sortie"].name, edition), "alerte")
        except OSError as e:
            self.gardien = None
            self._dire("Gardien non lancé ({}).\n".format(e), "alerte")

    def _arreter_gardien(self):
        if self.gardien is None:
            return
        try:
            self.gardien.terminate()
        except OSError:
            pass
        self.gardien = None

    # -- arrêt et fin -------------------------------------------------------

    def _arreter(self):
        if self.processus is None:
            return
        if not messagebox.askokcancel(
                "Arrêter ?",
                "Arrêter la compilation en cours ?\n\n"
                "L'arbre restera avec des auxiliaires possiblement tronqués : "
                "il faudra le purger avant toute reprise."):
            return
        pid = self.processus.pid
        # terminate() ne tue que build_book.py : latexmk et lualatex sont ses
        # petits-enfants et survivraient. taskkill /T descend l'arbre entier.
        if os.name == "nt":
            subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           creationflags=_sans_fenetre())
        else:
            self.processus.terminate()
        self._ecrire("\nArrêt demandé.\n", "alerte")

    def _fin_de_travail(self, code):
        self.debut = None
        self.processus = None
        if self.journal:
            try:
                self.journal.close()
            except OSError:
                pass
            self.journal = None
        self.b_compiler.state(["!disabled"])
        self.b_arreter.state(["disabled"])
        self.v_etat.set("terminé (rc={}) — {}".format(
            code, datetime.now().strftime("%H:%M:%S")))
        self._ecrire("\n=== terminé, rc={} ===\n".format(code),
                     "ok" if code == "0" else "alerte")

    def _fermer(self):
        if self.processus is not None:
            if not messagebox.askokcancel(
                    "Quitter ?",
                    "Une compilation est en cours. Quitter l'interrompra."):
                return
            self._arreter_gardien()
            try:
                subprocess.run(["taskkill", "/PID", str(self.processus.pid),
                                "/T", "/F"], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL,
                               creationflags=_sans_fenetre())
            except OSError:
                pass
        self.tk.destroy()


def _duree(secondes):
    secondes = int(secondes)
    h, reste = divmod(secondes, 3600)
    m, s = divmod(reste, 60)
    if h:
        return "{} h {:02d} min {:02d} s".format(h, m, s)
    if m:
        return "{} min {:02d} s".format(m, s)
    return "{} s".format(s)


def main():
    racine_tk = tk.Tk()
    try:
        racine_tk.call("tk", "scaling", 1.3)
    except tk.TclError:
        pass
    Fenetre(racine_tk)
    racine_tk.mainloop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
