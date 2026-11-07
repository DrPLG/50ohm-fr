Quand l'impédance de l'antenne n'est pas égale à l'impédance caractéristique de la ligne, une partie de l'onde se **réfléchit** au bout et revient vers l'émetteur. Onde directe et onde réfléchie forment des **ondes stationnaires** le long de la ligne. Quand les impédances sont égales, il n'y a pas de réflexion : la ligne est **adaptée**.

Le **rapport d'ondes stationnaires** [index:Rapport d'ondes stationnaires (ROS)], **ROS** (en anglais SWR), mesure cette désadaptation. Il vaut **1** pour une adaptation parfaite et devient **infini** pour une ligne ouverte, en court-circuit ou sans antenne, où toute la puissance revient.

<margin>
[picture:670:harec_rosmetre:ROS-mètre inséré entre l'émetteur-récepteur et l'antenne]
</margin>

Le **ROS-mètre** [index:ROS-mètre] s'insère entre l'émetteur et la ligne ; il mesure la puissance directe $P_\mathrm{d}$ et la puissance réfléchie $P_\mathrm{r}$ :

$s = \dfrac{\sqrt{P_\mathrm{d}} + \sqrt{P_\mathrm{r}}}{\sqrt{P_\mathrm{d}} - \sqrt{P_\mathrm{r}}}$

Pour une antenne purement résistive $R$ au bout d'une ligne d'impédance $Z_0$, le ROS est le rapport de la plus grande à la plus petite : $s = R / Z_0$ si $R > Z_0$, $s = Z_0 / R$ sinon.

| l: ROS | l: puissance réfléchie |
| $\num{1}$ | $\qty{0}{\percent}$ |
| $\num{1,5}$ | $\qty{4}{\percent}$ |
| $\num{2}$ | $\qty{11}{\percent}$ |
| $\num{3}$ | $\qty{25}{\percent}$ |
| $\infty$ | $\qty{100}{\percent}$ |
[table:harec_ros_reflechie:ROS et part de puissance réfléchie]

<tip>
**Méthode — trois calculs de ROS.** *Par les puissances* : $\qty{100}{\watt}$ directs, $\qty{25}{\watt}$ réfléchis : $(10 + 5) \div (10 - 5) = 3$. *Par les impédances* : dipôle de $\qty{75}{\ohm}$ sur un câble de $\qty{50}{\ohm}$ : $75 \div 50 = \num{1,5}$ ; ground-plane de $\qty{25}{\ohm}$ : $50 \div 25 = 2$. *Vers la puissance réfléchie* : coefficient de réflexion $r = (s - 1) \div (s + 1)$, puis part réfléchie $r^2$. Pour $s = 3$ : $r = \num{0,5}$, $r^2 = \qty{25}{\percent}$.
</tip>

---

Un ROS élevé ne détruit pas la puissance par lui-même, mais il augmente les pertes de la ligne et peut **endommager l'étage final** ; les émetteurs modernes réduisent alors leur puissance d'eux-mêmes.

<attention>
**Un long câble à fortes pertes « embellit » le ROS.** L'onde réfléchie est atténuée à l'aller **et** au retour : mesuré côté émetteur, le ROS paraît bien meilleur qu'il n'est à l'antenne. Un ROS excellent sur un long câble fin peut cacher une antenne mal adaptée.
</attention>

Le ROS-mètre ne doit pas être confondu avec le **S-mètre**, qui mesure la force du signal **reçu**.
