Dans la classe N, nous avons appris : si une antenne est parfaitement adaptée à sa ligne d'alimentation (par exemple un câble coaxial), le SWR-mètre indique la valeur 1. C'est le meilleur cas possible, puisque la totalité de la puissance d'émission est absorbée par l'antenne et qu'aucune puissance n'est réfléchie vers l'émetteur. Si, en revanche, aucune antenne n'est raccordée, ou si la ligne de transmission est interrompue ou court-circuitée, la valeur du SWR tend vers l'infini ($\infty$). Dans ces cas, la puissance d'émission est presque entièrement réfléchie. Une telle réflexion totale peut, dans le pire des cas, endommager l'étage final de l'émetteur. Dans la classe E, nous approfondissons maintenant quelque peu le sujet et faisons aussi connaissance avec des valeurs comprises entre $\num{1}$ et $\infty$.

Le rapport d'ondes stationnaires (SWR), de symbole $s$, peut se calculer à partir de la puissance directe $P_\text{V}$ et de la puissance réfléchie $P_\text{R}$. Nous trouvons la relation correspondante dans le recueil de formules :

$s = \frac{\sqrt{P_\text{V}}+\sqrt{P_\text{R}}} { \sqrt{P_\text{V}}-\sqrt{P_\text{R}}}$

Si, par exemple, l'émetteur délivre une puissance de $P_\text{V}=\qty{100}{\watt}$ et que $P_\text{R}=\qty{25}{\watt}$ sont réfléchis par l'antenne en direction de l'émetteur, on obtient :

$s = \frac{\sqrt{100}+\sqrt{25}}{\sqrt{100}-\sqrt{25}} = \frac{10+5}{10-5} = \frac{15}{5} = 3$

Cela signifie qu'un SWR de $\num{3}$ correspond à une réflexion de $\frac{\qty{25}{\watt}}{\qty{100}{\watt}}=\qty{25}{\percent}$. D'autres correspondances sont présentées dans le tableau [ref:e_swr_werte].

<margin>
| l: SWR | l: Puissance réfléchie |
| $\num{1}$ | $\qty{0}{\percent}$ |
| $\num{1,5}$ | $\qty{4}{\percent}$ |
| $\num{2}$ | $\qty{11,1}{\percent}$ |
| $\num{2,5}$ | $\qty{18,4}{\percent}$ |
| *$\num{3}$* | *$\qty{25}{\percent}$* |
| $\num{4}$ | $\qty{36}{\percent}$ |
| $\num{6}$ | $\qty{51}{\percent}$ |
| $\num{10}$ | $\qty{66,9}{\percent}$ |
| $\num{20}$ | $\qty{81,9}{\percent}$ |
| $\infty$ | $\qty{100}{\percent}$ |
[table:e_swr_werte:Valeurs de SWR en rapport avec la puissance réfléchie]
</margin>

---

<tip>
Pour répondre aux questions suivantes, il suffit de savoir qu'un rapport d'ondes stationnaires de $\num{3}$ correspond à une réflexion de $\qty{25}{\percent}$ de l'énergie, c'est-à-dire que l'onde réfléchie transporte un quart de l'énergie de l'onde directe. En conséquence, seuls $\qty{75}{\percent}$ de l'énergie sont délivrés à l'extrémité de la ligne, par exemple à une antenne ou à une résistance de perte (donc non réfléchis). 
</tip>

[question:EG401]
[question:EG402]
[question:EG403]
