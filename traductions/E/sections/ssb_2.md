En classe N, nous avons appris qu'avec la modulation d'amplitude, deux bandes latérales apparaissent à côté de la porteuse, une inférieure (LSB) et une supérieure (USB), qui contiennent toute l'information du signal modulant, tandis que la porteuse elle-même ne transporte aucune information. Comme les deux bandes latérales contiennent la même information, il suffit de n'en émettre qu'une seule et de supprimer la porteuse (cf. figure [ref:e_ssb_am_modulation]). Ce procédé s'appelle la modulation à bande latérale unique, ou Single Sideband (SSB), que nous avons également déjà rencontrée en classe N. L'avantage de la SSB est qu'aucune puissance d'émission n'est gaspillée pour la porteuse et la seconde bande latérale, de sorte que toute la puissance peut être utilisée efficacement pour la transmission de l'information, tandis que la largeur de bande nécessaire est nettement plus faible qu'en AM.


Avec la modulation à bande latérale unique (SSB), le signal émis contient — selon la bande latérale choisie sur l'émetteur-récepteur — soit la fréquence porteuse plus la fréquence de modulation BF (en USB), soit la fréquence porteuse moins la fréquence de modulation BF (en LSB). La figure [ref:e_ssb_einzelsignal] en montre deux exemples : si l'on module en USB un émetteur de fréquence porteuse $\qty{7,100}{\mega\hertz}$ avec un signal BF de $\qty{1}{\kilo\hertz}$, l'émetteur rayonne une fréquence de $\qty{7,100}{\mega\hertz} + \qty{1}{\kilo\hertz} = \qty{7,101}{\mega\hertz}$. Si l'on module en revanche l'émetteur en LSB, celui-ci rayonne une fréquence de $\qty{7,100}{\mega\hertz} -\qty{1}{\kilo\hertz} = \qty{7,099}{\mega\hertz}$.

<margin>
[picture:1056:e_ssb_einzelsignal:Bandes latérales en AM et en SSB]
</margin>

Les questions suivantes peuvent être résolues selon ce schéma.

[question:EE203]
[question:EE204]

---

Les signaux AM transmettent les deux bandes latérales et la porteuse, et ont donc une largeur de bande d'un peu plus du double de celle du signal BF modulant (cf. figure [ref:e_ssb_einzelsignal]). La largeur de bande d'un signal SSB correspond à peu près à la largeur de bande du signal BF modulant (après filtrage et limitation de la largeur de bande du signal BF). En SSB, les composantes du signal en dessous de $\qty{300}{\hertz}$ ainsi que la porteuse ($\qty{0}{\hertz}$) ne sont pas non plus transmises et sont supprimées. La SSB occupe donc un peu moins de la moitié de la largeur de bande de l'AM.

<margin>
[picture:743:e_ssb_einzelsignal:Bandes latérales en AM et en SSB]
</margin>

[question:EE202]
[question:EE201]

---

Comme nous l'avons déjà appris en classe N au sujet de la télégraphie Morse en *Continuous Wave* (CW), une porteuse haute fréquence constante y est mise en marche et arrêtée selon un certain rythme. Les signaux CW nécessitent la plus faible largeur de bande en comparaison des signaux modulés par la voix comme l'AM et la SSB. Cela tient au fait qu'en CW, une seule fréquence est manipulée, et non, comme pour les signaux vocaux, plusieurs composantes de fréquence d'un signal BF transmises simultanément.

<indepth>
La largeur de bande des signaux CW dépend de la vitesse de manipulation et s'élève, pour des vitesses de transmission moyennes de 20 mots par minute (100 caractères par minute), à environ $\qty{300}{\hertz}$.
</indepth>

[question:EE207]

Pour éviter de perturber les stations voisines dans la bande de fréquences, la largeur de bande occupée par un signal SSB devrait être limitée à environ $\qty{2,7}{\kilo\hertz}$ au maximum. Cette largeur de bande est tout à fait suffisante pour une bonne intelligibilité de la parole. C'est pourquoi le signal BF du microphone est limité en bande dans l'émetteur : les composantes de fréquence en dessous d'environ $\qty{300}{\hertz}$ ainsi qu'au-dessus d'environ $\qty{3}{\kilo\hertz}$ sont supprimées, car elles ne contribuent que peu à l'intelligibilité de la parole.

[question:EJ211]
[question:EJ210]

En pratique, les filtres SSB servant à produire un signal SSB ont souvent une largeur de bande d'environ $\qty{2,4}{\kilo\hertz}$ seulement. Cette largeur de bande plus réduite suffit elle aussi, dans de nombreux cas, pour une bonne intelligibilité de la parole, tout en permettant une utilisation encore plus efficace du spectre de fréquences disponible.

[question:EF310]

Des perturbations des stations voisines peuvent aussi être causées par ce qu'on appelle le *splatter*, qui peut résulter d'un gain de microphone réglé trop haut et donc d'une saturation des étages BF. Dans le signal émis, cela se traduit par une augmentation de la largeur de bande de la transmission SSB, ce qui peut perturber d'autres stations.

[question:EJ215]

Un gain de microphone trop faible (amplitude BF) conduit à une modulation plus faible de l'émetteur SSB, ce qui a pour conséquence une diminution de la puissance de sortie. Il est donc important que le gain de microphone soit réglé de manière optimale pour une bonne communication en SSB (ni trop fort, ni trop faible). Nous y reviendrons plus en détail dans le chapitre sur le compresseur de dynamique. 

[question:EE206]
[question:EE205]