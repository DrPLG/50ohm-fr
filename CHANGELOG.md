# Journal des versions

Les versions sont suivies **par classe**, chacune évoluant à son rythme.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).

Rubriques employées : *Ajouté*, *Modifié*, *Corrigé*, *Préservé* (défauts amont
laissés intacts et consignés), *Connu* (limitations non résolues).

---

## a.2 — 14 et 15 août 2026 (en cours)

| Classe | Sections | Questions | Encarts | Dessins forkés | Pages (a.1 → a.2) |
| ------ | -------: | --------: | ------: | ---: | ----: |
| N | 131 | 571 | 55 | 39 | 254 → 258 |
| E | 103 | 462 | 6 | 72 | 206 → 214 |
| A | 153 | 717 | 5 | 111 | 372 → 376 |

Pagination inchangée après la francisation des dessins du 15/08, et compteurs de
clamp identiques à ceux du 14/08 (E : 288 · 5 · 3) — les libellés traduits n'ont
pas dérangé la mise en page.

Effet mesuré des corrections, sur les trois classes :

| mesure | a.1 | a.2 |
| --- | ---: | ---: |
| plus grand débordement horizontal (N · E · A) | 125 · 104 · 200 pt | **20 · 11 · 11 pt** |
| débordements > 20 pt (N · E · A) | 1 · 8 · 17 | **0 · 0 · 0** |
| pages « Underfull \vbox » (total) | 306 | **0** |
| questions séparées de leurs réponses | 19 relevées en N | **0 sur 1 750** |
| figures ramenées dans leur gabarit | 0 | **948** |
| tableaux et formules réduits | 0 | 10 et 9 |
| dessins affichant de l'allemand | 62 | **0** (24 au 14/08, puis 93 mesurés et traités le 15/08) |
| dessins forkés | 126 | **222** |

**Plus aucun débordement au-delà de 20 pt dans les trois livres**, alors qu'il y
en avait vingt-six, dont un à 200 pt.

**Chantier de mise en page**, ouvert après la relecture page à page de Pierre
(une quarantaine de défauts relevés sur les trois livres). Le parti pris a été
de chercher les causes racines plutôt que de retoucher page par page : quatre
corrections de classe, puis deux de plus, ont remplacé l'essentiel des
retouches ponctuelles.

### Ajouté
- **Typographie française** (A1). Les trois livres étaient composés avec la
  césure et les espacements **allemands** : le `.sty` amont fait
  `\PassOptionsToPackage{ngerman}{babel}`, et rien ne l'avait jamais corrigé.
  Mesuré par `\showhyphens` : « ali-men-ta-ti-on », « ray-onne-ment » — des
  coupures allemandes, fautives en français. Corrigé par le mode **moderne** de
  babel (`\babelprovide[import, main, transforms = punctuation.space]{french}`),
  qui insère les espaces fines avant « : ; ! ? » par transformation de nœuds
  LuaTeX, sans rendre aucun caractère actif — contrairement à `french.ldf`,
  dont les catcodes actifs se seraient heurtés à la syntaxe à deux-points de
  siunitx, tcolorbox, circuitikz et pgfplots. Chaque règle pose une pénalité de
  10000 : la ponctuation haute ne peut plus tomber en début de ligne.
  Conventions françaises complètes ajoutées explicitement : puces en tiret
  cadratin, listes resserrées, légendes « Fig. 1 – ».
- **Contrôle exact des questions coupées** (B6) : deux `\label` par question,
  comparés dans le `.aux` par `verifier_questions.py`. Remplace une lecture du
  PDF qui produisait douze faux positifs sur la seule classe N.
- **Sonde anti-germanisme sur les dessins** : `sonde_dessins.py`. Elle sépare
  les dessins **forkés** portant encore de l'allemand — un défaut — des dessins
  **non forkés**, qui sortent tels quels de l'amont et relèvent du chantier de
  francisation.

