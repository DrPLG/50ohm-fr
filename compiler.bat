@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul
cd /d "%~dp0"

REM ============================================================================
REM  compiler.bat - lance une compilation N, E ou A avec build_book.py
REM
REM  Reprend le protocole de CLAUDE.md : purge des auxiliaires avant
REM  compilation, chemins amont, controles de non-regression apres coup.
REM  A adapter si l'emplacement de l'amont ou les versions changent.
REM ============================================================================

set "PYTHONIOENCODING=UTF-8"

REM --- Localisation des depots amont -----------------------------------------
REM Les deux depots amont (generateur + contenus) vivent cote a cote sous une
REM meme racine, mais celle-ci differe d'une machine a l'autre. On essaie les
REM racines connues dans l'ordre et on retient la premiere ou le paquet
REM renderer est reellement present. La variable d'environnement OHM_AMONT,
REM si elle est definie, l'emporte : c'est le point d'entree pour une machine
REM dont la disposition n'est pas listee ici.
set "OHM_RENDERER="
set "AMONT="
for %%R in ("%OHM_AMONT%" "D:\50ohm-amont" "C:\50ohm") do (
    if not defined OHM_RENDERER (
        if exist "%%~R\50ohm-main\renderer\document.py" (
            set "OHM_RENDERER=%%~R\50ohm-main"
            set "AMONT=%%~R\50ohm-contents-dl-main"
        )
    )
)

if not defined OHM_RENDERER (
    echo ERREUR : aucun depot amont trouve.
    echo Racines essayees : %%OHM_AMONT%%, D:\50ohm-amont, C:\50ohm
    echo Chaque racine doit contenir 50ohm-main\ et 50ohm-contents-dl-main\
    echo ^(tarballs codeload.github.com/DARC-e-V/50ohm et .../50ohm-contents-dl^).
    echo Definissez OHM_AMONT pour designer une autre racine.
    pause
    exit /b 1
)

REM --- Interpreteur Python ---------------------------------------------------
REM Le paquet renderer exige Python 3.12 ou plus (.python-version amont) et le
REM module mistletoe. On ne se contente PLUS de prendre le premier chemin
REM plausible : chaque candidat est ESSAYE, et n'est retenu que s'il sait
REM reellement importer mistletoe a une version suffisante.
REM
REM Pourquoi (16/08/2026) : l'ancienne regle prenait
REM %OHM_RENDERER%\.venv\Scripts\python.exe s'il existait, sinon "python" du
REM PATH, sans jamais verifier. Sur cette machine le venv uv du generateur est
REM bien la et convient (3.12.13, mistletoe 1.4.0) : la regle marchait. Mais le
REM repli, lui, est un piege -- le "python" du PATH est celui d'INKSCAPE
REM (C:\Program Files\Inkscape\bin\, 3.9.10, sans mistletoe). Sur une machine
REM sans venv, l'ancienne regle l'aurait retenu, puis aurait tente d'installer
REM mistletoe dedans. On essaie donc, au lieu de supposer.
REM
REM Ne pas confondre deux venv voisins : C:\50ohm\.venv est un reliquat PyCharm
REM (3.9.10, disposition Unix), sans rapport ; celui du generateur est
REM C:\50ohm\50ohm-main\.venv.
REM
REM OHM_PYTHON permet de designer un interpreteur explicitement.
set "PY="
if defined OHM_PYTHON call :essai "%OHM_PYTHON%"
call :essai "%OHM_RENDERER%\.venv\Scripts\python.exe"
call :essai "%OHM_RENDERER%\.venv\bin\python.exe"
call :essai py -3.14
call :essai py -3.13
call :essai py -3.12
call :essai python

if not defined PY (
    echo ERREUR : aucun interpreteur Python utilisable.
    echo Il faut Python 3.12 ou plus, avec le module mistletoe.
    echo Essayes : OHM_PYTHON, le venv de !OHM_RENDERER!, py -3.14/-3.13/-3.12, python.
    echo.
    echo Recreez le venv du generateur :  uv sync  ^(dans !OHM_RENDERER!^)
    echo ou designez un interpreteur :    set OHM_PYTHON=C:\chemin\python.exe
    echo.
    echo Attention : le "python" du PATH ne convient pas forcement. Sur cette
    echo machine c'est celui d'Inkscape, en 3.9, sans mistletoe.
    pause
    exit /b 1
)

REM latexmk est un script Perl ; MiKTeX ne fournit pas son propre Perl et
REM s'appuie sur un interpreteur externe. Celui de Git for Windows convient,
REM mais Git ne l'ajoute pas au PATH systeme (volontairement). Sans cette
REM ligne : "MiKTeX could not find the script engine 'perl'".
if exist "C:\Program Files\Git\usr\bin\perl.exe" set "PATH=C:\Program Files\Git\usr\bin;%PATH%"

