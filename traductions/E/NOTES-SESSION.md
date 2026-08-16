# Notes de session — classe E, chapitres 1–16 (v0.6)

## SESSION 15/08/2026 — version a.2, francisation des dessins (feuille d'arbitrage nº 3)

Génération : 103/103 sections, 463 questions, 72 dessins francisés,
6 encarts « En France ». **214 pages**, 3,14 Mo après Ghostscript.

Contrôles du §4 : tous conformes (0 · 0 · 0 · 0), 0 erreur LaTeX,
**1 référence « ?? »** (défaut amont connu, `e_ssb_am_modulation`),
0 question séparée de ses réponses.
Clamps : 288 figures, 5 tableaux, 3 formules — **identiques au 14/08**.

### Dessins traités — 23 fichiers

**4 forks portaient encore de l'allemand**, donc visibles dans le PDF a.2
livré : 411 (`ylabel=Wert`), 439 (`Kabel 1`/`Kabel 2`), 997 (`Distanz [km]`,
dans un pgfplots de 16 947 lignes), 1010 (`Temps [Stunden]`).

**19 dessins forkés pour la première fois.** Les plus parlants : 866
(`Langwelle`/`Mittelwelle` → ondes longues / ondes moyennes, et quatre `ca.` →
`env.`), 903 (`Eingangssignal`, `Frequenzgemisch` → mélange de fréquences), 96
(`Digitale Signalverarbeitung` → traitement numérique du signal, sur deux nœuds
séparés), 1008 (`Oberwellen`), 1055 (`1./2. Mischer`), 590 (`Mischer`,
`Demodulator`), 354 et 355, 650 (`mech.` → `méc.`), 745, 311, et les huit
dessins de puissance 250–259 · 592 · 594 (`Leistung`).

**666 : « CCathode »** — même défaut qu'en classe N, corrigé de même. Voir
`docs/defauts-amont.md` §5.

### Le fork de 16 947 lignes pour un mot

Le dessin 997 avait été forké le 14/08 pour traduire « Höhe » seul ; son axe
des abscisses portait encore `Distanz [km]` à côté d'un axe `Hauteur [km]`.
C'est l'illustration la plus nette du coût du fork consigné au §4 de
`docs/ANALYSE-DESSINS.md` : le fichier est énorme, la correction tient en un
mot, et rien n'avait signalé l'incohérence.

### Correctif du 15/08/2026 (fin de session) — le symbole « ü » remplacé par « m »

Découvert en vérifiant la cohérence entre les dessins 260/303/315, qui venaient
de passer à « m », et le texte qui les commente.

Un `ü` **nu** en mode mathématique est composé dans l'italique mathématique, qui
n'a pas le glyphe accentué : il **disparaît du PDF sans erreur de compilation**.
Le défaut était consigné depuis la a.1 pour `antennenformen_3` — mais il touchait
en réalité **cinq sections et 18 occurrences**, mesurées au journal :
`Missing character U+00FC` sortait **17 fois en classe A et 5 fois en E**.

Le cas le plus grave n'était pas celui qui avait été relevé. Dans
`uebertrager_2`, **la formule centrale du chapitre sur les transformateurs
s'imprimait sans son membre de gauche** :

```
Dans la classe E, nous avons déjà rencontré la formule du rapport de transformation :
    𝑁𝑃   𝑈𝑃  ==
    𝑁𝑆   𝑈𝑆
```

Et `antennenformen_3` donnait « un transformateur ayant un rapport de spires
**()** de 1:7 » — deux parenthèses vides.

Dérogation à la règle « formules `$…$` verbatim » du §5, assumée par Pierre, et
cohérente avec la décision du même jour sur les dessins : sans elle, le livre
aurait eu des figures disant « m » et un texte ne disant rien.

Le remplacement n'a eu lieu **que dans les spans `$…$`**, avec vérification
automatique que les `ü` hors math sont intacts avant écriture — le commentaire
allemand `% TODO: … prüfen` et l'ident de photo `Brückengleichrichter` sont
préservés, comme l'impose le §6.

**Vérifié après recompilation** : `Missing character U+00FC` tombe à **0** sur
les deux classes ; le PDF de E porte 9 « m » italiques mathématiques. Les
quatre `ü` qui subsistent dans le PDF de E sont légitimes et se composent
correctement — « Türöffnertag », « Bundesamt für Strahlenschutz » (deux fois) et
la rubrique « Prüfung », des noms propres allemands cités dans le texte
français, en mode texte où le glyphe existe.

