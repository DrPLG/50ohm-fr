# Brevet d'Initiation à la Radio (BIR) — plan de l'ouvrage

État au 30/09/2026. **Document de travail.** Il remplace les propositions
nº 1 et nº 2 de `Fichierstravail/`.

## 1. Cadrage arrêté par Pierre

- Public : collégiens et lycéens. Ouvrage **français autonome**, adapté des
  contenus CC BY 4.0 du DARC, non traduit ; sections renommées (`bir_…`).
- Marchepied vers le certificat d'opérateur français.
- **24 séances de 1 h 30**, soit 36 heures.
- Questions d'examen **neuves**.
- Même dépôt, même chaîne de compilation.
- Un radioamateur est présent à chaque séance : les démonstrations à
  l'antenne sont possibles. Une séance est consacrée à la prise de micro par
  les élèves. Les postes PMR446 servent aux exercices de trafic entre élèves.
- **Aucun encart « En France »** : l'ouvrage entier s'adresse à des
  Français, le droit français y est le texte courant.
- Séance pilote : la **8**.

## 2. Documents

| nº | document | état |
| --- | --- | --- |
| D1 | Référentiel — `referentiel.md` | premier jet |
| D2 | Manuel de l'élève — `sections/` | chapitres 1 et 8 en premier jet |
| D3 | Livre du formateur — `formateur/` | séances 1 et 8 en premier jet |
| D4 | Fiches d'activité — `fiches/` | séances 1 et 8 en premier jet |
| D5 | Banque de questions — `questions/` | 20 questions : séances 1 et 8 |
| D6 | Diaporamas de séance | à faire |
| D7 | Mallette type et budget | à faire |
| D8 | Livret de l'élève | à faire |

## 3. Les 24 séances

Trame : 25 min de cours, 50 min de manipulation par groupes de 2 ou 3,
15 min de bilan et de questions.

Domaines : **A** découvrir la radio · **B** électricité et électronique ·
**C** ondes, spectre et propagation · **D** modulations, antennes et station ·
**E** trafic, règles et sécurité.

| nº | dom. | séance | contenus | manipulation |
| --- | --- | --- | --- | --- |
| 1 | A | La radio autour de nous | usages de la radio ; des signaux de fumée au Morse ; qui sont les radioamateurs | première écoute : récepteur et WebSDR ; démonstration d'un contact par le radioamateur |
| 2 | E | Se présenter à l'antenne | indicatifs ; préfixes de pays ; alphabet d'épellation | **PMR** : épeler et noter des indicatifs d'une salle à l'autre |
| 3 | E | Un contact radio | déroulement d'un contact ; report RST ; codes Q ; carnet de trafic | **PMR** : contact simulé avec script, tenue du carnet |
| 4 | B | Tension et courant | tension, courant, circuit ; conducteurs et isolants ; dangers du courant | circuit pile-lampe ; mesures au multimètre |
| 5 | B | La résistance et la loi d'Ohm | résistance ; loi d'Ohm ; code des couleurs ; symboles | vérifier la loi d'Ohm sur trois résistances |
| 6 | B | Puissance et énergie | puissance ; piles et accus ; alimentation | mesurer une puissance ; calculer l'autonomie d'un poste |
| 7 | C | Du courant alternatif à l'onde | continu et alternatif ; fréquence, période ; onde radio ; longueur d'onde | visualiser une sinusoïde ; calculer des longueurs d'onde |
| 8 | C | Le spectre et les bandes | spectre ; partage des fréquences ; bandes radioamateur ; chute d'eau | dresser sa carte du spectre à la clé SDR |
| 9 | C | La propagation à vue | horizon radio ; relief et obstacles ; troposphère ; relais | **PMR** : mesurer la portée autour de l'établissement, la reporter sur un plan |
| 10 | C | Les ondes courtes et l'ionosphère | ionosphère ; jour et nuit ; balises ; contacts lointains | écouter balises et stations lointaines, les reporter sur une carte |
| 11 | D | Moduler : transporter la voix | signal vocal ; AM, FM, SSB ; largeur de bande | reconnaître AM, FM et SSB à l'oreille et à l'écran |
| 12 | D | Le Morse | code Morse ; télégraphie ; pourquoi il passe quand la voix ne passe plus | manipulateur et buzzer : envoyer et recevoir son prénom |
| 13 | D | Les modes numériques et l'image | analogique et numérique ; modes par ordinateur ; voix numérique ; SSTV | décoder du FT8 et une image SSTV au PC |
| 14 | D | Les antennes : principes | rôle de l'antenne ; dipôle demi-onde ; polarisation | calculer et couper les brins d'un dipôle 2 m |
| 15 | D | Construire son antenne | antennes omnidirectionnelles et Yagi ; directivité | assembler l'antenne ; comparer deux orientations en réception |
| 16 | D | Câbles, connecteurs et réglage | câble coaxial ; connecteurs ; rapport d'ondes stationnaires | régler l'antenne à l'analyseur ; monter une fiche |
| 17 | B | Le récepteur | chaîne de réception ; squelch ; commandes d'un poste | prise en main d'un poste en réception |
| 18 | B | L'émetteur | chaîne d'émission ; puissance ; charge fictive ; ne pas perturber | démonstration par le radioamateur : puissance sur charge fictive, effet d'un réglage |
| 19 | B | L'atelier de soudure | composants ; lire un schéma simple ; souder proprement | souder un petit kit |
| 20 | A | La radio en action | satellites et ISS ; locator ; concours ; chasse au renard ; radio d'urgence | chasse au renard dans l'établissement |
| 21 | E | Préparer son contact | ce qu'on dit et dans quel ordre ; l'indicatif de la station ; que noter | **PMR** : répétition générale par binômes, script en main |
| 22 | E | Au micro | un vrai contact depuis la station, aux côtés du radioamateur | chaque élève prend le micro ; carnet de trafic et carte QSL |
| 23 | E | Les règles, et après ? | qui peut émettre ; le certificat d'opérateur ; l'ANFR ; la suite du parcours | examen blanc corrigé |
| 24 | — | L'examen du BIR | — | examen, correction, remise des attestations |

