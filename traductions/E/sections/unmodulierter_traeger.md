La forme la plus simple d'un signal HF est une porteuse constante (non modulée), qui possède une amplitude, une fréquence et une phase constantes. Comme aucune modulation n'est imprimée à la porteuse et qu'elle n'occupe donc exactement qu'une seule fréquence, sa forme d'onde est un signal sinusoïdal constant. Avec une porteuse non modulée, aucune information ne peut être transmise sans modulation supplémentaire, par exemple par mise en marche et arrêt.

[question:EE101]

<margin>
[picture:904:e_unmodulierter_traeger:Porteuse non modulée]
</margin>

<france>
# La désignation normalisée des émissions

Les contenus allemands parlent de *modes* — SSB, FM, CW — sans jamais employer la désignation normalisée. Le programme français, lui, l'exige : elle figure au programme de l'épreuve de réglementation, et le droit s'en sert directement, la décision ARCEP n° 2012-1241 citant nommément les classes $\mathrm{A1A}$, $\mathrm{A2A}$, $\mathrm{A3E}$, $\mathrm{G3E}$, $\mathrm{J3E}$ et $\mathrm{F3E}$.

Le système est défini à l'appendice 1 du Règlement des radiocommunications. Une émission complètement désignée s'écrit ainsi :

> **quatre caractères de largeur de bande**, puis **trois à cinq caractères de classe**

## Les trois symboles obligatoires

**Premier symbole — modulation de la porteuse principale :**

| Symbole | Modulation |
| --- | --- |
| N | porteuse non modulée |
| A | amplitude, double bande latérale |
| H | bande latérale unique, porteuse complète |
| R | bande latérale unique, porteuse réduite ou variable |
| J | bande latérale unique, porteuse supprimée |
| B | bandes latérales indépendantes |
| C | bande latérale résiduelle |
| F | modulation de fréquence |
| G | modulation de phase |
| D | amplitude et angle modulées simultanément ou en séquence |

**Deuxième symbole — nature du signal modulant :**

| Symbole | Signal modulant |
| --- | --- |
| 0 | aucun signal modulant |
| 1 | une voie de données, sans sous-porteuse |
| 2 | une voie de données, avec sous-porteuse |
| 3 | une voie analogique |
| 7 | plusieurs voies de données |
| 8 | plusieurs voies analogiques |
| 9 | voies analogiques et de données combinées |

**Troisième symbole — nature de l'information :**

| Symbole | Information transmise |
| --- | --- |
| N | aucune information |
| A | télégraphie à réception auditive |
| B | télégraphie à réception automatique |
| C | fac-similé |
| D | données, télémesure, télécommande |
| E | téléphonie, radiodiffusion sonore comprise |
| F | télévision |
| W | combinaison de plusieurs des précédents |

La logique se retient facilement : le premier symbole dit *comment* on module, le deuxième *avec quoi*, le troisième *pour transmettre quoi*. Une téléphonie en bande latérale unique à porteuse supprimée est donc J, puis 3, puis E.

## Les quatre caractères de largeur de bande

C'est la partie que l'on oublie le plus souvent, et elle est parfaitement codifiée. La largeur de bande nécessaire s'écrit avec **trois chiffres et une lettre**. La lettre occupe la position de la virgule décimale et donne l'unité : H pour les hertz, K pour les kilohertz, M pour les mégahertz, G pour les gigahertz.

Deux contraintes s'y ajoutent : le premier caractère ne peut être ni le chiffre zéro, ni l'une des lettres K, M ou G.

Quelques lectures :

| Écriture | Largeur de bande |
| --- | --- |
| $\mathrm{100H}$ | $\qty{100}{\hertz}$ |
| $\mathrm{2K70}$ | $\qty{2,70}{\kilo\hertz}$ |
| $\mathrm{6K00}$ | $\qty{6}{\kilo\hertz}$ |
| $\mathrm{16K0}$ | $\qty{16}{\kilo\hertz}$ |
| $\mathrm{1M25}$ | $\qty{1,25}{\mega\hertz}$ |

## Les émissions que vous rencontrerez

| Désignation | Émission |
| --- | --- |
| $\mathrm{A1A}$ | télégraphie Morse par tout ou rien de la porteuse |
| $\mathrm{A2A}$ | télégraphie Morse par modulation d'amplitude d'une sous-porteuse |
| $\mathrm{A3E}$ | téléphonie en modulation d'amplitude |
| $\mathrm{H3E}$ | téléphonie BLU à porteuse complète |
| $\mathrm{R3E}$ | téléphonie BLU à porteuse réduite |
| $\mathrm{J3E}$ | téléphonie BLU à porteuse supprimée — la SSB des radioamateurs |
| $\mathrm{F3E}$ | téléphonie en modulation de fréquence |
| $\mathrm{G3E}$ | téléphonie en modulation de phase |
| $\mathrm{F1B}$ | télégraphie par déplacement de fréquence, réception automatique — la RTTY |
| $\mathrm{J2B}$ | données sur sous-porteuse en BLU — les modes numériques usuels |
| $\mathrm{F2D}$ | données par modulation de fréquence d'une sous-porteuse — le packet |
| $\mathrm{N0N}$ | porteuse pure non modulée |

