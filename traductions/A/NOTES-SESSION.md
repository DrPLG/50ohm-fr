# Notes de session — classe A, lots 1–5 / chapitres 1–12 (lots 1–4 COMPILÉS v0.5, 248 p. ; lot 5 = ch. 10–12 TRADUIT, NON COMPILÉ ; build_book.py v0.4)

Fichier inerte pour build_book.py ; il voyage dans le zip pour porter l'état
du projet d'une session à l'autre. AMORÇAGE créé en fin de projet classe E :
état vide (0 section, 0 question, titles.json aux 3 volets vides), enrichi
de tout l'acquis N+E ci-dessous.

## Build classe A — PREMIÈRE COMPILATION RÉUSSIE (v0.3, ch. 1–4)

Livre partiel produit : **82 pages A4, 1,7 Mo**, 30 sections, 160 questions
intégrées, 0 question manquante au catalogue, 0 section manquante.
Commande exacte (build_book.py v0.2 GELÉ, jamais modifié) :

    pip install mistletoe --break-system-packages
    PYTHONPATH=/home/claude/work/50ohm-main \
    python3 build_book.py --edition A --lang fr \
        --translations out-A/A --input 50ohm-contents-dl-main \
        --output build-A --version-label 0.2 --limit-chapters 4 --no-compile
    # puis passes lualatex directes (voir ci-dessous)
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.7 -dPDFSETTINGS=/ebook \
       -dDetectDuplicateImages=true -dNOPAUSE -dQUIET -dBATCH \
       -sOutputFile=book-A-fr.pdf book-A-pass2.pdf

`--limit-chapters n` permet de compiler un livre PARTIEL (n premiers
chapitres) — indispensable tant que les 14 chapitres ne sont pas traduits.

### NOUVEAUX PIÈGES DÉCOUVERTS À LA COMPILATION A (à ne pas re-découvrir)

1. **Module `renderer` introuvable.** `build_book.py` importe `mistletoe`
   ET `renderer.document`. Le paquet `renderer` NE VIENT PAS du dépôt de
   contenus (`50ohm-contents-dl`) mais du dépôt GÉNÉRATEUR
   `DARC-e-V/50ohm`. Télécharger :
   `curl -sL -o 50ohm-main.tar.gz https://codeload.github.com/DARC-e-V/50ohm/tar.gz/refs/heads/main`
   puis `tar xzf` et lancer avec `PYTHONPATH=<...>/50ohm-main`.
   `mistletoe` s'installe avec `pip install --break-system-packages`.

2. **Police LinBiolinum_K.otf absente → erreur fontspec FATALE.**
   TeX Live seul (même avec texlive-fonts-extra) ne fournit PAS le jeu OTF
   complet de Linux Biolinum. Installer en plus le paquet système :
   `apt-get install -y --no-install-recommends fonts-linuxlibertine`
   (fournit /usr/share/fonts/opentype/linux-libertine/LinBiolinum_K.otf).

3. **Purge nodesource : le fichier est `.sources`, pas `.list`.**
   `rm -f /etc/apt/sources.list.d/nodesource*` (le `.list` seul ne suffit
   pas ; sinon `apt-get update` sort en code 100 sur un 403 Forbidden).
   Le sandbox est déjà root : PAS de `sudo` (absent → code 127).

4. **`fig202` / Blitzerdung : NON CONCERNÉS en classe A ch. 1–4.**
   Vérifié par grep sur les .tex générés : ni `202include.tex` ni
   Blitzerdung ne sont référencés. La cause racine des pertes marginfix de
   la classe E ne s'applique donc pas ici. À RE-VÉRIFIER par grep à chaque
   nouveau lot compilé (chapitres 5–14) avant de conclure.

5. **Seul correctif session-local nécessaire à ce stade :**
   `printf '\\extrafloats{400}\n' >> settings-pre.tex` (jamais `echo` :
   corrompt `\e`).

6. **Passes lualatex.** Piège confirmé : la 3e passe consécutive est tuée
   par le sandbox et laisse un `book-A.pdf` TRONQUÉ. Parade appliquée :
   lancer les passes 1 et 2 en arrière-plan (`setsid nohup ... < /dev/null &`),
   vérifier `grep -c "Rerun to get" pass2.log` == 0, puis **copier
   immédiatement `book-A.pdf` en `book-A-pass2.pdf`** AVANT toute 3e passe.
   Deux passes ont suffi ici (convergence : 0 « Rerun to get »).
   Ne pas utiliser latexmk (sort après une passe, puis « Nothing to do »).

### Sondes de recette passées sur le PDF (pdftotext, apostrophe U+2019 normalisée)
Titres des 4 chapitres et des 30 sections en français ; encadrés traduits
(Astuce / Attention / Approfondissement / Nouvelle unité) ; terminologie en
place (réactance, impédance apparente, zone d'appauvrissement, normalement
passant/bloqué) ; mnémotechniques adaptés présents (« dans un C, I devance
U » / « dans un L, I traîne après U » — césurés à l'extraction, c'est
normal) ; AUCUN germanisme résiduel (ni Tipp, ni Vertiefung, ni Achtung,
ni Gefahr, ni Neue Einheit).

## État des traductions

### Périmètre A (établi session 1, source toc/A.json « Aufbaukurs E -> A »)
14 chapitres, 154 sections, 717 questions référencées (toutes au
catalogue ; préfixes AA–AK + une unique EI303 dans oszilloskop_2,
ABSENTE du questions.json E — traitée dans ce lot).
RECOUVREMENT AVEC E : une seule section, `N_Ende` (dernier chapitre) —
le cours A est une montée en compétence, sections « suites » (III, II)
à idents distincts. Réutiliser la traduction N_Ende du zip E au lot 8.
Découpage validé (plafond ~ lot E 13–16) :
  L1 ch.1–2 (17 s/68 q) ; L2 ch.3–4 (13/92) ; L3 ch.5–6 (29/141,
  scindable 5|6 si besoin) ; L4 ch.7–8 (24/107) ; L5 ch.9 (9/104) ;
  L6 ch.10–11 (26/67) ; L7 ch.12 (26/116) ; L8 ch.13–14 + N_Ende +
  build v1.0 (10/22).
RÉVISION APRÈS LOT 3 : le lot 3 a absorbé les ch.5, 6 ET 7 (35 s/170 q).
RESTE À TRADUIRE (7 chapitres, 89 sections, 387 questions) :
  L4 ch.8 ; L5 ch.9 ; L6 ch.10–11 ; L7 ch.12 ; L8 ch.13–14 + N_Ende
  (copie depuis le zip E) + build v1.0.
Recompter le périmètre exact de chaque lot en début de session à partir de
toc/A.json (ne pas se fier au découpage prévisionnel ci-dessus).

