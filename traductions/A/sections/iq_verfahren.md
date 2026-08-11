% TODO neu formulieren
% Idee DL9MJ: Beispiel mit Bild je ein Bit in I und Q und wie das Signal für 00, 01, 10, 11 aussieht

La QAM peut être produite de façon particulièrement simple à l'aide de deux porteuses de même fréquence. L'une des deux porteuses doit alors être déphasée de $\qty{90}{\degree}$. Les deux porteuses sont ensuite modulées en amplitude, chacune par un signal propre. L'un des signaux est désigné par I (pour In-Phase Component) et l'autre par Q (pour Quadrature Phase Component). La porteuse déphasée est modulée par le signal Q. Les deux porteuses modulées sont ensuite superposées, ce qui donne une porteuse qui varie à la fois en amplitude et en phase.

<indepth>
[include:applet_iq]
</indepth>
  
%TODO BILD QAM4 QAM8 oder mehr?

[question:AE404]
[question:AF632]

L'idée de base, consistant à traiter séparément un signal en deux parties, trouve elle aussi une large application en traitement numérique du signal. On la désigne, d'après les deux signaux partiels, sous le nom de procédé I/Q. Le procédé I/Q permet de produire n'importe quel signal. Pour cela, le flux de données à moduler se compose d'une composante I et d'une composante Q. Deux convertisseurs N/A transforment chacun l'une des deux composantes en un signal analogique I ou Q. Les signaux I et Q modulent à leur tour les deux porteuses déphasées. À la dernière étape, celles-ci sont superposées en une seule porteuse, qui est émise.

On procède de façon correspondante du côté du récepteur. Le signal d'entrée est mélangé avec une porteuse pour obtenir le signal I, qui est ensuite transformé, au moyen d'un convertisseur A/N, en la composante I d'un flux de données. Simultanément, le signal d'entrée est également mélangé avec une porteuse déphasée de $\qty{90}{\degree}$ pour obtenir le signal Q, lui-même transformé, au moyen d'un convertisseur A/N, en la composante Q du flux de données.

[question:AF633]

Un tel flux de données numériques peut toujours représenter une certaine plage de fréquences du signal d'entrée, située autour d'une fréquence centrale. Si le signal d'entrée est par exemple mélangé avec une porteuse à $\qty{435}{\mega\hertz}$ et avec une porteuse à $\qty{435}{\mega\hertz}$ déphasée de $\qty{90}{\degree}$, et que les deux signaux obtenus sont numérisés par des convertisseurs A/N, le flux de données I/Q ainsi produit représente la plage de fréquences située autour de $\qty{435}{\mega\hertz}$.

% TODO Verweis auf Abtasttheorem?
La largeur de bande couverte dépend ici de la fréquence d'échantillonnage de la conversion A/N. La largeur de bande en Hz correspond alors à la fréquence d'échantillonnage en samples par seconde. Si, dans notre exemple, la composante I comme la composante Q sont échantillonnées à 10 millions de samples par seconde, le flux de données I/Q obtenu peut couvrir une plage de fréquences de $\qty{10}{\mega\hertz}$ de largeur de bande, soit de $\qty{-5}{\mega\hertz}$ à $\qty{+5}{\mega\hertz}$ par rapport à la fréquence centrale. Le flux de données couvre donc alors les fréquences de $\qty{430}{\mega\hertz}$ à $\qty{440}{\mega\hertz}$.

[question:AF634]
[question:AF635]
[question:AF636]