Répartition : A 2 · B 6 · C 4 · D 6 · E 5 · examen 1.

## 4. Arborescence

```
bir/
  PLAN.md               ce document
  referentiel.md        D1
  toc.json              sommaire du manuel
  SOURCES.md            sections amont dont dérive chaque section du BIR
  sections/bir_*.md     manuel de l'élève, en DARCdown
  formateur/            livre du formateur, une page de séance par fichier
  fiches/               fiches d'activité, élève et encadrant
  questions/            catalogue de questions
```

## 5. Points ouverts

1. **Écoute et secret des correspondances.** La manipulation de la séance 8
   fait parcourir le spectre. Par prudence, elle ne fait *écouter* que la
   radiodiffusion et les bandes radioamateur ; le reste est seulement observé
   à l'écran. La règle française exacte n'a pas été relue à la source
   (CLAUDE.md §7 : sujet écarté faute de vérification).
2. **PMR446** : conditions d'usage libre (fréquences, puissance, antenne) à
   relire à la source avant de rédiger les séances 2, 3, 9 et 21.
3. **Fréquences des services cités au chapitre 8** (radiodiffusion FM, DAB+,
   aviation, télévision, Wi-Fi) : écrites de mémoire, à contrôler au TNRBF.
4. **Rattachement au programme du certificat** dans le référentiel :
   intitulés lus sur Légifrance à travers un outil de résumé, à confirmer sur
   le texte.
5. **Examen** : nombre de questions, durée et seuil restent une proposition ;
   la possibilité d'un format de type Pix n'a pas été étudiée.

## Tranché par Pierre le 30/09/2026

- **Séance 22** : le cadre reste formulé tel quel — « aux côtés du
  radioamateur ».
- **Ton du manuel** : « nous ».
- **Examen en ligne**, de type Moodle ou éléa, au mieux de type Pix.
  `exporter_moodle.py` produit la banque au format GIFT
  (`moodle/bir-questions.gift.txt`) ; l'import dans une vraie plateforme
  n'a pas été essayé.
- **Paragraphes autour des figures de marge** : séparés, pour le BIR seul
  (`build_book.py` v0.34). Dans une section, placer le bloc `<margin>`
  juste AVANT le paragraphe qu'il illustre.
- **Version** : le BIR a sa propre numérotation, `0.1`, proposée d'office
  par la fenêtre.

Tranché sur épreuve le 30/09/2026 : **page de titre** — « Brevet d'Initiation
à la Radio » en titre sur deux lignes, « Manuel de l'élève » en sous-titre,
BIR empilé dans le bandeau.

Première compilation par Pierre le 30/09/2026 (20 × 24 marge) : 12 pages,
0 erreur, 10 questions, 0 coupée.

Compilation des chapitres 1 et 8, même jour, version 0.1 : **18 pages**,
0 erreur, 20 questions, 0 coupée, 0 « ?? » ; un débordement de 0,34 pt,
invisible. Les paragraphes de la section 8.4 sont bien séparés.

## 6. Compiler le manuel

`build_book.py` v0.34, édition `BIR` (dans la fenêtre : édition BIR). À la
main :

```
python build_book.py --edition BIR --lang fr --format 20x24-marge \
  --input <amont>/50ohm-contents-dl-main --output build-BIR-20x24-marge \
  --version-label 0.1
```

- Dans le catalogue, la bonne réponse est toujours la A. Le livre mélange
  les réponses ; le corrigé est écrit dans `corrige-BIR.txt`, dans le
  répertoire de sortie.
- Un chapitre sans section est sauté ; les autres portent le numéro de leur
  séance.