Pagination inchangée : E 214 p., A 376 p. Contrôles du §4 conformes.

### Titres des pièces liminaires

Arrêtés le 15/08/2026 : « Avant-propos **du traducteur** » et « Remerciements
**du traducteur** », pour distinguer ces deux pièces, qui sont de Pierre, des
textes du DARC qui composent le reste du livre. Changement porté dans
`compiler.bat` ; **il ne s'appliquera qu'à la prochaine recompilation**, les
livres de cette session ayant été compilés avant l'arbitrage.

### Feuille d'arbitrage nº 4 — relecture de la classe E (15/08/2026, soir)

Dix points relevés par Pierre sur le livre E dans `Préparation_Version_a.2.txt`.
Tous reproduits, leur cause mesurée, et leurs équivalents cherchés en N et A.
**Deux points sur dix seulement étaient des réglages de classe** ; ce sont eux
qui ont imposé la recompilation des trois livres.

| décision | objet |
| --- | --- |
| **A4** | espace avant `!` et `?` — **rien changé**. Mesuré : babel donne 0,5 unité avant `; ! ?` et 1,0 avant `:`, ce qui EST la règle de l'Imprimerie nationale. Ce n'était pas un bogue |
| **B1** | nombres gras dans les énoncés — `build_book.py` v0.19 |
| **C1b** | dessin 942, libellés sur deux lignes |
| **C2b** | dessins 911 et 96, texte sur trois lignes, boîte élargie |
| **C3a** | dessin 666, « Anode » et « Cathode » en entier |
| **C4** | dessins 434-437, français fautif corrigé puis libellés ancrés à l'est |
| **D1** | `spannungsteiler_1`, point parasite retiré ; les 42 absences de point devant une formule restent, usage allemand |
| **E** | abréviation « OW » conservée, les légendes françaises l'emploient déjà |

### Le vrai diagnostic de B1 n'était pas celui de la feuille

La feuille proposait de « passer les énoncés en version mathématique grasse ».
En ouvrant le `.sty` amont, il s'est avéré que **le DARC le demande déjà** :
`\newkomafont{questiontext}{\bfseries\boldmath}`. Le fautif n'était pas la
définition de la question mais la **configuration des polices** —
`settings.tex` charge `unicode-math` sans jamais déclarer de version
mathématique grasse, si bien que `\boldmath` restait sans effet **et sans le
moindre avertissement**.

Le défaut touchait **418 énoncés** : N 102, E 122, A 194, soit un sur quatre.
Correctif en une ligne, vérifié sur document réduit puis dans le livre.

### Deux défauts trouvés en cherchant les équivalents en N et A

1. **Dessins 436 et 437 (classe A)** : le livre affichait « 1/2 **le Longueur**
   d'onde » et « **le Fréquence** perturbatrice ». Substitution mot à mot du
   14/08, `der` rendu par « le » sans accord ni minuscule. Pierre ne l'avait pas
   signalé.
2. **Le chevauchement du texte sur le circuit**, dans les quatre réponses
   illustrées de la question AF223. Il préexistait, un peu moins marqué ; la
   correction grammaticale, plus longue, l'a rendu criant. Corrigé en ancrant
   les libellés à l'est : le texte croît vers la gauche et ne peut plus
   atteindre le schéma, quelle que soit sa longueur.

### Ce que cette relecture a appris sur mes propres contrôles

**Mon audit du matin cherchait de l'ALLEMAND résiduel.** Les libellés « le
Longueur d'onde » n'en contiennent aucun : ils sont en français fautif, et
passaient donc au travers. Une seconde sonde, écrite après coup, cherche un
article français suivi d'un nom commun à majuscule ; elle sort 4 cas, tous en
classe A.

**Trois fois dans la journée, une conclusion tirée du SOURCE s'est révélée
fausse à l'écran** : le `rc=0` de `sonde_dessins.py` le matin, l'aide-mémoire du
dessin 666 qualifié à tort de défaut amont, et le chevauchement de AF223 que
l'extraction de texte ne montrait pas — `pdftotext` n'extrait rien de ces
quatre figures. La seule vérification qui tranche est **la page ouverte**.

### Résultats

