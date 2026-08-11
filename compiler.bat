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

set "OHM_RENDERER=D:\50ohm-amont\50ohm-main"
set "AMONT=D:\50ohm-amont\50ohm-contents-dl-main"
set "PYTHONIOENCODING=UTF-8"

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

set "VERSION="
if /i "%CLASSE%"=="N" set "VERSION=v0.9"
if /i "%CLASSE%"=="E" set "VERSION=v0.9"
if /i "%CLASSE%"=="A" set "VERSION=v1.2"

if not defined VERSION (
    echo.
    echo Classe inconnue : "%CLASSE%"  ^(attendu : N, E ou A^)
    pause
    exit /b 1
)

set "OUT=build-%CLASSE%"

echo.
echo ============================================================
echo  Compilation classe %CLASSE% ^(%VERSION%^)
echo ============================================================
echo.

REM --- Verifications prealables ----------------------------------------------
if not exist "%OHM_RENDERER%\renderer\document.py" (
    echo ERREUR : generateur ^(paquet renderer^) introuvable a
    echo   %OHM_RENDERER%
    echo Voir la memoire de session / CLAUDE.md pour le retelecharger
    echo ^(tarball codeload.github.com/DARC-e-V/50ohm^).
    pause
    exit /b 1
)
if not exist "%AMONT%\contents\sections" (
    echo ERREUR : contenu amont introuvable a
    echo   %AMONT%
    echo ^(tarball codeload.github.com/DARC-e-V/50ohm-contents-dl^)
    pause
    exit /b 1
)

where python >nul 2>nul
if errorlevel 1 (
    echo ERREUR : python introuvable dans le PATH.
    pause
    exit /b 1
)

REM --- Purge : un arbre non purge fait sortir latexmk en rc=12 ---------------
if exist "%OUT%" (
    echo Purge des auxiliaires LaTeX residuels dans %OUT%...
    del /q "%OUT%\*.aux" "%OUT%\*.fdb_latexmk" "%OUT%\*.fls" "%OUT%\*.toc" "%OUT%\*.idx" "%OUT%\*.log" "%OUT%\*.out" 2>nul
)

REM --- Dependance Python -------------------------------------------------
python -c "import mistletoe" 2>nul
if errorlevel 1 (
    echo Installation de mistletoe...
    python -m pip install --quiet mistletoe
)

REM --- Compilation ----------------------------------------------------------
python build_book.py --edition %CLASSE% --lang fr ^
    --translations traductions\%CLASSE% ^
    --input "%AMONT%" ^
    --output "%OUT%" ^
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

echo.
echo PDF genere   : %OUT%\book-%CLASSE%.pdf
echo Journal complet : %LOG%
echo.

REM --- Compression Ghostscript (facultative) ----------------------------
set "GSDIR="
for /d %%G in ("C:\Program Files\gs\gs*") do set "GSDIR=%%G"

if defined GSDIR (
    choice /m "Compresser le PDF avec Ghostscript maintenant "
    if not errorlevel 2 (
        echo.
        echo Compression en cours...
        "%GSDIR%\bin\gswin64c.exe" -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook ^
            -dDetectDuplicateImages=true -dNOPAUSE -dBATCH ^
            -sOutputFile=livre-%CLASSE%-%VERSION%.pdf "%OUT%\book-%CLASSE%.pdf"
        if exist "livre-%CLASSE%-%VERSION%.pdf" (
            echo.
            echo PDF compresse : livre-%CLASSE%-%VERSION%.pdf
        )
    )
) else (
    echo Ghostscript introuvable dans "C:\Program Files\gs\" -- compression ignoree.
)

echo.
pause
