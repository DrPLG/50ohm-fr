# Certificat d'Initiation à la Radio 1 (CIR 1) — plan de l'ouvrage

> **11/10/2026 — décision de Pierre : le CIR devient le CIR 1** (et le BIR
> devient le CIR 2, `bir/`). Édition `--edition CIR1`, case « CIR 1 » de la
> fenêtre, titre « Certificat d'Initiation / à la Radio — 1 », filigrane
> C/I/R/1 empilé. Le répertoire reste `cir/`. L'historique ci-dessous
> garde les noms de l'époque.

État au 01/10/2026. **Document de travail.** Second ouvrage autonome du
dépôt, construit sur le modèle du BIR (`bir/PLAN.md`).

## 1. Cadrage arrêté par Pierre (01/10/2026)

- Titre : **Certificat d'Initiation à la Radio** (CIR).
- Public : élèves de **CM2, 6ᵉ et 5ᵉ** (fin du cycle 3, début du cycle 4).
- **12 séances de 1 h**, soit 12 heures.
- Évaluation : **QCM court en séance 12**, une vingtaine de questions,
  puis remise d'une attestation. Pas de séance d'examen dédiée.
- Questions à **quatre réponses**, comme le BIR (décision du 03/10/2026).
- Séance pilote : la **6**, « Les ondes » (03/10/2026).
- Découpage en 12 séances : celui du § 3, **accepté tel quel**.

Repris du BIR, sauf décision contraire :

- ouvrage **français autonome**, adapté des contenus CC BY 4.0 du DARC
  par l'intermédiaire du BIR ; sections propres (`cir_…`), **réécrites**
  et non reprises du BIR ;
- un radioamateur présent à chaque séance ; postes PMR446 pour le trafic
  entre élèves ;
- aucun encart « En France » ; ton « nous » ;
- questions neuves ; indicatifs d'exercice en F4X….

## 2. Ce qui change par rapport au BIR

- **Pas de calcul littéral.** Ni U = RI, ni P = UI, ni λ = 300/f : le sens
  physique est gardé, les calculs sont remplacés par des tableaux et des
  abaques à lire.