N 258 p. · E 214 p. · A 376 p., pagination inchangée. Contrôles du §4 conformes
sur les trois, `??` à 0 · 1 · 3, aucune question coupée. Les pièces liminaires
portent désormais « du traducteur ».

### Édition combinée NEA — première compilation (15-16/08/2026)

**806 pages**, 384 sections, 1 751 questions, 805 dessins distincts. Contrôles du
§4 conformes du premier coup ; 4 références « ?? », soit les quatre orphelines
amont cumulées. Les compteurs de clamp s'additionnent proprement (948 figures,
10 tableaux, 7 formules) : aucun dessin n'est traité différemment en combiné.

Durée : environ 1 h 15 pour cinq passes, contre 50 min pour la classe A seule.

### Ordre des `--translations` : `A` d'abord

Décision de Pierre : la version de la classe la plus avancée l'emporte. **La
portée du choix a été mesurée avant de trancher, et elle est étroite :**

- **une seule section** est traduite dans plusieurs classes — `N_Ende`
  (« Conclusion du cours »), présente dans les trois. C'est du contenu
  **français**, pas une traduction de l'amont : les trois versions renvoient
  chacune à l'examen de leur classe. La version N dit « il n'existe pas de
  premier échelon équivalent », la E « il n'existe pas d'échelons » et ajoute
  trois points du programme français sans équivalent allemand ;
- **20 dessins forkés** sont partagés entre classes, mais **tous identiques au
  contenu**. Deux d'entre eux, 354 et 935, sont sortis « différents » d'une
  comparaison par empreinte : ils ne diffèrent en réalité que par leurs fins de
  ligne, CRLF contre LF. L'ordre n'a donc aucun effet sur les dessins.

Un document de comparaison des trois versions de `N_Ende` a été produit pour
la décision, chaque version sur sa page avec sa classe en titre courant.

### `vorwort` n'est pas dans le NEA

La section est traduite (`traductions/N/sections/vorwort.md`) et figure dans le
livre N, mais le sommaire amont du NEA ne l'appelle pas : **l'édition combinée
perd l'avant-propos allemand**. C'est ce qui explique l'écart de comptage — 385
idents distincts traduits pour 384 sections composées — et c'est aussi
l'origine de l'avertissement « clé *vorwort* n'est pas un ident connu » émis
par `titles.json` à chaque compilation NEA.

### Filigrane de la page de titre — `build_book.py` v0.20

Relevé par Pierre : dans le bandeau de droite, « NEA » à plat est illisible. La
mesure sur épreuve a montré pire que « trop étroit » — **le N mordait sur la
zone blanche à gauche et le A était coupé au bord droit de la page**, alors même
que la v0.9 avait déjà réduit le corps à 105 pt.

L'ancien gabarit ne pouvait faire varier que le corps et le texte, jamais
l'ancrage ni la position : il était structurellement incapable de loger trois
lettres. Le nœud entier est désormais construit côté Python.

Trois dispositions ont été composées et comparées sur épreuve — à plat, pivotée
à 90°, empilée. **Pierre a retenu l'empilement** : une lettre par ligne, 150 pt,
centrées sur l'axe du bandeau et calées en haut. Chaque lettre reste lisible à
l'endroit. Une lettre seule ne change pas.

---

## SESSION 14/08/2026 — version a.2 (build_book.py v0.18)

Génération : 103/103 sections, 463 questions traduites, 42 dessins francisés,
6 encarts « En France ». **214 pages** (206 en a.1), 3,00 Mo après Ghostscript.

Contrôles du §4 : tous conformes (0 · 0 · 0 · 0). Aucune référence indéfinie
au-delà du défaut amont connu.

| mesure | a.1 | a.2 |
| --- | ---: | ---: |
| plus grand débordement horizontal | 103,6 pt | **11,3 pt** |
| débordements > 20 pt | 8 | **0** |
| pages « Underfull \vbox » | 41 | **0** |
| questions séparées de leurs réponses | non mesuré | **0 sur 462** |
| dessins affichant de l'allemand | 21 | **10** |

Clamps déclenchés : 288 figures, 5 tableaux, 3 formules.
11 dessins forkés et traduits (total : 53).

**Le plus gros débordement, 103,6 pt, n'était pas une figure** mais le tableau
`{ll}` des désignations d'émission de `unmodulierter_traeger` (page 121) : deux
colonnes de largeur naturelle dont la seconde porte de la prose. Il débordait
déjà à l'identique en a.1 — au centième près, ce qui a mis sur la piste.