### Corrigé
- **Clamp de `\DARCimage` : il ne clampait rien** (A2). Il mesurait `\wd` d'une
  boîte contenant déjà le `\makebox[\linewidth]` final de la macro amont ; sa
  mesure valait donc toujours `\linewidth`. Vérifié sur quatre dessins d'essai,
  du minuscule au démesuré : 147,95 pt en marge et 335,74 pt dans le corps,
  sans une seule variation. Pire, dès que la cible était inférieure à
  `\linewidth`, la comparaison était vraie par construction et réduisait une
  figure conforme **au carré du facteur demandé** — une figure appelée à
  `0.5\linewidth` sortait à `0.25\linewidth`. 242 appels étaient concernés.
  La hauteur, elle, n'était comparée à rien. Réécrit : il mesure la boîte de
  l'autoscale amont avant tout `\makebox`, et borne largeur **et** hauteur.
- **Zones de vide** (A3). Le livre composait en `\flushbottom` alors que la
  classe amont fait `\raggedbottom` : le blanc laissé par un objet insécable
  était distribué entre les paragraphes au lieu d'être rassemblé en bas de
  page. 306 pages étaient concernées sur les trois classes.
- **Questions séparées de leurs réponses** (A4). L'énoncé est un paragraphe,
  les réponses un `tabular` insécable, et la boîte est `breakable` : la
  jointure était le seul point de rupture possible. Corrigé par `\samepage`.
- **Tableaux et formules débordant de la colonne de marge** (B1). Une fois les
  figures traitées, 151 des 180 débordements restants étaient du contenu
  insécable dans une colonne de 52 mm — jusqu'à 168,9 pt pour un tableau,
  97,2 pt pour une formule. Clamp analogue à celui des images.
- **Code Morse (classe N)** : quatre des cinq lignes du tableau des caractères
  spéciaux étaient fausses. Détail dans `docs/defauts-amont.md` §4.
- **Douze accolades imprimées** dans les énoncés de questions de la classe N
  (« ne devriez-vous **{pas}** établir… »), présentes depuis la a.1 : du LaTeX
  écrit dans un champ qui traverse le renderer, lequel échappe les accolades.
  Rétabli en markdown.
- **Dix dessins forkés** portaient encore de l'allemand (N 3 · E 5 · A 2),
  traduits avec le vocabulaire déjà en usage dans le corpus.

- **Francisation des dessins : 38 dessins forkés et traduits**, portant le total
  de 126 à 164. Les dessins affichant encore de l'allemand passent de 62 à 24
  (N 4 → 1 · E 21 → 10 · A 37 → 13). Le vocabulaire suit l'usage déjà établi
  dans les sections, relevé par comptage : « intensité de champ » (44 emplois),
  « longueur d'onde » (71), « porteuse » (177), « atténuateur » (36).
  La substitution ne touche **que les textes composés** — contenu de `\node{}`,
  `label=`, `\addlegendentry{}` — jamais le reste du fichier, où « der », « und »
  et « oder » se retrouvent dans des noms de macros et des clés de style. Les
  164 dessins forkés ont été compilés isolément avant toute recompilation :
  zéro erreur.
- **Pièces liminaires renommées** : `avant-propos-N.md` → `avant-propos.md` et
  `remerciements-N.md` → `remerciements.md`. Leur texte ne mentionne aucune
  classe et `compiler.bat` les imposait déjà aux trois : le suffixe `-N` était
  trompeur.
- **Tableau `{lX}` de `widerstand_materialien`** (classe E) : ne déborde plus.
  Sa colonne rigide portait « Résistances à couche d'oxyde métallique »
  (39 caractères) là où l'allemand tenait en 28 ; première colonne passée en
  `X`, sans toucher au texte.
