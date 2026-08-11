Au début de ce chapitre, nous avons étudié le dipôle comme forme fondamentale de toutes les antennes. Le dipôle demi-onde rayonne les ondes radio perpendiculairement à la direction du fil. D'autres formes d'antennes peuvent, selon leur construction, rayonner préférentiellement dans une ou plusieurs directions, et d'autant moins dans les autres :
* Une antenne ground-plane rayonne de façon presque uniforme dans toutes les directions de l'horizon, mais pas vers le haut ni vers le bas.
* Sur une antenne Yagi-Uda, les ondes radio sont concentrées vers l'avant en un faisceau, comme avec une lampe de poche, et réduites dans toutes les autres directions.

Les valeurs limites imposées par la procédure de justification pour la protection des personnes dans les champs électromagnétiques doivent être respectées par une installation d'émission dans chaque direction. Si, à une certaine distance de l'antenne, les valeurs limites sont respectées dans la direction où elle rayonne le plus fort, elles le seront aussi, à la même distance, dans toutes les autres directions. C'est pourquoi la direction du rayonnement le plus fort nous intéresse particulièrement. On l'appelle la *direction principale de rayonnement*.

---

La force avec laquelle une antenne rayonne dans sa direction principale s'exprime par le *facteur de gain* rapporté au dipôle demi-onde. Il indique combien une antenne rayonne mieux, dans sa direction principale, qu'un dipôle demi-onde. Un facteur de gain de $\num{2}$ par rapport au dipôle demi-onde signifie par exemple qu'une antenne rayonne dans sa direction principale deux fois plus fort qu'un dipôle demi-onde dans la sienne.

<indepth>
Au lieu du facteur de gain des antennes, on indique souvent le « gain en décibels ($\unit{\dB}$) ». L'unité décibel est traitée dans le cours pour la classe E.
</indepth>

---

Pour indiquer combien une antenne concrète rayonne dans sa direction principale quand on y injecte une certaine puissance d'émission, on multiplie la puissance d'émission par le facteur de gain rapporté au dipôle demi-onde. On obtient alors la *puissance apparente rayonnée*, le plus souvent abrégée ERP (de l'anglais « effective radiated power »). Si nous injectons par exemple une puissance de $\qty{5}{\watt}$ dans une antenne au facteur de gain de $\num{2}$ par rapport au dipôle demi-onde, la puissance rayonnée est de $\qty{10}{\watt}$ ERP.

<margin>
On peut aussi se représenter la puissance apparente rayonnée (ERP) ainsi : c'est la puissance qu'il faudrait injecter dans un dipôle demi-onde pour qu'il rayonne, dans sa direction principale, aussi fort que l'antenne considérée.
</margin>

Les antennes directives peuvent avoir des facteurs de gain bien plus grands. Une antenne Yagi-Uda de 9 éléments peut par exemple facilement atteindre un facteur de gain de $\num{10}$ ou plus par rapport au dipôle demi-onde. Si l'on injecte p. ex. $\qty{100}{\watt}$ dans une telle antenne, la puissance rayonnée atteint déjà $\qty{1000}{\watt}$ ERP ou plus !

[question:NG401]

<france>
# ERP se dit PAR

Le vocabulaire réglementaire français a ses propres sigles, et il vaut mieux les connaître avant de lire un texte de l'ANFR.

L'ERP, *effective radiated power*, se dit en français **puissance apparente rayonnée**, abrégée **PAR** : la puissance qu'il faudrait fournir à un dipôle demi-onde pour obtenir le même champ dans la direction considérée. C'est exactement la même grandeur qu'ici, avec le même dipôle de référence.

Ce sigle n'est pas décoratif : c'est en PAR qu'est exprimé le **seuil de déclaration des stations à l'ANFR**. Toute installation de radioamateur dont la PAR dépasse 5 W doit être déclarée, et la déclaration porte sur la PAR maximale utilisée en HF, VHF, UHF et SHF. Un opérateur français a donc besoin de savoir calculer sa PAR, non pour vérifier un droit d'émettre, mais pour savoir s'il doit remplir un formulaire.
</france>
