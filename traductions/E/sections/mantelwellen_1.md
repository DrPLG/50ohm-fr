Lors du raccordement d'antennes, nous voulons obtenir que seule l'antenne rayonne ou capte des signaux, mais pas la ligne d'alimentation elle-même, qui pourrait être posée dans la maison. Les lignes blindées, par exemple les câbles coaxiaux, s'y prêtent bien, car dans le cas idéal elles ne rayonnent ni ne captent elles-mêmes d'ondes électromagnétiques, mais conduisent le signal à travers le câble en l'isolant du monde extérieur (donc par exemple de l'installation électrique de la maison).

<indepth>
Pour que le blindage d'un câble coaxial remplisse effectivement la fonction souhaitée, une *condition* doit être remplie : le courant dans le conducteur intérieur doit être exactement opposé au courant dans le conducteur extérieur, et les deux courants doivent avoir la même valeur. Dans ce cas, un champ n'apparaît qu'entre les deux conducteurs, et l'environnement du câble n'est pas influencé. Le conducteur extérieur ne présente alors précisément aucune tension haute fréquence par rapport à la terre.

Inversement, cela signifie aussi : si le conducteur extérieur présente une tension haute fréquence par rapport à la terre, alors les courants dans le conducteur intérieur ne sont pas symétriques et le câble coaxial rayonne.

Les courants dans le câble coaxial devraient donc être symétriques (même valeur mais signe opposé, respectivement direction opposée) et les tensions par rapport à la terre devraient être *asymétriques* (seul le conducteur intérieur porte une tension par rapport à la terre).
</indepth>

---

Mais si l'on raccorde une antenne symétrique, par exemple un dipôle demi-onde, à un câble coaxial, il peut néanmoins arriver que le câble coaxial rayonne malgré le blindage ! Cela tient au fait que des courants haute fréquence peuvent circuler à la surface de la face externe du conducteur extérieur métallique, accompagnés d'un champ électromagnétique autour de l'isolation extérieure (cf. figure [ref:e_mantelwellen]). Nous appelons cet effet *ondes de gaine*, qui peuvent aussi bien perturber d'autres appareils de la maison à l'émission que provoquer des perturbations de réception, car le câble coaxial devient en quelque sorte une partie de l'antenne et les influences perturbatrices présentes dans la maison peuvent ainsi être plus facilement captées par l'appareil radio. Les courants de gaine supplémentaires « manquent » alors sur l'un des deux brins du dipôle, ce qui provoque en outre une déformation de la caractéristique de directivité.

[question:EG405]
[question:EG406]

La figure [ref:e_mantelwellen] montre clairement comment une partie du courant, qui devrait en réalité s'écouler dans le brin du dipôle, revient par le blindage du câble coaxial.

<margin>
[picture:633:e_mantelwellen:Ondes de gaine]
</margin>

Les courants de gaine circulent effectivement en grande partie à la surface du conducteur extérieur. Cela tient à ce qu'on appelle l'*effet de peau* (Skineffekt), qui fait que les courants haute fréquence circulent en grande partie à la surface des conducteurs métalliques. On peut donc aussi se représenter un câble coaxial comme un système à trois conducteurs :
  
1. la face externe du conducteur intérieur
2. la face interne du conducteur extérieur
3. la face externe du conducteur extérieur
  
Le courant sur la face externe du conducteur intérieur et le courant sur la face interne du conducteur extérieur ont toujours la même valeur et sont de sens opposés ($I_1$). Le courant sur la face externe du conducteur extérieur ($I_3$) constitue le courant de gaine.

[question:EG404]

---

On peut empêcher les ondes de gaine, par exemple, en utilisant un dispositif dit *symétriseur*, un balun, pour relier le câble coaxial et l'antenne.

<indepth>
Le mot *balun* est composé des mots anglais « balanced » et « unbalanced », puisqu'il s'agit de relier un côté symétrique (par exemple une antenne symétrique) à un côté asymétrique (le câble coaxial, dans lequel idéalement seul le conducteur intérieur présente une tension par rapport à la terre).
</indepth>

[question:EG407]

---

Une autre forme de construction d'un balun consiste à enrouler un câble coaxial autour d'un noyau de ferrite. Cela constitue une *self à compensation de courant* et on l'appelle aussi *bloqueur d'ondes de gaine* (Mantelwellensperre). Pour les signaux en mode différentiel, elle a une faible impédance, car, lorsque le courant dans le conducteur intérieur est l'inverse de celui du conducteur extérieur, il n'y a pas d'interaction notable avec le matériau en ferrite. Pour les ondes de gaine, en revanche, le montage agit comme une bobine (avec pertes).

<margin>
[photo:325:e_mantelwellendrossel:Bloqueur d'ondes de gaine]
</margin>

[question:EG408]
