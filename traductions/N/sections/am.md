Dans la modulation d'amplitude (AM), un signal modulant, p. ex. un signal vocal, est modulé sur la porteuse par variation de l'amplitude. La fréquence de la porteuse n'est pas influencée en AM : elle reste inchangée.

Nous avons déjà rencontré le cas le plus simple et le plus extrême avec la transmission de signaux Morse en Continuous Wave (CW). L'allumage et l'extinction de la porteuse au rythme du manipulateur Morse peuvent aussi se décrire comme une alternance entre amplitude minimale et maximale.

Pour moduler un signal vocal en AM, on exploite aussi la zone entre amplitude minimale et maximale. Le diagramme en chute d'eau de la figure [ref:n_Wasserfall0] montre un signal vocal modulé en amplitude. On reconnaît nettement au milieu la porteuse, ligne étroite à fréquence constante. Mais à gauche et à droite de la porteuse, on voit aussi quelque chose, alors que la fréquence de la porteuse n'a pas du tout été influencée !

<margin>
[picture:716:n_Wasserfall0:Signal d'un émetteur de radiodiffusion AM (voix/musique)]
</margin>

Cet effet inattendu provient de ce que la variation d'amplitude modifie la forme de la porteuse, qui ne correspond plus à une oscillation sinusoïdale pure. Ces fréquences supplémentaires s'appellent les *bandes latérales*. C'est en elles que réside l'information transmise, p. ex. la voix. La figure [ref:n_seitenband] montre une représentation symbolique usuelle de l'AM, avec la porteuse au milieu et les deux bandes latérales de part et d'autre.

<margin>
[picture:476:n_seitenband:Représentation symbolique d'un signal modulé en amplitude, avec porteuse et bandes latérales]
</margin>

<webindepth>
*Pourquoi des fréquences supplémentaires apparaissent-elles en AM à côté de la porteuse ?* Cela s'explique quand on comprend ce que représente exactement un spectre d'amplitude ou un diagramme en chute d'eau : il indique, pour chaque fréquence, la grandeur de l'amplitude. Plus précisément : il indique, pour toutes les oscillations sinusoïdales possibles de différentes fréquences, la force de leur amplitude. Si l'affichage réagit p. ex. à $\qty{144,3}{\mega\hertz}$, c'est qu'une oscillation sinusoïdale pure de fréquence $\qty{144,3}{\mega\hertz}$ est mesurée. Mais si l'affichage réagit simultanément à $\qty{144,300}{\mega\hertz}$ et à $\qty{144,301}{\mega\hertz}$, alors deux oscillations sinusoïdales ont été mesurées.

Regardons de nouveau, avec ce savoir, l'émission AM dans le diagramme en chute d'eau. Nous voyons maintenant qu'un grand nombre de fréquences différentes apparaissent entre $\qty{144,250}{\mega\hertz}$ et $\qty{144,350}{\mega\hertz}$ avec des amplitudes variées. De nombreuses oscillations sinusoïdales différentes sont donc mesurables en même temps.

[picture:738:n_seitenband_frequenzen_einzeln:Plusieurs oscillations sinusoïdales de fréquences différentes]

Reste la question : pourquoi une seule oscillation sinusoïdale, déformée par la modulation, devient-elle soudain plusieurs oscillations sinusoïdales ? Pour y répondre, prenons le chemin inverse. Si l'on prend plusieurs oscillations sinusoïdales de fréquences différentes et qu'on les additionne, on obtient une oscillation « déformée » !

[picture:739:n_seitenband_frequenzen_addiert:Somme de plusieurs oscillations sinusoïdales de fréquences différentes]

Ce sont simplement deux points de vue différents : on peut y voir soit une oscillation déformée, soit une somme de plusieurs oscillations sinusoïdales. Et c'est la raison pour laquelle la variation d'amplitude d'une porteuse fait apparaître d'autres fréquences à côté de la porteuse dans le diagramme en chute d'eau.
</webindepth>

[question:NE202]
[question:NE206]

La largeur de bande occupée par l'AM est d'ailleurs le double de la fréquence la plus haute du signal modulant. Dans notre exemple de la section précédente, la fréquence la plus haute était $\qty{2700}{\hertz}$. Ce signal occuperait donc, en émission AM, une largeur de bande de $\qty{5400}{\hertz}$.
