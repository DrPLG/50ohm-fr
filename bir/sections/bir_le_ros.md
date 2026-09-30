Quand tout est bien accordé, la puissance que l'émetteur envoie dans le câble est entièrement acceptée par l'antenne et part en onde radio. Mais si l'antenne n'est pas accordée à la fréquence, par exemple parce qu'elle est trop longue ou trop courte, elle n'accepte qu'une partie de la puissance et *renvoie* le reste vers l'émetteur, par le câble.

On mesure ce défaut par le *rapport d'ondes stationnaires* [index:Rapport d'ondes stationnaires], abrégé *ROS* ; en anglais *SWR* [index:SWR].

---

| c: ROS | X: Ce que cela veut dire |
| 1 | parfait : rien n'est renvoyé |
| jusqu'à 1,5 | très bon |
| jusqu'à 2 | acceptable |
| 3 et plus | mauvais : l'antenne est à régler, ou il y a une panne |
[table:bir_ros:Lire un rapport d'ondes stationnaires]

Un ROS élevé fait perdre de la puissance, et il peut abîmer l'étage d'émission du poste. Beaucoup de postes réduisent d'eux-mêmes leur puissance quand ils détectent un mauvais ROS.

---

<margin>
[picture:670:bir_ros_metre_place:Le ROS-mètre se place entre le poste et l'antenne]
</margin>

On le mesure avec un *ROS-mètre* [index:ROS-mètre], placé entre le poste et le câble d'antenne (figure [ref:bir_ros_metre_place]). Beaucoup de postes en ont un intégré.

<margin>
[photo:144:bir_ros_metre:Un ROS-mètre simple]
</margin>

Un ROS très élevé, supérieur à 5 ou même infini, signale presque toujours une panne : câble coupé, connecteur en court-circuit, antenne débranchée.

[question:RD1606]
[question:RD1607]
[question:RD1608]
