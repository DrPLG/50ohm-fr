Jusqu'à présent, nous avions considéré les champs électriques et magnétiques dans le cas où ils sont invariables dans le temps. En radiotechnique, de tels champs sont en réalité sans intérêt, car nous nous occupons de tensions et de courants variables dans le temps. De même, les champs électriques et magnétiques produits sont variables dans le temps.

<margin>
[picture:885:e_vertikalantenne_em:Champ électrique et champ magnétique sur une antenne]
</margin>

Des effets supplémentaires apparaissent alors. Dès 1831, Michael Faraday découvrit qu'un champ magnétique variable dans le temps engendre une tension électrique dans un conducteur voisin. Cet effet, appelé *induction*, est par exemple mis à profit dans le transformateur : un courant variable dans le temps (par exemple sinusoïdal) dans l'enroulement primaire crée un champ magnétique variable dans le temps, qui à son tour induit une tension dans l'enroulement secondaire.

Pour comprendre qu'inversement la variation d'un champ électrique conduit à un champ magnétique, imaginons un condensateur plan dont les armatures forment un circuit avec une source de tension externe. Si nous modifions le champ électrique à l'intérieur du condensateur, des charges doivent être déplacées dans le circuit extérieur. Or le déplacement de porteurs de charge implique un courant électrique. Mais ce courant électrique crée à son tour un champ magnétique autour du conducteur.

Si les représentations par modèles faisant intervenir des conducteurs électriques nous sont parlantes, il est toutefois très important que ces conducteurs ne soient pas nécessaires. Les champs magnétiques et électriques existent aussi en dehors des conducteurs, même dans le vide. Là encore, un champ magnétique variable dans le temps engendre un champ électrique variable dans le temps. Ce champ variable dans le temps conduit à son tour à un champ magnétique variable dans le temps. *Les champs magnétiques variables dans le temps et les champs électriques variables dans le temps sont donc toujours couplés.* C'est pourquoi nous parlons aussi de *champ électromagnétique*. En résumé : une onde électromagnétique capable de se propager librement dans l'espace repose sur l'interaction entre des champs magnétiques et électriques variables dans le temps.

[question:EB302]

Comme déjà décrit plus haut, des tensions et des courants constants dans le temps ne peuvent pas engendrer de champ électromagnétique. Pour cela, nous avons besoin d'un courant variable dans le temps dans un conducteur.

[question:EB301]

<indepth>
Le champ magnétique et le champ électrique sont en réalité décrits par des *vecteurs*, c'est-à-dire par des grandeurs qui ont une direction dans l'espace. On peut montrer mathématiquement que, dans le *champ lointain*, c'est-à-dire suffisamment loin de l'antenne, les vecteurs des deux champs doivent être perpendiculaires l'un à l'autre. La direction de propagation de l'onde électromagnétique (c'est-à-dire de notre signal radio…) est elle-même perpendiculaire à la fois au champ électrique et au champ magnétique.
  
[picture:886:e_emfeld_ausbreitung:Propagation de l'onde électromagnétique]
  
Les relations décrites sont décrites mathématiquement par les *équations de Maxwell*, du nom de James Clerk Maxwell, qui les a élaborées entre 1861 et 1864 à partir des observations d'autres physiciens. Il parvint ainsi à la conclusion que les champs magnétiques et électriques doivent être couplés :
  
1. $\vec{\nabla} \cdot \vec{E} =\frac{\rho}{\varepsilon_{0}}$
2. $\vec{\nabla} \cdot \vec{B} = 0$
3. $\vec{\nabla} \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$
4. $\vec{\nabla } \times \vec{B} =\mu_0 (\vec{j} +\varepsilon_0 \frac{\partial\vec{E}}{\partial t})$
  
L'équation (3) montre qu'un champ magnétique variable dans le temps engendre un champ électrique. Ce champ électrique variable dans le temps contribue à son tour, selon l'équation (4), à la création d'un champ magnétique via le courant de déplacement. Ces relations vont bien au-delà de ce qu'il faut savoir en radioamateurisme.
  
L'existence du champ électromagnétique ne fut toutefois démontrée expérimentalement que plus de vingt ans plus tard (1886) par Heinrich Hertz.
</indepth>

Comme le montrent les figures et [ref:e_emfeld_ausbreitung], la composante de champ magnétique est toujours, dans le champ lointain (loin de l'antenne), perpendiculaire à la composante de champ électrique.

[question:EB303]

Les composantes de champ magnétique et électrique, perpendiculaires entre elles dans le champ lointain, fixent aussi la direction de propagation $S$, comme le montre la figure [ref:e_vertikalantenne_em] : elle est elle-même perpendiculaire aux deux. On peut se le représenter ainsi : le champ magnétique et le champ électrique définissent un plan, sur lequel la direction de propagation est perpendiculaire.

[question:EB304]
