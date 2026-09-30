# Séance 18 — L'émetteur

Domaine B · 1 h 30 · chapitre 18 du manuel · fiche d'activité nº 18

## Ce que l'élève doit emporter

- Le schéma-bloc d'un émetteur : microphone, amplificateur BF, mélangeur,
  oscillateur, filtre, amplificateur HF, filtre passe-bas, antenne.
- La puissance d'émission se mesure au wattmètre ; on utilise la plus
  faible qui suffit ; en France, maximums par bande et indicateur de
  puissance obligatoire.
- La charge fictive : 50 Ω, toute la puissance en chaleur, rien de
  rayonné.
- Harmoniques et brouillages ; les règles pour ne pas perturber ; l'ANFR.

## Avant la séance

**Acquis nécessaires :** puissance (séance 6) ; ROS (séance 16) ; récepteur
(séance 17).

**Matériel, pour la démonstration :**

- le poste du radioamateur, réglable en puissance ;
- un wattmètre ou un ROS-mètre avec lecture de puissance ;
- une charge fictive adaptée à la puissance essayée ;
- un récepteur SDR sur ordinateur, projeté, avec une petite antenne, pour
  montrer le signal (et, si l'on dispose d'un atténuateur et de l'analyseur
  adapté, une harmonique) ;
- une radio FM ou une petite enceinte amplifiée, pour montrer une
  perturbation de proximité, **à très faible puissance et sur charge
  fictive**, uniquement si le radioamateur le juge sans risque.

**Par groupe :** la fiche élève nº 18, une calculatrice.

**Cadre.** Toutes les émissions de la séance sont faites par le
radioamateur, sous son indicatif et sous sa responsabilité, sur charge
fictive. Les élèves lisent les appareils.

## Déroulé

| durée | phase | ce que fait l'encadrant | ce que font les élèves |
| --- | --- | --- | --- |
| 5 min | accroche | « un émetteur, c'est un récepteur à l'envers ? » | comparent les deux schémas-blocs |
| 15 min | la chaîne d'émission | les huit blocs ; le commutateur PTT | complètent le schéma-bloc de la fiche |
| 10 min | puissance et charge fictive | wattmètre, charge fictive, maximums français | — |
| 35 min | démonstration | émet sur charge fictive à plusieurs puissances ; montre l'effet d'un réglage | relèvent puissance et courant ; observent l'écran (fiche nº 18) |
| 10 min | ne pas perturber | harmoniques, brouillage, règles | calculent des harmoniques |
| 15 min | bilan | — | complètent « à retenir » ; répondent aux questions |

## Conduite de la démonstration

1. **Le montage.** Poste, wattmètre, charge fictive. Faire dire aux élèves
   le rôle de chaque élément avant la première émission.
2. **Trois puissances.** Le radioamateur émet en porteuse (mode FM ou CW)
   quelques secondes à 5, 25 et 50 W. Les élèves relèvent la puissance lue
   et, si l'alimentation l'affiche, le courant consommé ; ils calculent la
   puissance absorbée et comparent.
3. **La chaleur.** Après un essai, l'encadrant touche prudemment le
   radiateur de la charge : il est tiède ou chaud. Les élèves ne le
   touchent pas.
4. **Le réglage.** En SSB, montrer l'effet d'un gain micro trop élevé sur
   l'écran du récepteur : le signal s'élargit. Revenir au bon réglage.

## Ce qui coince souvent

- **« Plus de puissance, c'est mieux. »** Faire calculer : doubler la
  puissance ne gagne qu'un demi-point de S-mètre environ.
- **Confondre puissance consommée et puissance émise.** Comparer les deux
  relevés : le rendement est loin de 100 %.
- **Croire que la charge fictive est une antenne.** Son ROS est parfait et
  elle ne rayonne presque rien.
- **Harmoniques : multiplier au lieu d'additionner.** 2 × 145 = 290, pas
  145 + 2.

## Pour aller plus loin

- **Le décibel.** Doubler la puissance, c'est +3 dB ; un point de S-mètre
  vaut en principe 6 dB, soit quatre fois la puissance.
- **PAR et PIRE.** La puissance rayonnée dans une direction dépend aussi du
  gain de l'antenne.
- **Les maximums français** varient selon la bande ; ils figurent à
  l'annexe de la décision ARCEP qui régit le service d'amateur.
- **La largeur de bande occupée** est elle aussi plafonnée en France selon
  la fréquence.

## Corrigé de la fiche

- Schéma-bloc : 1 microphone, 2 amplificateur BF, 3 mélangeur,
  4 oscillateur, 5 filtre, 6 amplificateur HF, 7 filtre passe-bas,
  8 antenne.
- Puissances : selon le poste ; la puissance absorbée (13,8 V × courant)
  est toujours supérieure à la puissance émise.
- Harmoniques de 145 MHz : 290, 435, 580 MHz. De 7 MHz : 14, 21, 28 MHz.

## Questions de la séance

RB1801 à RB1810.

## Sources

Manuel : sections `bir_la_chaine_d_emission`, `bir_la_puissance_d_emission`,
`bir_la_charge_fictive`, `bir_ne_pas_perturber`. Voir `SOURCES.md`.
