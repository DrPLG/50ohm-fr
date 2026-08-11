La synthèse numérique directe (Direct Digital Synthesis ou en abrégé DDS) sert à produire des signaux périodiques à bande limitée avec une haute résolution en fréquence.
Outre la synthèse de signaux au moyen de boucles d'asservissement PLL, cette méthode de production de signal est aujourd'hui très répandue en technique des télécommunications et de la mesure et constitue l'état actuel de la technique. Les signaux y sont réglables très finement en fréquence, contrairement à une PLL classique.

Principe de fonctionnement fondamental d'une DDS :

Au moyen d'un générateur d'horloge à fréquence fixe, un compteur d'adresses est incrémenté en permanence. Lors du débordement du compteur d'adresses, celui-ci repart de zéro. Une suite croissante de valeurs binaires est ainsi produite à sa sortie. Au moyen de ces valeurs, une table de sinus est parcourue en permanence. À la sortie de la table de sinus sont ainsi générées des valeurs d'amplitude numériques pour une oscillation sinusoïdale, qui sont ensuite transmises à un registre. Les valeurs d'amplitude numériques sont ensuite appliquées, par cadencement du registre, à un convertisseur N/A placé en aval, qui les convertit alors en un signal analogique (oscillation sinusoïdale) et le délivre en sortie.

<indepth>
Une DDS peut aussi parcourir différentes tables de valeurs, de sorte que des formes de signal cycliques quelconques peuvent également être générées. Par la commande du compteur d'adresses (au moyen d'un tuning-word), qui influence en permanence le pas du compteur, la fréquence à laquelle la table de valeurs est parcourue peut être commandée dans de larges limites.
Pour le registre d'adresses, on utilise souvent des registres de $\qty{32}{\bit}$ ou plus, dont seul un nombre plus restreint de bits de poids fort (par ex. les $\qty{14}{\bit}$ supérieurs) est ensuite utilisé pour parcourir la table de valeurs. Il est ainsi possible de délivrer aussi des fractions de la fréquence d'horloge, et la résolution en fréquence de la DDS s'en trouve augmentée.
L'avantage d'une DDS par rapport à une PLL est que, par la commande des paramètres précités, une résolution en fréquence quasiment quelconque peut être atteinte. De plus, on peut passer rapidement d'une fréquence à l'autre (par commande au moyen du tuning-word) sans phénomène transitoire d'établissement.

La qualité du signal de sortie d'une DDS dépend essentiellement de la qualité du générateur d'horloge utilisé (stabilité, jitter). De plus, la résolution en amplitude (quantification) du convertisseur N/A et sa linéarité sont elles aussi déterminantes pour la qualité du signal de sortie.
</indepth>

[question:AD620]