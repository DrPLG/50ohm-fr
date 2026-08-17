Idéalement, les courants circulant dans le conducteur intérieur et dans le conducteur extérieur d'un câble coaxial sont exactement d'égale intensité et de sens opposés. Leur somme est donc nulle et l'on parle alors d'un *signal en mode différentiel* pur. C'est exactement dans ce cas qu'aucune onde de gaine n'apparaît.

Si la somme du signal est en revanche différente de zéro, on est en présence de ce que l'on appelle un *signal en mode commun*. La composante de mode commun d'un courant dans le câble coaxial circule toujours sur la face extérieure du conducteur extérieur ; c'est donc un courant de gaine, avec l'onde de gaine associée tout autour du câble coaxial.

[question:AG425]

Nous avons déjà appris qu'un câble coaxial bobiné autour d'un noyau de ferrite convient à la suppression des ondes de gaine. C'est une forme de ce que l'on appelle la *self à compensation de courant*.

Une self de choc est une bobine destinée à bloquer les courants haute fréquence. La self à compensation de courant est une forme de construction de la self de choc, dans laquelle deux enroulements distincts sont bobinés sur le même noyau magnétique. La self à compensation de courant est câblée de telle sorte que les signaux en mode différentiel — c'est-à-dire les signaux pour lesquels le courant dans l'un des enroulements est exactement opposé à celui de l'autre enroulement, tout en présentant par ailleurs la même intensité — n'induisent aucun champ magnétique dans le noyau. La self à compensation de courant laisse donc passer sans entrave les signaux en mode différentiel. Les composantes de mode commun, en revanche, c'est-à-dire p. ex. les courants qui circulent uniquement sur le conducteur extérieur et donc uniquement dans un seul enroulement, sont bloquées par l'inductance.

[question:AG426]

<margin>
[picture:633:e_mantelwellen:Ondes de gaine]
</margin>

---

Un transformateur d'isolement HF constitue une alternative à la self à compensation de courant. Comme l'enroulement primaire et l'enroulement secondaire ne sont pas reliés entre eux, un courant qui entre dans le transformateur d'isolement par l'un des pôles doit (au moins approximativement) en ressortir avec la même intensité par l'autre pôle. Une composante de mode commun est ainsi exclue.

<indepth>
Comme une capacité apparaît entre les spires de la bobine d'un transformateur d'isolement et que la bobine forme également une capacité vis-à-vis de l'autre bobine, un transformateur d'isolement ne supprime pas non plus complètement la composante de mode commun d'un signal.
</indepth>

[question:AJ115]

Lorsqu'un câble coaxial est exempt de signaux HF de mode commun, le conducteur extérieur ne présente aucune tension haute fréquence par rapport à la terre. Cela tient à ce que, pour un signal en mode différentiel, c'est-à-dire pour des courants opposés dans le conducteur intérieur et le conducteur extérieur, un champ électrique se forme exclusivement entre le conducteur intérieur et le conducteur extérieur. Vu de l'extérieur, les effets des deux courants s'annulent, puisque leur somme est nulle. La présence d'ondes de gaine est donc directement liée à la présence de tensions HF sur le conducteur extérieur.

C'est précisément de telles tensions sur le conducteur extérieur qui apparaissent, p. ex., lorsque nous raccordons une antenne symétrique au câble, car au point d'alimentation, chaque brin du dipôle présente une tension par rapport à la terre. Si nous relions chacun des brins à l'un des conducteurs du câble coaxial, le conducteur extérieur présentera lui aussi une tension par rapport à la terre.

Les antennes bien mises à la terre, en revanche, p. ex. une antenne Groundplane comportant de nombreux radians bien accordés ou enterrés, présentent au point d'alimentation des radians une tension quasi nulle par rapport à la terre. Les antennes Groundplane mal mises à la terre peuvent en revanche être sensibles aux ondes de gaine.

Une autre façon dont les ondes de gaine peuvent apparaître est le couplage sans contact dans le blindage du câble coaxial. Si l'on fait par exemple cheminer un câble d'alimentation parallèlement à un brin de dipôle, il se produit un couplage par le champ proche électromagnétique de l'antenne.

[question:AG427]

Pour les antennes parfaitement symétriques, on peut employer ce que l'on appelle un balun de tension, afin de symétriser les courants dans le câble coaxial. Une forme de construction appréciée est l'autotransformateur, dans lequel le câble coaxial est raccordé au milieu et à l'extrémité d'une bobine, l'antenne étant reliée aux deux extrémités de la bobine.

% TODO: Bild Spannungsbalun / Spartransformator

Avec cette forme de construction, on obtient, outre la symétrisation recherchée, un doublement de la tension ($m = 2$) ainsi qu'une division par deux du courant, ce qui correspond à une transformation d'impédance 1:4 ; autrement dit, il convient de raccorder à un câble coaxial de $\qty{50}{\ohm}$ une antenne présentant, autant que possible, une résistance d'alimentation de $\qty{200}{\ohm}$.

[question:AG421]
[question:AG422]

Cette forme de construction n'est cependant apte à supprimer les ondes de gaine que si l'antenne raccordée se comporte effectivement de façon symétrique et n'est pas chargée de façon asymétrique du fait de l'environnement.

Tous les composants destinés à supprimer les ondes de gaine ont ceci en commun qu'un couplage « sans contact » par les champs proches électromagnétiques des antennes peut malgré tout se produire directement sur le blindage du coaxial, c'est-à-dire en aval du bloqueur d'ondes de gaine. Un second bloqueur d'ondes de gaine supplémentaire, placé à une certaine distance de l'antenne, peut alors p. ex. être utile.

[question:AG428]
[question:AG429]