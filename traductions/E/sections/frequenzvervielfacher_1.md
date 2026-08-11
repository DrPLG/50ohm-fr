Autrefois, pour ne pas devoir construire et régler un oscillateur distinct pour chaque gamme de fréquences dans les émetteurs radioamateurs multibandes, on utilisait le principe de la multiplication de fréquence. Un oscillateur stable fonctionnait sur la fréquence de la bande la plus basse (par exemple $\qty{3,5}{\mega\hertz}$), et son signal de sortie était ensuite transposé sur les bandes radioamateurs souhaitées au moyen de multiplicateurs de fréquence. Il est avantageux, à cet égard, que les différentes bandes de fréquences soient dans des rapports fixes entre elles (par exemple $\qty{3,5}{\mega\hertz}$, $\qty{7}{\mega\hertz}$, $\qty{14}{\mega\hertz}$, etc.) et soient le plus souvent des multiples entiers de la bande la plus basse. De ce fait, les harmoniques retombent elles aussi dans une bande radioamateur, ce qui est tout à fait souhaité par les autorités de régulation, afin d'éviter que les harmoniques ne perturbent d'autres services. De manière générale, il est plus facile de concevoir et de construire des oscillateurs à haute stabilité sur les basses fréquences que sur les hautes fréquences. 

---

La figure [ref:n_f_vervielfacher] montre le schéma synoptique d'un multiplicateur de fréquence de facteur $2$, dans lequel la fréquence d'entrée est élevée de $\qty{3,5}{\mega\hertz}$ à $\qty{7}{\mega\hertz}$. Un multiplicateur de fréquence est typiquement réalisé au moyen d'une non-linéarité (par exemple une diode), qui produit de façon ciblée des harmoniques du signal d'entrée, parmi lesquelles la fréquence multiple souhaitée est ensuite sélectionnée à l'aide d'un filtre passe-bande.

<margin>
[picture:1042:n_f_vervielfacher:Schéma synoptique d'un multiplicateur de fréquence]
</margin>

On utilise fréquemment une chaîne de multiplicateurs de fréquence pour atteindre les facteurs de multiplication souhaités. Lorsque des multiplicateurs sont montés en cascade, leurs facteurs individuels se multiplient entre eux.
Inversement, un tel circuit peut naturellement aussi se calculer en sens inverse. Il faut alors diviser par les facteurs partiels correspondants.

[question:EF303]
[question:EF302]
[question:EF301]