- **Francisation des dessins, achevée** (15/08/2026, feuille d'arbitrage nº 3).
  L'inventaire a été refait par mesure sur la version **réellement composée** de
  chaque dessin — 861 couples (classe, dessin), 418 mots distincts extraits des
  seules zones de texte composé. Il a montré que le périmètre n'était pas de 24
  dessins mais de **93**, et surtout que **39 d'entre eux étaient des dessins
  forkés affichant encore de l'allemand dans les PDF a.2 livrés** :
  `Wert`, `Distanz`, `Mischer`, `Koaxialkabel` ne figuraient dans aucune des
  deux détections de la sonde, qui rendait `rc=0`.
  - Le plus visible : le dessin **1092** composait « 2. AM de 1 : Einton
    moduliert Amplitude de la porteuse ». Le dessin **996**, forké sur
    8 782 lignes, n'avait vu traduire que « Höhe » : sa légende portait encore
    *Winter Nacht, Sommer Tag* et son axe *Distanz [km]* voisinait avec un axe
    *Hauteur [km]*. Les dessins **434** et **435** affichaient « Auf le Signal
    perturbateur abgestimmt », moins lisible que l'allemand d'origine.
  - Traitement par **remplacements littéraux comptés** (chaîne exacte vers
    chaîne exacte, échec fatal sur écart de comptage), et non par substitution
    mot à mot — celle-ci étant justement la cause des libellés mixtes.
  - Dictionnaire établi par **comptage dans les 387 sections traduites**
    (1,94 M caractères) : *mélangeur* 117 contre *mixeur* 0, *atténuateur* 52
    contre *affaiblisseur* 0. `Treiber` → « Étage pilote » et `Stromrichtung` →
    « sens physique du courant » ont été réglés par un précédent déjà composé
    dans les livres, ce qui vaut mieux qu'un comptage.
  - Six arbitrages tranchés par Pierre : `Verbraucher` → charge ·
    `Einton`/`Zweiton` → un ton / deux tons · `Netzteil` → alimentation
    secteur · `Ort` → position · `Langwelle`/`Mittelwelle` → ondes longues /
    ondes moyennes · `Frequenzgemisch` → mélange de fréquences.
  - Deux angles morts trouvés en chemin : le texte en **mode mathématique**
    (dessin **488**, `$\mathrm{Audioverstärker}$`, `NF` passé à `BF`) et le
    **symbole `ü`** du rapport de transformation (dessins 260, 303, 315),
    remplacé par `m`.
  - **222 dessins forkés** au total, tous compilés isolément sans erreur avant
    toute recompilation de livre, tous enregistrés au manifeste (606 éléments
    suivis par `verifier_amont.py`, 0 dérive).
- **« CCathode » corrigé** (dessins 666, classes N et E). Un fork antérieur
  substituait `Kathode` → `Cathode` **puis** `athode` → `Cathode`, la seconde
  règle s'appliquant au résultat de la première : le livre imprimait un mot
  d'aucune langue, **depuis la a.1**, sans que la relecture l'ait relevé. Le
  libellé amont tronqué qui l'a rendu possible est consigné en défaut amont
  (`docs/defauts-amont.md` §5).
- **Le symbole `ü` du rapport de transformation remplacé par `m`** — 18
  occurrences dans 5 sections (A : `uebertrager_2` 10, `antennenformen_3` 2,
  `brueckengleichrichter` 1, `mantelwellen_2` 1 · E : `uebertrager_1` 4).
  Un `ü` **nu** en mode mathématique est composé dans l'italique mathématique,
  qui n'a pas le glyphe : il **disparaissait du PDF** sans erreur de
  compilation. Mesuré au journal — `Missing character U+00FC` sortait 17 fois
  en classe A et 5 fois en E. Le cas le plus grave n'était pas celui qui avait
  été relevé en a.1 : dans `uebertrager_2`, **la formule centrale du chapitre
  sur les transformateurs s'imprimait sans son membre de gauche**, et
  `antennenformen_3` donnait « un rapport de spires **()** de 1:7 ».
  Dérogation à la règle « formules `$…$` verbatim » assumée par Pierre, et
  cohérente avec la décision du même jour sur les dessins 260, 303 et 315 : sans
  elle, les figures auraient dit « m » et le texte rien. Le remplacement n'a eu
  lieu que dans les spans `$…$` — le commentaire allemand `prüfen` et l'ident
  de photo `Brückengleichrichter` sont intacts. Détail dans
  `docs/defauts-amont.md` §2.
- **`$\text{Ordnung}=m+n$` → `$\text{Ordre}=m+n$`** validé, et la légende
  « 3. Ordnung » du dessin 1096 traduite en « ordre 3 ». La décision, en
  suspens au §9 depuis plusieurs sessions, est close ; la dérogation à la règle
  « math verbatim » est assumée.

- **Relecture de la classe E, feuille d'arbitrage nº 4** (15/08/2026). Dix points
  relevés par Pierre sur le livre E, tous reproduits et leur cause mesurée, puis
  cherchés systématiquement en N et A.
  - **Nombres gras dans les énoncés** (v0.19, ci-dessous). Deux réglages
    seulement sur les dix touchaient les trois livres ; c'est le principal.
  - **Dessin 942** : « Bobine à noyau de ferrite » (25 caractères contre 20 à
    « Spule mit Ferritkern ») faisait se toucher les libellés voisins. Passés
    sur deux lignes.
  - **Dessins 911 et 96** : « Traitement numérique du signal » sortait de son
    encadrement, dont la largeur est fixée. Texte sur trois lignes en un seul
    nœud centré, boîte élargie. *Première tentative écartée* : deux nœuds
    ancrés au nord et au sud se chevauchaient, la boîte n'ayant pas la hauteur
    de trois lignes — vu à l'image, la compilation sortant en `rc=0`.
  - **Dessin 666** : « Anode » et « Cathode » écrits en entier. Le dessin porte
    un aide-mémoire où les tracés rouge et bleu forment un **A** et un **K** que
    le texte complète (*A*+*node*, *K*+*athode*). Le procédé ne survit pas au
    français, *Cathode* ne commençant pas par K.
  - **Dessins 434 à 437** (classe A, défaut non signalé, trouvé en cherchant les
    équivalents) : le livre affichait « 1/2 **le Longueur** d'onde » et « **le
    Fréquence** perturbatrice », l'amont « 1/2 der Wellenlänge / der
    Störfrequenz » ayant subi la substitution mot à mot du 14/08. Corrigé, puis
    **les libellés ancrés à l'est** : le français, plus long que l'allemand,
    chevauchait le circuit. Le texte croît désormais vers la gauche et ne peut
    plus l'atteindre.
  - **`spannungsteiler_1`** : point parasite avant un deux-points, reproduit de
    l'amont (`Formelsammlung finden.:`). Corrigé côté français.
  - **Préservés sur décision de Pierre** : l'espace fine avant `!` et `?`
    (babel applique la règle de l'Imprimerie nationale — 0,5 unité contre 1,0
    avant `:` ; ce n'est pas un bogue), l'absence de point devant les formules
    hors texte (usage allemand constant, 16 cas en E et 26 en A), et
    l'abréviation « OW » d'*Oberwellen*, que les légendes françaises emploient
    déjà.
  - **Une entrée de `docs/defauts-amont.md` rétractée** : le §5, écrit le matin
    même, qualifiait à tort l'aide-mémoire du dessin 666 de « libellés
    tronqués » et proposait de le signaler au DARC. Conclusion tirée du source
    sans regarder la figure. L'entrée est conservée sous forme rétractée.

- **Édition combinée NEA compilée pour la première fois** (15/08/2026) :
  **806 pages**, 384 sections, 1 751 questions, 805 dessins. Contrôles du §4
  conformes du premier coup, 4 références « ?? » — les quatre orphelines amont
  cumulées, rien de nouveau. Les compteurs de clamp cumulent proprement (948
  figures, 10 tableaux, 7 formules), ce qui confirme qu'aucun dessin n'est
  traité différemment en édition combinée.
  - **Ordre des `--translations` arrêté : `A` en premier**, puis `E`, puis `N`.
    La portée du choix est étroite et a été mesurée : **une seule section** est
    traduite dans plusieurs classes, `N_Ende` (« Conclusion du cours »), du
    contenu français dont les trois versions renvoient chacune à l'examen de
    leur classe. Les **20 dessins forkés partagés sont identiques au contenu** —
    deux d'entre eux ne diffèrent que par leurs fins de ligne, CRLF contre LF.
  - **`vorwort` n'est pas dans le NEA.** La section est traduite et figure dans
    le livre N, mais le sommaire amont du NEA ne l'appelle pas : l'édition
    combinée perd l'avant-propos allemand. C'est aussi l'origine de
    l'avertissement « clé *vorwort* n'est pas un ident connu » de `titles.json`.

### Modifié
- **`build_book.py` v0.20 : filigrane de la page de titre empilé.** Le bandeau
  de droite fait 0,34 de la largeur du papier, soit 71 mm en A4. La v0.9
  réduisait le corps du filigrane à mesure — 220 pt pour une lettre, 150 pour
  deux, 105 pour trois. **Mesuré sur épreuve : « NEA » à 105 pt débordait
  encore**, le N mordant sur la zone blanche à gauche et le A se faisant couper
  au bord droit. Dès deux lettres, elles sont désormais empilées une par ligne,
  centrées sur l'axe du bandeau et calées en haut, à 150 pt — lisibles à
  l'endroit, et sans débordement. Une lettre seule est inchangée.
  L'ancien gabarit ne pouvait faire varier que le corps et le texte, jamais
  l'ancrage ni la position : le nœud entier est maintenant construit côté
  Python. Trois dispositions ont été composées et comparées sur épreuve — à
  plat, pivotée à 90°, empilée — avant la décision de Pierre.
- **`build_book.py` v0.19 : nombres gras dans les énoncés de question.** Une
  ligne, pour un défaut qui touchait **418 énoncés** — N 102, E 122, A 194, soit
  un sur quatre. Le parseur amont rend « 230 V » par « `$230$\,V` », et le mode
  mathématique n'hérite pas du gras du texte.
  Le diagnostic a d'abord visé la définition de `\Question` ; elle était hors de
  cause. **L'amont demande déjà le gras mathématique**
  (`\newkomafont{questiontext}{\bfseries\boldmath}`), mais `settings.tex` charge
  `unicode-math` sans déclarer de version mathématique grasse : `\boldmath` est
  alors sans effet, **et sans le moindre avertissement**. Correctif :
  `\setmathfont[version=bold, FakeBold=2]{Libertinus Math}` après
  `\input{settings.tex}` — Libertinus Math n'ayant pas de fonte grasse compagne,
  le gras est synthétique. Vérifié sur document réduit avant application, puis
  dans le livre (question NA212, classe N).
- **`sonde_dessins.py` v0.2** : la liste de mots reçoit les termes de la feuille
  d'arbitrage nº 3. « Signal », « Filter » et « Band » ont été essayés puis
  **retirés** — ils sont aussi français et produisaient du bruit ; « Tag » et
  « Ort » sont écartés pour la même raison.
- **`verifier_amont.py` v0.3 : détection des forks absents du manifeste.** Le
  script ne comparait l'amont qu'aux entrées **déjà** enregistrées ; un fork
  créé sans `enregistrer` lui était donc entièrement invisible, et n'aurait
  **jamais** été signalé en dérive. Trois dessins de la classe A (260, 303, 315)
  étaient dans ce cas, forkés après un `initialiser` : `verifier` répondait
  « 261 éléments suivis, 0 dérive » sans rien dire. Le script compte désormais
  les fichiers réellement présents dans `dessins/` et `sections/` — c'est le
  dossier qui fait foi, le manifeste n'étant que sa mémoire — et sort en `rc=1`
  sur tout fork non suivi. Testé sur les trois cas : arbre propre (`rc=0`), fork
  jetable non enregistré (`rc=1`, signalé), retour à l'état propre (`rc=0`).

### Connu
- Les tableaux à colonne `X` échappent au clamp : `tabularx` fixe leur largeur
  à `\linewidth`, si bien que la mesure est toujours conforme même quand le
  contenu déborde. Ces cas se corrigent à la source, pas dans la classe.
- ~~**24 dessins affichent encore de l'allemand**~~ — **traité le 15/08/2026,
  et le compte était très en deçà de la réalité** : voir *Corrigé* ci-dessus.
- `sonde_dessins.py`, même enrichie, **lit le source TikZ et non le PDF**, et sa
  détection reste une liste de mots. Elle donnera toujours un plancher. Le
  contrôle qui a réellement trouvé les 39 défauts — extraction des zones de
  texte composé, puis relecture — est reproductible (méthode décrite au §4 de
  `docs/ANALYSE-DESSINS.md`) mais n'est pas outillée au dépôt.
- **La classe A passe de 3 à 4 notes de marge rétrogradées.** `schwingkreis_2`
  contient 22 formules hors texte ; la redéfinition de `displaymath` coûte
  environ 1 pt à chacune, et la note franchit le seuil de 23 pt. Pas d'erreur de
  compilation — le garde-fou la compose dans le corps, en boîte sécable — mais
  une section change de mise en page.

---

## a.1 — 14 août 2026

**Première release publiée.** Les trois classes portent désormais un numéro de
version commun. Les versions par classe antérieures (N v0.9, E v0.9, A v1.2)
restent consignées plus bas à titre historique.

| Classe | Sections | Questions | Encarts | Pages |
| ------ | -------: | --------: | ------: | ----: |
| N | 131 | 571 | 55 | 254 |
| E | 103 | 462 | 6 | 206 |
| A | 153 | 717 | 5 | 372 |

### Ajouté
- **Avant-propos et remerciements** dans les trois livres, en chapitres non
  numérotés inscrits au sommaire. C'est ce qui distingue `a.1` des versions par
  classe qui précèdent, et ce qui explique environ deux pages de plus chacune.
- Squelette de dépôt public : README, LICENSE, NOTICE, CONTRIBUTING,
  GUIDE-GITHUB, `.gitignore`, `docs/defauts-amont.md`.
- **Suivi de la dérive amont étendu aux sections.** `verifier_amont.py` suit
  513 éléments — 126 dessins forkés et 387 sections traduites — en comparant
  l'empreinte SHA-256 de l'original allemand à celle enregistrée. Il remplace
  `verifier_dessins.py`, qui ne couvrait que les dessins.

### Modifié
- **Resynchronisation de quatre sections de classe A** sur la dérive amont :
  `antennenformen_3`, `photovoltaik`, `polarisation_3`, `remote_station`. Du
  contenu allemand ajouté en amont depuis notre traduction manquait au livre
  français sans qu'aucun signal ne le révèle.
- Paginations relevées sur amont à jour : 254 · 206 · 372.
- `compiler.bat` localise seul les dépôts amont et l'interpréteur, au lieu de
  chemins codés en dur.

### Corrigé
- **Les pièces liminaires manquaient à toute compilation lancée par
  `compiler.bat`** : l'option `--front-matter` n'y figurait pas.
- `build_book.py` v0.16 — `\qty{0.05}{\lambda}` : `\lambda` n'étant pas une
  unité siunitx, le glyphe disparaissait du PDF sans la moindre erreur, et le
  lecteur lisait « au moins 0,05 », sans unité.
- Détection de Ghostscript en 32 bits, dont l'exécutable console porte un autre
  nom que celui de la version 64 bits.
- Le décompte des références non résolues se fait désormais dans le PDF et non
  dans le journal, qui ne conserve que la dernière passe et sous-compte.

### Préservé
- **Référence orpheline `a_zeppelinantenn`** dans `antennenformen_3` : l'ident
  est tronqué en amont, le dessin déclarant `a_zeppelinantenne`. Sort en `??`,
  côté allemand comme côté français.
- **`$ü = 1:7$`** dans la même section : un caractère accentué nu en mode
  mathématique est composé dans l'italique mathématique, qui n'a pas le glyphe.
  L'umlaut disparaît du PDF, dans les deux langues.

### Connu
- **Discordances texte / figure.** Les indices allemands des formules ont été
  francisés dans le corps du texte, mais tous les dessins TikZ amont ne le sont
  pas encore : **126 dessins francisés sur 403 référencés** par les sections
  traduites (N 81 · E 156 · A 199). Exemple : le dessin 1082 affiche
  « Taktgenerator » là où le texte écrit `f_horloge`.
- **20 dessins à double citation.** Ils sont appelés à la fois par une section
  et par une question d'examen. Les franciser modifierait simultanément une
  illustration officielle de la BNetzA — arbitrage en attente.
- Terminologie en attente de validation : rendu de l'acronyme ERP,
  `\text{Ordnung}` dans une formule, indice `P_\mathrm{S}` non résolu.
- Trois notes de marge de la classe A dépassent la hauteur de colonne et sont
  rétrogradées dans le corps du texte par le garde-fou prévu à cet effet.

---

## Classe A

### v1.2

#### Ajouté
- Traduction française complète : 153 sections, 717 questions.
- 5 encarts « En France ».
- 368 pages, pagination paire garantie pour un dos carré collé.

#### Connu
- Dessins 1096 et 687 : dimensions hors gabarit non résolues. Le clamp de
  `\DARCimage` ne borne que la largeur.

---

## Classe E

### v0.9

#### Ajouté
- Traduction française complète : 103 sections, 462 questions.
- 6 encarts « En France ».
- 202 pages.

#### Corrigé
- Dessin 202 (diagramme d'affaiblissement des câbles) : l'axe pgfplots fixait
  ses propres dimensions, 21 × 29 cm, que l'autoscale amont n'atteint pas.
  Placée en note de marge, la figure devenait inplaçable ; `marginfix` perdait
  cette note et toutes les suivantes, et la classe E ne compilait plus du tout.
  Le dessin est désormais précompilé isolément à 52 mm et substitué par un
  `\includegraphics`.

---

## Classe N

### v0.9

#### Ajouté
- Traduction française complète : 131 sections, 571 questions.
- 55 encarts « En France » — la classe N concentre l'essentiel des
  divergences réglementaires.
- 252 pages.

#### Modifié
- Deux points corrigés par rapport à la documentation radioamateur
  francophone courante :
  - **Seuil d'urbanisme porté de 2 m² à 5 m²**, en application du décret
    n° 2024-1023 du 13 novembre 2024, pour les demandes déposées à compter du
    1<sup>er</sup> décembre 2024.
  - **Attribution des indicatifs fondée sur l'adresse de la station
    déclarée**, et non sur le domicile fiscal, depuis l'arrêté du
    2 mars 2021.
- Mention du droit d'opposition à la publication dans l'annuaire ANFR
  (« liste orange »), instauré par le même arrêté.

---

## Défauts amont préservés

Constatés dans les sources allemandes, **volontairement non corrigés** dans
l'œuvre dérivée, consignés dans `docs/defauts-amont.md` et destinés à être
signalés au DARC :

- 20 libellés dupliqués ;
- 5 légendes cassées par un caractère `:` — le parseur amont impose
  `caption = [^:\]]+` ;
- 5 références orphelines, dont `a_zeppelinantenn` relevée le 14/08/2026 ;
- défauts d'emploi de siunitx et coquilles diverses ;
- syntaxe `\tikzstyle{…};` dépréciée, 22 occurrences sur 21 dessins.

---

## Historique du générateur

Le journal détaillé de `build_book.py` figure dans l'en-tête du script
lui-même, où chaque version documente le défaut qu'elle corrige et sa cause
racine.
