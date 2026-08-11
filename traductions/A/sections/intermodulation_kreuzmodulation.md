Dans un récepteur à l'entrée duquel sont présents deux signaux HF forts, des perturbations peuvent être causées par intermodulation ou par transmodulation.
Dans le cas de l'intermodulation, cet effet se manifeste par la création de fréquences supplémentaires indésirables, du fait du comportement non linéaire de l'étage du récepteur (fonctionnement dans la zone limite non linéaire), de façon analogue à ce qui se passe dans un mélangeur. Celles-ci peuvent se superposer aux signaux de réception souhaités et les perturber.
Dans le cas de la transmodulation, cet effet se manifeste par le fait que le signal de réception souhaité est influencé par la modulation d'un signal AM voisin en fréquence et de forte amplitude. La modulation de l'émetteur voisin devient de ce fait audible dans le signal reçu et le perturbe.

[question:AF217]
[question:AF219]
[question:AF222]
[question:AF218]

Pour supprimer un signal indésirable fort dès avant l'entrée du récepteur, un circuit d'absorption accordé sur la fréquence exacte du signal perturbateur, placé devant l'entrée du récepteur, peut par exemple apporter une solution.

[question:AF223]

La tenue aux forts signaux d'un récepteur peut être décrite par ce qu'on appelle le point d'interception d'ordre 3 (IP3). Il est une mesure du point auquel les produits de mélange indésirables du 3e ordre atteignent la valeur d'amplitude du signal d'entrée. Plus l'IP3 d'un récepteur est élevé, plus les signaux que celui-ci peut encore traiter sans perturbation sont importants.

<indepth>
Nous considérons dans cet approfondissement l'IP3 en tant que grandeur caractéristique de la tenue aux forts signaux d'un récepteur. De manière générale, les produits de mélange naissent des non-linéarités dans les amplificateurs, les mélangeurs ou d'autres étages du récepteur. Avec deux signaux d'entrée $f_1$ et $f_2$, il peut apparaître des produits d'intermodulation de la forme

$f_\text{mix} = \left| m \cdot f_1 \pm n \cdot f_2 \right|$

où $m,n \in \mathbb{N}_0$ et où les deux coefficients ne doivent pas être nuls simultanément. L'ordre d'un tel produit de mélange résulte de la somme des coefficients :

$\text{Ordre} = m+n$

Les produits d'intermodulation du 3e ordre sont particulièrement critiques, car ils se situent souvent de nouveau à proximité des signaux d'entrée d'origine. Ils peuvent de ce fait tomber dans la plage de réception souhaitée et ne sont alors que difficilement, voire pas du tout, éliminables par les filtres placés en aval.

La figure suivante [ref:a_intermodulation] représente l'intermodulation de deux signaux $f_1$ et $f_2$. Les produits d'intermodulation du 3e ordre y sont particulièrement mis en évidence :

[picture:1095:a_intermodulation:Intermodulation de deux signaux $f_1$ et $f_2$]

Un point important : ces produits d'intermodulation ne sont pas reçus de l'extérieur, ils naissent dans le récepteur même, du fait de son comportement non linéaire. Un test à deux tons permet d'examiner la linéarité d'un récepteur. On y injecte pour cela deux signaux d'entrée définis. Si, à côté de ces deux signaux fondamentaux, des produits d'intermodulation du 3e ordre apparaissent en plus dans le spectre, par exemple dans le diagramme en cascade, c'est là un indice de comportement non linéaire.

La figure [ref:a_zweitontest] montre un test à deux tons avec balayage en puissance, dans lequel les produits d'intermodulation du 3e ordre deviennent nettement visibles.

[picture:1096:a_zweitontest:Test à deux tons avec balayage en puissance]

Si l'on porte la puissance de sortie en fonction de la puissance d'entrée, les signaux fondamentaux croissent dans la zone linéaire avec une pente de $1{:}1$. Les produits d'intermodulation du 3e ordre croissent en revanche avec une pente de $3{:}1$. En prolongeant les parties linéaires de ces deux courbes, on obtient un point d'intersection théorique. Ce point est appelé IP3, c'est-à-dire point d'interception du 3e ordre.

L'IP3 décrit ainsi le point extrapolé auquel les produits d'intermodulation du 3e ordre atteindraient par le calcul la même puissance de sortie que les signaux fondamentaux. En pratique, ce point n'est généralement pas atteint, car le récepteur entre auparavant en compression ou en saturation.

Plus l'IP3 d'un récepteur est élevé, meilleure est sa tenue aux forts signaux. Un IP3 élevé signifie que même de forts signaux voisins peuvent être traités sans que des produits d'intermodulation gênants n'apparaissent dans la plage de réception souhaitée.
</indepth>

[question:AF221]

Pour réduire l'apparition de produits de mélange indésirables à l'entrée du récepteur du fait de signaux forts, on peut placer en amont, à l'entrée du récepteur, un atténuateur commutable. Les produits d'intermodulation ainsi que la transmodulation dans le récepteur s'en trouvent réduits. Le signal utile n'est ici réduit que du facteur de l'atténuateur — les produits de mélange gênants sont en revanche affaiblis, en raison des lois mathématiques du processus de mélange, du facteur $\num{3}$ (3e ordre) en $\unit{\dB}$. Par exemple, un atténuateur de $\qty{10}{\dB}$ ne réduit le signal utile que de $\qty{10}{\dB}$, tandis que les produits de mélange indésirables sont déjà atténués de $\qty{30}{\dB}$.

[question:AF220]