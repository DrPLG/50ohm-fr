<#
.SYNOPSIS
    Gardien d'auxiliaires : sauvegarde le .aux sain d'une compilation longue.

.DESCRIPTION
    Copie periodiquement le fichier book-<CLASSE>.aux dans un sous-dossier
    gardien/, mais UNIQUEMENT quand ce .aux est celui d'une passe achevee.

    IL NE RESTAURE JAMAIS RIEN TOUT SEUL. C'est la difference essentielle avec
    le gardien.sh du bac a sable Linux, disparu du depot, qui restaurait
    automatiquement un .aux anterieur : c'est cette restauration qui reinjectait
    des numeros de page perimes et provoquait l'oscillation 198/200 sans fin sur
    les classes N et E (CLAUDE.md par. 4). En sauvegarde seule, la nuisance
    disparait : copier un fichier ne change pas la compilation en cours.

    Sur la machine de Pierre une compilation n'est plus tuee sans preavis
    (CLAUDE.md par. 11). Le risque reel est autre : un arret de la machine, une
    coupure, une erreur de manipulation. Le 05/09/2026, le NEA s'est arrete a la
    3e passe apres avoir DEJA converge a 816 pages aux passes 1 et 2 ; ces deux
    passes, soit pres de 1 h 10, ont ete entierement reperdues faute d'un .aux
    sauvegarde.

.PARAMETER Classe
    N, E, A, NEA ou SWL. Determine build-<CLASSE>\book-<CLASSE>.aux.

.PARAMETER IntervalleSecondes
    Delai entre deux inspections. 120 s par defaut : une passe de NEA dure une
    demi-heure, inutile de sonder plus souvent.

.PARAMETER Garder
    Nombre de copies conservees (les plus recentes). 3 par defaut.

.PARAMETER DureeMaxHeures
    Garde-fou : le gardien s'arrete de lui-meme au-dela. 6 h par defaut.

.EXAMPLE
    powershell -File gardien.ps1 -Classe NEA

.NOTES
    RESTAURATION -- manuelle, et c'est voulu. Apres un arret brutal :
      1. purger les auxiliaires LaTeX de build-<CLASSE> (PAS l'arbre genere :
         sections\, img\ et les .cls sont produits par Python et restent sains) ;
      2. copier la sauvegarde la plus recente en book-<CLASSE>.aux ;
      3. relancer latexmk, qui repart des numeros de page deja converges.
    Ne jamais restaurer un .aux dans un arbre dont les sources ont change
    depuis : les numeros de page seraient perimes, ce qui est exactement le
    defaut de l'ancien gardien.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('N', 'E', 'A', 'NEA', 'SWL')]
    [string]$Classe,

    [ValidateRange(10, 3600)]
    [int]$IntervalleSecondes = 120,

    [ValidateRange(1, 50)]
    [int]$Garder = 3,

    [ValidateRange(1, 24)]
    [int]$DureeMaxHeures = 6,

    # Delai de grace au demarrage : le gardien peut etre lance AVANT latexmk,
    # et la generation Python precede la premiere passe. Pendant cette periode,
    # l'absence de lualatex ne vaut pas fin de compilation.
    [ValidateRange(1, 120)]
    [int]$AttenteInitialeMinutes = 10
)

$ErrorActionPreference = 'Stop'
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

$racine = Split-Path -Parent $MyInvocation.MyCommand.Path
$build  = Join-Path $racine "build-$Classe"
$aux    = Join-Path $build  "book-$Classe.aux"
$coffre = Join-Path $build  'gardien'

if (-not (Test-Path $build)) {
    Write-Output "ERREUR : $build est introuvable. Lancer la compilation d'abord."
    exit 1
}
if (-not (Test-Path $coffre)) { New-Item -ItemType Directory -Path $coffre | Out-Null }

Write-Output "Gardien $Classe -- sauvegarde seule, aucune restauration automatique."
Write-Output "  surveille : $aux"
Write-Output "  coffre    : $coffre"
Write-Output "  intervalle: $IntervalleSecondes s, $Garder copie(s) conservee(s), arret a $DureeMaxHeures h"
Write-Output ""

