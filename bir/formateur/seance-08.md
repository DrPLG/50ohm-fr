# Séance 8 — Le spectre et les bandes

Domaine C · 1 h 30 · chapitre 8 du manuel · fiche d'activité nº 8

## Ce que l'élève doit emporter

- Le spectre radio va de 30 kHz à 300 GHz ; il se découpe en domaines, dont
  HF, VHF et UHF.
- Les fréquences sont partagées entre de nombreux usages ; ce partage est
  organisé entre les pays, puis dans chaque pays.
- Les radioamateurs disposent de bandes, nommées par leur longueur d'onde.
- Un spectre se lit en fréquence et en force ; une chute d'eau ajoute le temps.

## Avant la séance

**Acquis nécessaires :** fréquence et longueur d'onde (séance 7).

**Matériel, par groupe de 2 ou 3 :**

- un ordinateur avec un logiciel de réception SDR installé et essayé ;
- une clé SDR et son antenne ;
- la fiche élève nº 8, un crayon.

**Pour l'encadrant :** un poste ou un récepteur relié au vidéoprojecteur ;
un accès à un WebSDR en secours, et pour montrer les bandes HF que la clé ne
reçoit pas.

**À préparer :** relever à l'avance, depuis la salle, quatre ou cinq signaux
sûrs — deux stations FM, un multiplex DAB+, le relais radioamateur local, une
balise. Noter leurs fréquences : ce sont les points de repère de la séance.
La couverture exacte de la clé est à lire dans sa notice.

## Déroulé

| durée | phase | ce que fait l'encadrant | ce que font les élèves |
| --- | --- | --- | --- |
| 5 min | accroche | projette une chute d'eau de la bande FM : « combien de stations ici ? » | comptent les bandes verticales |
| 10 min | le spectre | déroule le tableau des domaines ; place la radio FM, le Wi-Fi, le relais local | situent trois fréquences données dans HF, VHF ou UHF |
| 10 min | le partage et les bandes | pourquoi partager ; qui décide ; six bandes radioamateur | retrouvent le nom d'une bande par le calcul de la séance 7 |
| 50 min | manipulation | circule, dépanne, relance | dressent leur carte du spectre (fiche nº 8) |
| 15 min | bilan | fait comparer les cartes ; corrige trois questions | complètent « à retenir » ; répondent aux questions |

## Conduite de la manipulation

1. **Prise en main (10 min).** Tout le monde sur une station FM connue.
   Faire repérer l'axe des fréquences, le pic, la trace dans la chute d'eau.
   Couper le son, puis le remettre : la trace ne dépend pas du son.
2. **Exploration guidée (25 min).** Les groupes cherchent les signaux de la
   fiche, dans l'ordre. Pour chacun : fréquence, domaine, aspect à l'écran.
3. **Exploration libre (15 min).** Chaque groupe trouve un signal qui n'est
   pas sur la fiche et le décrit aux autres.

**Ce qu'on écoute, ce qu'on regarde.** Les élèves n'écoutent que la
radiodiffusion et les bandes radioamateur. Tout autre signal est observé à
l'écran, son coupé : on note sa fréquence et sa forme, pas son contenu.

## Ce qui coince souvent

- **Confondre les deux axes.** « Plus à droite » est lu comme « plus fort ».
  Faire montrer du doigt : droite-gauche, c'est la fréquence.
- **Confondre spectre et oscillogramme.** À la séance 7, l'axe horizontal
  était le temps. Ici, c'est la fréquence. Le dire explicitement.
- **Croire qu'une bande est une seule fréquence.** Faire compter les stations
  visibles dans la bande FM : une bande, beaucoup de fréquences.
- **Croire que « 2 m » est une distance ou une taille d'antenne.** Refaire le
  calcul : 300 divisé par 145.
- **Prendre pour un émetteur un pic qui ne bouge pas quand on change
  d'antenne.** C'est un parasite de l'ordinateur ou de la clé. Débrancher
  l'antenne : un vrai signal disparaît.

## Pour aller plus loin

Réservé aux groupes en avance, ou à l'encadrant qui veut du fond.

- **Statut primaire ou secondaire.** Sur certaines bandes, les radioamateurs
  sont prioritaires ; sur d'autres, ils ne doivent pas gêner le service
  principal et acceptent d'être gênés par lui. En France, la bande des 2 m
  est à statut primaire, celle de 430 à 434 MHz à statut secondaire.
- **Les trois régions de l'UIT.** Le monde est découpé en trois régions ; les
  bandes n'y sont pas toutes identiques. La France métropolitaine est en
  région 1.
- **Les plans de bande.** À l'intérieur d'une bande, les radioamateurs se
  répartissent eux-mêmes les usages — télégraphie ici, voix là, balises
  ailleurs — par des plans de bande établis par leurs associations.
- **L'échelle verticale du spectre** est graduée en décibels : chaque
  graduation correspond à un rapport, pas à un écart. Notion reprise plus tard.

## Corrigé de la fiche

Les fréquences relevées dépendent du lieu. Sont attendus : le bon domaine
pour chaque signal, une description juste de la trace (largeur, continuité),
et la longueur d'onde calculée à 10 % près.

| signal | domaine | aspect attendu à la chute d'eau |
| --- | --- | --- |
| station FM | VHF | bande large, continue |
| multiplex DAB+ | VHF | bloc très large, uniforme, à bords nets |
| relais radioamateur | VHF ou UHF | bande étroite, par moments seulement |
| balise | selon la bande | trait fin, continu ou découpé |

## Questions de la séance

RC0801 à RC0810. La bonne réponse est toujours la réponse A dans le
catalogue ; le manuel et la plateforme d'examen mélangent les réponses.

## Sources

Manuel : sections `bir_spectre_radio`, `bir_partage_des_frequences`,
`bir_bandes_radioamateur`, `bir_lire_une_chute_d_eau`. Voir `SOURCES.md`.
