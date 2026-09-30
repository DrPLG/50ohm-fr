Pour régler une antenne, on n'a pas besoin d'émettre. Un *analyseur d'antenne* [index:Analyseur d'antenne] est un petit appareil qui envoie lui-même un signal très faible dans l'antenne, en balayant une plage de fréquences, et qui affiche le ROS pour chacune. On voit ainsi d'un coup d'œil la courbe du ROS et la fréquence où il est le plus bas : c'est la fréquence de résonance de l'antenne.

<margin>
[photo:323:bir_courbe_ros:Une courbe de ROS affichée par un analyseur — le creux indique la fréquence de résonance]
</margin>

---

Il suffit alors de comparer cette fréquence à celle qu'on vise :

* si le creux est **plus bas** que la fréquence voulue, l'antenne est trop *longue* : on la raccourcit ;
* si le creux est **plus haut**, l'antenne est trop *courte* : il faudrait l'allonger.

C'est pourquoi on coupe toujours les brins un peu trop longs au départ : on sait raccourcir, pas rallonger.

On raccourcit un dipôle par petites étapes, de quelques millimètres à la fois, **les deux brins de la même longueur**, et l'on mesure à nouveau après chaque coupe. Le creux remonte peu à peu vers la fréquence voulue.

<tip>
L'environnement change le réglage. Une antenne réglée sur la table, près des mains et des meubles, se décale une fois installée sur son mât. On fait le réglage final dans la position d'utilisation.
</tip>

[question:RD1609]
[question:RD1610]