$fin = (Get-Date).AddHours($DureeMaxHeures)
$graceJusqua = (Get-Date).AddMinutes($AttenteInitialeMinutes)
$dernierHash = ''
$copies = 0
$toursSansLatex = 0

while ((Get-Date) -lt $fin) {

    $sain = $false
    $hash = ''

    if (Test-Path $aux) {
        try {
            # Deux conditions, et les deux comptent :
            #  - non tronque : le dernier octet doit etre un saut de ligne. Un
            #    .aux surpris en cours d'ecriture casse la passe suivante
            #    (CLAUDE.md par. 4).
            #  - \DARCimageCache present : cette macro est ecrite au hook
            #    enddocument/afterlastpage, donc a la toute fin. Mesuree le
            #    05/09/2026 sur le NEA : ligne 7916 sur 7920. Sa presence
            #    atteste qu'une passe s'est achevee, et c'est le seul .aux qui
            #    vaille la peine d'etre garde.
            $octets = [System.IO.File]::ReadAllBytes($aux)
            if ($octets.Length -gt 0 -and $octets[-1] -eq 10) {
                $texte = [System.Text.Encoding]::UTF8.GetString($octets)
                # « \DARCimageCache { » et non « \DARCimageCache » nu : une
                # sous-chaine nue serait aussi trouvee dans un nom de macro plus
                # long. Forme reelle mesuree dans le .aux du NEA :
                #   \DARCimageCache {579include=0.9256,421include=0.92886,...
                if ($texte.Contains('\DARCimageCache {')) {
                    $sain = $true
                    $hash = (Get-FileHash -Path $aux -Algorithm SHA256).Hash
                }
            }
        } catch {
            # Fichier verrouille ou en cours d'ecriture : on repassera.
            $sain = $false
        }
    }

    if ($sain -and $hash -ne $dernierHash) {
        $nom = "book-$Classe-{0:yyyyMMdd-HHmmss}.aux" -f (Get-Date)
        Copy-Item -Path $aux -Destination (Join-Path $coffre $nom)
        $dernierHash = $hash
        $copies++
        $ko = [math]::Round($octets.Length / 1KB)
        Write-Output ("[{0:HH:mm:ss}] passe achevee -> {1} ({2} Ko)" -f (Get-Date), $nom, $ko)

        # Elagage : ne garder que les plus recentes.
        Get-ChildItem -Path $coffre -Filter "book-$Classe-*.aux" |
            Sort-Object LastWriteTime -Descending |
            Select-Object -Skip $Garder |
            Remove-Item -Force
    }

    # Arret spontane : plus aucun lualatex en vie, trois tours de suite.
    #
    # La condition ne depend PAS du nombre de copies faites, et c'est delibere :
    # une premiere version exigeait $copies -gt 0, si bien qu'une compilation
    # qui echouait avant la premiere passe laissait le gardien tourner a vide
    # jusqu'a DureeMaxHeures. Defaut trouve en testant le refus d'un .aux
    # tronque, le 05/09/2026 -- le cas ou le gardien ne copie jamais rien est
    # precisement celui ou il tournait le plus longtemps pour rien.
    $latex = @(Get-Process lualatex -ErrorAction SilentlyContinue)
    if ($latex.Count -eq 0) {
        if ((Get-Date) -gt $graceJusqua) {
            $toursSansLatex++
            if ($toursSansLatex -ge 3) {
                Write-Output ("[{0:HH:mm:ss}] plus aucun lualatex actif -- gardien arrete ({1} copie(s))." -f (Get-Date), $copies)
                break
            }
        }
    } else {
        $toursSansLatex = 0
    }

    Start-Sleep -Seconds $IntervalleSecondes
}

Write-Output ""
Write-Output "$copies sauvegarde(s) dans $coffre"
Get-ChildItem -Path $coffre -Filter "book-$Classe-*.aux" -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    ForEach-Object { Write-Output ("  {0}  {1:yyyy-MM-dd HH:mm:ss}" -f $_.Name, $_.LastWriteTime) }
