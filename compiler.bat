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
REM Le paquet renderer exige Python 3.12 (.python-version amont) et ses
REM dependances sont installees dans le venv uv du generateur. On le prefere
REM au python du PATH, qui peut etre une version plus ancienne sans les
REM dependances.
set "PY=%OHM_RENDERER%\.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"

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

if "%PY%"=="python" (
    where python >nul 2>nul
    if errorlevel 1 (
        echo ERREUR : aucun venv dans !OHM_RENDERER! et python absent du PATH.
        echo Creez le venv du generateur : uv sync ^(dans !OHM_RENDERER!^).
        pause
        exit /b 1
    )
)

REM --- Purge : un arbre non purge fait sortir latexmk en rc=12 ---------------
if exist "%OUT%" (
    echo Purge des auxiliaires LaTeX residuels dans %OUT%...
    del /q "%OUT%\*.aux" "%OUT%\*.fdb_latexmk" "%OUT%\*.fls" "%OUT%\*.toc" "%OUT%\*.idx" "%OUT%\*.log" "%OUT%\*.out" 2>nul
)

REM --- Dependance Python -------------------------------------------------
REM Le venv uv du generateur est cree sans pip : on n'y installe rien a la
REM volee, on renvoie vers "uv sync". Sur un python du PATH, l'installation
REM automatique d'origine reste valable.
"%PY%" -c "import mistletoe" 2>nul
if errorlevel 1 (
    if "%PY%"=="python" (
        echo Installation de mistletoe...
        python -m pip install --quiet mistletoe
    ) else (
        echo ERREUR : le module mistletoe manque au venv du generateur.
        echo Lancez "uv sync" dans !OHM_RENDERER!
        pause
        exit /b 1
    )
)

REM --- Compilation ----------------------------------------------------------
"%PY%" build_book.py --edition %CLASSE% --lang fr ^
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
