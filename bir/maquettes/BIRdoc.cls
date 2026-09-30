% BIRdoc — documents d'accompagnement du Brevet d'Initiation à la Radio
% (référentiel, livre du formateur, fiches d'activité, mallette, livret).
% Le manuel de l'élève, lui, est composé par build_book.py (édition BIR).
% Compilation : lualatex. Polices et couleurs reprises du manuel.
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{BIRdoc}[2026/09/30 Documents d'accompagnement du BIR]
% Option a5 : page A5, pour le livret de l'élève (imprimé en A4 plié).
\newif\ifBIRacinq
\DeclareOption{a5}{\BIRacinqtrue}
\ProcessOptions\relax
\LoadClass[10pt]{article}

\ifBIRacinq
  \RequirePackage[a5paper,left=12mm,right=12mm,top=24mm,bottom=15mm,
                  headheight=12mm,headsep=5mm,footskip=8mm]{geometry}
\else
  \RequirePackage[a4paper,left=20mm,right=20mm,top=30mm,bottom=20mm,
                  headheight=12mm,headsep=8mm,footskip=10mm]{geometry}
\fi
\RequirePackage{sourceserifpro}
\RequirePackage{sourcesanspro}
\RequirePackage[french]{babel}
\RequirePackage[table]{xcolor}
\RequirePackage{tabularx,booktabs,array,enumitem,fancyhdr,titlesec,multicol}
\RequirePackage{tcolorbox}

% Couleurs de la page de titre du manuel.
\definecolor{BIRbleu}{cmyk}{.9,.55,.1,.35}
\definecolor{BIRrouge}{cmyk}{.05,.8,1,0}
\colorlet{BIRclair}{BIRbleu!7}

\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt plus 1pt}
\setlength{\emergencystretch}{2em}
\renewcommand{\arraystretch}{1.25}
\setlist{nosep,leftmargin=1.4em}
\frenchsetup{StandardLists=true}

% --- En-tête et pied ---------------------------------------------------
\newcommand{\BIR@type}{}
\newcommand{\BIR@court}{}
% \BIRdocument{type de document}{titre court de l'en-tête}
\newcommand{\BIRdocument}[2]{\renewcommand{\BIR@type}{#1}\renewcommand{\BIR@court}{#2}}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\colorbox{BIRbleu}{\textcolor{white}{\sffamily\bfseries\large\strut\ BIR\ }}%
  \hspace{.7em}{\sffamily\bfseries\color{BIRbleu}\BIR@type}}
\fancyhead[R]{\sffamily\small\BIR@court}
\renewcommand{\headrule}{{\color{BIRrouge}\hrule height 1.2pt}}
\fancyfoot[L]{\sffamily\scriptsize\color{black!55}Brevet d'Initiation à la Radio --- d'après les contenus de 50ohm.de, licence CC BY 4.0}
\fancyfoot[R]{\sffamily\small\thepage}
\renewcommand{\footrulewidth}{0pt}

% --- Titres --------------------------------------------------------------
% \BIRtitre{titre}{sous-titre}
\newcommand{\BIRtitre}[2]{%
  {\sffamily\bfseries\fontsize{21}{25}\selectfont\color{BIRbleu}#1\par}%
  \vspace{2pt}{\sffamily\large #2\par}\vspace{8pt}}
\titleformat{\section}{\sffamily\bfseries\large\color{BIRbleu}}{\thesection}{.6em}{}
\titleformat{\subsection}{\sffamily\bfseries\normalsize}{\thesubsection}{.6em}{}
\titlespacing*{\section}{0pt}{12pt plus 2pt}{4pt}
\titlespacing*{\subsection}{0pt}{8pt plus 2pt}{2pt}

% --- Encadrés ------------------------------------------------------------
% \begin{BIRencadre}{titre} … \end{BIRencadre}
\newtcolorbox{BIRencadre}[1]{colback=BIRclair,colframe=BIRbleu,boxrule=0pt,
  leftrule=3pt,arc=0pt,left=6pt,right=6pt,top=5pt,bottom=5pt,
  before upper={{\sffamily\bfseries\color{BIRbleu}#1}\par\vspace{2pt}}}
% Variante d'alerte (règle du jour, sécurité).
\newtcolorbox{BIRalerte}[1]{colback=BIRrouge!6,colframe=BIRrouge,boxrule=0pt,
  leftrule=3pt,arc=0pt,left=6pt,right=6pt,top=5pt,bottom=5pt,
  before upper={{\sffamily\bfseries\color{BIRrouge!80!black}#1}\par\vspace{2pt}}}

% --- À remplir -----------------------------------------------------------
\newcommand{\BIRcase}{\raisebox{-.15ex}{\fboxsep0pt\fbox{\rule{0pt}{1.7ex}\rule{1.7ex}{0pt}}}\hspace{.35em}}
\newcommand{\BIRligne}[1][\linewidth]{\makebox[#1]{\dotfill}}
\newcommand{\BIRhaut}{\rule{0pt}{7.5mm}}        % ligne de tableau à remplir
% Pointillés jusqu'au bout de la ligne ou de la cellule (composer.py).
\newcommand{\BIRfin}{\unskip~\dotfill\mbox{}}
% Cadre vide où l'élève dessine : \BIRcadrevide{hauteur}.
\newcommand{\BIRcadrevide}[1]{\par\smallskip\noindent
  {\color{BIRbleu!45}\fboxsep0pt\fbox{\rule{0pt}{#1}\hspace{\dimexpr\linewidth-2\fboxrule\relax}}}\par\smallskip}
% Symbole « courant continu » des multimètres : un trait sur trois tirets.
\newcommand{\BIRcontinu}{\raisebox{.1ex}{\makebox[1.15em]{%
  \rlap{\raisebox{.55ex}{\rule{1.15em}{.5pt}}}%
  \rule{.27em}{.5pt}\hfill\rule{.27em}{.5pt}\hfill\rule{.27em}{.5pt}}}}

% --- Documents composés depuis le Markdown (composer.py) -----------------
\RequirePackage{fancyvrb}
\tcbuselibrary{breakable}
\tcbset{breakable}
\newcommand{\BIRcode}[1]{{\ttfamily\small #1}}
% Nouvelle FEUILLE : on saute à la prochaine page impaire, en laissant au
% besoin un verso blanc, pour que des fiches recto verso restent séparables.
\newcommand{\BIRfeuille}{\clearpage
  \ifodd\value{page}\else\thispagestyle{empty}\null\clearpage\fi}

% --- Tableaux ------------------------------------------------------------
\newcolumntype{L}{>{\raggedright\arraybackslash}X}
\newcolumntype{P}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcommand{\BIRth}[1]{\textcolor{white}{\sffamily\bfseries #1}}
\newcommand{\BIRentete}{\rowcolor{BIRbleu}}
