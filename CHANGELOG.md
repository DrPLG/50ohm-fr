# Journal des versions

Les versions sont suivies **par classe**, chacune évoluant à son rythme.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).

Rubriques employées : *Ajouté*, *Modifié*, *Corrigé*, *Préservé* (défauts amont
laissés intacts et consignés), *Connu* (limitations non résolues).

---

## En cours — non publié

### Ajouté
- Squelette de dépôt public : README, LICENSE, NOTICE, CONTRIBUTING,
  GUIDE-GITHUB, `.gitignore`, `docs/defauts-amont.md`.

### Connu
- **Discordances texte / figure.** Les indices allemands des formules ont été
  francisés dans le corps du texte, mais les dessins TikZ amont portent encore
  leurs libellés d'origine. Sur 884 dessins amont, 805 sont effectivement
  référencés dans les trois classes et 228 portent du texte traduisible.
  Exemple : le dessin 1082 affiche « Taktgenerator » là où le texte écrit
  `f_horloge`.
- **20 dessins à double citation.** Ils sont appelés à la fois par une section
  et par une question d'examen. Les franciser modifierait simultanément une
  illustration officielle de la BNetzA — arbitrage en attente.
- Terminologie en attente de validation : rendu de l'acronyme ERP,
  `\text{Ordnung}` dans une formule, indice `P_\mathrm{S}` non résolu.

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
- 4 références orphelines ;
- défauts d'emploi de siunitx et coquilles diverses ;
- syntaxe `\tikzstyle{…};` dépréciée, 22 occurrences sur 21 dessins.

---

## Historique du générateur

Le journal détaillé de `build_book.py` figure dans l'en-tête du script
lui-même, où chaque version documente le défaut qu'elle corrige et sa cause
racine.
