# Journal des versions

Les versions sont suivies **par classe**, chacune évoluant à son rythme.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).

Rubriques employées : *Ajouté*, *Modifié*, *Corrigé*, *Préservé* (défauts amont
laissés intacts et consignés), *Connu* (limitations non résolues).

---

## a.2 — 14 août 2026 (en cours)

| Classe | Sections | Questions | Encarts | Pages (a.1 → a.2) |
| ------ | -------: | --------: | ------: | ----: |
| N | 131 | 571 | 55 | 254 → 258 |
| E | 103 | 462 | 6 | 206 → 214 |
| A | 153 | 717 | 5 | 372 → 376 |

Effet mesuré des corrections, sur les trois classes :

| mesure | a.1 | a.2 |
| --- | ---: | ---: |
| plus grand débordement horizontal (N · E · A) | 125 · 104 · 200 pt | **20 · 11 · 11 pt** |
| débordements > 20 pt (N · E · A) | 1 · 8 · 17 | **0 · 0 · 0** |
| pages « Underfull \vbox » (total) | 306 | **0** |
| questions séparées de leurs réponses | 19 relevées en N | **0 sur 1 750** |
| figures ramenées dans leur gabarit | 0 | **948** |
| tableaux et formules réduits | 0 | 10 et 9 |
| dessins affichant de l'allemand | 62 | **24** |

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

### Connu
- Les tableaux à colonne `X` échappent au clamp : `tabularx` fixe leur largeur
  à `\linewidth`, si bien que la mesure est toujours conforme même quand le
  contenu déborde. Ces cas se corrigent à la source, pas dans la classe.
- **24 dessins affichent encore de l'allemand** (N 1 · E 10 · A 13) : ceux dont
  le texte allemand n'est pas dans une zone repérable automatiquement. Examen
  manuel nécessaire, dessin par dessin.
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
