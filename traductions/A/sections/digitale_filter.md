Un avantage essentiel du traitement numérique des signaux est que les informations disponibles sous forme numérique peuvent être traitées de façon quasiment quelconque. Une suite d'échantillons d'entrée est convertie, au moyen de fonctions mathématiques, en une suite d'échantillons de sortie. Les filtres numériques simples, tels que les passe-bas, passe-bande ou passe-haut, peuvent être réalisés de deux manières différentes : en filtres FIR et en filtres IIR. FIR signifie *Finite Impulse Response* (réponse impulsionnelle finie) et IIR *Infinite Impulse Response* (réponse impulsionnelle infinie).

La caractéristique principale des filtres FIR est, comme l'indique déjà la désignation « finite » (en français : finie), que seul un nombre limité d'échantillons d'entrée est utilisé pour le calcul d'un échantillon de sortie. Les filtres IIR emploient en revanche, en plus, des échantillons de sortie déjà calculés, qui sont réinjectés à l'entrée du calcul. Du fait de cette réaction, un échantillon d'entrée isolé peut théoriquement influencer les échantillons de sortie suivants pendant une durée illimitée.

Les filtres numériques peuvent être mis en œuvre aussi bien de façon logicielle sur un DSP que dans du matériel programmable sur un FPGA. Il existe en outre ce que l'on appelle des *mixed signal frontends*, qui réalisent différentes fonctions de traitement du signal, comme par exemple des filtres de décimation, en même temps que des convertisseurs A/N et N/A sur une même puce, afin de les exécuter de la façon la plus économe en énergie possible et de décharger les étages de traitement du signal qui suivent.

[question:AF631]

<indepth>
[picture:1133:a_fir:Filtre FIR]

La figure [ref:a_fir] montre schématiquement la structure d'un filtre FIR. Un échantillon d'entrée est écrit dans une mémoire d'entrée. À chaque coup d'horloge, les valeurs mémorisées sont décalées d'une case mémoire, comme dans un registre à décalage. Les prises des différentes cases mémoire sont multipliées par les coefficients de filtrage correspondants, puis additionnées. Le résultat est délivré comme échantillon de sortie.

Si l'on suppose que les quatre coefficients de filtrage valent chacun $\frac{1}{4}$, les quatre derniers échantillons d'entrée sont chacun multipliés par $\frac{1}{4}$, puis additionnés. L'échantillon de sortie est ainsi la moyenne des quatre derniers échantillons d'entrée. Un tel filtre est aussi appelé *moyenne glissante*.

Une suite d'entrée $0,0,0,4,0,0,0,0$ conduit ainsi à la suite de sortie $0,0,0,1,1,1,1,0$.

Le filtre lisse donc les variations rapides, c'est-à-dire les composantes à fréquence élevée du signal d'entrée. Les variations lentes, autrement dit les basses fréquences, sont largement laissées passer, tandis que les variations rapides, autrement dit les composantes à fréquence élevée, sont atténuées. Une moyenne glissante agit par conséquent comme un filtre passe-bas numérique très simple.

Le filtre exécute ce que l'on appelle une opération de convolution ; celle-ci est d'ailleurs aussi à la base de nombreux réseaux de neurones qui animent l'intelligence artificielle.
</indepth>
