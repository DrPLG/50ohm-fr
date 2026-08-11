Le montage en pont est un agencement de quatre résistances, employé entre autres pour la mesure précise de résistances. Un exemple pratique connu est le pont de mesure de Wheatstone. Le circuit se compose de deux diviseurs de tension montés en parallèle. Entre les points milieux des deux diviseurs de tension se trouve ce qu'on appelle la branche du pont, aux bornes de laquelle la tension de pont $U_\mathrm{AB}$ peut être mesurée.

<margin>
[picture:343:a_Brückenschaltung:Montage en pont typique à 4 résistances]
</margin>

Le cas du pont équilibré est particulièrement intéressant. Il se présente lorsque les rapports des diviseurs de tension des deux côtés sont de même valeur. Les deux points milieux possèdent alors le même potentiel électrique et aucun courant ne circule dans la branche du pont ni dans l'instrument de mesure raccordé.

Les résistances individuelles n'ont pas besoin pour cela d'avoir la même valeur. Ce qui est décisif, c'est seulement que le rapport des résistances concorde des deux côtés.

Pour l'état équilibré, on a donc :

$ U_\mathrm{AB} = \qty{0}{\volt} $

et ainsi :

$ \frac{R_1}{R_2} = \frac{R_3}{R_4} $

Le pont de Wheatstone convient donc particulièrement bien à la détermination de résistances inconnues ou de petites variations de résistance. Comment cela fonctionne exactement est décrit dans l'approfondissement ci-contre.

<indepth>
Le cas particulier où les rapports des diviseurs de tension du montage en pont sont de même valeur à gauche et à droite est appliqué à la mesure de résistances inconnues. Charles Wheatstone (physicien britannique) reconnut dès 1833 l'importance du montage en pont pour la mesure de résistances inconnues. 

Lors de la mesure, une résistance de précision réglable est modifiée jusqu'à ce que l'instrument de mesure sensible dans la branche du pont n'indique plus aucun passage de courant. Le pont est alors équilibré, et l'on peut déterminer la valeur de la résistance inconnue à l'aide de l'échelle et du multiplicateur de gamme de mesure.

On en voit un exemple sur la figure [ref:a_pontavi]. Il y a ici un multiplicateur pouvant prendre les valeurs 0,1/1/10/100. Pour le réglage fin, il y a le grand bouton rotatif. 
[photo:286:a_pontavi:Pont de mesure de résistance selon Wheatstone (Pontavi)]

La figure [ref:a_pontavi_schaltung] montre le schéma simplifié de cet appareil de mesure. La résistance inconnue est raccordée à l'emplacement $X$. On règle d'abord avec le multiplicateur l'ordre de grandeur estimé de la résistance inconnue. Puis, avec le grand bouton rotatif, la résistance de précision est modifiée jusqu'à ce que le pont soit équilibré. L'instrument de mesure indique alors qu'aucun courant ne circule plus dans la branche du pont.

[picture:1076:a_pontavi_schaltung:Schéma du pont de mesure de résistance (Pontavi)]
</indepth>

[question:AD111]

Comme, dans l'exercice suivant, toutes les résistances sont de même valeur, les rapports des diviseurs de tension doivent eux aussi être égaux. Cela correspond au cas particulier décrit.

[question:AD112]

Dans la question suivante, le cas particulier ne s'applique pas, puisque les rapports des diviseurs de tension sont inégaux. Il y a certes des résistances semblables, mais, considérées de haut en bas, elles sont interverties. L'exercice peut être résolu avec les connaissances sur le diviseur de tension non chargé.

[question:AD113]

Du côté gauche, nous trouvons le rapport $\qty{1}{\kilo\ohm}$ à $\qty{10}{\kilo\ohm} = 1/10$.
À condition que l'instrument de mesure soit à très haute impédance ou débranché, nous mesurons, pour une tension d'alimentation de $\qty{11}{\volt}$, du côté gauche exactement $\qty{1}{\volt}$ aux bornes de la résistance du haut ($R_1$) et $\qty{10}{\volt}$ aux bornes de la résistance du bas ($R_2$). Le potentiel au point de mesure A vaut donc $\qty{10}{\volt}$ mesuré par rapport à la masse.

Du côté droit, nous trouvons le rapport $\qty{10}{\kilo\ohm}$ à $\qty{1}{\kilo\ohm} = 10/1$ et mesurons donc $\qty{10}{\volt}$ aux bornes de la résistance du haut ($R_3$) et $\qty{1}{\volt}$ aux bornes de la résistance du bas ($R_4$). Le potentiel au point de mesure B vaut donc $\qty{1}{\volt}$ mesuré par rapport à la masse.

La différence de potentiel entre A et B vaut ainsi $\qty{9}{\volt}$, le point de mesure A étant plus positif de $\qty{9}{\volt}$ que le point de mesure B.