**Cinq dessins forkés portaient encore de l'allemand** (439, 741, 991, 1022,
1024) : `Verstärkung`, `Frequenz`, `Bodenwelle`, `Raumwelle`. Traduits avec le
vocabulaire déjà en usage. La sonde retourne désormais 0.

**Reste 21 dessins non forkés affichant de l'allemand** — chantier de
francisation, pas un défaut.

**`widerstand_materialien` — corrigé (B2).** Ce `{lX}` débordait de 28 pt et
échappait au clamp : `tabularx` fixe la largeur du tableau à `\linewidth`, donc
la mesure le voit toujours conforme. La cause était la **traduction** — sa
colonne rigide portait « Résistances à couche d'oxyde métallique »
(39 caractères) là où l'allemand tenait en 28 avec
« Metalloxidschichtwiderstände ». Première colonne passée en `X` : plus aucun
débordement, sans toucher au texte. La limite du clamp reste vraie en général,
mais ces cas se corrigent à la source.

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

- Chapitres 1–2 : COMPLETS (15 sections + N_Ende, 46 questions,
  3 volets de titles.json). Vérifié programmatiquement (structure DARCdown
  identique à l'allemand, sondes pdftotext du PDF final toutes OK).
- Les 15 corps de sections étaient déjà présents en début de session
  (synchronisation résiduelle du stockage partagé / session parallèle,
  origine non élucidée) ; ils ont été relus INTÉGRALEMENT contre l'allemand
  et validés — aucun correctif nécessaire.
- Chapitres 3, 4 et 5 : TRADUITS, LIVRÉS POUR RELECTURE. Détail :
  - Ch. 3 (Strom, Spannung, Widerstand, Leistung, Energie) : 10 sections,
    48 questions (15 complètes / 33 énoncé seul).
  - Ch. 4 (Elektromagnetisches Feld) : 3 sections, 15 questions (10 / 5).
  - Ch. 5 (Bauelemente) : 5 sections, 60 questions (44 / 16).
  Total livré cette session : 18 sections, 123 questions, 3 chapitres dans
  les 3 volets de titles.json. Validation structurelle regex OK (comptage +
  ordre des marqueurs identiques à l'allemand sur les 18 sections) ; sonde
  anti-germanisme OK sur tous les corps. questions.json = 169 entrées ;
  titles.json = 5 chapitres / 5 abstracts / 34 sections. PAS ENCORE compilé.
  Nouvelles balises/marqueurs rencontrés (ch. 4–5) à couvrir au build :
  `<unit>` (Neue Einheit→Nouvelle unité), équations de Maxwell (vecteurs),
  `\qtyrange{}{}{}`, `\num{}`, notation `\qty{...e-11}{...}`, symbole `ü`
  (rapport de transformation, conservé verbatim), `<u>...</u>` dans un énoncé
  (EC205), ident de figure contenant des espaces (`e_Trafo mit getrennten
  Wicklungen`, préservé verbatim), macro `\milliOhm` dans une réponse-leurre
  (EC521, conservée verbatim). `<warning>` (ch. 3) et `[table:…]` déjà notés.
- Chapitre 6 (Reihen- und Parallelschaltung von Bauelementen) : TRADUIT,
  LIVRÉ POUR RELECTURE. 4 sections, 24 questions (1 complète : ED107 ;
  23 énoncé seul — réponses purement numériques). Validation structurelle
  regex OK (lignes commentées exclues du comptage), sonde anti-germanisme OK.
  questions.json = 193 entrées ; titles.json = 6 chapitres / 6 abstracts /
  38 sections. Particularités préservées verbatim : ident de figure
  `E 63. Spannungsteiler` (avec espaces/point), ident photo
  `a_Netzteil BEKO PA $7 \times \qty{10000}{\micro\farad}$ parallel`
  (maths dans l'ident), gros bloc d'aides de solution commenté
  (`%<margin>…%</margin>`, 14 lignes, laissé en allemand car commenté),
  commentaire `% TODO implementiere Attention in CSS!`.
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
- Chapitres 8 (Grundlegende Schaltungen → Circuits fondamentaux, 6 sections)
  et 9 (Modulation, 5 sections) : TRADUITS, LIVRÉS POUR RELECTURE.
  66 questions référencées, dont ED216 déjà traduite au ch. 5 (entrée
  existante conservée telle quelle) → +65 entrées : 53 complètes /
  12 énoncé seul (images vides : ED210, ED213, EF307, EE101 ; numériques
  pures : EF301–EF303, EE203, EF310 ; acronymes : EE301, EE303, EF306 —
  noms d'appareils anglais). Règle « und »→« et » appliquée (forme
  complète) : EF201–EF205, EE204. questions.json = 264 entrées ;
  titles.json = 9 chapitres / 9 abstracts / 53 sections.
  Validation structurelle regex OK sur les 11 sections (comptage + ordre,
  légendes picture/photo normalisées sur type:id:ident, lignes % exclues) ;
  sonde anti-germanisme OK (homographe fr « des » exclu de la liste ;
  gloses allemandes volontaires entre parenthèses : Schwingkreise,
  Bandsperren, Saugkreis, Sperrkreis, Leitkreis, Konverter,
  Serien-/Reihen-/Parallelschwingkreis).
  Particularités préservées verbatim : `[include:applet_schwingkreis]`
  (×2 : schwingkreis_1, oszillatoren), commentaire `% TODO ////`
  (schwingkreis_1), idents avec fautes allemandes d'origine
  (`e_wiederstaende_tiefpass`, `e_wiederstaende_hochpass`), ident avec
  tréma (`e_frequenzabhängiger_widerstand`), `</indepth>` avec espaces
  finaux (schwingkreis_1 l. 82). NB : ssb_2 référence
  [ref:e_ssb_am_modulation] sans [picture] correspondant dans la section
  (défaut préexistant de la source allemande, laissé tel quel) et contient
  deux [picture] d'idents identiques `e_ssb_einzelsignal` (1056 et 743,
  également d'origine).
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
- Prochaine étape : BUILD v0.5 (ch. 1–12) dans cette session, puis
  relecture PLG ; ensuite chapitres 13 et suivants en SESSION FRAÎCHE,
  par paires avec relecture entre chaque paire. Contrôler par sonde
  pdftotext si la traduction des ch. 10–12 résorbe les pertes marginfix
  connues de vorverstaerker_daempfungsglied (×2, ch. 10).
- BUILD v0.5 (ch. 1–12 traduits) : RÉUSSI (session précédente ; bloc ajouté
  rétroactivement en session 13–16). 209 pages, 0 erreur LaTeX, 1 perte
  marginfix résiduelle limitée à la zone de repli allemand, toutes les
  sondes pdftotext de titres de sections FR passantes.
  Livré : livre-E-fr-v0.5-ch1-12.pdf.
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
- Prochaine étape : relecture PLG des ch. 13–16 et de l'ensemble ;
  Classe E terminée → passer à la Classe A (réutiliser le correctif
  fig202 si le même diagramme y figure).

## RÉGÉNÉRATION v0.7 (classe E, ch. 1–16) avec build_book.py v0.4 — RÉUSSIE

ÉCART DE CONSIGNE À SIGNALER : la consigne de session décrivait la
régénération de la classe **N** ; le zip fourni était celui de la classe **E**
(`traductions-E-16_1.zip`). Le pipeline a été appliqué tel quel à E (seul
matériel disponible, et régénération également prévue au programme). La
régénération N reste À FAIRE, avec le même mode opératoire.

### Objet
Recompilation du livre E avec le script COURANT v0.4 pour corriger les deux
défauts du PDF v0.6 distribué : (1) légendes contenant un « : » qui cassent le
parseur amont et font disparaître silencieusement la figure ; (2) préfixes SI
perdus par la v0.2. Contenu pédagogique inchangé.

### Périmètre vérifié programmatiquement
toc/E.json : 16 chapitres / 103 sections — 103 sections traduites présentes,
aucune manquante, aucune surnuméraire. titles.json = 16/16/103.
questions.json = 462 entrées, 463 usages au build (ED216 référencée deux fois).

### Légendes corrigées (3 marqueurs non rendus signalés par validate_output)
Correction CÔTÉ CONTENU FR uniquement (build_book.py non modifié) :
1. `tote_zone_1.md` [picture:992:e_tote_zone_2d] — « 07:00 UTC » → « 07 h 00 UTC »
   (le « : » venait de l'heure ; présent aussi en allemand → la figure manquait
   également dans le repli allemand).
2. `unerwuenschte_aussendungen_2.md` [picture:1008:e_unerwuenschte_aussendungen_uebersicht]
   — « Émissions non désirées : harmoniques… » → « … non désirées — harmoniques… ».
3. `vna_1.md` [photo:327:e_vna_solt] — « De gauche à droite : Load… » →
   « De gauche à droite — Load… » (l'allemand utilisait « - » ; le « : » avait
   été introduit à la traduction).
Après correction : 0 marqueur non rendu. Seul avertissement restant = la
référence orpheline amont `e_ssb_am_modulation` (ssb_2), défaut connu conservé.

### Résultat de compilation
196 pages A4 (208 en v0.6), **0 erreur LaTeX**, **0 erreur marginfix**,
0 « Rerun », **1 seule référence « ?? »** contre 7 en v0.6 — le passage de 7 à 1
vient de la normalisation SYMÉTRIQUE des `\ref` introduite en v0.4 (les idents
non-ASCII, à tréma, produisaient un `\label` assaini face à un `\ref` non
assaini). Ghostscript /ebook : 246 Mo → 3,23 Mo.

Contrôle de non-régression : les 209 numéros de figure de v0.6 se retrouvent
tous dans v0.7 (comparaison des 25 premiers caractères de chaque légende,
0 manquante), et v0.7 en compte 212 — les 3 figures restaurées. 103/103 titres
de sections et 16/16 titres de chapitres sondés présents. Page de titre saine
(aucun « 14.63995pt » dans le .log). Préfixes SI vérifiés (145 MHz, 583,6 MHz,
µF ; zéro occurrence de « 145 Hz »). Les 31 légendes de marge autrefois perdues
(swr, vna, kabeldaempfung, eirp, grenzwerte, blitz, antennenformen…) sont toutes
présentes.

### Les 3 retouches session-locales sont désormais CADUQUES
build_book.py v0.4 les remplace : `\extrafloats{400}` est injecté
automatiquement (settings-pre.tex) et le clamp de largeur sur `\DARCimage`
supprime la cause racine du bouchon marginfix — le correctif fig202
(précompilation standalone) N'EST PLUS NÉCESSAIRE, et le `\clearpage` autour de
Blitzerdung non plus. Build lancé sans aucune retouche : 0 erreur marginfix.
La baisse 208 → 196 pages s'explique par la suppression de ces `\clearpage` et
par la réduction des figures hors gabarit par le clamp.

### Pièges de build observés cette session (nouveaux)
(a) `latexmk -lualatex` sort en **rc=12** dès la 1re passe si une erreur
    survient, puis se croit à jour (« Nothing to do ») ; `touch` du .tex ne
    suffit pas (latexmk compare des sommes de contrôle). Remède : supprimer
    `book-E.fdb_latexmk` ET utiliser `-f`. Cette session, la convergence a
    finalement été obtenue par **passes `lualatex` unitaires séparées**
    (une par appel bash), la 3e passe consécutive étant tuée par le bac à sable.
(b) **NOUVEAU — le PDF non compressé (246 Mo) a DISPARU du disque après avoir
    été écrit** (« Output written » présent, fichier absent ensuite), et une
    passe antérieure a laissé un `.aux` truffé d'octets NUL (symptôme
    ENOSPC/nettoyage du bac à sable). Remède adopté : enchaîner **dans le même
    script de fond** la passe lualatex ET la compression Ghostscript, de sorte
    qu'un PDF léger (3 Mo) soit produit avant tout nettoyage. Vérifier
    l'intégrité du .aux (`compte d'octets NUL == 0`) avant la passe suivante.
(c) Sondes pdftotext : faux négatifs confirmés sur les légendes contenant des
    maths (`$\frac{\lambda}{2}$`, `\qty`) et sur la césure (« Magnetic-Loop »
    coupé) — sonder par fragments courts et tester les deux formes
    (avec et sans décésure).

### Livré
`livre-E-fr-v0.7-ch1-16.pdf` (196 pages, 3,23 Mo) + zip de traductions E à jour.
### Prochaine étape
Régénérer de même la classe **N** avec v0.4 (fournir le zip N) ; poursuivre la
classe A (lot 5 : chapitre 12 restant).

---

## SESSION 10/08/2026 — encarts « En France » et compilation v0.9

### 6 encarts créés (la classe E n'en avait AUCUN)

| section | sujet |
| --- | --- |
| `personenschutzabstand_grenzwerte` | encart pivot du chapitre Protection des personnes |
| `senderausgangsleistung` | plafonds de puissance : la France plafonne la PEP, pas la PAR |
| `unmodulierter_traeger` | désignation UIT normalisée des émissions |
| `stoerungen_elektronischer_geraete_1` | CEM, ANFR, exemption de l'auto-construction |
| `N_Ende` | examen français (l'encart existait en classe N seulement) |

Arbitrage Pierre : traitement au cas par cas, **défaut C** (ne rien mettre) pour
les sections dont l'homologue N porte déjà un encart. Écartées à ce titre :
`bandbreite_2` (l'encart N donne déjà les plafonds 6/12/20 kHz),
`unerwuenschte_aussendungen_2`, `eirp_2`, `dummy_load_2`.

### Sources — vérifiées en séance sur les textes officiels

- décret n° 2002-775 du 3 mai 2002, **consolidé Légifrance en vigueur au
  10/08/2026** : art. 1, 2, 3 (cumul), 5 (dossier à la demande), annexe § 2.2 A
- décision ARCEP n° 2012-1241, **annexe telle que réécrite par la décision
  n° 2019-1412, JORF n° 0037 du 13/02/2020**
- décret n° 2015-1084 du 27 août 2015 **modifié**, art. 1 II c)
- appendice 1 du Règlement des radiocommunications (désignation des émissions)
- arrêté du 21 septembre 2000 modifié, annexe 1 (programme de l'examen français)

Rien n'a été tiré de F6KGL/F5KFF ni d'Exam'1 (CC BY-NC-SA, incompatibles).

### PIÈGE DE RÉDACTION — le parseur d'unités crée des faux positifs

Découvert par rétro-conversion du LaTeX généré. Le token `Unit` capte
**nombre + lettre**, y compris là où il ne s'agit pas d'une unité :

| écrit | rendu | correction |
| --- | --- | --- |
| « le calcul s'appuie, lui, sur… » | `lui${,}$\,s` -> lu comme SECONDES | reformuler : « s'appuie bien, quant à lui, sur » |
| « notes 5.67A, 5.80A » | `5.$67$\,A` -> lu comme AMPÈRES | reformuler sans la notation collée |
| « bande 60 m » | `$60$\,m` -> mètres | correct ici, mais à surveiller |

**Règle : après rédaction d'un encart, relire le `.tex` généré**, pas seulement
le `.md`. Un `\,` inattendu signale un faux positif d'unité.

### Compilation v0.9 — définitive

- génération : 103/103 sections, 463 questions, 5 encarts rendus,
  1 avertissement (`e_ssb_am_modulation`, défaut amont connu, conservé)
- 3 passes : 198 p., 200 p., 200 p. stable — **rc=0 au premier tour**
- 0 « lost some margin notes », 0 « Float too large »
- Ghostscript `/ebook` : **3,11 Mo**
- **200 pages contre 196 avant les encarts** (+4 pages pour 5 encarts)

### PIÈGE DE BUILD — le gardien nuit aux volumes courts

Le `gardien.sh` (sauvegarde périodique des auxiliaires sains) est
**indispensable pour la classe A** — 10 min par passe, la perte du `.aux` et de
son `\DARCimageCache` condamne toute reprise — mais **contre-productif sur E
et N** : il restaure un `.aux` antérieur, donc des numéros de page périmés, ce
qui relance indéfiniment le cycle. Observé : oscillation 198/200 sans fin.
Sans gardien, sur arbre purgé : rc=0 au premier tour.

**Règle : gardien pour les volumes longs seulement.**

### Deuxième passe d'arbitrage — un encart de plus, et la clôture du chantier

`fm_2` : le texte allemand renvoie aux « prescriptions légales » sans les
chiffrer. Côté français ce sont des valeurs précises, et elles emportent une
conséquence pratique forte — une FM courante (une quinzaine de kHz par Carson)
tient sur 145 MHz mais **dépasse le plafond de 12 kHz sur 29 MHz**, et a
fortiori les 6 kHz en dessous de 28 MHz. C'est la raison pour laquelle la FM ne
se pratique pas en décamétrique hors du haut du 10 m. L'encart donne aussi tout
son sens à l'amplificateur limiteur décrit dans la section.

### Sections examinées et ÉCARTÉES au cas par cas (défaut C)

Deux balayages ont été conduits : par mot-clé normatif allemand (BEMFV, VDE,
AFuV, Grenzwert, gesetzlich…) puis par thème du titre (antenne, terre, sécurité,
mesure, indicatif, satellite…). Toutes les sections restantes ont été écartées,
avec motif :

| section | motif |
| --- | --- |
| `bandbreite_2` | l'encart N « La largeur de bande est plafonnée par le texte » donne déjà 6/12/20 kHz |
| `unerwuenschte_aussendungen_2` | encart N `unerwuenschte_aussendungen_1` |
| `aequivalente_isotrope_strahlungsleistung_eirp_2` | encart N « EIRP se dit PIRE » |
| `personenschutzabstand_2`, `naeherungsformel_1` | couverts par l'encart pivot `personenschutzabstand_grenzwerte` |
| `blitzerdung`, `schutzerdung_1`, `antennen_beruehrung_1`, `statische_aufladung` | encart N `n_blitzschutz` « Les normes NF à la place des normes VDE » |
| `antennengewinn` | encarts N `eirp_1` et `erp_1` |
| `alc` | couvert par l'encart `senderausgangsleistung` |
| `digimode_ssb` | couvert par l'encart `unmodulierter_traeger` (classes d'émission) |
| `spannungsquelle` | sécurité électrique générale, pas de spécificité radioamateur |
| `ionosphaere_2`, `tote_zone_1`, `spitze_effektiv_wert`, `uebertrager_1`, `ueberlagerungsempfaenger_einfachsuper_1` | faux positifs (« erlaubt », « Deutschland » en contexte non normatif) |

**Le chantier des encarts de la classe E est clos à 6 encarts.**

### Encart `unmodulierter_traeger` — version approfondie (10/08, chantier 2)

Sur demande de Pierre, l'encart des classes d'émission a été repris en
profondeur. Il faisait 2 500 caractères, il en fait 7 800.

**Le manque principal était la LARGEUR DE BANDE NÉCESSAIRE.** Une désignation
complète s'écrit `BBBB` + 3 à 5 caractères de classe. La partie largeur de bande
s'exprime par trois chiffres et une lettre, la lettre occupant la position de la
virgule décimale et donnant l'unité (H, K, M, G) ; le premier caractère ne peut
être ni zéro, ni K, M ou G. Sans cela, un candidat lit `J3E` mais pas
`2K70J3E` — c'est-à-dire la moitié du système.

Contenu ajouté :
- tables complétées des trois symboles obligatoires (manquaient B, C, D au
  premier ; 8, 9 au deuxième ; W au troisième)
- **table complète du 4e symbole** (détails du signal, 15 valeurs)
- **table complète du 5e symbole** (nature du multiplexage, 6 valeurs)
- convention du tiret pour marquer l'absence des symboles facultatifs
- **trois formules de largeur de bande** utiles au radioamateur :
  - Morse tout ou rien : `Bn = B·K`, K=5 avec évanouissements, K=3 sans
  - BLU porteuse supprimée : `Bn = M − f_min`
  - FM téléphonie : `Bn = 2M + 2DK` (la formule de Carson sous forme réglementaire)
- douze désignations usuelles, dont J2B (modes numériques) et F2D (packet)
- raccord avec les plafonds français : les 16 kHz d'une FM dépassent les 12 kHz
  applicables entre 28 et 144 MHz

**ERREUR CORRIGÉE :** la première version donnait `150HA1A` pour la télégraphie
Morse. La source officielle donne `100HA1A` — à 25 mots/min, B = 20 et K = 5,
donc Bn = 100 Hz. Le 150H venait de la mémoire, pas d'un texte.

**Source :** circulaire CRT-43 (3e édition, novembre 2012, Innovation, Sciences
et Développement économique Canada), qui reproduit intégralement l'appendice 1
du Règlement des radiocommunications ainsi que ses exemples de désignation et
ses formules de largeur de bande. Consultée le 10/08/2026. Les valeurs y sont
identiques à celles du RR ; le document canadien a l'avantage d'être accessible
en français et in extenso.

**PIÈGE DE RÉDACTION :** toute désignation doit être écrite en `$\mathrm{...}$`.
En texte brut, `2K70J3E` est lu par le parseur DARCdown comme la valeur 2 suivie
de l'unité kelvin. Vérifié sur le `.tex` généré : aucun faux positif.
