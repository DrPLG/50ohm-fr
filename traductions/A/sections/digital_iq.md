Dans l'un des chapitres précédents, nous avons découvert la représentation I/Q et le modulateur I/Q. Dans un système numérique, les deux composantes I et Q sont traitées comme deux flux de données numériques distincts. Ceux-ci peuvent être produits, modifiés et exploités par traitement numérique du signal.

Du côté du récepteur, le signal d'entrée est pour cela mélangé avec deux signaux de même fréquence, déphasés de $\qty{90}{\degree}$ l'un par rapport à l'autre. Il en résulte un signal I et un signal Q. Les deux signaux sont ensuite numérisés chacun par un convertisseur A/N et peuvent alors être traités numériquement. Du côté de l'émetteur, le processus fonctionne en sens inverse : des flux de données numériques I et Q sont convertis en signaux analogiques par deux convertisseurs N/A, puis appliqués à un modulateur I/Q.

Un flux de données I/Q numérique peut représenter une plage de fréquences située autour d'une fréquence centrale déterminée. Les fréquences inférieures à la fréquence centrale sont alors décrites par des écarts de fréquence négatifs, et les fréquences supérieures à la fréquence centrale par des écarts de fréquence positifs.

Si un signal d'entrée est par exemple mélangé avec deux signaux de $\qty{435}{\mega\hertz}$ chacun, déphasés de $\qty{90}{\degree}$ l'un par rapport à l'autre, le flux de données I/Q obtenu représente une plage de fréquences située autour de la fréquence centrale de $\qty{435}{\mega\hertz}$.

L'étendue de cette plage de fréquences dépend de la fréquence d'échantillonnage. Si I et Q sont tous deux échantillonnés à une fréquence d'échantillonnage $f_\mathrm{S}$, on peut idéalement représenter une plage de fréquences de

$-\frac{f_\mathrm{S}}{2}\text{ à }+\frac{f_\mathrm{S}}{2}$

autour de la fréquence centrale. La bande passante représentable au total correspond ainsi à la fréquence d'échantillonnage $f_\mathrm{S}$.

Si par exemple I et Q sont échantillonnés chacun à $\qty{10}{\mega\sps}$, le flux de données I/Q peut représenter une plage de fréquences de $\qty{-5}{\mega\hertz}$ à $\qty{+5}{\mega\hertz}$ autour de la fréquence centrale. Pour une fréquence centrale de $\qty{435}{\mega\hertz}$, cela correspond à une plage de fréquences de $\qty{430}{\mega\hertz}$ à $\qty{440}{\mega\hertz}$.

[question:AF634]
[question:AF635]
[question:AF636]