REM --- Choix de la classe ----------------------------------------------------
set "CLASSE=%~1"
if "%CLASSE%"=="" (
    echo Quelle classe compiler ?
    echo   1 = N
    echo   2 = E
    echo   3 = A  ^(attention : environ 30 minutes^)
    choice /c 123 /n /m "Votre choix : "
    if errorlevel 3 (set "CLASSE=A") else if errorlevel 2 (set "CLASSE=E") else if errorlevel 1 (set "CLASSE=N")
)

REM Chantier a.2 (cf. CLAUDE.md section 12) : les trois classes portent
REM desormais l'etiquette a.2. Elles gardent les pieces liminaires
REM (avant-propos, remerciements) introduites en a.1.
set "VERSION="
if /i "%CLASSE%"=="N" set "VERSION=a.2"
if /i "%CLASSE%"=="E" set "VERSION=a.2"
if /i "%CLASSE%"=="A" set "VERSION=a.2"

if not defined VERSION (
    echo.
    echo Classe inconnue : "%CLASSE%"  ^(attendu : N, E ou A^)
    pause
    exit /b 1
)

set "OUT=build-%CLASSE%"

REM --- Pieces liminaires -----------------------------------------------------
REM --front-matter est repetable et l'ORDRE compte : avant-propos d'abord,
REM remerciements ensuite.
REM Le suffixe "-N" des deux fichiers est HISTORIQUE (ils ont ete rediges pour
REM Les pieces liminaires servent aux TROIS classes : leur texte ne mentionne
REM aucune classe en particulier. Elles s'appelaient avant-propos-N.md et
REM remerciements-N.md, ce qui laissait croire a des pieces propres a la classe
REM N alors que compiler.bat les imposait deja aux trois. Renommees sans
REM suffixe le 14/08/2026 (B5). Ne pas les deriver de %CLASSE%, sinon E et A
REM sortent sans pieces liminaires. Constate le 15/08/2026 : build_book.py NE SE
REM PLAINT PAS de leur absence, et les livres perdent quatre pages sans un mot.
REM Lancer build_book.py a la main impose donc de passer --front-matter soi-meme.
REM
REM Titres arretes le 15/08/2026 : « du traducteur » distingue ces deux pieces,
REM qui sont de Pierre, des textes du DARC qui composent le reste du livre.
REM set sans guillemets englobants : la valeur contient elle-meme des
REM guillemets, que "set "VAR=..."" avalerait.
set "FRONTMATTER="
if exist "avant-propos.md" (
    set FRONTMATTER=--front-matter "Avant-propos du traducteur=avant-propos.md"
) else (
    echo ATTENTION : avant-propos.md introuvable, le livre sortira sans.
)
if exist "remerciements.md" (
    set FRONTMATTER=!FRONTMATTER! --front-matter "Remerciements du traducteur=remerciements.md"
) else (
    echo ATTENTION : remerciements.md introuvable, le livre sortira sans.
)

echo.
echo ============================================================
echo  Compilation classe %CLASSE% ^(%VERSION%^)
echo ============================================================
echo.

REM --- Verifications prealables ----------------------------------------------
REM Le generateur a deja ete localise plus haut ; reste a verifier que les
REM contenus l'accompagnent bien sous la meme racine.
echo Amont : %AMONT%
echo Python : %PY%
echo.
if not exist "%AMONT%\contents\sections" (
    echo ERREUR : contenu amont introuvable a
    echo   !AMONT!
    echo ^(tarball codeload.github.com/DARC-e-V/50ohm-contents-dl^)
    pause
    exit /b 1
)

REM --- Purge : un arbre non purge fait sortir latexmk en rc=12 ---------------
if exist "%OUT%" (
    echo Purge des auxiliaires LaTeX residuels dans %OUT%...
    del /q "%OUT%\*.aux" "%OUT%\*.fdb_latexmk" "%OUT%\*.fls" "%OUT%\*.toc" "%OUT%\*.idx" "%OUT%\*.log" "%OUT%\*.out" 2>nul
)

REM --- Compilation ----------------------------------------------------------
REM PY porte deja ses guillemets quand c'est un chemin : ne pas en rajouter,
REM sinon la forme "py -3.14" serait prise pour un nom d'executable.
%PY% build_book.py --edition %CLASSE% --lang fr ^
    --translations traductions\%CLASSE% ^
    --input "%AMONT%" ^
    --output "%OUT%" ^
    !FRONTMATTER! ^
    --version-label %VERSION%

if errorlevel 1 (
    echo.
    echo ECHEC de la compilation. Voir les messages ci-dessus et %OUT%\book-%CLASSE%.log
    pause
    exit /b 1
)

REM --- Controles de non-regression (CLAUDE.md section 4) ---------------------
echo.
echo ============================================================
echo  Controles de non-regression
echo ============================================================

set "LOG=%OUT%\book-%CLASSE%.log"

findstr /c:"14.63995pt" "%LOG%" >nul
if errorlevel 1 (echo [OK]      desynchronisation DARCimageCache : 0 occurrence) else (echo [ALERTE]  14.63995pt detecte -- deux lualatex enchaines au lieu de latexmk ?)

findstr /c:"lost some margin notes" "%LOG%" >nul
if errorlevel 1 (echo [OK]      lost some margin notes : 0 occurrence) else (echo [ALERTE]  "lost some margin notes" detecte dans le journal)

findstr /c:"Float too large" "%LOG%" >nul
if errorlevel 1 (echo [OK]      Float too large : 0 occurrence) else (echo [ALERTE]  "Float too large" detecte dans le journal)

REM Quatrieme controle du tableau CLAUDE.md section 4. Celui-ci se compte au
REM lieu de se detecter : le garde-fou \DARCmarginpar (v0.13) retrograde
REM legitimement des notes dans le corps du texte sur la classe A. Zero attendu
REM ailleurs, donc toute derive se voit.
REM
REM La valeur etait de 2 ici alors que CLAUDE.md section 4 documentait 3 : la
REM valeur 2 datait d'avant l'ajout des pieces liminaires, qui a decale la
REM pagination.
REM Portee a 4 le 14/08/2026, apres mesure sur la a.2 : la redefinition de
REM displaymath (v0.18) coute environ 1 pt par formule, et la note de marge de
REM schwingkreis_2, qui en contient 22, bascule au-dessus du seuil (734,6 pt
REM pour 711,3). Le garde-fou v0.13 la compose alors dans le corps, en boite
REM secable : pas d'erreur fatale, mais une section change de mise en page.
set "NMARGE=0"
for /f %%N in ('findstr /c:"Note de marge trop haute" "%LOG%" ^| find /c /v ""') do set "NMARGE=%%N"
set "NMARGE_ATTENDU=0"
if /i "%CLASSE%"=="A" set "NMARGE_ATTENDU=4"
if "%NMARGE%"=="%NMARGE_ATTENDU%" (echo [OK]      Note de marge trop haute : %NMARGE% ^(attendu %NMARGE_ATTENDU%^)) else (echo [ALERTE]  Note de marge trop haute : %NMARGE% au lieu de %NMARGE_ATTENDU% attendu)

echo.
echo PDF genere   : %OUT%\book-%CLASSE%.pdf
echo Journal complet : %LOG%
echo.

REM --- Compression Ghostscript (facultative) ----------------------------
REM Ghostscript s'installe sous "Program Files" en 64 bits, mais sous
REM "Program Files (x86)" en 32 bits -- et son executable console s'appelle
REM alors gswin32c.exe, pas gswin64c.exe. Les deux dispositions coexistent
REM sur les machines du projet : on essaie les quatre combinaisons, en
REM preferant le 64 bits quand les deux sont installes.
set "GSEXE="
for %%P in ("C:\Program Files\gs" "C:\Program Files (x86)\gs") do (
    for /d %%G in ("%%~P\gs*") do (
        if exist "%%~G\bin\gswin64c.exe" set "GSEXE=%%~G\bin\gswin64c.exe"
        if not defined GSEXE if exist "%%~G\bin\gswin32c.exe" set "GSEXE=%%~G\bin\gswin32c.exe"
    )
)

REM !GSEXE! et non %GSEXE% : le chemin 32 bits contient "(x86)", et une
REM parenthese fermante issue d'une expansion immediate refermerait ce bloc
REM if( ) en plein milieu. L'expansion differee a lieu apres l'analyse.
if defined GSEXE (
    echo Ghostscript : !GSEXE!
    choice /m "Compresser le PDF avec Ghostscript maintenant "
    if not errorlevel 2 (
        echo.
        echo Compression en cours...
        "%GSEXE%" -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook ^
            -dDetectDuplicateImages=true -dNOPAUSE -dBATCH ^
            -sOutputFile=livre-%CLASSE%-%VERSION%.pdf "%OUT%\book-%CLASSE%.pdf"
        if exist "livre-%CLASSE%-%VERSION%.pdf" (
            echo.
            echo PDF compresse : livre-%CLASSE%-%VERSION%.pdf
        )
    )
) else (
    echo Ghostscript introuvable sous "C:\Program Files\gs\" ni "C:\Program Files (x86)\gs\" -- compression ignoree.
)

echo.
pause
exit /b 0

REM ============================================================================
REM  :essai — retient le premier interpreteur Python REELLEMENT utilisable.
REM
REM  %* est la ligne de commande complete du candidat, ce qui couvre aussi bien
REM  un chemin entre guillemets ("C:\...\python.exe") que le lanceur avec sa
REM  version ("py -3.14"). PY conserve cette forme telle quelle : les appels se
REM  font donc en %PY%, SANS guillemets ajoutes.
REM
REM  Le test est le seul qui vaille : importer mistletoe et verifier la version.
REM  Un "if exist" ne prouve rien -- le python d'Inkscape existe et ne sert a
REM  rien. Pas de parentheses dans l'expression Python : a l'interieur d'un
REM  bloc batch, une parenthese fermante refermerait le bloc.
REM ============================================================================
:essai
if defined PY exit /b 0
%* -c "import sys, mistletoe; assert sys.version_info.major*100+sys.version_info.minor >= 312" >nul 2>nul
if errorlevel 1 exit /b 0
set "PY=%*"
exit /b 0
