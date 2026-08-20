Les signaux peuvent être représentés de différentes manières. Jusqu'à présent, nous avons souvent considéré le *domaine temporel*. On y représente par exemple comment la tension d'un signal varie avec le temps. Le même signal peut cependant aussi être considéré dans le *domaine fréquentiel*. On n'y représente plus l'allure temporelle, mais les composantes de fréquence dont le signal se compose et l'importance de chacune d'elles. Cette représentation est aussi appelée *spectre de fréquences*. Elle repose sur le fait que les signaux périodiques peuvent être décrits comme la superposition d'oscillations sinusoïdales de fréquence, d'amplitude et de phase différentes. Un signal sinusoïdal pur ne se compose par exemple que d'une seule fréquence et n'apparaît donc, dans le spectre de fréquences, qu'à cette fréquence.

La *transformation de Fourier* permet de passer du domaine temporel au domaine fréquentiel et inversement. Elle décompose mathématiquement un signal en ses différentes composantes de fréquence. Pour les signaux disponibles sous forme numérique, à temps discret, on utilise pour cela la *transformation de Fourier discrète* (DFT). Le calcul direct d'une DFT peut être très lourd lorsque le nombre d'échantillons est grand. La *transformation de Fourier rapide* (FFT) met à disposition un algorithme nettement plus efficace pour le calcul de la DFT. C'est pourquoi la FFT est fréquemment employée en logiciel et en matériel numérique, par exemple pour déterminer le spectre de fréquences d'un signal.

<indepth>
Les formes de signal non sinusoïdales se composent de plusieurs composantes de fréquence. Les variations et les arêtes vives dans l'allure temporelle du signal exigent en particulier des composantes supplémentaires à fréquence élevée. L'applet suivant permet d'examiner comment différentes oscillations sinusoïdales se superposent et font naître différentes formes de signal.

[include:fourier]
</indepth>

[question:AF630]

---

Le lien entre domaine temporel et domaine fréquentiel apparaît particulièrement nettement pour les signaux présentant des arêtes vives. Un signal rectangulaire idéal peut par exemple être composé d'une fondamentale et de plusieurs harmoniques. À côté de la fréquence fondamentale apparaissent alors les multiples impairs de celle-ci. Leurs amplitudes diminuent à mesure que la fréquence augmente.

Ces harmoniques ont aussi leur importance pour les émetteurs. Si un signal rectangulaire idéal était par exemple appliqué directement à une antenne, ses harmoniques seraient rayonnées à côté de la fréquence fondamentale souhaitée. Un filtre passe-bas peut supprimer les composantes de fréquence élevée indésirables, de sorte que seule la fondamentale souhaitée parvienne pour l'essentiel à l'antenne.

Pour quelques formes de signal périodiques typiques, le spectre de fréquences se décrit particulièrement simplement. Nous considérons ici des formes de signal idéalisées, sans composante continue :

* Un *signal sinusoïdal* ne se compose que d'une seule fréquence. Seule la fréquence fondamentale $f$ apparaît donc dans le spectre de fréquences.
* Un *signal rectangulaire* se compose de la fréquence fondamentale et des *multiples impairs* de celle-ci. Il contient donc les fréquences $f$, $3\cdot f$, $5\cdot f$, $7\cdot f$, etc. Les amplitudes des harmoniques diminuent à mesure que la fréquence augmente.
* Un *signal en dents de scie* contient aussi bien les multiples pairs que les multiples impairs de la fréquence fondamentale. Il contient donc $f$, $2\cdot f$, $3\cdot f$, $4\cdot f$, $5\cdot f$, etc. Là encore, les amplitudes diminuent à mesure que la fréquence augmente.
* Un *signal triangulaire* ne contient, comme le signal rectangulaire, que les multiples impairs de la fréquence fondamentale, soit $f$, $3\cdot f$, $5\cdot f$, $7\cdot f$, etc. Les amplitudes des composantes de fréquence élevée décroissent cependant nettement plus vite que pour le signal rectangulaire.

Les formes de signal peuvent ainsi être distinguées d'après leur spectre de fréquences. Une composante spectrale unique indique un signal sinusoïdal. Si des multiples impairs apparaissent, il s'agit toujours, dans les questions d'examen, d'un signal rectangulaire.

[question:AB404]
[question:AB405]
[question:AB406]
[question:AB407]
