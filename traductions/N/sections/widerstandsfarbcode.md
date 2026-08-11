Nous avons maintenant fait connaissance avec la résistance et son unité $\unit{\ohm}$ (ohm). En pratique, toutefois, la valeur numérique n'est le plus souvent pas imprimée sur les résistances. On utilise à la place des anneaux de couleur. Ces anneaux de couleur codent la valeur de la résistance.

<margin>
[picture:665:n_widerstandsfarbcodes: Une résistance avec 4 anneaux de couleur]
</margin>

La figure [ref:n_widerstandsfarbcodes] montre une résistance avec quatre anneaux de couleur. Chaque couleur correspond à une valeur numérique, comme le montre le tableau [ref:n_widerstandsfarbcodes_tabelle] dans la colonne *Valeur* :
* Le premier anneau de couleur correspond au premier chiffre, dans ce cas *jaune*, donc quatre.
* Le deuxième anneau de couleur correspond au deuxième chiffre, dans notre exemple *violet*, donc sept.
* Le troisième anneau de couleur est ce qu'on appelle le multiplicateur (voir tableau [ref:n_widerstandsfarbcodes_tabelle]), dans notre cas *orange*, donc la valeur 1000.

<webmargin>
| X:Couleur | l:Valeur | l:Multiplicateur | l:Tolérance |
| Argent | - | $\num{0,01}$ | $\qty{\pm 10}{\percent}$ |
| Or | - | $\num{0,1}$ | $\qty{\pm 5}{\percent}$ |
| Noir | 0 | $\num{1}$ | - |
| Marron | 1 | $\num{10}$ | $\qty{\pm 1}{\percent}$ |
| Rouge | 2 | $\num{100}$ | $\qty{\pm 2}{\percent}$ |
| Orange| 3 | $\num{1000}$ | - |
| Jaune | 4 | $\num{10000}$ | - |
| Vert | 5 | $\num{100000}$ | - |
| Bleu | 6 | $\num{1000000}$ | $\qty{\pm 0,25}{\percent}$ |
| Violet | 7 | $\num{10000000}$ | $\qty{\pm 0,1}{\percent}$ |
| Gris | 8 | $\num{100000000}$ | - |
| Blanc | 9 | $\num{1000000000}$ | - |
| Aucun | - | - | $\qty{\pm 20}{\percent}$ |
[table:n_widerstandsfarbcodes_tabelle:Tableau des codes couleur des résistances]
</webmargin>

Le premier et le deuxième anneau donnent ensemble le nombre 47. En multipliant ce nombre par le multiplicateur, on peut calculer la valeur de la résistance :

$ 47 \cdot \qty{1000}{\ohm} = \qty{47000}{\ohm} = \qty{47}{\kilo\ohm} $

---

Il reste encore un quatrième anneau de couleur. Celui-ci représente ce qu'on appelle la tolérance, qui indique de combien la valeur réelle de la résistance peut s'écarter de la valeur indiquée.
Plus de détails à ce sujet suivront dans la classe E. 

<indepth>
*Approfondissement :* dans notre exemple, le dernier anneau est *argent*, ce qui signifie une tolérance de $\qty{\pm 10}{\percent}$. La valeur réelle de la résistance peut être supérieure ou inférieure de $\qty{10}{\percent} \cdot \qty{47}{\kilo\ohm} = \qty{4,7}{\kilo\ohm}$ à la valeur indiquée. Elle peut donc se situer entre $\qty{42,3}{\kilo\ohm}$ et $\qty{51,7}{\kilo\ohm}$.
</indepth>

---

Il n'est pas nécessaire d'apprendre par cœur le tableau des codes couleur. Il est fourni, en tant que partie du formulaire, comme document d'aide lors de l'examen. Il faut toutefois retenir la disposition des anneaux et leur signification. Pour s'exercer, les questions suivantes peuvent être résolues à l'aide du code couleur, afin d'acquérir de la routine.

<indepth>
*Approfondissement :* il existe aussi des résistances avec plus de quatre anneaux de couleur. Celles-ci ne sont toutefois pas pertinentes pour l'examen. D'autres composants sont aussi souvent marqués avec des anneaux de couleur.
</indepth>

[question:NC107]
[question:NC105]
[question:NC106]
[question:NC104]
[question:NC103]
[question:NC102]
[question:NC108]
[question:NC109]
[question:NC110]
