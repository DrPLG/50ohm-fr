# Séance 11 — Moduler : transporter la voix

Domaine D · 1 h 30 · chapitre 11 du manuel · fiche d'activité nº 11

## Ce que l'élève doit emporter

- Le microphone change la voix en signal BF ; 300 à 3000 Hz suffisent
  pour la comprendre.
- Moduler, c'est modifier la porteuse au rythme du signal : son amplitude
  en AM, sa fréquence en FM.
- La SSB ne transmet qu'une bande latérale, sans porteuse ; LSB sous
  10 MHz, USB au-dessus, par habitude.
- La largeur de bande d'un signal ; ordres de grandeur du Morse, de la SSB,
  de l'AM et de la FM.

## Avant la séance

**Acquis nécessaires :** porteuse et modulation (séance 1), sinusoïde et
fréquence (séance 7), spectre et chute d'eau (séance 8).

**Matériel :**

- par groupe de 2 ou 3 : ordinateur avec logiciel SDR et clé SDR, ou
  WebSDR ; écouteurs ; la fiche nº 11 ;
- pour l'encadrant : un récepteur ou un WebSDR projeté avec le son, et, si
  possible, le poste du radioamateur, pour faire entendre la même station
  SSB dans le bon mode et dans le mauvais.

**À préparer :** relever à l'heure de la séance un exemple sûr de chaque
mode :

- AM : une station de radiodiffusion en ondes courtes, ou les ondes
  moyennes si elles existent encore dans la région ;
- FM : une station de la bande FM, le relais radioamateur local ;
- SSB : un contact en phonie sur 40 m ou 20 m (WebSDR en secours) ;
- Morse : un signal télégraphique, ou une balise.

## Déroulé

| durée | phase | ce que fait l'encadrant | ce que font les élèves |
| --- | --- | --- | --- |
| 5 min | accroche | fait entendre une voix SSB en AM : « qu'est-ce qui ne va pas ? » | décrivent le son |
| 10 min | le signal vocal | microphone, BF, spectre de la voix | chantent un son grave et un aigu devant un analyseur de spectre (application) |
| 10 min | AM et FM | porteuse, amplitude, fréquence ; les parasites | associent chaque figure à un mode |
| 5 min | SSB et largeur de bande | bandes latérales ; tableau des largeurs | classent quatre modes du plus étroit au plus large |
| 45 min | manipulation | aide au choix du mode de démodulation | reconnaissent AM, FM, SSB et Morse à l'oreille et à l'écran (fiche nº 11) |
| 15 min | bilan | fait comparer les largeurs mesurées | complètent « à retenir » ; répondent aux questions |

## Conduite de la manipulation

1. **Quatre signaux connus (20 min).** Pour chacun des signaux repérés :
   régler le récepteur dans le bon mode ; décrire le son ; dessiner la trace
   à la chute d'eau ; estimer sa largeur à l'écran.
2. **Le mauvais mode (10 min).** Écouter le signal SSB en AM, puis en FM,
   puis dans l'autre bande latérale. Décrire ce qu'on entend.
3. **Signaux mystères (15 min).** L'encadrant donne trois fréquences sans
   dire le mode ; les groupes le trouvent, à l'écran d'abord, à l'oreille
   ensuite.

**Ce qu'on écoute.** Radiodiffusion et bandes radioamateur seulement.

## Ce qui coince souvent

- **« La FM, c'est la radio musicale. »** La FM est un mode de modulation ;
  la « bande FM » en est un usage. Le relais radioamateur est lui aussi en
  FM.
- **Voix de canard en SSB.** Ce n'est pas un défaut de l'émetteur : il faut
  ajuster la fréquence, à quelques dizaines de hertz.
- **Confondre largeur de bande et bande radioamateur.** L'une est la place
  prise par un signal, l'autre une plage de fréquences autorisée.
- **Croire que la porteuse transporte la voix.** Elle ne fait que la
  porter : c'est dans les bandes latérales qu'est l'information.

## Pour aller plus loin

- **L'excursion en FM** : l'écart maximal de fréquence autour de la
  porteuse ; elle fixe, avec la BF, la largeur du signal.
- **Pourquoi LSB en bas et USB en haut ?** Un héritage technique des
  premiers émetteurs SSB, devenu une convention.
- **Les classes d'émission** : un code international décrit le mode, par
  exemple J3E pour la phonie en SSB, F3E pour la phonie en FM, A1A pour le
  Morse. Au programme de l'examen français.
- **En France, la largeur de bande occupée est plafonnée par les textes**
  selon la fréquence (6 kHz sous 28 MHz, par exemple).

## Corrigé de la fiche

- Ordre des largeurs : Morse < SSB < AM < FM radioamateur < FM musicale.
- Aspect à la chute d'eau : Morse, trait fin haché ; SSB, bande étroite
  irrégulière, sans trait central ; AM, bande plus large avec un trait
  central continu (la porteuse) ; FM radioamateur, bande d'une dizaine de
  kilohertz qui ondule ; FM musicale, bande très large et continue.
- SSB écoutée en AM ou dans la mauvaise bande latérale : incompréhensible.

## Questions de la séance

RD1101 à RD1110.

## Sources

Manuel : sections `bir_le_signal_vocal`, `bir_am_et_fm`,
`bir_la_bande_laterale_unique`, `bir_la_largeur_de_bande`. Voir
`SOURCES.md`.