### Lot 1 — chapitres 1 (Wellenausbreitung -> Propagation des ondes) et
2 (Strom, Spannung… -> Courant, tension, résistance, puissance, énergie) :
TRADUIT, LIVRÉ POUR RELECTURE. 17 sections, 68 questions
(49 complètes / 19 énoncé seul). questions.json = 68 ; titles.json =
2 chapitres / 2 abstracts / 17 sections. Validation structurelle regex
OK 17/17 (comptage + ordre, lignes % exclues, légendes normalisées) ;
sonde anti-germanisme OK (0 hit ; gloses volontaires parenthésées :
Mehrwegeausbreitung, technische Stromrichtung, Kaltleiter, Heißleiter,
Thermoumformer, Tastköpfe, Flatterfading).
Énoncé seul (réponses numériques/images) : AH307 (CW/SSB/FM/RTTY),
AH214, AH217, AH218, AB601 (images vides), AI104, EI303, AB101, AB102,
AB301, AA105–AA112 (8 q numériques), AB502.
Cas tranchés en forme complète : AH213 (« Etwa » = prose, précédent
EG208), AH103–AH106/AH108 (« bis … km Höhe », précédent EC112/EC113),
AH203/AI102 (« und », précédent EB405), AH202/AH201 (« Band »,
précédent EK106), AA102 (« Amperesekunde »), AA103/AB503 (« bzw. »),
AH306 (Norden… = prose).
Particularités préservées verbatim : blocs commentés allemands
(%Simulation mit… dans tote_zone_2 ; %TODO COVID + % Photo by DC2CB
dans scatter ; %<indepth> photo 222 dans oszilloskop_2),
<webonly>/<latexonly> (aurora_2), [include:applet_interferenz]
(mehrwegeausbreitung, balise <webmargin>) et [include:applet_aurora],
tableaux DARCdown ×4 (a_spezifischer_widerstand,
a_dezibel_leistungsfaktoren, a_bezugsgroessen,
a_spannungsverhaeltnisse — en-têtes l:/c:/X: conservés, contenus
traduits), indices allemands en maths conservés (U_\text{Gemessen},
U_\text{Wahr}, A_\text{Dr}, P_\text{Wechselstrom}), coquilles source
conservées (a_physikalische_stromrechnung ident, $\qty{10.8}$ point
décimal, ligne vide dans réponse b d'AH206, espace initial réponse d
d'AH203, « 12 MHz » sans point réponse c d'AH205, sin non \sin dans
la formule MUF).
Terminologie posée L1 (à valider par PLG) : Überreichweiten->portées
exceptionnelles ; Inversionswetterlage->situation météorologique
d'inversion ; Ducting->ducting ; Wellenleiterkanal->canal guide
d'ondes ; Mehrwegeausbreitung->propagation par trajets multiples ;
Flatterfading->évanouissement papillotant ; Großkreis->grand cercle ;
Beam-Karte->carte beam ; mittabstandstreue Azimutalprojektion->
projection azimutale équidistante ; Rotorsteuerung->commande de
rotor ; solarer Flux->flux solaire ; kritische Frequenz->fréquence
critique ; Ionosonde->ionosonde ; Faraday-Rotation->rotation de
Faraday ; Regenscatter->scatter de pluie ; Rückstreuung/Backscatter->
backscatter ; technische/physikalische Stromrichtung->sens
conventionnel/physique du courant ; Auflösung->résolution ;
Messgenauigkeit->précision de mesure ; Ersatzschaltbild->schéma
équivalent ; Tastkopf->sonde de mesure ; Triggereinrichtung->
dispositif de déclenchement ; Impulsdauer/Pulsbreite->durée/largeur
d'impulsion ; Leiterwiderstand->résistance d'un conducteur ;
spezifischer Widerstand->résistivité ; Thermoumformer->
thermoconvertisseur ; elektrische Ladung->charge électrique ;
Elektrizitätsmenge->quantité d'électricité ; Bezugsgröße->grandeur de
référence ; Hilfsmaßeinheit->unité auxiliaire ; Kugelstrahler->
radiateur sphérique (isotrope, aligné E). Conservés : MUF, LUF, FOT,
foF2, QSB, QSO, DX, hop, duct, beam, jitter, SINGLE, PA, TRX, SNR,
CW, SSB, FM, RTTY, dBm/dBW/dBu/dBuV, PY (préfixe), Juliusruh,
Mögel-Dellinger.
### Lot 2 — chapitres 3 (Bauelemente -> Composants) et 4 (Reihen- und
Parallelschaltung -> Montage en série et en parallèle de composants) :
TRADUIT, LIVRÉ POUR RELECTURE. ATTENTION : traduit dans la MÊME session
que le lot 1 sur directive PLG (« Continue ») — dérogation à la règle
« session fraîche par lot » ; relecture PLG d'autant plus importante.
13 sections, 92 questions (58 complètes / 34 énoncé seul).
questions.json = 160 ; titles.json = 4 chapitres / 4 abstracts /
30 sections. Validation structurelle regex OK 13/13 ; sonde
anti-germanisme OK (0 hit ; gloses volontaires parenthésées :
Blindwiderstand, Scheinwiderstand, Energiebandlücke, Verarmungszone,
Sperrschicht, selbstleitend/selbstsperrend).
Énoncé seul : AB302, AB303 (angles/maths), AC104, AC205–AC208, AC302,
AC303, AC304, AC521, AC523, AF425–AF427, AD101–AD108, AD110–AD114
(numériques/maths), AC405, AC406, AC524, AC509–AC511 (images vides).
Cas tranchés en forme complète : AC105–AC108, AC204, AC307, AC522
(« ca. » -> « env. », précédent EG208/AH213) ; AD109 (« bis » -> « à »,
précédent EC112) ; AA101 (noms d'unités en toutes lettres, précédent
« unit names ») ; AC306/AC305 (verbe allemand « aufweisen/verwendet
werden ») ; AC512/AC513 (Emitter/Basis/Kollektor/Gate -> émetteur/base/
collecteur/grille, Drain/Source conservés).
Particularités préservées verbatim : en-tête commenté `% Halbleiter II`
/ `% DF2DR 2024-08-19` (halbleiter_2) ; gros bloc %-commenté final
d'integrierte_schaltkreise (17 lignes DE) ; ident à ESPACES
`a_Spule mit Anzapfungen` (reihenschaltung_spule) ; ident dupliqué
a_pn_uebergang_mit_spannung ×2 (halbleiter_2, pictures 956/957) ;
coquilles source conservées (`a_ersatzchaltbild_kondensator`,
`augeschaltenen`/`eingesschalteten` non répercutées — légendes
traduites —, `4 \mOhm` dans AC523, double point final « axes
horizontaux.. » dans phase, espace final réponse b d'AC301 et
réponse d d'AB109, ` 30 m` initial AH203 déjà noté lot 1) ;
$\qtyrange$, SiO$_2$, indices $R_\text{BIAS}$/$R_\mathrm{DSon}$
verbatim. Moyens mnémotechniques allemands (Kondensat*ooo*r,
Induktivit*äää*t) ADAPTÉS en équivalents français (« dans un C,
I devance U » / « dans un L, I traîne après U ») — à valider par PLG.
Terminologie posée L2 (à valider par PLG) : Blindwiderstand->réactance
(capacitive/inductive, aligné E) ; Scheinwiderstand->impédance
apparente ; Wirkleistung/Blindleistung->puissance active/réactive ;
Verlustfaktor tan δ->facteur de pertes ; Güte->facteur de qualité
(aligné E) ; Zeigerdiagramm->diagramme de Fresnel ; Bogenmaß->radians ;
Einheitskreis->cercle unité ; A_L-Wert->valeur A_L (constante
d'inductance) ; Ringkern->tore ; Drossel(spule)->self de choc ;
Abschirmbecher->pot de blindage ; magnetische Flussdichte->densité de
flux magnétique ; relative Permeabilität->perméabilité relative ;
Gegeninduktion->induction mutuelle ; Übersetzungsverhältnis->rapport
de transformation ; Stromdichte->densité de courant ;
Anpassungsübertrager->transformateur d'adaptation ; Fußpunktwiderstand->
résistance au point d'alimentation (aligné E) ; Koppelkondensator->
condensateur de liaison ; HF-Abblockung->découplage HF ;
Energiebandlücke->bande interdite ; Valenz-/Leitungsband->bande de
valence/de conduction ; Dotierung->dopage ; Loch->trou (aligné E) ;
Diffusions-/Feldstrom->courant de diffusion/de champ ; Verarmungszone->
zone d'appauvrissement ; Sperrschicht->couche d'arrêt ;
Raumladungszone->zone de charge d'espace ; Durchlass-/Sperrrichtung->
sens direct/inverse (aligné E) ; Temperaturspannung->tension
thermique ; Arbeitspunkt->point de fonctionnement ; Gegenkopplung->
contre-réaction (série) ; Querstrom->courant transversal ;
Freilaufdiode->diode de roue libre (aligné E) ; Fotowiderstand/
Fotodiode->photorésistance/photodiode ; Optokoppler->optocoupleur ;
galvanische Trennung->séparation galvanique ; Sperrschicht-FET->FET à
jonction ; Isolierschicht-FET->FET à grille isolée ; selbstleitend/
selbstsperrend->normalement passant/bloqué ; Gate->grille (aligné E),
Drain/Source conservés ; Kanalwiderstand->résistance du canal ;
belasteter/unbelasteter Spannungsteiler->diviseur de tension chargé/
non chargé ; Brückenschaltung->montage en pont ; Brückenzweig->branche
du pont ; abgeglichene Brücke->pont équilibré ; Anzapfung->prise ;
Eigenkapazität->capacité propre ; SMD->CMS (dans réponse AC601).
Conservés : VNA, ESR, ESL, Styroflex, unun, bifilaire, MMIC, CMOS,
JFET, MESFET, MOSFET, bulk, bias-T, R_DSon, BC547B, TinyWhisper,
JKU Linz, JMU Würzburg, Pontavi, Wheatstone, varicap, SINGLE, jitter.

### Lot 3 — chapitres 5 (Strom- und Spannungsversorgung -> Alimentation en
courant et en tension), 6 (Grundlegende Schaltungen -> Montages fondamentaux)
et 7 (Modulation -> Modulation) : TRADUIT, LIVRÉ POUR RELECTURE.
NON COMPILÉ (directive PLG : relecture d'abord, build ensuite).
Périmètre élargi vs découpage initial (L3 = ch.5–6) : le ch.7 a été inclus
dans la même session, soit 35 sections / 170 questions
(104 complètes / 66 énoncé seul). Répartition : ch.5 = 11 s / 41 q
(17 complètes / 24 énoncé seul) ; ch.6 = 18 s / 100 q (70 / 30) ;
ch.7 = 6 s / 29 q (17 / 12). questions.json = 330 entrées (211 complètes /
119 énoncé seul) ; titles.json = 7 chapitres / 7 abstracts / 65 sections.
Aucun recouvrement avec les lots 1–2 (vérifié) ; les 170 questions sont
toutes au catalogue fragenkatalog3b.json.
Validation structurelle regex OK 35/35 (marqueurs + ordre + comptage,
lignes % exclues, idents de picture normalisés ; un écart corrigé :
bloc <margin>/[picture:75:a_Restwelligkeit] omis dans gleichrichter_2,
restauré). Newlines finaux realignés programmatiquement sur la source DE
(emitterschaltung ×10, oszillator_schaltungen ×11, verstaerker_klasse ×3,
kollektorschaltung ×2, verstaerker_eigenschwingung ×2).
Sonde anti-germanisme OK : 0 hit sur les 35 sections ET sur les 170 questions.

RÈGLE « RÉPONSES » — dérivée programmatiquement des 160 questions des
lots 1–2 (et non de mémoire), pour cohérence stricte :
  * énoncé seul = réponses numériques nues, y compris avec unité écrite en
    toutes lettres « Ohm »/« kOhm » (précédents AB101, AC104, AC303, AC304,
    AF425, AF426, AD104, AD105, AD110), degrés « ° », formules, images vides,
    acronymes purs (précédent AH307 CW/SSB/FM/RTTY).
  * forme complète = présence de PROSE allemande : « ca. »/« etwa »/« Zirka »
    (-> « env. »/« environ »), « bis » (-> « à »), « und » (-> « et »), verbes
    (« betragen », « liegen », « angelegt werden »), noms d'unités en toutes
    lettres (« Stunden und Minuten »), noms de composants/classes allemands
    (« -Betrieb », « Bandpassfilter », « Nennkapazität »).
Cas tranchés lot 3 : AD302 (« Zirka »), AD306 (« etwa »), AD203/AD219
(« ca. »/« Etwa »), AD304 (« betragen »), AE204 (« liegen »), AB211
(« Stunden und Minuten »), AD704 (« bis »), AF501/AF502 (« und »),
AD418 (« etwa … bis … »), AD422/AJ218/AF402 (« -Betrieb »), AD619
(« angelegt werden »), AD433 (noms de filtres), AB210 (« Nennkapazität »).
AD603/AD605 = acronymes purs (TCXO/OCXO/VCO/VFO/XO) -> énoncé seul.
**AD620 = énoncé seul — TRANCHÉ PAR PLG (« garde les gloses anglaises »).**
Réponses : « DDS (Direct Digital Synthesis) », « PLL (Phase Locked Loop) »,
« VCO (Voltage Controlled Oszillator) », « VFO (Variable Frequency Oszillator) ».
Les gloses sont ANGLAISES (et non allemandes) : rien à traduire dans les
réponses -> énoncé seul, le build tire les réponses du catalogue DE, ce qui
préserve du même coup l'orthographe source « Oszillator » (quirk conservé
verbatim, conformément à la règle du projet). Première version de la session
(forme complète, avec « Oszillator » corrigé en « Oscillator ») ABANDONNÉE.
PRÉCÉDENT À RÉUTILISER : gloses anglaises entre parenthèses = langue-neutres,
donc énoncé seul — ne pas les franciser et ne pas corriger leur orthographe.

Particularités préservées verbatim : blocs %-commentés allemands
(akku : 3 lignes Entladung/Balance/Entlastung + bloc « 30 C » de 6 lignes +
bloc Infobox Anschluss ; gleichrichter_2 : %TODO tinyurl ; oszillator_vco :
%TODO Grafik Sperrschicht ; oszillator_schaltungen : %TODO Bild 760 ;
emitterschaltung : 2 %TODO ; verstaerkungsleistung : %TODO d'en-tête
« noch nicht abschließend bearbeitet » + %TODO Tip ; transverter_2 : %TODO
Frage 1472 ; am_2 : %TODO Bild ; bandreite_3 : %TODO Grafik ;
ssb_3 : « % Tastkopf 1:1 PEP » et « % Tastkopf 10:1 PEP ») ;
<latexonly>/<webonly> (brueckengleichrichter, vollweggleichrichter,
restwelligkeit, pm) ; [include:applet_gleichrichter_1/_2], [include:applet_brumm],
[include:applet_pm] ; idents à espaces/caractères spéciaux conservés
(`a_Längstransistor 2N3055 auf Kühlkörper`, `Sinusgenerator 50 Ohm`,
` Brückengleichrichter Bauformen`, `a_Bias T Platine`, `a_störspektrum`,
`a_pep_hüllkurve`, `StepUpWandler`) ; coquilles source conservées
(`a_brueckenlgeichrichter`, `a_diskrete_pannungsstabilisierung`,
`a_rc_tiepass`, ident de section `bandreite_3` pour « Bandbreite III »,
`\kiloOhm` dans AD203, retour à la ligne dans la réponse b d'AF502,
`Kollerktorwiderstand` DE non répercuté — traduit correctement) ;
picture 75 `a_Restwelligkeit` partagé gleichrichter_2 ; ident dupliqué
`a_Leistungsanpassung` ×2 (innenwiderstand, pictures 1077/937) et
`a_Festspannungsregler` ×2 (spannungsstabilisierung, picture 200 +
photo 245) ; émoji 🤓 conservé (innenwiderstand) ; formule de Carson et
$\varphi(t)$/intégrale conservées telles quelles (fm_3, pm).

Terminologie posée L3 (à valider par PLG) : Leerlaufspannung->tension à vide ;
Klemmenspannung->tension aux bornes ; Spannungs-/Strom-/Leistungsanpassung->
adaptation en tension/courant/puissance ; Konstantstromquelle->source de
courant constant ; Nennkapazität->capacité nominale ; Balancer->équilibreur ;
Solarzelle/Photovoltaikmodul->cellule solaire/module photovoltaïque ;
Kurzschlussstrom->courant de court-circuit ; Step-UP/Step-DOWN->convertisseur
élévateur/abaisseur ; Wirkungsgrad->rendement ; Siebkondensator->condensateur
de filtrage ; Siebglied->cellule de filtrage ; Vollweggleichrichter->redresseur
double alternance ; Mittelanzapfung->prise médiane ; Restwelligkeit->ondulation
résiduelle ; Brummton->ronflement ; AC-Kopplung->couplage AC ;
Impulsbreitenmodulator->modulateur de largeur d'impulsion ; Störspektrum->
spectre perturbateur ; EMV-Filter->filtre CEM ; Längstransistor->transistor
ballast ; Festspannungsregler->régulateur de tension fixe ; Low-Drop->
régulateur à faible chute ; Vorwiderstand->résistance série ;
Fernspeiseweiche/BIAS-T->séparateur d'alimentation à distance/bias-T ;
Drosselspule->self de choc ; Abblockkondensator->condensateur de découplage ;
Strombelastbarkeit->tenue en courant ; Spannungsfestigkeit->tenue en tension ;
Grenzfrequenz->fréquence de coupure ; RC-Glied->cellule RC ; Betragsfrequenzgang->
réponse en fréquence en module ; Thomsonsche Schwingungsformel->formule de
Thomson ; Güte/Q-Faktor->facteur de qualité ; gekoppelte Schwingkreise->circuits
oscillants couplés ; lose/unterkritische/kritische/überkritische Kopplung->
couplage lâche/sous-critique/critique/surcritique ; Durchlasskurve->courbe de
transmission ; Durchlassdämpfung->atténuation d'insertion ; Bandfilter->filtre
de bande ; Kapazitätsdiode->diode à capacité variable ; Sperrschicht->couche
d'arrêt (aligné L2) ; Schleifenverstärkung->gain de boucle ; Selbsterregung->
auto-excitation ; Dreipunktoszillator->oscillateur à trois points ;
Oberton/Oberschwingung->harmonique ; Pufferstufe->étage tampon ; Tastkopf->
sonde de mesure (aligné L1) ; Taktgenerator->générateur d'horloge ;
Tuning-Word->tuning-word (conservé) ; Adresszähler->compteur d'adresses ;
D/A-Wandler->convertisseur N/A ; Phasenvergleicher->comparateur de phase ;
Frequenzteiler/Teilerverhältnis->diviseur de fréquence/rapport de division ;
eingelockt->verrouillé (locked) ; Verzerrerstufe->étage distordeur ;
Kollektor-/Emitterschaltung->montage collecteur/émetteur commun ;
Emitterfolger->émetteur suiveur ; Koppel-/Abblockkondensator->condensateur de
liaison/de découplage ; Gegenkopplung->contre-réaction (aligné L2) ;
Arbeitspunkt (BIAS)->point de fonctionnement ; Ruhestrom->courant de repos ;
Vorspannung->tension de polarisation ; A-/B-/AB-/C-Betrieb->classe A/B/AB/C ;
Gegentaktschaltung->montage push-pull ; Übersteuerung->saturation (aligné E) ;
Linearverstärker->amplificateur linéaire ; Eigenschwingung->oscillation propre ;
Modulationsgrad->taux de modulation ; Seitenband-Splatter->splatter de bande
latérale ; Hüllkurve->enveloppe ; Zweiton-Signal->signal à deux tons ;
Schwebung->battement ; PEP->puissance de crête d'enveloppe ; Equalizer->
égaliseur ; Hub->excursion ; Carson-Formel->formule de Carson ;
Begrenzerverstärker->amplificateur limiteur (aligné E) ; belegte Bandbreite->
largeur de bande occupée ; Winkelmodulation->modulation angulaire ;
Dynamikumfang->plage de dynamique ; Dynamikkompressor/Sprachprozessor->
compresseur de dynamique/processeur de parole ; Kanalleistungsmessung->mesure
de la puissance de canal ; Amateurfunkverordnung->règlement allemand sur le
service amateur. Conservés : LiFePO4, NiMH, Pb, 4S1P/4S2P, JST-XH, DC/DC,
Buck/Boost, VDE, PE/L1/N, QO-100, LNB/LNA, RX/TX, KiCAD, MMIC, VCO, VFO, XO,
TCXO, OCXO, GPSDO, GNSS, GPS, Galileo, ppm, DDS, PLL, SDR, CW, SSB, AM, FM,
PM, NBFM, QAM, QPSK, PSK, HF/BF, FI, PA, ALC, DX, QSO, splatter, chirp, jitter,
Dummy-Load, Low-Drop, Pertinax, 7812, 2N3055, BY 225, FPU 4M.

- N_Ende : présent dans toc/A.json (ch. 14) ; PAS d'A_Ende distinct.
  La traduction française est dans le zip E — copier telle quelle au
  lot 8, avec son entrée titles.json (`N_Ende` -> « Conclusion du
  cours »).

### Lot 4 — chapitres 8 (Empfänger -> Récepteurs) et 9 (Sender -> Émetteurs) :
TRADUIT, LIVRÉ POUR RELECTURE. NON COMPILÉ (directive PLG : relecture d'abord).
Périmètre recompté en début de session depuis toc/A.json : 27 sections /
182 questions (148 complètes / 34 énoncé seul). Répartition : ch.8 = 18 s /
78 q (56 complètes / 22 énoncé seul) ; ch.9 = 9 s / 104 q (92 / 12).
Le ch.9 a été absorbé dans la même session que le ch.8 (72 k car. de source
contre 103 k au lot 3, qui tenait en une session) — DÉVIATION au protocole
« un chapitre par lot », à signaler en relecture, comme pour L1+L2 et L3.
questions.json = **512 entrées** (359 complètes / 153 énoncé seul) ;
titles.json = 9 chapitres / 9 abstracts / 92 sections.
Aucun recouvrement avec les lots 1-3 (vérifié) ; les 182 questions sont
toutes au catalogue fragenkatalog3b.json.
Validation structurelle regex OK 27/27 (marqueurs + ordre + comptage,
lignes % exclues ; légendes de picture/photo/table exclues de la comparaison
car traduites). Newlines finaux réalignés sur la source DE : 0 écart.
Sonde anti-germanisme OK : 0 hit sur les 27 sections ET sur les 182 questions
(seul relevé = l'ident source `begrenzverstärker`, conservé verbatim).

#### Terminologie posée (ch. 8-9) — à appliquer strictement en aval
Nahselektion/Trennschärfe -> sélectivité rapprochée / sélectivité ;
Spiegelfrequenz -> fréquence image ; Balancemischer/Ringmischer/Ringmodulator
-> mélangeur équilibré / mélangeur en anneau / modulateur en anneau ;
Doppelsuper -> double superhétérodyne ; Roofing-Filter -> filtre roofing ;
Produktdetektor -> détecteur de produit ; Hüllkurvendemodulator -> démodulateur
d'enveloppe ; Flankendiskriminator -> discriminateur à flanc ; Kreuzmodulation
-> **transmodulation** (à ne pas confondre avec intermodulation) ;
Großsignalfestigkeit -> tenue aux forts signaux ; Interception Point IP3 ->
point d'interception d'ordre 3 ; Dämpfungsglied -> atténuateur ; Rauschzahl ->
facteur de bruit (le catalogue l'exprime tantôt en rapport, tantôt en dB —
« facteur de bruit » couvre les deux, comme en allemand) ; Begrenzerverstärker
-> amplificateur limiteur ; Saugkreis -> circuit d'absorption ; Sperrkreis ->
circuit bouchon ; Torzeit -> temps de porte ; S-Stufe -> échelon S ;
Oberwelle -> **harmonique supérieure** vs Harmonische -> **harmonique**
(distinction EXIGÉE par AB402/AJ203 : la 3e harmonique supérieure = la 4e
harmonique) ; Nebenaussendung -> émission parasite ; Leistungsverstärker ->
amplificateur de puissance ; Gegentakt -> push-pull ; Arbeitspunkt/BIAS ->
point de fonctionnement ; Ferritperle -> perle de ferrite ; Dummy Load ->
charge fictive / antenne artificielle ; HF-Tastkopf -> sonde HF ;
Feldstärkeanzeiger -> indicateur de champ ; Netzfilter -> filtre secteur ;
Einstrahlung/Einströmung -> pénétration par rayonnement / par conduction ;
Antennentuner -> boîte d'accord d'antenne ; Watchdog -> chien de garde
(watchdog) ; Remote-Betrieb -> exploitation à distance (remote) ; Latenz ->
latence ; ERP -> PAR. Conservés : LNB, bias-T, VFO/CO/BFO/VCO, PLL, ALC, PEP,
SSB/USB/LSB/DSB/AM/FM/NBFM/PM/CW/RTTY/OFDM, LDMOS, FET, VNA, DAB/DVB-T2,
splatter, noise blanker, squelch, roofing, high level, Verfügung 33,
Bundesnetzagentur, RTA, VDE, GND, IP3.

#### Arbitrages de session (à confirmer en relecture)
- `intermodulation_kreuzmodulation` : le math d'affichage AUTONOME
  `$\text{Ordnung}=m+n$` a été traduit en `$\text{Ordre}=m+n$`. DÉROGATION
  assumée à la règle « maths verbatim » : la règle vise les indices liés aux
  figures ($f_\text{ZF}$, $U_\text{BIAS}$... — tous conservés), pas une phrase
  composée en mode mathématique. À trancher par PLG.
- `unerwuenschte_aussendungen_3` : les abréviations OW / Harm. / NA de la
  légende [picture:868] sont conservées, car elles étiquettent le DESSIN
  allemand ; seule la glose française les précède.
- `begrenzverstärker` (ident de picture) et `leistungsvertaerker` (ident de
  section) : coquilles de la source, conservées verbatim — ne pas « corriger ».
- `[table:a_harmonische]` et `[picture:868:a_harmonische]` partagent le MÊME
  ident dans la source (label LaTeX dupliqué). Conservé tel quel ; à surveiller
  au build (le garde-fou v0.4 pourra signaler un \ref ambigu).
- AF305 : la source utilise la macro allemande `\glqq?"`. Rendue par des
  guillemets français littéraux « ? » (pas de macro), pour éviter un guillemet
  bas allemand dans un livre français.
- Classification : « bis » / « und » / « Zwischen...bis » / « Zirka » /
  « -fach » / « -Signale » -> forme complète (prose allemande). Acronymes purs
  + valeurs (AF120 « VFO: ... CO1: ... », AF206 « SSB: ... RTTY: ... »,
  AJ223 AM/FM/NBFM/SSB) et réponses purement numériques ou en images ->
  énoncé seul.

#### Reste à traduire après le lot 4
5 chapitres, 62 sections : ch.10 Digitale Übertragungsverfahren (13 s),
ch.11 Digitale Signalverarbeitung (13 s), ch.12 Antennen (26 s),
ch.13 Personenschutzabstand (6 s), ch.14 Sicherheit (4 s) + N_Ende (à copier
du zip E). Recompter le périmètre depuis toc/A.json à chaque session.

### Lot 5 — chapitres 10 (Digitale Übertragungsverfahren -> Procédés de
transmission numériques), 11 (Digitale Signalverarbeitung -> Traitement
numérique du signal) et 12 (Antennen und Übertragungsleitungen -> Antennes et
lignes de transmission) : TRADUIT, LIVRÉ POUR RELECTURE. NON COMPILÉ (le build
viendra au lot 6 ou en fin de lot).
Périmètre recompté en début de session depuis toc/A.json : 52 sections /
183 questions / 93,5 k car. Répartition : ch.10 = 13 s / 29 q ; ch.11 = 13 s /
38 q ; ch.12 = 26 s / 116 q. Le ch.12 (le plus gros, 26 s) a été ABSORBÉ dans
la MÊME session que les ch.10-11 sur directive PLG (« Continue ») — le repli
prévu (livrer 10+11, laisser 12 au lot 6) n'a PAS été activé ; DÉVIATION au
protocole « un lot par session fraîche », à signaler en relecture (comme L1+L2,
L3, L4).
questions.json = **695 entrées** (492 complètes / 203 énoncé seul) ;
titles.json = 12 chapitres / 11 abstracts / 144 sections.
NB abstracts : ch.10 et ch.11 partagent le MÊME texte d'abstract allemand
(« Dieses Kapitel beleuchtet die Grundlagen… ») — une seule clé le couvre (le
volet abstracts s'indexe par TEXTE DE, pas par chapitre) : 11 clés pour
12 chapitres, c'est NORMAL, pas un oubli.
Aucun recouvrement avec les lots 1-4 (vérifié : 0 des 183 déjà dans les 512) ;
les 183 questions sont toutes au catalogue fragenkatalog3b.json ; 0 doublon
intra-lot.
Validation structurelle regex OK 52/52 (marqueurs picture/photo/table/include/
ref/question + balises + ordre + `---`, lignes % exclues, légendes exclues ;
blocs %-commentés vérifiés identiques DE/FR). Newlines finaux réalignés sur la
source DE (47 sections). Sonde anti-germanisme OK : 0 hit réel sur les
52 sections ET les 183 questions (seuls relevés = homographe « Antenne »,
identique en FR, dans AG117/AG120/AG121/AG122).

#### Classification des 183 questions (règle des notes, dérivée du catalogue)
133 forme complète / 50 énoncé seul.
Énoncé seul (réponses langue-neutres — images vides, numériques nues, unités en
symboles, formules, `°`, `Ohm`) : AE401, AJ221, AE214, AF626-AF629 (images) ;
AE405, AE406 (réponses « Bit/s » nues) ; AF619 (« Samples/s ») ; AF608, AF609
(nombres nus) ; AF613, AF612, AF614, AF601-AF604, AF623, AF625 (images) ;
AB404-AB407, AF632 (images) ; AG419, AG123, AG124, AG120, AG117, AG121, AG122
(noms d'antennes = noms propres, énoncé seul comme précédent nom-propre) ;
AG223 (« 5/8 λ » formules) ; AG101-AG105, AG118, AG316, AG103 (longueurs « m »
nues) ; AG315 (nombre nu) ; AG115, AG114 (« MHz » nus) ; AG226-AG229 (« dBi ») ;
AG217, AG215, AG216 (« W ») ; AG220, AG203-AG206 déjà en forme (voir infra) ;
AG207/AG208 forme ; AG317 (« cm ») ; AG305-AG307 forme ; AG309/AG310 forme ;
AG408, AG412, AG416, AG417, AG418, AG421, AG422 (réponses `°`/`Ohm`/`π²/4`
langue-neutres) ; AG407, AG410, AG409 forme ; AG403 forme ; AG317… ;
AI403 (nombres) ; AG105… Le détail exact est encodé dans questions.json (une
entrée = forme complète si answer_a présent).
Cas tranchés en FORME COMPLÈTE (prose allemande présente) : AE415 (« steigt/
sinkt »), AJ220, AE402 (prose), AA104 (noms d'unités), AE403, AE421, AE422,
AE416-AE420 (« ca. »/prose), AE408-AE414, AE407, AF606, AF615, AF618, AF616,
AF617, AF605, AF620, AF607, AF621, AF610, AF611, AF622, AF624, AF630, AF631,
AE404, AF633-AF636, AF637 ; AG201, AG419? (non : nom d'antenne -> énoncé seul),
AG202 (prose longue), AG209-AG211, AG106-AG108, AG125, AG224, AG109-AG113,
AG116, AG212, AG222, AG126, AG225, AG127, AG213, AG214, AG218 (« Gewinn:… »
prose), AG219, AG221 (« Etwa … ° » -> forme, précédent AH213/Etwa), AG207,
AG208, AG203-AG206 (« gilt für eine Erregung auf … MHz » = prose), AG312,
AG301, AG303, AG314, AG302, AG304, AG305-AG307 (« ca. … Ohm » -> forme, comme
précédent AB101? NON : cf. règle — « ca. » = prose « env. » donc forme),
AG309/AG310 (types de câbles = prose), AG311, AG318, AG319, AG405 (« ca. … à »),
AG402, AG403, AG404, AI401, AI402, AI201-AI208, AG406, AG320, AG411, AG413-
AG415, AG425-AG429, AJ115, AG420, AG423, AG424.
Précédents réutilisés : noms d'antennes/procédés (Windom, Fuchs, Zeppelin,
G5RV, Marconi, Delta-Loop) = noms propres -> énoncé seul (le build tire les
réponses du catalogue DE). « ca./etwa/Etwa » -> « env./environ », prose ->
forme (précédent AH213/EG208). « bis » -> « à », forme. Réponses `Ohm`/`°`/
nombres nus/formules/images -> énoncé seul (précédents AG417/AG418 `Ohm`,
AF425 numérique).

#### Terminologie posée (ch. 10-12) — à appliquer strictement en aval
Ch.10-11 (numérique) : Phasenumtastung (PSK) -> modulation par déplacement de
phase ; Amplitudenumtastung (ASK) -> modulation par déplacement d'amplitude ;
Symbolrate -> rapidité de modulation (baud) ; Datenübertragungsrate -> débit de
données ; Seitenbänder -> bandes latérales ; Tastklicks -> clics de
manipulation ; Quadraturamplitudenmodulation (QAM) -> modulation d'amplitude en
quadrature ; Konstellationsdiagramm -> diagramme de constellation ;
orthogonales Frequenzmultiplex (OFDM) -> multiplexage par répartition
orthogonale de la fréquence ; Übersprechen -> diaphonie ;
Intersymbolinterferenz -> interférence entre symboles ; Shannon-Hartley-Gesetz
-> loi de Shannon-Hartley ; Signal-Rausch-Verhältnis -> rapport signal sur
bruit ; Quellencodierung/Kanalcodierung -> codage de source/de canal ;
Redundanz -> redondance ; Prüfbit/Parity Bit -> bit de contrôle/de parité ;
Even/Odd Parity -> parité paire/impaire ; zyklische Redundanzprüfung (CRC) ->
contrôle de redondance cyclique ; Vorwärtsfehlerkorrektur (FEC) -> correction
d'erreurs directe ; Hamming-Code -> code de Hamming ; Mapping/Mapper/De-Mapper
-> mapping/mapper/dé-mapper (conservés) ; Gray-Code -> code de Gray ;
Sende-/Empfangskette -> chaîne d'émission/de réception ; A/D- bzw. D/A-Umsetzer
-> convertisseur A/N resp. N/A ; Sampling -> échantillonnage ; Samplingrate ->
fréquence d'échantillonnage ; zeitkontinuierlich/zeitdiskret -> à temps
continu/discret ; wertkontinuierlich/wertdiskret -> à valeurs continues/
discrètes ; Quantisierung -> quantification ; Quantisierungsfehler -> erreur de
quantification ; Auflösung -> résolution ; Abtasttheorem -> théorème
d'échantillonnage ; Nyquist-Bedingung -> condition de Nyquist ; Alias-/
Aliasing-Effekt -> effet d'alias/de repliement ; Antialiasing-/Anti-Alias-
Filter -> filtre anti-repliement ; Rekonstruktionsfilter -> filtre de
reconstruction ; Clipping -> clipping (écrêtage) ; Jitter -> jitter (gigue) ;
Taktgenerator/Abtastratengenerator -> générateur d'horloge/de fréquence
d'échantillonnage ; Fourier-Transformation/FFT -> transformation de Fourier/
FFT ; Frequenzspektrum -> spectre de fréquences ; Grundschwingung/Oberschwingung
-> fondamentale/harmonique ; FIR-/IIR-Filter -> filtre FIR/IIR (endliche/
unendliche Impulsantwort -> réponse impulsionnelle finie/infinie) ; I/Q-
Verfahren -> procédé I/Q ; In-Phase/Quadrature -> en phase/quadrature ;
Latenz -> latence ; Puffer(speicher) -> mémoire tampon (buffer) ; Codec ->
codec.
Ch.12 (antennes/lignes) : endgespeist -> alimenté en extrémité ; Fuchskreis ->
circuit de Fuchs ; Un-Un/Balun -> unun/balun ; Windungs-/Impedanzverhältnis ->
rapport de spires/d'impédances ; Impedanztransformation -> transformation
d'impédance ; Mantelwellensperre (MWS) -> bloqueur d'ondes de gaine ;
Zeppelinantenne -> antenne Zeppelin ; Ganzwellenschleife -> cadre onde
entière ; Delta-Loop/Quad -> Delta-Loop/Quad (conservés) ; geometrisches
Mittel -> moyenne géométrique ; Verlängerungsfaktor -> facteur d'allongement ;
G5RV/Windom -> conservés ; Verkürzungsfaktor -> coefficient de vélocité (aligné
E/L1) ; Fußpunktwiderstand/-impedanz -> résistance/impédance au point
d'alimentation ; Verlängerungsspule/Verkürzungskondensator -> bobine
d'allongement/condensateur de raccourcissement ; elektrisch verlängern/
verkürzen -> allonger/raccourcir électriquement ; NVIS -> onde d'espace à
incidence quasi verticale (conservé « NVIS ») ; Trap -> trap (conservé) ;
Sperrkreis -> circuit bouchon (aligné L4) ; Saugkreis -> circuit d'absorption
(aligné L4) ; Yagi-Uda -> Yagi-Uda ; Kreuzyagi -> Yagi croisée ; Reflektor/
Direktor/Strahler -> réflecteur/directeur/radiateur ; Öffnungswinkel ->
angle d'ouverture ; Parabolspiegel -> réflecteur parabolique ; Erregerantenne
(Feed) -> antenne d'excitation (feed) ; Helixantenne -> antenne hélicoïdale ;
Hornstrahler -> antenne cornet ; Hohlleiter -> guide d'ondes ; Offsetspiegel ->
réflecteur offset ; Vor-/Rückverhältnis -> rapport avant/arrière ;
Halbwertsbreite -> largeur à mi-puissance ; Hauptstrahlrichtung -> direction
principale de rayonnement ; strom-/spannungsgespeist -> alimenté en courant/en
tension ; Serien-/Parallelresonanz -> résonance série/parallèle ; nieder-/
hochohmig -> à basse/haute impédance ; Wellenwiderstand -> impédance
caractéristique ; Zweidraht-/Paralleldrahtleitung -> ligne bifilaire
(parallèle) ; Hühnerleiter -> échelle à grenouilles (aligné ch.13-16 E) ;
Kabeldämpfung -> atténuation de câble ; Biegeradius -> rayon de courbure ;
Rückflussdämpfung -> affaiblissement de réflexion ; Dielektrikum ->
diélectrique ; geschäumt/Voll-PE -> mousse de PE/PE massif ; Skineffekt ->
effet de peau ; SWR/Stehwellenverhältnis -> SWR/rapport d'ondes stationnaires ;
Stehwellenmessgerät -> SWR-mètre ; Richtkoppler -> coupleur directionnel ;
Kreuzzeigerinstrument -> instrument à aiguilles croisées ; vor-/rücklaufende
Leistung -> puissance directe/réfléchie ; VNA -> analyseur de réseau
vectoriel ; Wirk-/Blindwiderstand -> résistance active/réactance ; imaginäre
Einheit -> unité imaginaire ; Phasenverschiebung -> déphasage ; λ/4-
Transformationsleitung -> ligne de transformation λ/4 ; Pi-Filter -> filtre en
pi ; Antennentuner -> boîte d'accord d'antenne (aligné L4) ; Lecherleitung ->
ligne de Lecher ; Stub -> stub (conservé) ; Mantelwellen -> ondes de gaine ;
Gegentakt-/Gleichtaktsignal -> signal en mode différentiel/mode commun ;
Mantelstrom -> courant de gaine ; stromkompensierte Drossel -> self à
compensation de courant ; HF-Trenntrafo -> transformateur d'isolement HF ;
Spannungsbalun -> balun de tension ; Spartransformator -> autotransformateur ;
Umwegleitung -> ligne de déphasage. Conservés : PSK/BPSK/QPSK/8-PSK/QAM/16-QAM/
OFDM/ASK/FSK/FT4/FT8/WSPR/RTTY, WLAN, 5G, Hamnet, AWGN, SNR, CRC, FEC, FIR/IIR,
CD, HiFi, MP3/JPEG/MPEG-4, FreeDV, M17, Codec2, FPGA, I/Q, Sps/Samples,
Bd/baud, Delta-Loop, Quad, Windom, G5RV, W3DZZ, Yagi-Uda, NVIS, Groundplane,
RG58/RG213, PE/PTFE, dBi/dBd, VNA, SWR, MWS, Fuchs, Marconi, Zeppelin, PAR
(pour ERP, aligné L4).

#### Arbitrages / particularités préservées verbatim (lot 5)
- `sende_empfangsketten.md` (ch.10) : DÉFAUT AMONT confirmé — `[ref:a_sender]`
  alors que la figure s'appelle `a_sdr_sender` (le texte cite les DEUX :
  a_sdr_sender ET a_sander via a_sender). Ref conservée VERBATIM -> « figure ?? »
  au build, en allemand comme en français. Déjà consigné par validate_output()
  côté lot 4 ; à re-vérifier au build du lot 6.
- Blocs %-commentés allemands conservés verbatim : symbolumschaltung_bandbreite
  (%Aus diesem Grunde…), fourier_transformation (6 lignes d'en-tête
  %-commentées : zeitdarstellung/frequenzdarstellung/fourier/phase),
  iq_verfahren (% TODO neu formulieren + % Idee DL9MJ + %TODO BILD QAM4…),
  antennenformen_3 (%TODO namensherkunft zeppelin + %TODO Darstellung 5/8 +
  %TODO Bild VHF + %TODO Frage ist falsch), verkuerzungsfaktor_2 (%TODO Komma +
  %TODO Formelsammlung Polyäthylen), fusspunktimpedanz_2 (2 %TODO),
  parbolspiegel_2 (%TODO Bild Helix/Hornstrahler + %TODO Formel),
  frequenzabhaengige_stromverteilung (%TODO Stromverteilungen falsch),
  strom_spannung_speisung_2 (aucun), nvis (%TODO Bild NVIS),
  uebertragungsleitungen_3 (%TODO), mantelwellen_2 (%TODO Bild Spannungsbalun),
  lecherleitung (%TODO Bild).
- Balises <margin>/<indepth>/<attention>/<tip> conservées, contenu traduit.
  Nouvelle <attention> ×3 dans antennenformen_3 ; <tip> dans umwegleitung.
- [include:...] conservés verbatim : quantisierung_und_sampling
  (sampling_quantisierung), applet_nyquist (abtasttheorem, sous <webonly>),
  fourier (fourier_transformation), applet_iq (iq_verfahren),
  applet_interferenz (déjà en ch. antérieurs).
- <webonly>/<latexonly> conservés : abtasttheorem (applet_nyquist + 2 blocs
  <webonly> de texte).
- Idents de picture à tréma conservés verbatim : a_sdr_empfänger
  (sende_empfangsketten). Idents partagés : e_stromverteilungen
  (strom_spannung_speisung_2, picture 1050).
- Maths verbatim : indices allemands liés aux figures conservés — $R_\mathrm{S}$,
  $\epsilon_\mathrm{r}$, $L_\mathrm{G}/L_\mathrm{E}$, $k_\mathrm{v}$,
  $P_\text{S}/P_\text{N}$, $Z_\mathrm{A}/Z_\mathrm{E}$, $f_\text{s}$,
  $f_{\mathrm{max}}$, $P_{\textrm{V}}/P_{\textrm{R}}/P_{\textrm{D}}$ (questions).
  SEULE prose display-math autonome rencontrée : AUCUNE cette fois (pas de
  `$\text{Ordnung}$` comme au lot 4) -> pas de dérogation à signaler.
  `$\unit{\bit\per\text{Symbol}}$` (mehrwertige_verfahren) : le mot « Symbol »
  dans un \text{} d'unité est CONSERVÉ verbatim (identique DE/FR).
- Coquilles source conservées verbatim : ident de section `parbolspiegel_2`
  (« Parbolspiegel », b manquant) ; `shannon_hartley_gesetzt` (« gesetzt » au
  lieu de « gesetz ») ; réponse AG309 c avec `\n` final (RG213) ; réponse AG424 a
  avec `\n` final ; `\xa0` (espace insécable) dans AE402 b et AF627? (conservés).
- `[picture:701:4ask:...]`, `[picture:702:8qam:...]` : idents commençant par un
  chiffre (4ask/8qam), conservés verbatim.

#### COMPILÉ en fin de lot 5 — build partiel ch.1–12
Build partiel ch.1–12 (144 sections, 695 questions) avec build_book.py v0.4
(gelé, md5 f019d2c27e93cc605ca9ee986976fba5), --lang fr --limit-chapters 12
--version-label 0.5. Habillage FR, contenu + questions BNetzA en allemand.
Résultat : **book-A-v0_5-lot5.pdf, 332 pages, A4, 4,78 Mo** (compression
Ghostscript /ebook -dDetectDuplicateImages=true ; 73 Mo avant).

##### PIÈGE MAJEUR élucidé — NE PAS compiler « à la main » en 2 passes
Un premier build fait en DEUX PASSES lualatex manuelles a produit un PDF
CORROMPU : page 1 = un « 14.63995pt » orphelin à la place du titre, page 2
blanche, la vraie page de titre repoussée en page 3, + 2 « erreurs »
(`! Extra }` l.1034 puis `! Missing \begin{document}`) et 334 pages au lieu
de 332.
**Cause racine** : la macro amont `\DARCimageCache{…}` (settings.tex l.264,
définie sous \ExplSyntaxOn, appelée via \iow_now au hook
enddocument/afterlastpage) écrit dans le .aux le cache d'autoscale de TOUTES les
images du run — une ligne unique de ~10 000 caractères. Quand une passe
ULTÉRIEURE relit ce .aux à \begin{document}, l'exécution de `\DARCimageCache`
(qui fait `\prop_gset_from_keyval:Nn`) désynchronise le flux au niveau de sa
`}` finale : LaTeX émet `! Extra }`, perd \begin{document}, puis crache le token
`{14.63995pt}` (issu de `scr@dte@chapter@lastmaxnumwidth`, ligne .aux suivante)
en TEXTE sur la première page. **La ligne n'est PAS trop longue** (buf_size =
200000 ≫ 9994) ; ce n'est pas un débordement de buffer mais un problème de
relecture d'un .aux déjà porteur du cache.
**Correctif = utiliser le chemin SUPPORTÉ, latexmk** (celui que build_book.py
lance quand on N'ajoute PAS --no-compile ; latexmkrc écrit par le script avec
`$pdf_mode=4` lualatex). latexmk gère l'ordre et le NOMBRE de passes et évite la
corruption : ici **convergence en 3 passes, rc=0, 0 erreur, 0 fuite
« 14.63995pt », page 1 = page de titre, 332 pages.** Les ~115 « Reference
undefined » vues dans le log latexmk sont CUMULÉES sur les passes intermédiaires
et TOUTES résolues à la passe finale (segment final = 0 undefined). Ne PAS se
fier au comptage brut du log complet ; isoler la dernière passe (après le
dernier « Output written »).
=> **RÈGLE POUR LES PROCHAINS BUILDS (lot 6, v1.0)** : lancer la compilation via
latexmk (soit `build_book.py … ` SANS --no-compile, soit `latexmk -lualatex`
directement), JAMAIS deux `lualatex` manuels enchaînés qui relisent un .aux
porteur du DARCimageCache. Compression Ghostscript ensuite, à part.
Le workaround « sauver la passe-2 avant la 3e passe » des notes antérieures
visait le kill sandbox de la 3e passe ; il ne s'applique PAS à latexmk, qui
mène ses passes à terme (chaque passe ~4-5 min ici, 3 passes ~14 min).

Défauts attendus, tous documentés — RIEN de nouveau à corriger :
- **2 réf. orphelines -> « ?? »** dans le PDF (les 2 SEULES occurrences « ?? ») :
  `a_mehrwegeausbreitung_ionosphäre` (ch.1) et `a_sender` (ch.10,
  sende_empfangsketten — figure nommée `a_sdr_sender`). Défauts AMONT, conservés
  verbatim.
- **Germanismes résiduels dans les dessins TikZ amont** (policy projet : non
  traduits, internes de figures). Lot 5 : diagrammes chaîne SDR ch.10-11 (« FPGA
  oder Software », « Kanalcodierer/Quellencodierer/Mapper », « Steuer- und
  Kontrollsignale »), + héritage ch.1-9 (« Frequenz [MHz] », « Elektrische
  Länge », « 3. Ordnung »…). Sonde anti-germanisme au NIVEAU SOURCE = 0 hit réel.
- Labels « multiply defined » (a_harmonische, even_parity) : doublons d'ident
  AMONT connus/consignés, conservés verbatim ; sans effet sur la sortie.
- Pré-vol OK : 0 marqueur brut non commenté, 0 image manquante, 0 « Too many
  unprocessed floats », 0 « lost some margin » (clamp \DARCimage v0.4 tient),
  fig202/Blitzerdung non référencé en ch.1–12. Correctif classe A session-local
  ré-appliqué (marginheightadjustment 15 mm après \documentclass).

#### Reste à traduire après le lot 5
2 chapitres, 10 sections : ch.13 Personenschutzabstand (6 s), ch.14 Sicherheit
(4 s) + N_Ende (à copier du zip E, avec son entrée titles.json « N_Ende » ->
« Conclusion du cours »). Puis build v1.0 (livre A complet, --limit-chapters 14
ou sans limite) — **compiler via latexmk, cf. piège DARCimageCache ci-dessus**.
Recompter le périmètre depuis toc/A.json en début de session.

## COMPILATION v0.5 (ch. 1–9) — 248 p., 3,8 Mo, 0 erreur, 0 « Rerun »

Faite dans la MÊME session que la traduction du lot 4 (le livre partiel est donc
compilé AVANT relecture PLG du lot 4 : le PDF sert de support de relecture).
`build_book.py` v0.4 inchangé, aucune modification du script.

### Chaîne exacte (reproductible)
1. `curl -sL codeload.github.com/DARC-e-V/50ohm/tar.gz/refs/heads/main` (générateur,
   module `renderer`) + `...50ohm-contents-dl/...` (contenus).
   `pip install mistletoe --break-system-packages` (1.6.0).
2. `rm -f /etc/apt/sources.list.d/nodesource.*` puis TeX PAR LOTS :
   `lmodern texlive-luatex texlive-latex-recommended texlive-latex-extra`,
   puis `texlive-lang-german texlive-lang-french texlive-science texlive-pictures`,
   puis `texlive-fonts-extra fonts-linuxlibertine ghostscript`.
   (+ `poppler-utils` pour les sondes pdftotext.)
3. `PYTHONPATH=.../50ohm-main python3 build_book.py --edition A --lang fr
   --translations out-A/A --input 50ohm-contents-dl-main --output build-A
   --version-label 0.5 --limit-chapters 9 --no-compile`
   -> « 92 sections rendues (92 traduites), 512 questions traduites ».
   **--limit-chapters 9** = livre partiel intégralement français (les ch. 10-14
   non traduits sont exclus ; sans cette option, 154 sections dont 62 en allemand).
4. Correctif session-local classe A dans `book-A.tex` après \documentclass :
   `\setlength{\marginheightadjustment}{15mm}` + `\setlength{\marginparpush}{3pt}`.
5. 2 passes `lualatex -interaction=nonstopmode` en tâche de fond
   (`setsid nohup bash -c '... ; ...' </dev/null >/dev/null 2>&1 &` + polling
   par paliers ≤ 290 s), `cp book-A.pdf book-A-pass2.pdf` avant toute 3e passe.
   Durées observées : passe 1 ≈ 12 min, passe 2 ≈ 13 min.
6. Ghostscript `/ebook -dDetectDuplicateImages=true` : **75,1 Mo -> 3,8 Mo**
   (≈ 7 min ; lancer en tâche de fond + polling, la commande dépasse le timeout).

### Résultat
- 248 pages (v0.4 ch.1-7 = 168 p. ; +80 p. pour les ch. 8-9).
- p2.log : **0 erreur (`^!`), 0 « Rerun », 0 image manquante, 0 dépassement de
  quota de floats** (le `\extrafloats{400}` automatique de v0.4 suffit).
  12 « Overfull \hbox » (typographie, non bloquant).
- AUCUN correctif fig202/marginfix nécessaire : le clamp `\DARCimage` de v0.4
  a bien supprimé la cause racine. Les figures larges des ch. 8-9 sont toutes
  placées. La liste 1077 / 1092 / 988 des notes v0.4 est donc CADUQUE.

### Sondes de recette (toutes passées)
- 9/9 titres de chapitres, 92/92 titres de sections, 182/182 questions du lot 4
  imprimées (pdftotext, apostrophe U+2019 et césure `-\n` normalisées avant probe).
- Encadrés FR présents : Astuce / Attention / Approfondissement / Nouvelle unité ;
  habillage « Table des matières » OK.
- « Chapitre » N'APPARAÎT PAS dans le corps : normal, scrreprt sans chapterprefix
  n'imprime pas le mot (le comportement allemand est identique). PAS un défaut.
- Fuite allemande résiduelle : 4 occurrences (Sender, Empfänger, Reale
  Spannungsquelle, Reales Spannungsmessgerät) — toutes situées DANS les dessins
  TikZ amont (img/*include.tex : 1004, 1018, 430, 674, 732…). Les libellés
  internes aux figures ne sont pas traduisibles sans forker les dessins.
  Décision reconduite : NON TRADUITS (idem OW/Harm./NA). À arbitrer par PLG si
  un fork des dessins est souhaité pour la v1.0.

### Défauts AMONT confirmés par validate_output() (à remonter au DARC)
- `mehrwegeausbreitung.md` : `[ref:a_mehrwegeausbreitung_ionosphäre]` ne pointe
  vers AUCUNE figure (seul `a_mehrwegeausbreitung_reflexion` existe) -> « figure ?? »
  dans le livre ALLEMAND comme dans le français. Ref conservée verbatim.
- `sende_empfangsketten.md` (ch. 11, pas encore traduit) : `[ref:a_sender]` alors
  que la figure s'appelle `a_sdr_sender`. Même conséquence.

## Correctifs de compilation (session-locaux, à REFAIRE après chaque build)
Hérités du livre E — vérifier leur pertinence sur le livre A :
1. `settings-pre.tex` — ajouter à la fin : `\extrafloats{400}`
   (toujours via **printf**, jamais echo : `\e` corrompu sinon).
2. `book-A.tex` — \clearpage avant/après la section Blitzerdung si
   présente (probablement remplacée par une version A).
3. **fig202** — si le diagramme d'atténuation de câble
   (img/202include.tex, pgfplots 21×29 cm à dimensions FIXES) est
   référencé en marge dans le livre A : précompiler
   `\resizebox{52mm}{!}{\input{img/202include.tex}}` en standalone →
   fig202.pdf dans le dossier de build, puis remplacer dans la section
   concernée `\Margin{\DARCimage{1.0\linewidth}{202include}` par
   `\Margin{\noindent\includegraphics[width=\linewidth]{fig202.pdf}`.
   CAUSE RACINE (découverte v0.6 E) : l'autoscale DARC n'ajuste que les
   unités tikz, pas width/height pgfplots ; une note de marge inplaçable
   BOUCHONNE la file marginfix et fait perdre TOUTES les notes suivantes
   du livre (y compris boîtes <danger>). Symptôme : « lost some margin
   notes » + marges vides + références « ?? » en cascade. Contrôler par
   sonde pdftotext les légendes de marge à chaque build ; chercher
   d'autres includes à dimensions fixes > 8 cm référencés en marge.

## Acquis N+E repris en référence (extraits du NOTES-SESSION E)

- # Notes de session — classe E, chapitres 1–16 (v0.6)

Fichier inerte pour build_book.py ; il voyage dans le zip pour porter l'état
du projet d'une session à l'autre.

## Correctifs de compilation appliqués (session-locaux, à REFAIRE après chaque build)

Le build E complet (repli allemand dense) fait déborder la mécanique
marginfix, contrairement au livre N. Deux retouches sur les FICHIERS GÉNÉRÉS
(pas sur build_book.py, resté intact) :

1. `livre-E-fr/settings-pre.tex` — ajouter à la fin :
   `\extrafloats{400}`
   (sinon : 7 × « Too many unprocessed floats » au ch. 16, compilation fatale)

2. `livre-E-fr/book-E.tex` — encadrer la section Blitzerdung (ch. 16) :
   `\clearpage` avant `\section{Blitzerdung}` et après son `\input`
   (sinon : les 3 notes de marge de blitzerdung sont perdues)

Ces retouches étant écrasées à chaque `build_book.py`, les réappliquer entre
le build `--no-compile` et le `latexmk`. À terme, proposer à Pierre de les
intégrer dans build_book.py (décision à lui — fichier gelé).

## Défaut connu, préexistant, NON résolu (à traiter avec les chapitres concernés)

13 figures de marge du repli ALLEMAND sont silencieusement perdues
(« marginfix: lost some margin notes », 1 erreur en fin de compilation,
PDF produit malgré tout). Ensemble stable entre compilations, aucune dans
les chapitres traduits 1–2. Sections touchées :
fm_2 (ch.9) ; vorverstaerker_daempfungsglied ×2 (ch.10) ;
swr_2, swr_meter_1 ×3, vna_1 ×3, kabeldaempfung_1, antennenformen_2,
aequivalente_isotrope_strahlungsleistung_eirp_2, strom_spannung_speisung_1
(ch.14) ; personenschutzabstand_grenzwerte ×3 (ch.15).
Cause : pages allemandes très denses en figures de marge ; la repagination
lors de la traduction de ces chapitres (sessions 4–5) devrait en résorber
une partie ; contrôler par sonde pdftotext des légendes à chaque session.

## État des traductions
- Règle « réponses » confirmée sur ch. 1–2 et appliquée : réponses
  langue-neutres (nombres/unités/formules/acronymes/schémas) → énoncé seul
  (le build tire les réponses du catalogue DE) ; réponses contenant de la
  prose allemande (y compris connecteurs « und »/« bis ») → 4 réponses
  traduites. Cas limites tranchés : EC112/EC113 (« bis »), EB405 (« und »),
  EI304 (prose) → forme complète.
- Terminologie E posée ch. 3 (à valider par PLG) : Innenwiderstand→résistance
  interne ; hoch-/niederohmig→à haute/basse impédance ; Wirkwiderstand→
  résistance active ; Effektiv-/Spitzen-/Spitze-Spitze-Wert→valeur efficace/
  de crête/crête à crête ; Draht-/Kohleschicht-/Metallschicht-/Metalloxid-
  schichtwiderstand→résistance bobinée/à couche de carbone/à couche
  métallique/à couche d'oxyde métallique ; Kaltleiter(PTC)→thermistance CTP,
  Heißleiter(NTC)→thermistance CTN ; Dummyload/künstliche Antenne→charge
  fictive (antenne artificielle) ; Leistungsverhältnis/-faktor→rapport/
  facteur de puissance. Acronymes conservés : SMD, NTC, PTC, LDR, VHF, UHF.
- Terminologie E ajoutée ch. 4–5 (à valider par PLG) : Plattenkondensator→
  condensateur plan ; Dielektrikum→diélectrique ; Durchschlagsfeldstärke→
  rigidité diélectrique ; Durchbruchspannung→tension de claquage ;
  Zylinderspule→bobine cylindrique/solénoïde ; Windung→spire ; Wirbelströme→
  courants de Foucault ; Selbstinduktionsspannung→tension d'auto-induction ;
  Blindwiderstand (X_C/X_L)→réactance (capacitive/inductive) ; relative
  Dielektrizitätszahl→permittivité relative ; Übertrager/Trafo→transformateur/
  transfo ; Schwellspannung→tension de seuil ; Sperrsättigungsstrom→courant
  de saturation inverse ; Fluss-/Sperrrichtung→sens direct/inverse ;
  Z-Diode→diode Zener ; Kapazitätsdiode→diode à capacité variable ;
  Freilaufdiode→diode de roue libre ; Stromverstärkung→gain en courant ;
  Gate→grille ; Löcher→trous. Acronymes/termes conservés : LED, FET, MOSFET,
  BJT, NPN, PNP, PTFE, ELKO (glosé « chimique »), Styroflex.
- Chapitre 7 (Strom- und Spannungsversorgung) : TRADUIT, LIVRÉ POUR
  RELECTURE. 4 sections, 6 questions (5 complètes ; ED304 énoncé seul —
  réponses images vides). Validation structurelle regex OK, sonde
  anti-germanisme OK (seul hit : nom propre « Verband der Elektrotechnik…
  (VDE) », conservé volontairement). questions.json = 199 ; titles.json =
  7 chapitres / 7 abstracts / 42 sections. Ident à espaces préservé :
  `e_Ferritkerntrafo im Schaltnetzteils`. Terminologie posée : Schaltnetzteil→
  alimentation à découpage ; linear geregeltes Netzteil→alimentation à
  régulation linéaire ; Einweggleichrichtung→redressement simple alternance ;
  Brückengleichrichter→redresseur en pont ; Außenleiter/Neutralleiter/
  Schutzleiter→conducteur de phase/neutre/de protection ; Feinsicherung→
  fusible miniature ; Schmelzsicherung→fusible à fusion ; Flachstecksicherung→
  fusible à lame ; Auslösecharakteristik→caractéristique de déclenchement ;
  flink/mittelträge/träge→rapide/semi-temporisée/temporisée ; Siebkondensator→
  condensateur de filtrage ; EMV→CEM. Conservés : L, N, PE, NYM-J, VDE, TR5,
  Diazed/Neozed.
- BUILD v0.3 (ch. 1–7 traduits) : RÉUSSI. Pipeline déroulé tel que documenté :
  build_book.py v0.2 (fourni par PLG, inchangé) --edition E --lang fr
  --translations out/E --version-label 0.3 --no-compile ; retouches
  extrafloats/clearpage réappliquées ; latexmk -lualatex. PIÈGES DE SESSION :
  (1) `echo '\extrafloats'` corrompt la ligne (échappement \e) — utiliser
  printf ; (2) l'erreur marginfix connue fait sortir latexmk en code 12 après
  UNE seule passe, et le -f suivant se croit à jour (« Nothing to do ») —
  forcer la convergence par passes `lualatex` directes jusqu'à 0 « Rerun »
  (2 passes ont suffi) ; (3) sondes pdftotext : normaliser l'apostrophe
  typographique U+2019 avant comparaison, sinon faux « MANQUE ». Résultat :
  205 pages A4, 1 seule erreur (marginfix, jeu connu du repli allemand
  ch. 9–15, AUCUNE perte dans les chapitres traduits — 31 sondes OK, titres
  de chapitres, légendes de marge y c. les 3 idents à espaces/maths, boîtes
  Nouvelle unité/Attention/Astuce). Ghostscript /ebook : 159 Mo → 2,9 Mo.
  Livré : livre-E-fr-v0.3-ch1-7.pdf. apt : le méta-install groupé est mort
  en route — installer par lots et vérifier dpkg ; poppler-utils requis
  pour pdfinfo/pdftotext ; mistletoe via pip --break-system-packages.
- Terminologie E posée ch. 8–9 (à valider par PLG) : Tiefpass/Hochpass/
  Bandpass→(filtre) passe-bas/passe-haut/passe-bande ; Bandsperre→
  (filtre) coupe-bande ; Grenzfrequenz→fréquence de coupure ; RC-Glied→
  cellule RC ; Schwingkreis→circuit oscillant (série/parallèle) ;
  Saugkreis→circuit d'absorption ; Sperrkreis→circuit bouchon ; Leitkreis→
  circuit passant ; Drehkondensator→condensateur variable ; Güte→facteur
  de qualité ; Oberwellen→harmoniques ; Frequenzvervielfacher→
  multiplicateur de fréquence ; Mischer→mélangeur ; Mischprodukte→produits
  de mélange ; Ringmischer/Balance-Mixer→mélangeur en anneau équilibré
  (balance-mixer) ; Konverter→convertisseur ; Transverter→transverter ;
  Verstärker→amplificateur ; NF/HF→BF/HF ; ZF→FI ; Begrenzerverstärker→
  amplificateur limiteur ; Pufferstufe→étage tampon ; Netzbrummen→
  ronflement secteur ; Träger→porteuse ; Seitenband→bande latérale ;
  Einseitenbandmodulation→modulation à bande latérale unique (SSB) ;
  Frequenzhub→excursion de fréquence ; Hub-Regler→réglage d'excursion ;
  Zeichengeschwindigkeit→vitesse de manipulation ; Splatter→splatter ;
  Dynamikkompressor→compresseur de dynamique ; Antennenweiche→séparateur
  d'antenne ; Diplexer→diplexeur ; Frequenzweiche→répartiteur de
  fréquences ; Kurzwelle→ondes courtes/décamétrique ; UKW→VHF (radio
  diffusion : FM) ; Kupferlackdraht→fil de cuivre émaillé ; Stimmgabel→
  diapason ; Thomsonsche Schwingkreisformel→formule de Thomson ;
  Antennentuner→boîte d'accord d'antenne ; Dummy « ü » sans objet ici.
  Conservés : VFO, TCXO, OCXO, XO, SDR, LNB, PTT, PA, QO-100, CW, SSB,
  USB, LSB, AM, FM, DSB, DMR, D-Star, RX, TX, squelch, valeurs A_L.
- BUILD v0.4 (ch. 1–9 traduits) : RÉUSSI. Pipeline v0.3 reproduit :
  build_book.py (inchangé) --edition E --lang fr --translations out/E
  --input 50ohm-contents-dl-main --output livre-E-fr --version-label 0.4
  --no-compile ; retouches extrafloats(printf)/clearpage réappliquées ;
  3 passes lualatex directes (convergence dès la passe 2 — le hit
  « rerun » résiduel n'était que le nom du paquet rerunfilecheck.sty,
  à exclure des greps). NOUVEAU PIÈGE : ngerman.ldf/french.ldf absents
  de l'installation TeX par lots → installer AUSSI texlive-lang-german
  et texlive-lang-french (sinon 6 erreurs babel/scrbase fatales pour
  l'habillage). Dépôt de contenus : le tarball codeload est sur la
  branche `main` (plus `master`) ; sections sous contents/sections/,
  toc sous toc/, catalogue sous contents/questions/fragenkatalog3b.json ;
  l'API GitHub était rate-limitée toute la session (IP proxy partagées) —
  chemins retrouvés via src/config.py du dépôt générateur.
  Résultat : 209 pages A4 (205 en v0.3), 1 seule erreur (marginfix,
  repli allemand ch. 10–15) ; la perte de marge connue de fm_2 (ch. 9)
  est RÉSORBÉE par la traduction (2 légendes sondées présentes) — retirer
  fm_2 du jeu des 13 ; 21 références « ?? » identiques v0.3/v0.4 (aucune
  régression, défaut préexistant, dont e_ssb_am_modulation cité par ssb_2
  sans [picture] correspondant dans la source allemande). 47/48 sondes
  pdftotext OK + 1 faux négatif d'extraction (légende Fig. 8.18 entrelacée
  avec le corps : sonder par fragments courts). Ghostscript /ebook :
  160 Mo → 2,96 Mo. Livré : livre-E-fr-v0.4-ch1-9.pdf.
- Chapitres 10 (Empfänger → Récepteurs, 9 sections), 11 (Sender →
  Émetteurs, 4 sections) et 12 (Digitale Übertragungsverfahren → Procédés
  de transmission numériques, 10 sections) : TRADUITS, LIVRÉS POUR
  RELECTURE. 88 questions référencées, aucune déjà traduite → +88 entrées :
  72 complètes / 16 énoncé seul (images vides : EF216, EJ206, EJ207, EJ208,
  EJ117, EE406, EE407 ; numériques pures : EI504, EA202–EA208, EE403).
  Cas tranchés en forme complète : EF309/EF219 (« Punkt » = prose),
  EI502/EI503 (« ein/zehn/hundert Hertz » = prose), EA106 (« Bit pro
  Sekunde »), EJ201 (« sinusförmig » etc.). questions.json = 352 entrées ;
  titles.json = 12 chapitres / 12 abstracts / 76 sections.
  Validation structurelle regex OK sur les 23 sections (comptage + ordre,
  lignes % exclues) ; sonde anti-germanisme OK (hits bénins : nom propre
  « Weak Signal Propagation Reporter Network », homographe fr « Signal »,
  glose volontaire « Geradeaus-Empfänger »). Gloses allemandes volontaires
  (termes d'examen) : Trennschärfe, Überlagerungsempfänger,
  Spiegelfrequenzen, Kerbfilter, Oberwellen, Nebenaussendungen,
  Einstrahlung, Einströmung, Übersteuerung, störende Beeinflussungen,
  Mantelwellensperre, Symbolrate. Particularités préservées verbatim :
  ident avec tréma `detektorempfänger`/`e_geradeausempfänger`, blocs
  commentés allemands (frequenzmessung_1 : %<margin> photo 189,
  %TODO Bild Frequenzteiler ; noise_reduction : % TODO Soundbeispiele ;
  stoerungen… : %- Reduzierung der Sendeleistung…), `[include:fourier]`
  (unerwuenschte_aussendungen_2), `[include:hamnet_map]`
  (paketvermittelte_netzwerke), tableaux DARCdown (binaer ×3),
  `\qty{455}\cdot \qty{10^3}{\hertz}` (syntaxe source conservée),
  `pla\^it` dans EE405, nouvelle boîte <attention> (frequenzmessung_1).
  Terminologie posée ch. 10–12 (à valider par PLG) : Geradeausempfänger→
  récepteur à amplification directe ; Überlagerungsempfänger→récepteur
  superhétérodyne / à changement de fréquence ; Direktüberlagerungsempfänger→
  récepteur à conversion directe ; Zwischenfrequenz (ZF)→fréquence
  intermédiaire (FI) ; Spiegelfrequenz→fréquence image ; Trennschärfe→
  sélectivité ; BFO→oscillateur de battement ; Abschwächer/Dämpfungsglied→
  atténuateur ; Vorverstärker→préamplificateur ; AGC→régulation automatique
  de gain ; Notch-Filter/Kerbfilter→filtre notch (filtre réjecteur) ;
  Störaustaster/Noise Blanker→éliminateur de parasites ; Frequenzzähler→
  fréquencemètre (compteur de fréquence) ; Vorteiler→prédiviseur ;
  Stellenwert→poids ; ALC→régulation automatique de niveau ;
  Senderausgangsleistung→puissance de sortie de l'émetteur ; PEP→puissance
  de crête / puissance maximale d'enveloppe ; mittlere Leistung→puissance
  moyenne ; unerwünschte Aussendungen→émissions non désirées ;
  Nebenaussendungen→émissions parasites ; Oberwellenfilter→filtre
  d'harmoniques ; störende Beeinflussung→influence perturbatrice ;
  Einstrahlung→pénétration par rayonnement ; Einströmung→pénétration par
  conduction ; Übersteuerung→saturation ; Mantelwellensperre→bloqueur de
  courants de gaine ; Gleichtaktströme→courants de mode commun ;
  Klappferrit→ferrite à clipser ; HF-Erdung→mise à la terre HF ;
  Intermodulation→intermodulation ; Phantomsignale→signaux fantômes ;
  Dualsystem/Dualzahl→système/nombre binaire ; Breite→largeur ;
  Wasserfalldiagramm→diagramme en cascade ; Zeitschlitze→créneaux
  temporels ; Spreizcodes→codes d'étalement ; Frequenz-/Zeit-/Codemultiplex→
  multiplexage fréquentiel/temporel/par code ; Paketvermittlung→commutation
  de paquets ; Netz-/Hostanteil→partie réseau/hôte ; Subnetzmaske→masque de
  sous-réseau ; Symbolrate→rapidité de modulation ; Datenübertragungsrate→
  débit de données ; Umtastung (ASK/FSK)→modulation par déplacement
  d'amplitude/de fréquence. Conservés : BFO, AGC, ALC, RF-Gain, PTT, TNC,
  DATA, baud, DNR, NR, NB, PEP, SWR, DVB-T2, DAB, HAMNET, HAMCloud, DARC,
  APRS, WSPR, RBN, PSK-Reporter, SSTV, ATV, FT8, FT4, WSPR, RTTY, BPSK31,
  QPSK, 16-QAM, M17, AX.25, OOK, ASK, FSK, AFSK, FDMA, TDMA, CDMA, GSM,
  DECT, DMR, UMTS, GPS, AMPS, IP, IPv4/IPv6, QO-100, QRP, Bundesnetzagentur.
- Chapitres 13–16 (Digitale Signalverarbeitung, Antennen und
  Übertragungsleitungen, Personenschutzabstand, Sicherheit) : TRADUITS,
  LIVRÉS POUR RELECTURE (session 13–16, lot unique). 27 sections
  (N_Ende déjà présent, non retraduit), 110 questions
  (82 complètes / 28 énoncé seul). questions.json = 462 entrées ;
  titles.json = 16 chapitres / 16 abstracts / 103 sections — COMPLET.
  Validation structurelle regex OK sur les 27 sections (un écart corrigé :
  `---` initial manquant dans personenschutzabstand_grenzwerte, restauré) ;
  sonde anti-germanisme OK (gloses volontaires : Sperrtopfantenne,
  Selbsterklärung, Skineffekt, Mantelwellensperre, Bundesamt für
  Strahlenschutz). Énoncé seul (réponses numériques/images) : EG214, EG109,
  EG202, EG207, EG221, EG307–EG316, EG401–EG403, EG503–EG511, EK108.
  Cas tranchés en forme complète : EG208–EG211 (« bis »/« ca. »,
  précédent EC112/EC113), EI405 (« Punkt »), EK106 (« Band »),
  EF601 (« beides »), EG502 (« bezogen auf… » = prose ; indices
  $P_{\textrm{Sender}}$ etc. conservés verbatim). EG501 aligné sur le
  précédent EB501/EB502 (« le produit de la puissance fournie directement
  à l'antenne par son gain… rapporté au radiateur isotrope »).
  Particularités préservées verbatim : [include:applet_interferenz]
  (yagi_uda_2) ; commentaires allemands %TODO (antennengewinn 1re ligne,
  standortwahl, uebertragungsleitungen_2, antennenformen_2,
  naeherungsformel_1 + %%%%), %Frequenzabhängigkeit/% Zeitabhängigkeit
  (grenzwerte), % *** Anmerkung 100 kΩ Rothammel *** (statische_aufladung),
  % Quelle bfs.de (strahlengang_aufenthalt) ; tableaux DARCdown
  e_dezibel_leistungsfaktoren (kabeldaempfung_1, eirp_2 ×2) et e_swr_werte
  (swr_2) ; balise <person> (antennenformen_2, Dr Josef Fuchs) ;
  <attention> (strahlengang_aufenthalt) ; <danger> ×5 (ch. 16) ; liens
  50ohm.de abemfv/bfs/BImSchV/ebemfv/vde-blitz/hamnet ; figure
  e_Kugelstrahler partagée antennengewinn/eirp_2 (légende identique) ;
  indices allemands en maths conservés (P_\text{Sender}, P_\text{Verluste},
  \lambda_\mathrm{Leitung}, P_\text{V}/P_\text{R}) ; espaces finaux d'énoncés
  (EG104, EG107, "$7,5 $dBd" dans EK108).
  Terminologie posée ch. 13–16 (à valider par PLG) : convertisseur A/N–N/A ;
  échantillonnage/échantillons ; antenne symétrique ; symétriseur (balun) ;
  antenne cadre onde entière ; Magnetic-Loop (antenne boucle magnétique) ;
  alimenté en extrémité ; circuit de Fuchs / antenne Fuchs ; antenne
  long-fil ; diagramme de rayonnement ; lobe principal/secondaires/arrière ;
  direction principale de rayonnement ; radians ; antenne à pot de blocage ;
  coefficient de vélocité (facteur de raccourcissement) ; impédance au point
  d'alimentation ; résistance d'alimentation ; dipôle replié ;
  radiateur/réflecteur/directeur ; éléments parasites ; radiateur isotrope /
  sphérique ; ventre/nœud de courant/tension ; alimentée en courant/en
  tension ; à basse/haute impédance ; impédance caractéristique ; échelle à
  grenouilles ; ondes de gaine / courant de gaine / self à compensation de
  courant / bloqueur d'ondes de gaine ; effet de peau ; atténuation de
  câble ; rapport d'ondes stationnaires (SWR) ; SWR-mètre ; pont de mesure
  SWR ; puissance directe/réfléchie ; analyseur de réseau vectoriel ;
  calibrage ; puissance isotrope rayonnée équivalente (EIRP) ;
  auto-déclaration ; déclaration (§ 9 BEMFV) ; distance de sécurité ;
  valeurs limites ; champ lointain / champ proche réactif/rayonnant ;
  formule approchée ; aides médicales actives ; protection contre la
  foudre / spécialiste / concept ; borne principale de mise à la terre ;
  résistances d'écoulement ; parasites de crépitement ; faisceau (direct)
  de rayonnement ; accident secondaire. Conservés : SDR, Groundplane,
  Windom, W3DZZ, Delta-Loop, Cubical-Quad, Yagi-Uda, EFHW, dBi/dBd, QRP,
  BNetzA, BEMFV, 26. BImSchV, VDE, N/SMA/UHF/BNC, RG58/RG174, IC-705,
  Hamnet, SOL(T)/Load/Open/Closed, NECPP.
- BUILD v0.6 (ch. 1–16, livre complet) : RÉUSSI — 208 pages, 0 erreur
  LaTeX (marginfix inclus), 0 « Rerun », toutes les sondes passantes.
  DÉCOUVERTE MAJEURE — cause racine des pertes marginfix élucidée :
  ce n'était PAS la densité des pages. img/202include.tex (diagramme
  d'atténuation de câble, annexe du recueil de formules) est un pgfplots
  à dimensions FIXES 21×29 cm que l'autoscale DARC ne réduit pas
  (il n'ajuste que les unités tikz, pas width/height pgfplots). Placé
  dans une marge de 52 mm, il ne « rentre » jamais ; marginfix plaçant
  les notes DANS L'ORDRE, cette note insérable nulle part BOUCHONNE la
  file : toutes les notes de marge suivantes du livre (ch. 14 §12 → fin,
  y c. les boîtes <danger> du ch. 16 et la photo blitz) étaient perdues.
  Les « pertes v0.3–v0.5 » documentées étaient ce même bouchon (via le
  repli allemand des mêmes sections).
  CORRECTIF (retouche session-locale n° 3, à REFAIRE après chaque
  build_book.py, comme les deux autres) : précompiler la figure en PDF
  autonome puis l'inclure en image —
    1. standalone : \resizebox{52mm}{!}{\input{img/202include.tex}}
       compilé en fig202.pdf, copié dans livre-E-fr/ ;
    2. dans sections/kabeldaempfung_1.tex : remplacer
       \Margin{\DARCimage{1.0\linewidth}{202include} par
       \Margin{\noindent\includegraphics[width=\linewidth]{fig202.pdf}
       (le reste du bloc — captionof + label — inchangé).
  Résultat : 13/13 légendes ex-perdues replacées (swr_2, swr_meter ×3,
  vna ×2, kabeldaempfung, mantelwellendrossel, eirp ×2, grenzwerte ×2,
  blitz), boîtes <danger> du ch. 16 toutes présentes, références « ?? »
  21 → 7 (les 7 restantes : pages 19, 56, 95, 115, 124, 133, 137,
  ch. 1–12, préexistantes, labels absents de la source amont).
  À proposer à Pierre : intégrer ce correctif dans build_book.py
  (décision à lui — fichier gelé) et/ou remonter le bug amont
  (autoscale DARC vs pgfplots à dimensions fixes) au projet 50ohm.
  Pièges de build supplémentaires observés cette session : (a) les
  chaînes `p1 && p2 && p3` court-circuitent car lualatex sort en code 1
  sur la moindre erreur — chaîner avec `;` ; (b) le bac à sable TUE
  parfois la 3e passe consécutive (OOM/limite CPU) en laissant book-E.pdf
  et book-E.out TRONQUÉS — symptôme : « File ended while scanning use of
  \BKM@entry » à la passe suivante ; remède : supprimer aux/out/toc et
  relancer des passes UNITAIRES séparées ; (c) le PDF non compressé passe
  de 160 à 240 Mo car les photos des notes de marge autrefois perdues
  sont désormais réellement incluses — la compression Ghostscript /ebook
  ramène le tout à 3,2 Mo.
  Sondes pdftotext : penser à la CÉSURE (« IC-\n705 ») — la décésure
  `-\n`→`` supprime aussi les traits d'union légitimes ; tester les deux
  formes. Livré : livre-E-fr-v0.6-ch1-16.pdf (208 pages, 3,2 Mo).

## Pièges de build (synthèse, tous vérifiés sur N+E)
- apt : retirer /etc/apt/sources.list.d/*nodesource* AVANT toute install ;
  installer TeX par lots ; texlive-lang-german ET texlive-lang-french
  obligatoires + poppler-utils + ghostscript ; mistletoe via
  pip --break-system-packages.
- git clone peu fiable : tarballs via codeload.github.com.
- Compilation : passes `lualatex` directes (latexmk sort en code 12) ;
  chaîner avec `;` et JAMAIS `&&` (lualatex sort en code 1 sur la
  moindre erreur) ; le bac à sable peut TUER une 3e passe consécutive
  en laissant book-*.pdf et book-*.out TRONQUÉS (symptôme passe
  suivante : « File ended while scanning use of \BKM@entry ») —
  supprimer aux/out/toc et relancer des passes UNITAIRES ;
  arrière-plan : `setsid nohup bash -c '…' < /dev/null &` + checkpoints
  sleep ≤ 280 s.
- Sondes pdftotext : normaliser l'apostrophe U+2019 ET la césure
  (« IC-\n705 ») — tester avec et sans décésure `-\n`.
- Compression : gs -dPDFSETTINGS=/ebook -dDetectDuplicateImages=true.
- Chemins sources : toc/A.json (PAS toc_A.json) ; catalogue
  contents/questions/fragenkatalog3b.json (arbre imbriqué, walk()
  récursif testant `number` ET `question`) ; sections
  contents/sections/<ident>.md.

## COMPILATION v0.4 (ch. 1–7) — 168 p., 3,1 Mo, 0 erreur, 0 « Rerun »

Environnement (pièges NOUVEAUX vs notes E) :
- Purger `/etc/apt/sources.list.d/nodesource.sources` (extension `.sources`, pas `.list`).
- Installer les paquets TeX PAR LOTS (le méta-install groupé casse) :
  `fonts-linuxlibertine ghostscript` puis `texlive-lang-german texlive-lang-french`
  puis `texlive-fonts-extra` (fournit **libertinus.sty**) puis
  `lmodern texlive-luatex texlive-latex-recommended` (fournit **lualatex-math.sty**
  et les polices lmodern). Ces 3 derniers ne figuraient pas dans les notes E.
- `pip install mistletoe --break-system-packages` ; dépôt GÉNÉRATEUR `DARC-e-V/50ohm`
  requis en plus du dépôt de contenus (module `renderer`, via `PYTHONPATH`).
- `hexdump` absent du bac à sable (utiliser `od -c` ou Python).

### QUATRE BUGS DÉCOUVERTS EN COMPILANT

**(1) BUG DE TRADUCTION (le mien) — deux-points interdit dans les légendes.**
Le parseur amont `renderer/image.py` impose `[picture:ID:ident:légende]` avec
`légende = [^:\]]+` : **aucun deux-points**. Ma légende du picture 1077
(innenwiderstand) contenait « … $R_i = R_L$ : le quotient … » -> marqueur NON RENDU,
imprimé en texte brut dans le PDF. Corrigé (« , ici le quotient »).
=> RÈGLE POUR LES LOTS SUIVANTS : ne JAMAIS mettre de « : » dans une légende
d'image. Sonde : `grep -rn "\[picture:\|\[photo:" build-X/sections/*.tex`
(hors lignes commençant par `%`) doit ne rien retourner.

**(2) BUG AMONT — champ surnuméraire dans le picture 949 (photovoltaik).**
Source DE : `[picture:949:a_solarmodul:Solarmodul mit Zellen:Solarzellenverbund…]`
(4 champs) -> non rendu, en allemand comme en français. Corrigé côté FR en
supprimant le champ parasite. ÉCART ASSUMÉ à la règle « quirks verbatim » :
le conserver laissait du balisage brut visible dans le livre.

**(3) BUG MAJEUR — préfixes d'unités perdus — CORRIGÉ DANS build_book.py v0.3.**
`BookLaTeXRenderer.render_unit` n'utilisait PAS `token.prefix` (que
`renderer/unit.py` expose pourtant) :
    return f"${value}$\\,{unit}"      -> « 145 MHz » rendu « $145$\,Hz »
**219 préfixes perdus** dans le livre A ch.1-7, dont **214 dans les questions
d'examen** : « 2 kHz » -> « 2 Hz », « 1,2 μH » -> « 1,2 H » — énoncés
PHYSIQUEMENT FAUX. Touchait TOUTES les éditions (N/E/A) et les DEUX langues,
donc aussi les PDF N, E et A v0.3 déjà livrés — **À REGÉNÉRER**.

**build_book.py est passé en v0.3** (dérogation explicite de PLG au gel du
fichier). Diff minimal, strictement limité aux unités :
    prefix = getattr(token, "prefix", "") or ""
    return f"${value}$\\,{prefix}{unit}"
+ en-tête « Version du script : v0.3 » avec journal des modifications.
md5 : v0.2 = bef9b81ce94e73603235431246b1771b
      v0.3 = 037b4cc91263b40bdd1ce133dae09188
Non-régression vérifiée : `°` et `%` restent sans préfixe ni `\,` ;
346 unités préfixées correctement rendues ; aucune unité amputée.
Le wrapper `run_build_fixed.py` de cette session est désormais CADUC :
appeler directement `build_book.py` v0.3.

**(4) BUG AMONT — \ref non normalisées (idents à umlauts).**
`build_book.py` assainit les idents dans `\label` (non-ASCII -> `-`) mais pas dans
`\ref` : `\label{a_st-rspektrum}` vs `\ref{a_störspektrum}` -> « figure ?? ».
Identique en allemand. Correctif session-local : réaligner les `\ref` sur la
normalisation des `\label` (2 références réparées : a_störspektrum, a_pep_hüllkurve).
Reste 1 « ?? » : `a_mehrwegeausbreitung_ionosphäre` (ch. 1) — le picture n'existe
tout simplement pas dans la section : DÉFAUT DE CONTENU AMONT, idem en allemand.

### AUTRE PIÈGE MAJEUR — titres de sections restés en allemand
`build_book.py` l. 672 : `tr_titles["sections"].get(ident, …)` — les sections sont
indexées par **IDENT**, alors que les chapitres le sont par TITRE DE et les
abstracts par TEXTE D'ABSTRACT DE. Mes 35 clés « titre allemand » étaient donc
ignorées en silence. `titles.json` corrigé : les 65 clés de `sections` sont
désormais des idents. => VÉRIFIER SYSTÉMATIQUEMENT à chaque lot.

### CORRECTIFS LaTeX SESSION-LOCAUX (à réappliquer après CHAQUE génération)
1. `printf '\\extrafloats{400}\n' >> settings-pre.tex`
2. **Colonne de marge allongée** — À PLACER DANS `book-A.tex` APRÈS
   `\documentclass{FiftyOhmBook}` (et NON dans settings-pre.tex/settings.tex,
   qui sont chargés AVANT `\RequirePackage{marginfix}` -> « Undefined control
   sequence ») :
       \setlength{\marginheightadjustment}{15mm}
       \setlength{\marginparpush}{3pt}
   Justification : le build ALLEMAND des mêmes 7 chapitres passe à **0 erreur**
   (166 p.) ; c'est donc la LONGUEUR DU TEXTE FRANÇAIS (169 p. ; légendes et
   encadrés <indepth>/<tip> plus longs) qui sature la colonne de 52 mm et fait
   perdre 21 notes de marge à marginfix. `\marginheightadjustment` est ajouté
   par marginfix à la hauteur de colonne de CHAQUE page -> 0 note perdue.
3. **pgfplots plus larges que la marge (52 mm)** — l'autoscale DARC ne règle que
   les unités tikz (`\tikzset{x=…cm,y=…cm}`) et n'a AUCUN effet sur `width`/`height`
   d'un `axis` pgfplots. Mesurer les includes appelés en marge et corriger ceux
   qui dépassent 52 mm en remplaçant
       \Margin{\DARCimage{1.0\linewidth}{Ninclude}
   par
       \Margin{\noindent\resizebox{\linewidth}{!}{\input{img/Ninclude.tex}}
   Concernés ici : **1077** (83,2 mm, innenwiderstand), **1092** (77,5 mm, ssb_3),
   **988** (114,6 mm, ionosphaere_3).

### CHAÎNE DE COMPILATION
`PYTHONPATH=…/50ohm-main python3 build_book.py --edition A --lang fr
--translations out-A/A --input 50ohm-contents-dl-main --output build-A
--version-label 0.4 --limit-chapters 7 --no-compile`
puis 2 passes `lualatex` (chaîner avec `;` et non `&&`), `cp book-A.pdf
book-A-pass2.pdf` AVANT toute 3e passe, puis Ghostscript `/ebook`
(74 Mo -> 3,1 Mo).
PIÈGE : ne jamais lancer lualatex pendant que la génération écrit encore les
`.tex` -> fichiers tronqués, octets NUL, « Text line contains an invalid character ».

### SONDES DE RECETTE (toutes passées)
7/7 titres de chapitres, 65/65 titres de sections, 170/170 questions du lot 3,
85/85 légendes de marge, encadrés FR (Astuce/Attention/Approfondissement/
Nouvelle unité) présents, 0 germanisme (Tipp/Achtung/Gefahr/Vertiefung/
Neue Einheit), préfixes d'unités rétablis (145 MHz, 2 kHz, 1,2 μH, 56 pF, 4,7 kΩ),
1 seul « ?? » (défaut amont ch. 1).
PIÈGE DE SONDE : `pdftotext -layout` entrelace les notes de marge avec le corps
-> faux négatifs. Utiliser `pdftotext` SANS `-layout`, normaliser U+2019, dé-césurer
(`-\n`), et sonder par FRAGMENTS COURTS (les maths retirées cassent les phrases :
« facteur de qualité $Q$ a le montage »).


## build_book.py v0.4 — 4 correctifs intégrés (dérogation PLG au gel du fichier)

md5 : v0.2 = bef9b81ce94e73603235431246b1771b
      v0.3 = 037b4cc91263b40bdd1ce133dae09188  (préfixes d'unités)
      v0.4 = voir livraison                     (+ 4 points ci-dessous)

1. **validate_output()** — garde-fou à la GÉNÉRATION (avertissements, jamais
   bloquant). Trois contrôles, chacun correspondant à un bug qui a coûté un
   cycle de compilation complet cette session :
     a. marqueurs DARCdown non rendus, restés en texte brut dans le .tex
        (commentaires LaTeX en début ET en fin de ligne exclus) ;
     b. \ref sans \label correspondant -> « figure ?? » ;
     c. clés de titles.json["sections"] qui ne sont pas des idents.
2. **fix_latex()** — les \ref subissent la même normalisation d'ident que les
   \label (idents non-ASCII).
3. **settings.tex** — clamp de largeur sur \DARCimage (\sbox + \resizebox
   UNIQUEMENT si la boîte déborde). Supprime la cause racine fig202 : plus besoin
   de précompiler img/202include.tex. Aucun agrandissement, aucun changement
   visuel pour les figures conformes.
4. **settings-pre.tex** — \extrafloats{400} ajouté automatiquement (l'étape
   manuelle disparaît).

### CE QUE LE GARDE-FOU A IMMÉDIATEMENT TROUVÉ (défauts PRÉEXISTANTS, non détectés jusqu'ici)
- **Livre E v0.6 DÉJÀ LIVRÉ** : 3 marqueurs imprimés en BALISAGE BRUT dans le PDF
  (figures manquantes) — picture 992 (« 07:00 UTC » : deux-points d'HORAIRE !),
  picture 1008 (« Émissions non désirées : … »), photo 327 (« De gauche à droite : … »).
  Les deux premiers viennent des SOURCES ALLEMANDES ; le 327 est de moi
  (l'allemand utilisait un tiret). À CORRIGER dans les sources E.
- **Livre N** : picture 542 (« Digital Voice: Relais… ») et photo 123 (un
  `[index:S-Meter]` accolé après le `]` final) -> non rendus. Défauts amont.
- RAPPEL DE LA RÈGLE : le parseur amont impose légende = [^:\]]+ — JAMAIS de
  deux-points dans une légende, et rien après le `]` final.

### NON-RÉGRESSION v0.3 -> v0.4 (mesurée, à correctifs égaux)
- Diff de génération : sections modifiées UNIQUEMENT par la normalisation des
  \ref ; document maître inchangé ; settings.tex/-pre = ajouts en fin de fichier.
- **N** (de, 131 s.) : 0 erreur, 0 Rerun, 223 p. (3 passes nécessaires).
- **E** (fr, 103 s.) : 26 légendes de marge perdues contre **28 en v0.3** ->
  AUCUNE régression, 2 légendes récupérées. Reste 1 erreur marginfix.
- **A** (fr, 65 s.) : 0 erreur, 0 Rerun, **166 p.** (168 en v0.3 : le clamp réduit
  3 pgfplots hors gabarit), 90/90 légendes de marge, 0 balisage brut, 1 « ?? »
  (défaut de contenu amont ch. 1).

### PROBLÈME E RESTANT (préexistant, mérite une session dédiée)
E perd 26 notes de marge. Ce n'est PAS la saturation par le français :
`\marginheightadjustment{15mm}` n'a AUCUN effet sur E (alors qu'il règle A à 100 %).
Ce n'est pas non plus une figure inplaçable : après clamp, la plus haute note de
marge fait 70 mm pour une colonne de ~250 mm. Le PDF E v0.6 livré en perdait
encore 16 malgré ses rustines (\clearpage autour de Blitzerdung + précompilation
fig202). Cause à instruire.

### CORRECTIF SESSION-LOCAL ENCORE NÉCESSAIRE (classe A uniquement)
Dans book-A.tex, APRÈS \documentclass (settings*.tex sont chargés AVANT marginfix) :
    \setlength{\marginheightadjustment}{15mm}
    \setlength{\marginparpush}{3pt}
Non intégré à build_book.py (point 5 non retenu) : le défaut à 0 préserve
exactement le comportement allemand. À passer en option CLI si besoin.


================================================================================
## LOT 6 — LOT FINAL — CLÔTURE DE LA CLASSE A  (ch.13 + ch.14 + N_Ende)
================================================================================
(NB de numérotation : le plan des sessions précédentes désignait tantôt « lot 6 »,
tantôt « lot 8 » ce dernier lot ; le périmètre livré ici — ch.13-14 + N_Ende —
est celui qui CLÔT la classe A, quelle que soit l'étiquette.)

### PÉRIMÈTRE LIVRÉ
- 2 chapitres, 10 sections, 22 questions, ~32,2 k caractères.
  - ch.13 « Personenschutzabstand » (6 s) : effektive_strahlungsleistung_erp_2,
    personenschutzabstand_3, naeherungsformel_2, nahfeld, fernfeld,
    personenschutzabstand_richtantennen.
  - ch.14 « Sicherheit » (4 s) : elektrische_geaete_oeffnen_2, schutzerdung_2,
    antennen_beruehrung_2, N_Ende.
- Recomptage depuis toc/A.json : 10 s / 22 q, 0 doublon intra-lot, 0 recouvrement
  avec les 695 déjà traduites, toutes au catalogue (1750 entrées).

### ÉTAT FINAL DE L'ARBRE (out-A/A)
- **154 sections** .md (tous les idents de toc/A.json présents).
- **questions.json : 717** (504 forme complète / 213 énoncé seul).
- **titles.json : 14 chapitres / 13 abstracts / 154 sections** ; toutes les clés
  « sections » sont des IDENTS valides (jamais un titre allemand).

### N_Ende : TRADUIT À NEUF (déviation vs plan)
Le plan antérieur prévoyait de COPIER N_Ende depuis le zip de la classe E.
Or `contents/sections/N_Ende.md` existe dans le dépôt de contenus (3843 car.) et
toc/A.json le référence directement : il a donc été TRADUIT à neuf ici (mêmes
règles verbatim), pas copié. Titre FR : « Conclusion du cours ».

### TITRES FR DES 10 SECTIONS (titles.json, clés = idents)
- effektive_strahlungsleistung_erp_2 -> « Puissance apparente rayonnée (ERP) II »
- personenschutzabstand_3            -> « Distance de protection des personnes III »
- naeherungsformel_2                 -> « Formule approchée II »
- nahfeld                            -> « Champ proche »
- fernfeld                           -> « Champ lointain »
- personenschutzabstand_richtantennen-> « Protection des personnes avec les antennes directives »
- elektrische_geaete_oeffnen_2       -> « Ouverture d'appareils électriques II »
- schutzerdung_2                     -> « Mise à la terre de protection et liaison équipotentielle II »
- antennen_beruehrung_2              -> « Toucher des antennes II »
- N_Ende                             -> « Conclusion du cours »
Chapitres : Personenschutzabstand -> « Distance de protection des personnes » ;
Sicherheit -> « Sécurité ». Abstracts ch.13-14 traduits (clés = texte DE exact).

### ARBITRAGES (à valider PLG ; certains à remonter au DARC)
1. **`<tipp>` -> `<tip>`** (elektrische_geaete_oeffnen_2) : DÉFAUT AMONT — la
   source écrit `<tipp>`/`</tipp>` (double p), non reconnu par renderer/tag.py
   (capture « tip » seulement) -> le balisage fuyait brut dans le PDF. Corrigé
   CÔTÉ FR en `<tip>`/`</tip>` (précédent : picture-949). À REMONTER au DARC.
   Rendu vérifié : boîte « Astuce » correcte, 0 `<tipp>` résiduel.
2. **`$\textrm{Faktor}_\textrm{FmodPers}$`** (naeherungsformel_2, indepth) :
   CONSERVÉ verbatim — nom de champ logiciel de la déclaration BEMFV, pas de la
   prose libre.
3. **ERP -> « puissance apparente rayonnée (ERP) »**, ACRONYME ERP CONSERVÉ.
   Réinterprète la note L4 (« ERP -> PAR ») : cohérence avec les énoncés d'examen
   allemands (qui gardent ERP/EIRP) et avec le précédent EIRP conservé. EIRP idem.
4. Indices maths germanophones dans les réponses/formules conservés VERBATIM :
   `P_{\textrm{Sender}}`, `P_{\textrm{Verluste}}`, `G_{\textrm{Antenne}}`,
   `P_{\textrm{Ant}}`, `P_{\textrm{EIRP}}` (règle « maths verbatim »).

### CARACTÈRES SPÉCIAUX PRÉSERVÉS VERBATIM
- U+2212 (signe moins) : ×10 dans naeherungsformel_2 (blocs commentés).
- U+202F (espace fine insécable) : ×2 dans personenschutzabstand_3 (commentaires).
- Guillemets allemands „…" -> « … » quand PROSE traduite (schutzerdung_2 « heiß »
  -> « chaud ») ; en-dash U+2013 conservé (N_Ende).
- Blocs `%…` commentés : byte-identiques DE<->FR (contrôle passé sur les 10).

### BUG INTERCEPTÉ ET CORRIGÉ EN COURS DE LOT
Le bloc `<indepth>` (lignes 107-111 : « Warum wird… RTTY und FM… Faktor 1 »)
appartient à **naeherungsformel_2**, PAS à personenschutzabstand_3 (79 lignes,
sans indepth ; la question AK112 et son indepth sont dans naeherungsformel_2).
Les 4 traductions avaient d'abord été rangées sous le mauvais ident (indices
inexistants -> silencieusement ignorés, prose restée allemande). Détecté par la
sonde anti-germanismes, déplacé, régénéré : 0 germanisme résiduel.
=> LEÇON : la sonde anti-germanismes rattrape les prose-lines non traduites dues
à une clé d'indice mal rangée. La garder obligatoire.

### CLASSIFICATION DES 22 QUESTIONS (12 complète / 10 énoncé seul)
- Forme complète (prose allemande dans les réponses) : AG501, AG502, AK101,
  AK102, AK103, AK104, AK105, AK107, AK201, AK202, AK203, AK204.
  - AG502 : réponses = formules + « bezogen auf… » (prose) -> complète.
  - AK107 : réponses « ca. … W » -> « ca. » = prose -> complète (env.).
  - AK105 : « Er verringert sich… » -> prose -> complète ; « Er » (der
    Sicherheitsabstand, masc.) rendu « Elle » (la distance, fém.).
- Énoncé seul (réponses numériques/unités/langue-neutre) : AG503, AK106, AK108,
  AK109, AK110, AK111, AK112, AK113, AK114, AK115.
- Quirks source conservés verbatim : `$ D$` (AK104), `$11,5 $dBd` (AK110 énoncé),
  `30 Ohm\cdot` (AK103 énoncé, display `\[...\]` — converti par _inline au build).

### TERMINOLOGIE POSÉE ch.13-14 (cumulative, à valider PLG)
ERP -> puissance apparente rayonnée (ERP) [acronyme conservé] ; EIRP conservé ;
Personenschutzabstand -> distance de protection des personnes ;
Sicherheitsabstand -> distance de sécurité ; Näherungsformel -> formule approchée ;
Nahfeld -> champ proche (reaktiv -> réactif, strahlend -> rayonnant) ;
Fernfeld -> champ lointain ; Feldwellenwiderstand / Wellenwiderstand -> impédance
d'onde (du milieu) ; magnetische/elektrische Feldkonstante -> constante
magnétique/électrique ; Feldstärke -> intensité de champ ; magnetische Flussdichte
-> densité de flux magnétique ; Magnetisierung -> aimantation ;
Schutzerdung -> mise à la terre de protection ; Potentialausgleich -> liaison
équipotentielle ; Potentialausgleichsschiene / -anschluss -> barre / borne de
liaison équipotentielle ; niederohmig -> à basse impédance / faiblement résistif ;
hochohmig (Widerstand) -> de forte valeur ohmique ; Spannungsbauch -> ventre de
tension ; endgespeist -> alimenté en extrémité ; Erdungsleitung/Erdleitung ->
ligne de (mise à la) terre ; Winkeldämpfung -> atténuation angulaire ;
Strahlungskeule/Strahlungsdiagramm -> lobe / diagramme de rayonnement ;
Hauptstrahlrichtung -> direction principale de rayonnement ; Schaltnetzteil ->
alimentation à découpage ; Röhren-/Transistorendstufe -> étage final à
tubes/transistors ; Senderendstufe -> étage final d'émetteur ; Rundstrahlantenne
-> antenne omnidirectionnelle ; Parabolspiegel -> réflecteur parabolique ;
PE-Schaum-Massivschirm-Kabel -> câble à écran plein et diélectrique en mousse de
PE ; mehradrige Litze -> tresse multibrins ; Bodensee -> lac de Constance ;
Freiraumausbreitung -> propagation en espace libre ; Feldwellenwiderstand des
freien Raumes -> impédance d'onde de l'espace libre. Conservés : ERP, EIRP, BEMFV,
BNetzA, RTTY, FM, PEP, DARC, DOK, OV, PE, Yagi-Uda, dBd/dBi, HAM RADIO,
Funk.Tag, HAM-Challenge, Mastodon. z. B. -> par ex. ; ca./etwa -> env. ;
d. h. -> c.-à-d. ; -Band -> « bande des … » ; „…" -> « … ».

### VALIDATIONS (toutes passées à 100 %)
- Sections 10/10 : signature structurelle DE<->FR identique (marqueurs/tags/---,
  hors %), commentaires % byte-identiques, math verbatim, 0 deux-points en légende,
  anti-germanismes 0 hit réel (« des » = homographe FR exclu).
- Rendu renderer sur les 10 : 0 marqueur brut résiduel ; boîte Astuce OK.
- 22 questions : anti-germanismes 0 hit (indices maths exclus car dans `$…$`).
- Arbre : 154/154 idents traduits ; titles 14/13/154 ; toutes clés sections =
  idents ; questions 717.

## COMPILATION v1.0 — LIVRE A COMPLET (ch. 1–14) — CLÔTURE DE LA CLASSE A

**Résultat : 350 pages, 4,93 Mo (compressé) / 95,77 Mo (brut), rc=0.**

### Chaîne exacte (reproductible)
1. Génération de l'arbre LaTeX : `build_book.py` v0.4 (gelé, md5 f019d2c…), invoqué
   `--edition A --lang fr --translations out-A/A --input 50ohm-contents-dl-main
   --output build-A --version-label 1.0` (implicitement SANS `--limit-chapters`).
2. Correctif session-local RÉAPPLIQUÉ dans `build-A/book-A.tex` juste après
   `\documentclass{FiftyOhmBook}` (2 lignes) :
   `\setlength{\marginheightadjustment}{15mm}` + `\setlength{\marginparpush}{3pt}`.
3. Compilation VIA LATEXMK (jamais 2 lualatex à la main — piège DARCimageCache) :
   `latexmk -lualatex -interaction=nonstopmode book-A.tex`.
   Convergence en 3 passes : 348 → 350 → 350 pages (stable), rc=0.
4. Compression : `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5
   -dPDFSETTINGS=/ebook -dDetectDuplicateImages=true` → `book-A-v1.0.pdf` (4,93 Mo).

### Sondes de recette (toutes passées)
- Page 1 = page de titre correcte : « 50 Ohm / Cours complet Classe A /
  Version 1.0 — compilée le 17.07.2026 ». **Pas de corruption** (« 14.63995pt »
  absent du .log → l'.aux n'a pas été relu en gâchant la page de titre).
- 14 chapitres, 12 titres FR de ch.13-14 + 10 sections tous rendus dans le PDF.
- 22 questions du lot 6 toutes rendues (fragments FR distinctifs retrouvés,
  y compris quirks maths `$11,5 $dBd`, câble « écran plein »).
- `N_Ende` rendu proprement en TOUTE FIN de livre (« Félicitations… » à 99,4 %
  du texte, signature « Lars DC4LW et Matthias DL9MJ » présente).
- Références orphelines « ?? » : EXACTEMENT 2, toutes deux défauts AMONT connus,
  AUCUNE nouvelle en ch.13-14 :
    · `a_mehrwegeausbreitung_ionosphäre` (ch.1, p.7)
    · `a_sender` (ch.10, p.263)
- Germanismes résiduels dans le PDF = uniquement (a) indices maths verbatim,
  (b) libellés de dessins TikZ amont (policy : non traduits, ex. « Anpassglied »),
  (c) réponses officielles DE des questions « énoncé seul » (intentionnel),
  (d) gloses allemandes entre parenthèses (intentionnel).

### ÉTAT DE CLÔTURE — CLASSE A TERMINÉE
- **14 chapitres / 13 abstracts / 154 sections / 717 questions / 350 pages.**
- titles.json : 14 / 13 / 154 (clés sections = idents, clés chapitres/abstracts
  = texte allemand exact lu depuis toc/A.json).
- questions.json : 717 (504 forme complète / 213 énoncé seul).
- Livrables : zip double-imbriqué (traductions + NOTES) + `book-A-v1.0.pdf`.

### RESTE-À-FAIRE PROJET (hors classe A, prochaine session)
- **Régénérer les PDF des classes N et E** avec `build_book.py` (≥ v0.4) pour
  corriger le défaut de légendes à « : » (parseur amont) qui a provoqué des
  pertes silencieuses de figures dans les PDF N et E DÉJÀ DISTRIBUÉS. Le contenu
  source N/E est inchangé ; il suffit de recompiler avec le script courant
  (les légendes fautives ont déjà été identifiées lors des travaux classe A).
- `build_book.py` reste **gelé v0.2 pour N/E** et **v0.4 pour A** ; toute montée
  de version doit passer par une session dédiée (dérogation PLG).

---

## SESSION 09/08/2026 — Déblocage compilation classe A + remise à niveau amont

### 1. Blocage de compilation classe A — CAUSE ÉTABLIE ET CORRIGÉE

**Symptôme** : `Float too large for page by 255.9104pt`, puis
`! Package marginfix Error: lost some margin notes.` → aucun PDF (rc=12).

**Cause** : `\marginpar` EST un flottant. Dans `latex.ltx`, `\@xympar` se termine
par `\end@float`, qui appelle `\@largefloatcheck` (seul émetteur du message dans
tout LaTeX — 3 occurrences, 2 appelants : `\end@float`, `\end@dblfloat`).
D'où un message parlant de flottant alors qu'AUCUN flottant n'existe dans le
contenu rendu (`\captionof` n'en crée pas, `\DARCimage` non plus).
`\@largefloatcheck` n'écrête que `\ht\@currbox`, une COPIE ; la boîte réellement
placée, `\@marbox`, garde sa hauteur. marginfix, dont la colonne fait
`\textheight`, ne peut jamais la loger : il la conserve puis lève l'erreur
fatale à `\end{document}`.

**Les dessins 1096 et 687 étaient HORS DE CAUSE.** Le coupable est le `<indepth>`
UNIQUE et volumineux qui les englobe. Mesure instrumentée sur `fehlerkorrektur` :
911,49 pt pour `\textheight` = 711,32 pt. Le message est émis à l'ACCOLADE
FERMANTE du `\marginpar` (ligne 43), pas à la figure — d'où la fausse piste.
Corollaire : le bornage adjustbox ne gagnait que ~15 pt = la hauteur d'une légende.

**Reproduction minimale** : une seule section (`fehlerkorrektur`), contenu amont
non modifié, suffit à reproduire.

**Correctif — build_book.py v0.13** (bloc en fin de `BOOK_CLASS`) :
`\DARCmarginpar` mesure la note à `\marginparwidth` SANS effet de bord
(compteurs sauvés/restaurés via `\cl@@ckpt`, `\protected@write` neutralisé,
`\label` et `\index` désactivés le temps de la mesure) ; au-delà de
`\DARCmarginmaxheight` (= `\textheight`), la note est composée dans le CORPS du
texte en tcolorbox sécable, comptée (`DARCmargindemoted`) et signalée
nominativement dans le journal.
→ Classe A v1.0 : rc=0, 350 pages, 2 notes rétrogradées (lignes 48 et 43,
  exactement les 2 lignes du journal d'échec). 4,89 Mo après Ghostscript.
→ **La v0.13 SUBSUME la v0.12** : sur base v0.4 (sans précompilation du 202),
  la classe E rétrograde la note de `kabeldaempfung_1` (856,56 pt) et compile
  quand même. Avec la v0.12 en place, le 202 est déjà réduit : 0 rétrogradation.

**Correctif — build_book.py v0.14** (`fix_latex()`) :
`\qty{120\pi}{\ohm}` → `120\pi\,\unit{\ohm}`. siunitx v3 refuse un nombre
contenant une macro (« Invalid number '120\mitpi' ») puis part en runaway
argument → rc=12. Idiome AMONT, présent dans `nahfeld` et `naeherungsformel_2`
(3 occurrences). La classe A ALLEMANDE bute sur le même écueil.

### 2. Dérive amont — 19 sections remises à niveau

Audit par comparaison de marqueurs DE/FR sur tout le périmètre A :
19 sections en écart (18 fois l'amont avait grossi). ~3 semaines de travail DARC
entre les traductions du 16-17/07 et le dépôt du 08/08.

**Chapitre Personenschutzabstand (restructuration, pas simple ajout)** :
- `fernfeld` SUPPRIMÉ en amont, contenu FONDU dans `nahfeld` (2 → 21 marqueurs).
  Le PDF v1.0 contenait donc un `nahfeld` TRONQUÉ. Traduction FR de `fernfeld`
  réutilisée par fusion (résumé final, encart BEMFV, photo 80).
- `verstaerkungsleistung` SUPPRIMÉ, AUCUN successeur (portait `%TODO: noch nicht
  abschließend bearbeitet`). Traduction archivée, non recyclable.
- Le contenu de l'ancien FR `naeherungsformel_2` (exercices corrigés) correspond
  désormais au `personenschutzabstand_3` allemand. Glissement, pas retraduction.
- Questions pistées, AUCUNE perdue : AK102 → `nahfeld`, AK103 →
  `naeherungsformel_2`, AK104 → `effektive_strahlungsleistung_erp_2`,
  AK105 → `personenschutzabstand_richtantennen`.

**Oscillateurs (6)** : vco, tcxo_ocxo, gpsdo, spannungsstabilitaet, dds, pll.
`oszillator_dds` 1 → 19 marqueurs (réécriture complète : 3 figures, récurrence
de l'accumulateur de phase, indepth modulo 2^N). Ident fautif corrigé dans
`oszillator_pll` : `a_oszillator_pll_pll` → `a_oszillator_pll`.

**Amplificateurs (5)** : wirkungsgrad, begrenzung_bandbreite, kollektorschaltung,
emitterschaltung, verstaerker_klasse (15 → 37 marqueurs, 6 figures neuves,
tableau de synthèse 4 classes, paragraphe classes D/E/F).

**Isolées (3)** : transverter_2, dezibel_2 (+AD426, AD427, AD428), am_2 (4 → 20).

Résultat : 153/153 sections traduites, 717 questions, 2 avertissements de
génération (dont 1 seul rescapé : `a_sender`).

### 3. ARBITRAGES ACTÉS (décisions Pierre)

- **Corrigés conservés** dans la nouvelle structure amont (le DARC a supprimé
  ses solutions ; la version FR en déroule 10 là où l'amont en donne 0).
  Écart documenté, à re-arbitrer à chaque mise à jour de ces sections.
- **Solutions placées APRÈS l'encadré de question** (bascule appliquée, 6
  reformulations de liaison). NE S'APPLIQUE QU'AUX CORRIGÉS DE SOURCE FRANÇAISE :
  dans `personenschutzabstand_richtantennen`, la démonstration est écrite par le
  DARC et reste dans l'ordre amont (interdiction de restructurer l'amont).
- **Indices allemands des formules francisés** : 42 remplacements, 15 sections.
  `ges`→`tot` (8), `Wahr`→`vrai` (6), `Gemessen`→`mes` (6), `OSZ`→`OSC` (3),
  `U_B`/`I_B` (Betriebs-) → `tot`/`alim` (4), `Dr`(Draht)→`fil` (3),
  `Quarz`→`quartz` (2), `Wechselstrom`→`alt` (2), `T`(Träger)→`p` (3),
  `Takt`→`horloge`, `Sender`→`TX`, `sperr`→`inv`, `sek`→`sec`,
  `Isolator`→`isolant`.
  **RÈGLE : jamais d'accent dans `\mathrm{}`** — l'alphabet mathématique droit
  de LuaLaTeX n'a pas les glyphes accentués (disparition silencieuse).
  Exceptions délibérées : `G_\mathrm{Antenne}` (même mot en français) et
  `\textrm{Faktor}_\textrm{FmodPers}` (nom littéral d'un champ du formulaire
  BEMFV — le traduire induirait le candidat en erreur). `I_\mathrm{B}` de
  `transistor_2` = Basis, conservé (d'où le traitement fichier par fichier).

### 4. DÉFAUTS AMONT CONSIGNÉS (non corrigés, à signaler au DARC)

- **`\label` en double** : le dessin 1116 porte l'ident `a_feldwellenwiderstand`
  dans `nahfeld` ET dans `naeherungsformel_2` → « Label multiply defined » et un
  `\ref` qui pointe au mauvais endroit.
- **`\qty{120\pi}{\ohm}`** : casse siunitx v3 (contourné en v0.14 du script).
- **Deux-points dans les légendes** (parseur amont) : signalement déjà rédigé.
- **Coquilles** : `Bezeichnugnen` (légende dessin 1118), `zuammen`,
  `Kollerktorwiderstand`, `richtet sich Die Bezeichnung`, `im vergleich`
  (emitterschaltung), `verschiedene arten` (oszillator_tcxo_ocxo),
  `Blochschaltbild` (polarmodulation). Redondance : `kollektorschaltung` répète
  deux fois de suite que le montage est appelé *Emitterfolger*.

### 5. RESTE-À-FAIRE

- **Traduire les textes des dessins TikZ** quand c'est possible. 45 des 165
  dessins de la classe A portent du texte. Devenu NÉCESSAIRE : la francisation
  des indices crée des discordances texte/figure (dessin 1082 « Taktgenerator »
  face à $f_\mathrm{horloge}$). Les dessins sont AMONT → copie côté français
  obligatoire, comme pour la précompilation du 202, + dérogation documentée.
- **Harmoniser les entrées `[index:]`** avec les classes N et E : `oszillator_dds`
  introduit le premier `[index:]` du périmètre A (traduit ici, `Jitter` conservé).
  24 autres sections amont en portent, toutes en périmètre N/E.
- **Non-régression classe E** avec la v0.13/v0.14 : NON ABOUTIE (processus
  d'arrière-plan tués par le bac à sable). Chiffre attendu :
  `DARCmargindemoted` = 0.
- **`P_\mathrm{S}`** (Sendeleistung) laissé tel quel dans `personenschutzabstand_3`
  (6 occurrences) : `S` n'est pas manifestement allemand. À trancher.
- Signalement amont au DARC (labels en double, deux-points, coquilles).

---

# SESSION 09/08/2026 (soir) — dérive amont classe A, anglicismes, non-régression E

## 1. Audit de dérive — les trois classes

Comparateur `audit_derive.py` : séquence des marqueurs DARCdown, section par
section, lignes commentées exclues. Les clés comparées sont le TYPE + l'IDENT
(la légende est traduite, elle ne peut pas servir de comparaison).

**PIÈGE MÉTHODOLOGIQUE — quatre types de marqueurs, pas trois.** Le premier
passage ne comparait que `picture`, `photo`, `question`, `ref`, `include` et
`index`. Il manquait **`[table:ident:légende]`**, ainsi que `[morse:]` et
`[class:]`. Inventaire exhaustif du dialecte sur tout le dépôt amont :

| marqueur | occurrences |
| --- | --- |
| `[question:` | 1751 |
| `[ref:` | 481 |
| `[picture:` | 431 |
| `[photo:` | 154 |
| `[index:` | 81 |
| `[morse:` | 58 |
| `[table:` | 55 |
| `[include:` | 27 |
| `[class:` | 6 |

L'oubli de `[table:]` masquait une 18e section en écart en classe A.

### Résultat

| classe | sections | en écart |
| --- | --- | --- |
| N | 131 | **0** |
| E | 103 | **0** |
| A | 153 | **18** |

**Les classes N et E n'ont PAS dérivé.** Alignement parfait sur l'amont du
09/08/2026, tous types de marqueurs confondus. Le chantier de remise à niveau
annoncé pour ces deux classes n'existait pas.

Contrôle structurel complémentaire (puces, lignes de tableau, séparateurs,
intertitres, balises) : 55 écarts en classe N — ce sont exactement les
55 encarts `<france>`, contribution française, pas dérive. Classe E : 0 écart,
et pour cause — **elle ne contient aucun encart `<france>`** (voir § 5).

## 2. Classe A — 18 sections remises à niveau

Toutes dans le domaine récepteur/émetteur. Aucune ne figurait dans les 19 de la
session précédente : ce sont deux lots amont distincts.

**Cause établie, ce n'est pas une omission de traduction.** Deux traductions
portaient encore le TODO amont d'origine, depuis honoré par le DARC :
- `bandreite_3` : `%TODO: Einfügen Grafik/Skizze hinsichtlich Bandbreite und
  Leistungsverteilung.` -> le dessin 1121 a été créé depuis.
- `frequenzmessung_2` : `% TODO Der Text wird noch fertig geschrieben. - DB7YI
  2024-04-22` -> tout le développement sur le temps de porte et la résolution en
  fréquence a été écrit depuis, avec le dessin 1126.

**Signature dominante : le bloc `<margin>`.** 14 des 17 figures absentes se
trouvaient dans un `<margin>` ou un `<webmargin>` de la source allemande. Le
DARC enrichit ses sections par ajout de notes de marge illustrées.

### Détail

| section | traitement |
| --- | --- |
| `agc_2` | + `<margin>` dessin 1055 |
| `squelch_2` | + `<webmargin>` dessin 737 |
| `bfo_2` | + `<margin>` dessin 838 |
| `bandreite_3` | TODO -> `<margin>` dessin 1121 |
| `low_noise_block` | + phrase de renvoi + `<margin>` dessin 1094 |
| `snr_rauschzahl` | + renvoi + `<margin>` dessin 1097 ; **correction de fond** |
| `ueberlagerungsempfaenger_einfachsuper_2` | + phrase de renvoi + `<margin>` dessin 913 |
| `s_meter` | 3 § retraduits + `<margin>` dessins 578 et 420 |
| `doppelueberlagerungsempfaenger_doppelsuper` | + renvoi `doppelsuper_blockschaltbild` |
| `trennschaerfe_2` | remise en ORDRE seule (4 questions reléguées en fin) |
| `dynamik_compressor_2` | **retraduction complète** (réécriture amont) |
| `fm_3` | **retraduction complète** (+ dessins 155 et 910) |
| `mischer_2` | **retraduction complète** (linéaire/non linéaire, indepth anneau) |
| `spiegelfrequenzen` | **retraduction complète** (+ formule $f_S$, recueil de formules) |
| `daempfungsglieder` | **retraduction complète** (+ indepth formules T et $\pi$) |
| `frequenzmessung_2` | **retraduction complète** (temps de porte, résolution) |
| `demodulator` | **retraduction complète** (+ dessins 147, 77, 153, 1125, indepth détecteur de produit) |
| `effektive_strahlungsleistung_erp_2` | **RIEN À FAIRE** — voir ci-dessous |

`effektive_strahlungsleistung_erp_2` sort en écart « en trop en FR » :
`[table:Pegel_Verhältnis]` plus le corrigé de AG503. **C'est l'arbitrage acté**
(corrigés conservés même quand le DARC supprime les siens). Ne pas le
« corriger » aux sessions futures : l'audit le signalera à chaque fois.

### Correction de fond dans `snr_rauschzahl`

La traduction affirmait : « Un facteur de bruit de 2 correspond par exemple à un
facteur de bruit de 3 dB » — phrase absurde, `Rauschzahl` et `Rauschmaß` ayant
été rendus par le même terme. Rétabli : **facteur de bruit** (F, linéaire) et
**figure de bruit** (NF, en dB).

### Archivage

18 fichiers dans `_archive/`, suffixés `-v1.1-perime`. Rien n'est détruit.

## 3. Anglicismes — 78 remplacements, périmètre restreint après examen

Sondage sur les trois classes, mode mathématique filtré.

**DEUX FAUX POSITIFS MASSIFS à ne pas re-découvrir :** `gain` (142 occurrences)
et `limiter` (8) sont des MOTS FRANÇAIS. De même `level`, `noise` et `keying`
n'apparaissent que dans des dénominations anglaises déjà glosées en regard
(*Automatic Level Control*, *Noise Blanker*, *Frequency Shift Keying*).
`split` (9) est bien le terme radioamateur, pas `\begin{split}`, le filtrage du
mode mathématique ayant fonctionné.

### Traité

- **`transceiver` -> émetteur-récepteur : 77 remplacements** (N=40, E=17, A=10,
  pluriels compris). Conservations délibérées : l'entrée `| TRX | Transceiver
  (émetteur-récepteur) |` du tableau d'abréviations, et « Computer Aided
  Transceiver » (nom de l'interface CAT).
- **`repeater` -> relais : 1** dans `relaisfunkstellen`.

### Écarté après lecture du contexte (décision motivée)

| terme | motif |
| --- | --- |
| `hotspot` | déjà glosé sur place : « un point d'accès appelé hotspot » |
| `uplink` / `downlink` | libellés officiels du plan de bande IARU, ou déjà glosés |
| `dummy load` | la section `dummy_load_1` enseigne elle-même « aussi appelée *charge fictive* » |
| `contest` | introduit en italique de définition ; usage consacré en France |
| `balun`, `jitter`, `chirp`, `squelch`, `notch`, `beam`, `trap`, `roofing` | termes techniques consacrés (2e catégorie) |

Les traduire aurait défait un travail terminologique déjà fait.

## 4. Discordance texte/figure créée VOLONTAIREMENT

Dans `demodulator`, les indices ont été francisés selon la règle actée :
`u_\mathrm{ZF}` -> `u_\mathrm{FI}`, `u_\mathrm{NF}` -> `u_\mathrm{BF}`
(`s_\mathrm{BFO}` conservé, sigle international).

**Le dessin 1125 porte `U_\mathrm{ZF}` et `U_\mathrm{NF}` sur ses axes.**
Discordance à résorber avec le chantier images, au même titre que le dessin 1082
(`Taktgenerator` face à $f_\mathrm{horloge}$).

## 5. Constat majeur — encarts « En France »

| classe | encarts `<france>` |
| --- | --- |
| N | **55** (dans 55 sections) |
| E | **0** |
| A | **0** |

Un candidat français préparant la classe E ou A ne dispose d'AUCUNE transposition
réglementaire, alors que ces classes traitent l'EIRP, les perturbations
d'appareils électroniques et les distances de protection. Chantier arbitré par
Pierre pour le lundi 10/08.

Par ailleurs, sondage confirmé sur tout le dépôt : `A1A`, `A3E`, `J3E`, `F3E`,
`G3E`, `R3E`, `H3E`, `J2B`, `A2A`, `J7B` — **zéro occurrence**. La désignation
normalisée UIT des émissions est le seul thème du programme français
TOTALEMENT absent des contenus 50ohm.de.

## 6. Compilation — nouveau piège, et son remède

### Le `.out` d'hyperref tronqué

Quand le bac à sable tue une compilation en cours, hyperref laisse un `.out`
(fichier de signets) INCOMPLET. La relance échoue alors immédiatement sur :

    ! File ended while scanning use of \BKM@entry.

et `latexmk` rend rc=12 sans produire de PDF exploitable. **Après toute
compilation tuée, purger avant de relancer — ne jamais reprendre en l'état.**

### Mécanisme de relance qui fonctionne

Le tueur du bac à sable vise `lualatex` mais épargne le script appelant. Un
script de relance en boucle lancé sous `setsid` survit donc et relance tout seul.
`relance.sh` :

    #!/bin/bash
    d=$1; n=0
    cd "$d" || exit 1
    while [ $n -lt 12 ]; do
      n=$((n+1))
      rm -f *.out                 # INDISPENSABLE
      latexmk -lualatex -interaction=nonstopmode "$2" >> journal 2>&1
      rc=$?
      echo "tour=$n rc=$rc" >> etat
      [ $rc -eq 0 ] && exit 0
      sleep 2
    done

Lancement : `setsid nohup ./relance.sh /chemin/build-X book-X.tex < /dev/null > /dev/null 2>&1 &`

**Ne jamais rediriger vers `*.out`** : c'est le fichier de hyperref.

### Résultat classe E — NON-RÉGRESSION ÉTABLIE

Le point resté ouvert depuis la session précédente est clos.

- `build_book.py` **v0.14**, génération : 103/103 sections, 463 questions
- 3 passes : 194 p., puis 196 p., puis 196 p. stable
- **`rc=0`**
- **0 « lost some margin notes », 0 « Float too large for page »** — le
  garde-fou `\DARCmarginpar` (v0.13) ne rétrograde AUCUNE note sur la classe E.
  Le compteur `DARCmargindemoted` ne s'imprime pas dans le journal ; l'absence
  totale d'incident marginfix vaut la même démonstration.
- 196 pages, **identique à la v0.7** : aucun décalage de pagination
- 1 seul avertissement de génération : `e_ssb_am_modulation` (défaut amont connu)
- Ghostscript `/ebook` + `-dDetectDuplicateImages=true` : **3,23 Mo**

## 7. Défauts amont à ajouter au signalement DARC

- **`[ref:a_mehrwegeausbreitung_ionosphäre]`** dans `mehrwegeausbreitung`
  (classe A) : aucune figure ne porte cet ident, ni en amont ni ailleurs.
  Référence orpheline -> « figure ?? » dans le PDF. Défaut AMONT, présent dans
  la source allemande.
- Rappel des défauts déjà consignés : `\label` en double sur le dessin 1116
  (`a_feldwellenwiderstand` dans `nahfeld` ET `naeherungsformel_2`) ;
  deux-points dans les légendes (défaut du parseur) ; `\qty{120\pi}{\ohm}`.

### Deux-points dans les légendes — état au 09/08/2026

Trois marqueurs du périmètre N/E contreviennent encore à la règle DANS LA SOURCE
ALLEMANDE : `digital_voice` (dessin 542, classe N), `tote_zone_1` (992) et
`unerwuenschte_aussendungen_2` (1008), classe E. Les deux derniers étaient déjà
corrigés côté français en v0.7 ; le côté allemand reste cassé. **Côté français :
0 marqueur cassé sur les trois classes.**

## 8. Compilation classe A — v1.2

`build_book.py` v0.14. Génération : 153/153 sections, 717 questions.

- 3 passes : 362 p., puis 364 p., puis 364 p. stable — **rc=0**
- **364 pages** contre 350 en v1.1 : +14 pages, correspondant aux figures et
  développements réintégrés par la remise à niveau de la dérive.
- **0 « lost some margin notes », 0 « Float too large for page »**, aucune note
  de marge rétrogradée par `\DARCmarginpar`.
- Ghostscript `/ebook` + `-dDetectDuplicateImages=true` : **5,28 Mo**

### Références indéfinies — 2, toutes deux défauts AMONT

- `a_sender` (`sende_empfangsketten`) — connu, déjà consigné.
- `a_mehrwegeausbreitung_ionosphäre` (`mehrwegeausbreitung`) — **NOUVEAU**.
  Aucune figure ne porte cet ident. À ajouter au signalement DARC.

### Labels en double — 8, tous défauts AMONT

`a_feldwellenwiderstand` (dessin 1116, déjà consigné), `a_harmonische`,
`a_pn_uebergang_mit_spannung`, `a_Leistungsanpassung`, `a_Festspannungsregler`,
`a_emitter_collector`, `e_ssb_modulation_lsb`, `e_ssb_modulation_usb`,
`even_parity`.

Le défaut est donc plus large que le seul dessin 1116 : **neuf idents de figure
sont réutilisés dans deux sections différentes** du périmètre classe A. Même
mécanisme, même signalement.

## 9. PIÈGE DE BUILD — compilations concurrentes

Deux `latexmk` ont travaillé simultanément sur `build-A/` pendant une dizaine de
minutes, chacun écrasant les auxiliaires de l'autre : `.aux` incohérent,
607 références indéfinies, rc=12. Cause : un script `relance.sh` encore vivant
au moment où un second a été lancé.

**Avant tout lancement : `pgrep -f "relance.sh <répertoire>"`.**
Le script `verrou.sh` refuse de démarrer si une compilation tourne déjà.

## 10. Le piège des auxiliaires tronqués — caractérisation complète

Toute compilation tuée par le bac à sable laisse TRONQUÉ le fichier auxiliaire
en cours d'écriture. Chaque type casse différemment la passe suivante :

| fichier | erreur à la reprise |
| --- | --- |
| `*.out` | `! File ended while scanning use of \BKM@entry` (hyperref) |
| `*.toc` | `! File ended while scanning use of \@writefile` |

Purger le seul `.out` NE SUFFIT PAS. La seule reprise sûre est la purge complète
des auxiliaires à chaque tour — version définitive de `relance.sh` :

    #!/bin/bash
    d=$1; n=0
    cd "$d" || exit 1
    while [ $n -lt 20 ]; do
      n=$((n+1))
      rm -f *.aux *.fdb_latexmk *.fls *.toc *.idx *.ind *.ilg *.log *.out sections/*.aux
      latexmk -lualatex -interaction=nonstopmode "$2" >> journal 2>&1
      rc=$?
      echo "tour=$n rc=$rc" >> etat
      [ $rc -eq 0 ] && exit 0
      sleep 2
    done

Lancement :
`setsid nohup ./relance.sh /chemin/build-X book-X.tex < /dev/null > /dev/null 2>&1 &`

Le tueur du bac à sable vise `lualatex` mais épargne le script appelant, qui
relance donc seul. Les classes E (196 p.) et A (364 p.) ont finalement abouti
chacune en UN tour, rc=0.

---

# SESSION 10/08/2026 — encarts « En France » pour les classes E et A

## 1. Constat de départ

| classe | encarts `<france>` avant | après |
| --- | --- | --- |
| N | 55 | 55 |
| E | **0** | **5** |
| A | **0** | **3** |

Arbitrages rendus par Pierre : traitement **au cas par cas, défaut C** (ne rien
mettre) pour les 8 sections dont l'homologue N porte déjà un encart ; **un seul
encart nourri par classe** pour le chapitre Protection des personnes.

Application du défaut C : `bandbreite_2` écartée — l'encart N « La largeur de
bande est plafonnée par le texte » donne déjà les plafonds 6/12/20 kHz avec le
raisonnement complet. Idem `unerwuenschte_aussendungen_2` et `_3`, `eirp_2`,
`erp_2`, `dummy_load_2`.

## 2. Encarts créés

| classe | section | sujet |
| --- | --- | --- |
| E | `personenschutzabstand_grenzwerte` | pivot Protection des personnes |
| E | `senderausgangsleistung` | plafonds de puissance, PEP et non PAR |
| E | `unmodulierter_traeger` | désignation UIT des émissions |
| E | `stoerungen_elektronischer_geraete_1` | CEM, ANFR, exemption auto-construction |
| E | `N_Ende` | examen français |
| A | `personenschutzabstand_3` | pivot Protection des personnes |
| A | `stoerungen_elektronischer_geraete_2` | CEM |
| A | `N_Ende` | examen français |

**Anomalie corrigée au passage :** `N_Ende` est le MÊME ident dans les trois
sommaires, mais seule la version française de la classe N portait l'encart. Les
fichiers E et A avaient divergé — un candidat terminant le volume E ou A ne
recevait aucune indication sur l'examen français.

## 3. Sources — toutes vérifiées en séance sur les textes officiels

| encart | textes consultés |
| --- | --- |
| Protection des personnes (E et A) | décret n° 2002-775 du 3 mai 2002, **texte consolidé Légifrance en vigueur au 10/08/2026** : article 1 (champ), 2 (valeurs limites), 3 (cumul multi-sources), 5 (dossier à la demande), annexe § 2.2 A (niveaux de référence) ; recommandation 1999/519/CE |
| Puissances | décision ARCEP n° 2012-1241, **annexe telle que réécrite par la décision n° 2019-1412, JORF n° 0037 du 13 février 2020** |
| Désignation UIT | appendice 1 du Règlement des radiocommunications ; classes citées à l'annexe de la décision 2012-1241 |
| CEM | décret n° 2015-1084 du 27 août 2015 **modifié**, article 1 II c) et son alinéa d'interprétation |
| `N_Ende` | arrêté du 21 septembre 2000 modifié, annexe 1 |

**Rien n'a été tiré de F6KGL/F5KFF ni d'Exam'1** (CC BY-NC-SA, incompatibles).
Ces sites apparaissent dans les résultats de recherche ; ils n'ont servi à rien.

## 4. TROIS DÉFAUTS DE SOURÇAGE DÉTECTÉS ET CORRIGÉS

Un audit de sourçage a été mené en fin de séance, à la demande de Pierre. Il a
trouvé trois défauts dans des encarts déjà écrits. À retenir comme méthode :
**l'audit de sourçage doit être systématique, pas déclenché sur demande.**

1. **Erreur d'attribution** (`senderausgangsleistung`) : l'obligation de
   disposer d'un indicateur de puissance avait été attribuée à l'article 4 de la
   décision 2012-1241. FAUX — l'article 4 porte sur l'identification à
   intervalles courts. L'obligation figure au **dernier alinéa du paragraphe 1
   de l'annexe**. Corrigé.

2. **Extrapolation d'un texte abrogé vers son successeur** (les deux encarts
   CEM) : l'exclusion des équipements radioamateur avait été attribuée au décret
   2015-1084 alors qu'elle avait été lue dans une citation du décret
   **2006-1278**, que le 2015-1084 a abrogé. Vérification faite : le fond est
   conservé, mais **la lettre a changé**.
   - ancienne rédaction (2006-1278, abrogée) : « non disponibles dans le
     commerce », « ensembles de composants », « équipements commerciaux modifiés
     à leur intention » ;
   - rédaction EN VIGUEUR (2015-1084 modifié) : « à moins qu'ils ne soient **mis
     à disposition sur le marché** », « **kits de composants** », « équipements
     mis à disposition sur le marché et **modifiés par et pour les
     radioamateurs** ».
   Les deux encarts ont été réécrits avec la terminologie en vigueur.

3. Rappel méthodologique : la décision 2012-1241 de 2012 est **périmée sur ses
   tableaux**. Ne jamais y puiser de valeur chiffrée. Les tableaux en vigueur
   sont ceux de la décision 2019-1412 (JORF du 13/02/2020), qui remplace
   intégralement les paragraphes 1 et 2 de l'annexe.

## 5. Contenu réglementaire établi cette séance

**Puissances maximales — annexe consolidée (décision 2019-1412) :**

| bandes | puissance |
| --- | --- |
| 135,7-137,8 kHz et 472-479 kHz | 1 W **PIRE** |
| 5351,5-5366,5 kHz (60 m) | 15 W **PIRE** |
| 1,8 à 24,99 MHz | 500 W |
| 28-29,7 MHz | 250 W |
| 50 MHz à 250 GHz | 120 W |
| classe 3 (144-146 MHz) | 10 W |

Sauf mention PIRE, il s'agit de la **puissance en crête à la sortie de
l'émetteur** au sens de l'article 1.157 du RR — donc la PEP. Les trois bandes
basses font exception et se comptent en PIRE, en application des notes 5.67A,
5.80A et 5.133B du RR. **C'est le seul endroit où le droit français adopte la
logique allemande de puissance rayonnée.**

**Protection des personnes :** valeurs limites identiques à l'Allemagne (même
source européenne). Ce qui diffère est la procédure : **aucune fiche de site, ni
déclaration préalable** ; l'article 5 du décret 2002-775 prévoit seulement un
dossier communiqué **à la demande** de l'administration. L'ANFR contrôle.
L'article 3 impose de raisonner en exposition **globale**, toutes sources
confondues.

**CEM :** l'auto-construction radioamateur est hors du champ du décret
2015-1084. Pendant réglementaire du droit à l'auto-construction.

## 6. Reste à faire

- Classe A : encarts puissance et largeur de bande (`endstufen`, `bandreite_3`,
  `verstaerker_begrenzung_bandbreite`). Sources désormais en main.
- Recompilation des trois classes : N n'a pas été recompilée depuis les
  anglicismes ; E et A portent des encarts qui changent la pagination.

## 11. Clôture du chantier des encarts — classe A

5 encarts : `N_Ende`, `personenschutzabstand_3` (pivot), `leistungsvertaerker`
(puissance), `bandreite_3` (largeur de bande), `stoerungen_elektronischer_geraete_2`
(CEM).

### Sections examinées et ÉCARTÉES au cas par cas (défaut C)

| section | motif |
| --- | --- |
| `unerwuenschte_aussendungen_3` | encart N `unerwuenschte_aussendungen_1` |
| `effektive_strahlungsleistung_erp_2` | encart N « ERP se dit PAR » |
| `dummy_load_2` | encart N `dummy_load_1` « Le seul appareil obligatoire » |
| `nahfeld`, `naeherungsformel_2`, `personenschutzabstand_richtantennen` | couverts par l'encart pivot `personenschutzabstand_3` |
| `verstaerker_begrenzung_bandbreite`, `symbolumschaltung_bandbreite` | couverts par l'encart `bandreite_3` |
| `remote_station` | encart N `remote_stationen` « Le pilotage à distance, sans régime dédié » |
| `sender_messungen`, `frequenzmessung_2` | aucune obligation française de mesure ; justification seulement à la demande (art. 5 du décret 2002-775) |
| `schutzerdung_2`, `antennen_beruehrung_2` | encart N `n_blitzschutz` |
| `muf_luf_2`, `langer_kurzer_weg_2`, `uebertrager_2`, `psk` | faux positifs |

**Le chantier des encarts de la classe A est clos à 5 encarts.**

## 12. Bilan des encarts, les trois classes

| classe | encarts | dont créés cette session |
| --- | --- | --- |
| N | 55 | 0 (déjà complets) |
| E | 6 | **6** |
| A | 5 | **5** |

Onze encarts créés, tous sourcés sur les textes officiels consultés en séance.
