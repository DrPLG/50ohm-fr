<margin>
[picture:978:a_swr:Onde stationnaire]
</margin>
Dans de nombreux cas, on peut indiquer simplement le rapport d'ondes stationnaires lorsque la résistance d'alimentation d'une antenne est connue. Pour autant qu'une antenne (ou une charge fictive) ne se comporte ni de façon inductive ni de façon capacitive, c'est-à-dire qu'elle constitue une résistance active pure, le rapport d'ondes stationnaires résulte du rapport entre la résistance de charge et l'impédance caractéristique de la ligne, le numérateur et le dénominateur devant être choisis de sorte que l'on obtienne un SWR supérieur ou égal à un.

Une antenne présentant une résistance d'alimentation de $\qty{100}{\ohm}$ provoque, lorsqu'elle est alimentée par un câble de $\qty{50}{\ohm}$, un rapport d'ondes stationnaires de $\num{2}$, car la résistance d'alimentation est deux fois plus grande. Une antenne présentant une résistance d'alimentation de $\qty{10}{\ohm}$ aurait un rapport d'ondes stationnaires de $\num{5}$, car l'impédance caractéristique de la ligne est cinq fois plus grande.

Pour répondre à la question suivante, nous devons en outre nous souvenir que la résistance d'un dipôle replié vaut un peu moins de $\qty{300}{\ohm}$.

[question:AG405]

L'effet de l'atténuation de ligne sur le rapport d'ondes stationnaires est trompeur. Plus une ligne présente de pertes, plus le rapport d'ondes stationnaires sur cette ligne peut se révéler petit (donc « bon »). Cela tient à ce qu'une ligne à pertes réduit aussi bien la puissance directe que la puissance réfléchie. Même si aucune antenne n'est raccordée en bout de ligne (circuit ouvert ou court-circuit) et que $\qty{100}{\percent}$ de l'énergie y est réfléchie, c'est-à-dire que le rapport d'ondes stationnaires vaut *là-bas* $\infty$, on peut mesurer à l'autre extrémité un rapport d'ondes stationnaires nettement meilleur. Si, p. ex., la moitié de la puissance est perdue à l'aller et à nouveau la moitié au retour, l'énergie se réduit au quart ($\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$). Un SWR-mètre placé du côté de l'émetteur indique en conséquence un rapport d'ondes stationnaires de $\num{3}$, ce qui correspond à $\qty{25}{\percent}$ de puissance réfléchie, alors même que $\qty{100}{\percent}$ sont réfléchis en bout de ligne – mais seuls $\qty{25}{\percent}$ parviennent jusqu'au SWR-mètre.
[question:AG402]
[question:AG403]

Avec une atténuation de ligne de $\qty{5}{\dB}$ et une réflexion totale en bout de câble, p. ex. du fait d'une antenne débranchée, nous mesurons même un SWR étonnamment bon, alors qu'aucune antenne n'est raccordée ! Nous pouvons calculer cela comme suit :

$s = \frac{\sqrt{P_\mathrm{v}}+\sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{v}}-\sqrt{P_\mathrm{r}}}$

Cela permet de calculer la question suivante, pour peu que nous notions que l'onde réfléchie mesurée ne représente qu'un dixième de l'énergie de l'onde directe : $\qty{5}{\dB}$ d'atténuation à l'aller et $\qty{5}{\dB}$ d'atténuation au retour, soit $\qty{10}{\dB}$ d'atténuation au total. $P_\mathrm{r}$ ne vaut donc, dans ce cas, qu'un dixième de $P_\mathrm{v}$.

[question:AG404]
