Dans la classe E, nous avons déjà fait connaissance avec la ligne d'alimentation à conducteurs parallèles, aussi appelée échelle à grenouilles (cf. figure [ref:a_huenerleiter]). Elle est constituée de deux conducteurs cheminant parallèlement. Les lignes bifilaires se comportent aussi de façon symétrique du point de vue de leur répartition du courant et de la tension, pour autant qu'elles soient alimentées et chargées symétriquement. Autrement dit, en un point donné, le courant et la tension ont sur les deux conducteurs le même module, mais des signes opposés, comme le montre la figure [ref:a_zweidrahtleitung].

<margin>
[photo:324:a_huenerleiter:Échelle à grenouilles, aussi appelée ligne bifilaire]
</margin>

Les courants des deux conducteurs circulent ainsi à chaque instant en sens opposés. On parle de *courants de mode différentiel*. Les champs électromagnétiques engendrés par les deux conducteurs agissent de ce fait très largement l'un contre l'autre à plus grande distance et s'annulent pour l'essentiel. Une ligne bifilaire exploitée symétriquement ne rayonne donc que peu.

<margin>
[picture:1107:a_zweidrahtleitung:Répartition du courant et de la tension sur une ligne bifilaire]
</margin>

Si la ligne d'alimentation n'est en revanche pas complètement symétrique, des *courants de mode commun* peuvent apparaître en plus. Une partie du courant circule alors dans le même sens sur les deux conducteurs. Les champs engendrés par ces courants ne s'annulent pas mutuellement. La ligne d'alimentation peut alors agir elle-même comme une antenne et rayonner de l'énergie haute fréquence. De telles composantes de mode commun peuvent apparaître par exemple lorsqu'un dipôle n'est pas construit exactement symétriquement, lorsqu'une antenne ou une charge dissymétrique est raccordée, ou lorsque la transition entre une antenne symétrique et une ligne d'alimentation dissymétrique n'est pas découplée par un balun approprié ou par un bloqueur d'ondes de gaine.

[question:AG312]

Dans le champ proche d'autres lignes ou d'appareils électriques en particulier, un couplage électromagnétique plus fort peut en outre se produire. C'est pourquoi les lignes d'alimentation posées à l'intérieur des bâtiments sont habituellement blindées, par exemple sous forme de câbles coaxiaux. Dans un câble coaxial, les champs électromagnétiques du mode différentiel se trouvent très largement entre le conducteur intérieur et le blindage. Cela réduit aussi bien le rayonnement de la ligne d'alimentation que le couplage des perturbations extérieures.

[question:AG301]

Comme câble blindé, le câble coaxial s'impose, que nous avons également déjà découvert dans la classe E. Les câbles coaxiaux existent dans les exécutions les plus diverses. La question suivante porte sur les *propriétés haute fréquence* des câbles coaxiaux, c'est-à-dire sur leurs propriétés électriques du point de vue des fréquences élevées. Ce sont pour l'essentiel :

* l'impédance caractéristique,
* l'atténuation de câble et le
* coefficient de vélocité,

que nous allons examiner sous peu de plus près. Le rayon de courbure, en revanche, est une propriété mécanique, qui indique jusqu'à quel rayon le câble peut être posé dans un coude. L'affaiblissement de réflexion indique combien de réflexions sont présentes, ce qui dépend de la charge raccordée à une ligne et n'est donc pas une propriété du câble.

[question:AG303]

Le coefficient de vélocité résulte du diélectrique situé entre le conducteur intérieur et le conducteur extérieur. C'est là que se trouve la plus grande partie de l'onde électromagnétique guidée par le câble. Le choix du diélectrique détermine la vitesse à laquelle une onde peut se propager dans le câble. La vitesse de propagation dans le câble coaxial est inférieure à la vitesse de la lumière en espace libre. Les matériaux usuels du diélectrique sont le polyéthylène (PE) et le téflon (PTFE). L'expansion en mousse produit en quelque sorte un mélange avec de l'air, pour lequel l'atténuation de câble se révèle plus faible.

[question:AG314]
[question:AG302]

La vitesse de propagation réduite par le diélectrique se traduit dans le coefficient de vélocité, qui indique à quelle longueur un câble doit être raccourci mécaniquement pour présenter électriquement une longueur donnée (p. ex. pour faire un quart de longueur d'onde). Pour le coefficient de vélocité, nous trouvons dans le recueil de formules la relation suivante :

$k_\mathrm{v} = \frac{L_\mathrm{G}}{L_\mathrm{E}} = \frac{1}{\sqrt{\epsilon_\mathrm{r}}}$

Ici, $k_\mathrm{v}$ est le coefficient de vélocité, $L_\mathrm{G}$ la longueur géométrique (« mécanique ») et $L_\mathrm{E}$ la longueur électrique. La permittivité relative $\epsilon_\mathrm{r}$ dépend du diélectrique employé. Pour le polyéthylène (PE) non expansé, le recueil de formules nous donne une permittivité de $\num{2,29}$.

[question:AG317]
