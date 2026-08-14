# Journal des versions

Les versions sont suivies **par classe**, chacune évoluant à son rythme.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).

Rubriques employées : *Ajouté*, *Modifié*, *Corrigé*, *Préservé* (défauts amont
laissés intacts et consignés), *Connu* (limitations non résolues).

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