Assemblées avec leur largeur de bande, ces désignations donnent les écritures complètes que vous verrez sur les fiches techniques et dans les textes : $\mathrm{2K70J3E}$ pour une BLU téléphonique, $\mathrm{16K0F3E}$ pour une FM de trafic, $\mathrm{100HA1A}$ pour une télégraphie Morse à $25$ mots par minute.

Vérifiez au passage la cohérence avec les plafonds français : $\qty{2,70}{\kilo\hertz}$ tient partout, tandis que les $\qty{16}{\kilo\hertz}$ d'une FM dépassent le plafond de $\qty{12}{\kilo\hertz}$ applicable entre $\qty{28}{\mega\hertz}$ et $\qty{144}{\mega\hertz}$. La désignation n'est donc pas une formalité d'écriture : elle donne à lire, d'un coup d'œil, si une émission entre dans son gabarit réglementaire.

## Les deux symboles facultatifs

L'appendice 1 prévoit un quatrième et un cinquième symbole. Ils sont facultatifs, et l'usage radioamateur comme les textes français s'en tiennent aux trois premiers — mais les fiches techniques et les notifications officielles les emploient, et il faut savoir les lire. Lorsqu'on les omet tout en voulant marquer leur absence, la convention est de les remplacer par un tiret : $\mathrm{1K98J3C\text{-}\text{-}}$.

**Quatrième symbole — détails du signal :**

| Symbole | Détails |
| --- | --- |
| A | code bivalent, éléments différant en nombre ou en durée |
| B | code bivalent, éléments identiques, sans correction d'erreurs |
| C | code bivalent, éléments identiques, avec correction d'erreurs |
| D | code quadrivalent, chaque état représentant un élément de signal |
| E | code plurivalent, chaque état représentant un élément de signal |
| F | code plurivalent, chaque état ou combinaison représentant un caractère |
| G | son de qualité radiophonique, monophonique |
| H | son de qualité radiophonique, stéréophonique ou quadriphonique |
| J | son de qualité commerciale |
| K | son de qualité commerciale, avec inversion de fréquences |
| L | son de qualité commerciale, avec signaux séparés de commande de niveau |
| M | image en noir et blanc |
| N | image en couleur |
| W | combinaison des cas ci-dessus |
| X | cas non couverts |

**Cinquième symbole — nature du multiplexage :**

| Symbole | Multiplexage |
| --- | --- |
| N | pas de multiplexage |
| C | par répartition en code, étalement de spectre compris |
| F | par répartition en fréquence |
| T | par répartition dans le temps |
| W | combinaison des répartitions en fréquence et dans le temps |
| X | autres types |

## Calculer la largeur de bande nécessaire

La largeur de bande ne se devine pas : l'appendice donne une formule par famille d'émission. Trois intéressent directement le radioamateur.

**Télégraphie Morse par tout ou rien.** $B_n = B \cdot K$, où $B$ est la rapidité de modulation en bauds et $K$ vaut $5$ sur une liaison sujette aux évanouissements, $3$ sinon. À $25$ mots par minute, $B = 20$, d'où $B_n = \qty{100}{\hertz}$ : la désignation complète est $\mathrm{100HA1AAN}$, ou $\mathrm{A1A}$ en forme courte.

**Téléphonie en bande latérale unique à porteuse supprimée.** $B_n = M - f_\mathrm{min}$, différence entre la fréquence de modulation la plus haute et la plus basse. Avec $M = \qty{3000}{\hertz}$ et $f_\mathrm{min} = \qty{300}{\hertz}$, on obtient $\qty{2,7}{\kilo\hertz}$, soit $\mathrm{2K70J3EJN}$.

**Téléphonie en modulation de fréquence.** $B_n = 2M + 2DK$ — vous reconnaissez la formule de Carson, ici sous sa forme réglementaire. Avec une excursion $D = \qty{5}{\kilo\hertz}$, une modulante $M = \qty{3}{\kilo\hertz}$ et $K = 1$, la largeur vaut $\qty{16}{\kilo\hertz}$, soit $\mathrm{16K0F3EJN}$.

## Pourquoi cela vous servira

Le journal de bord, obligatoire en France, doit mentionner la classe d'émission de chaque liaison. Cette notation n'est donc pas un exercice scolaire : elle s'écrit tous les jours, et c'est aussi sous cette forme que les textes réglementaires désignent ce que vous avez le droit d'émettre.
</france>