- **Sécurité.** Pas de fer à souder, piles seulement, jamais le secteur.
  Les montages se font sans soudure (pinces, plaque d'essai).
- **Langue.** Phrases courtes, une notion par paragraphe, beaucoup
  d'images ; deux à trois sections par chapitre.
- **Trame d'une séance** : 15 min de cours, 35 min de manipulation par
  groupes de 2 ou 3, 10 min de bilan.

## 3. Les 12 séances

| nº | séance | puisée dans le BIR | manipulation |
| --- | --- | --- | --- |
| 1 | La radio autour de nous | 1 | première écoute ; démonstration d'un contact par le radioamateur |
| 2 | Se présenter : indicatif et alphabet | 2 | **PMR** : épeler son prénom d'une salle à l'autre |
| 3 | Un contact radio | 3, simplifiée | **PMR** : contact avec script |
| 4 | Le circuit électrique | 4 | pile, lampe, interrupteur ; conducteurs et isolants |
| 5 | L'énergie : piles et accus | 6, sans calcul | combien de temps tient un poste ? |
| 6 | Les ondes | 7, sans formule | corde, ressort, cuve à vagues |
| 7 | Le spectre | 8 | chute d'eau à la clé SDR |
| 8 | Jusqu'où va une onde ? | 9 et 10 | **PMR** : portée autour de l'école |
| 9 | Le Morse | 12 | buzzer : envoyer son prénom |
| 10 | L'antenne | 14 et 15 | assembler une antenne ; comparer deux orientations |
| 11 | La radio en action | 13 et 20 | chasse au renard ; image SSTV de l'ISS |
| 12 | Au micro, et l'attestation | 21 à 24 | contact aux côtés du radioamateur ; QCM ; attestation |

Non repris du BIR : loi d'Ohm, puissance calculée, modulation, câbles et
ROS, récepteur et émetteur, soudure, droit.

## 4. Documents prévus

Mêmes familles que le BIR : référentiel, manuel de l'élève, livre du
formateur, fiches d'activité (élève et encadrant), banque de questions,
livret de l'élève. Numéros de questions : `CI` + séance + ordre
(`CI0601`).

**Séance 6 rédigée le 03/10/2026** (pilote) : chapitre du manuel en trois
sections, page du formateur, fiches élève et encadrant, dix questions.
Génération sans compilation, par l'édition BIR pointée sur `cir/`
(`--local cir --no-compile`) : 3 sections, 10 questions, 0 erreur,
0 faux positif du parseur d'unités.

**Séances 4 et 9 rédigées le 03/10/2026** (choix laissé par Pierre) :
« Le circuit électrique » et « Le Morse », même structure que la 6, dix
questions chacune (`CI0401`…, `CI0901`…), trois dessins propres (9401,
9402, 9901). Le montage d'entraînement au Morse de la séance 9 est le
circuit de la séance 4, où la lampe devient un buzzer. Génération sans
compilation : 9 sections, 30 questions, 6 dessins propres, 0 erreur.

**Première compilation en édition CIR par Pierre le 03/10/2026**
(20 × 24 marge, 0.1) : 24 pages, 0 erreur, 0 débordement, 0 caractère
manquant, 0 « ?? », 7 figures et 30 questions contrôlées, 0 coupée ;
page de titre conforme. **Mais trois dessins déformés sur épreuve** :
`\DARCimage` met à l'échelle en agrandissant les unités TikZ, pas les
symboles circuitikz ni le texte — 9402 et 9901 étirés, symboles
minuscules ; 9401, deux circuits superposés (`xshift` absolu). Corrigé
par des unités fixées (`x=1cm, y=1cm`) dans ces trois dessins, vérifié
sous unités agrandies 2,5 fois. **Règle pour tout dessin propre :**
courbes seules, unités libres ; circuitikz ou décalage en cm, unités
fixées. **Recompilé par Pierre le même jour : 22 pages**, mêmes
contrôles verts (7 figures, 30 questions, 0 coupée, 0 « ?? », 0 erreur,
0 figure ramenée par le clamp) ; les trois dessins relus sur épreuve
(p. 5, 7, 19), nets et à leur place.

## 5. Chaîne de compilation

**`build_book.py` v0.35, 03/10/2026** : dessins propres (numéros absents
de l'amont) et **édition `CIR`** — `--edition CIR`, répertoire `cir/` par
défaut, titre « Certificat d'Initiation / à la Radio », filigrane CIR.
Case CIR dans la fenêtre. Arbres N et BIR identiques à la v0.34.
Restent : `composer.py` et `exporter_moodle.py`, qui visent `bir/` seul.

## 6. Points ouverts

1. ~~Figures de la séance 6~~ : **trois dessins propres au CIR**
   (03/10/2026), `cir/dessins/9601.tex` à `9603.tex` — la vague et le
   bouchon, main lente et main rapide, de l'émetteur au récepteur.
   Aucun dessin amont ne convenait (728 gradué en temps, 886 en champs
   E et H). Numérotation : `96xx` pour la séance 6, `9Sxx` en général.
   Pris en charge par `build_book.py` **v0.35**. **Compilé dans le livre
   par Pierre le 03/10/2026** (édition BIR pointée sur `cir/`,
   20 × 24 marge) : 12 pages, 0 erreur, 0 débordement, 0 caractère
   manquant, 0 « ?? », 3 figures et 10 questions contrôlées, 0 coupée.
   Épreuve relue : les trois dessins sont en place, lisibles.
2. Rattachement au programme de sciences et technologie du cycle 3
   (« signaux et informations ») : à lire sur le texte avant de l'écrire
   dans le référentiel.
3. Usage des PMR446 par des élèves de primaire : rien de particulier
   connu, à confirmer (même point ouvert que le BIR, § 5.2).
