Comme nous l'avons appris, les postes radioamateur et les lignes de transmission courantes en radioamateurisme utilisent le plus souvent une impédance caractéristique de $\qty{50}{\ohm}$. Nous avons aussi appris qu'aux points de jonction des lignes de transmission, des réflexions indésirables se produisent quand l'impédance caractéristique ne concorde pas.

Les antennes possèdent elles aussi une propriété analogue à l'impédance caractéristique, qui dépend de la disposition exacte des éléments de l'antenne. Cette propriété s'appelle la résistance d'alimentation, ou résistance au point d'alimentation. Comme pour la jonction de deux lignes d'impédances différentes, la règle vaut ici aussi : si la résistance d'alimentation de l'antenne ne correspond pas à l'impédance caractéristique de la ligne, des réflexions indésirables se produisent. Une partie de la puissance d'émission est réfléchie vers le poste et ne peut pas être rayonnée par l'antenne.

Si, en revanche, la résistance d'alimentation de l'antenne et l'impédance caractéristique de la ligne concordent, garantissant un transfert optimal de la puissance vers l'antenne, on dit qu'il y a *adaptation*.

<margin>
[photo:144:swr_meter:Un ROS-mètre simple pour déterminer le rapport d'ondes stationnaires]
</margin>

La qualité de l'adaptation de l'antenne se mesure. En simplifiant, on détermine pour cela quelle part de la puissance d'émission est réfléchie par l'antenne. La valeur affichée par l'appareil de mesure s'appelle le *rapport d'ondes stationnaires*. On utilise le plus souvent l'abréviation SWR, dérivée de l'anglais « standing wave ratio » (en français, on parle aussi de ROS). Pour déterminer le SWR, on utilise un *mesureur d'ondes stationnaires*, appelé en abrégé *SWR-mètre* ou *ROS-mètre*.

% TODO: Editionsspezifisch machen

<indepth>
Un ROS-mètre mesure simultanément la puissance directe, que l'émetteur envoie vers l'antenne, et la puissance réfléchie. Cela se voit bien sur le ROS-mètre de la figure [ref:swr_meter_kreuzzeiger], qui affiche séparément puissances directe et réfléchie. Le SWR n'indique toutefois pas directement le rapport de ces deux mesures : il se calcule de façon un peu plus compliquée, $\text{SWR} = \frac {\sqrt{P_\text{V}}+\sqrt{P_\text{R}}} { \sqrt{P_\text{V}}-\sqrt{P_\text{R}}}$, où $P_\text{V}$ est la puissance directe et $P_\text{R}$ la puissance réfléchie. Cette formule n'est pas exigée à l'examen de la classe N.
</indepth>

<margin>
[photo:143:swr_meter_kreuzzeiger:ROS-mètre à aiguilles croisées, aiguille gauche pour la puissance directe et aiguille droite pour la puissance réfléchie ; pour lire le SWR, on suit la ligne verte vers le bas depuis l'intersection des deux aiguilles]
</margin>

[question:NI201]

---

<margin>
[photo:67:n_swr_display:Écran d'un émetteur-récepteur]
</margin>

Les émetteurs-récepteurs modernes ont déjà un ROS-mètre intégré. L'affichage se trouve le plus souvent à l'écran, voir la figure [ref:n_swr_display].

<attention>
SWR-mètre et S-mètre se ressemblent phonétiquement, mais sont différents : le SWR-mètre mesure le rapport d'ondes stationnaires à l'émission, tandis que le S-mètre mesure la force du signal à la réception.
</attention>

% TODO Big Picture: Im Bild Trx_Display "SWR" kennzeichnen

[question:NF101]

---

Si l'émetteur-récepteur n'a pas de ROS-mètre intégré, on peut aussi utiliser un ROS-mètre externe. Il se raccorde alors entre le poste et l'antenne, comme sur la figure [ref:n_trx_kabel_swr_antenne]. On dit aussi : « le ROS-mètre est inséré entre l'émetteur-récepteur et l'antenne ».

[question:NI202]

Si une antenne est parfaitement adaptée à sa ligne (p. ex. le câble coaxial), le ROS-mètre affiche une valeur de $\num{1}$. C'est la meilleure valeur possible. Toute la puissance est alors absorbée par l'antenne. Aucune puissance n'est réfléchie vers l'émetteur.

<margin>
[picture:670:n_trx_kabel_swr_antenne:Schéma de principe — ROS-mètre entre émetteur-récepteur et antenne]
</margin>

[question:NG301]
[question:NI203]

---

Si aucune antenne n'est raccordée à l'émetteur-récepteur, ou si la ligne de transmission est soit interrompue soit court-circuitée, la valeur du SWR est presque infinie ($\infty$). Un câble ouvert ou en court-circuit réfléchit en effet la totalité de la puissance d'émission. Dans le pire des cas, cela peut même détruire l'émetteur du poste.

<indepth>
Outre les deux valeurs de *SWR* $\num{1}$ et infini ($\infty$), les valeurs $\num{2}$ et $\num{3}$ sont marquantes. Pour un SWR de $\num{2}$, $\qty{11}{\percent}$ de la puissance d'émission est réfléchie vers l'émetteur ; pour un SWR de $\num{3}$, $\qty{25}{\percent}$. Sur les émetteurs-récepteurs modernes, une détérioration de l'émetteur est prévenue par une réduction automatique de la puissance d'émission dans le poste.
</indepth>

Un très mauvais SWR, par exemple proche de l'infini, peut aussi s'obtenir quand l'adaptation de l'antenne est très mauvaise ou que la ligne de transmission est endommagée.

[question:NG302]
[question:NG303]

Si une antenne mal adaptée est raccordée à un poste avec ROS-mètre par un long câble coaxial, la valeur de SWR affichée peut être nettement meilleure que ce à quoi on s'attendrait vu la mauvaise adaptation. La cause en est un fort affaiblissement du câble, qui atténue non seulement le signal allant vers l'antenne, mais aussi le signal réfléchi.

[question:NG208]
