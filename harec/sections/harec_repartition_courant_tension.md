Une antenne est alimentée par une tension et un courant dont le rapport est sa **résistance d'alimentation** (ou impédance au point d'alimentation). Ce rapport dépend de l'endroit où l'on alimente.

Sur un dipôle demi-onde, les charges oscillent d'un bout à l'autre. Au centre, beaucoup de charges se déplacent : c'est un **ventre de courant**, où la tension est faible (**nœud de tension**). Aux extrémités, le courant s'annule (**nœud de courant**) et la tension est maximale (**ventre de tension**).

<margin>
[picture:787:harec_repartition_dipole:Dipôle demi-onde, répartition du courant et de la tension]
</margin>

D'après la loi d'Ohm $R = \frac{U}{I}$ :

* alimenté **au centre**, le dipôle reçoit peu de tension pour beaucoup de courant : il est **alimenté en courant**, à **basse impédance** (de l'ordre de $\num{36}$ à $\qty{100}{\ohm}$) ;
* alimenté **à une extrémité**, il reçoit beaucoup de tension pour peu de courant : il est **alimenté en tension**, à **haute impédance** (de l'ordre de $\num{1500}$ à $\qty{4000}{\ohm}$), et demande un adaptateur.

---

<margin>
[picture:1050:harec_repartition_multiples:Répartition du courant aux multiples de la fréquence fondamentale]
</margin>

La répartition dépend aussi de la fréquence. Sur un dipôle alimenté au centre, on compte autant de ventres de courant que le rang du multiple de la fréquence fondamentale :

* aux multiples **impairs** (1, 3, 5…), un ventre de courant tombe au centre : le dipôle reste alimenté en courant, à basse impédance, et résonne. Un dipôle de $\qty{3,5}{\mega\hertz}$ résonne ainsi vers $\qty{10,5}{\mega\hertz}$ et $\qty{17,5}{\mega\hertz}$ ;
* aux multiples **pairs** (2, 4…), c'est un nœud de courant qui tombe au centre : l'impédance y devient élevée, et la fréquence n'est pas utilisable directement ($\qty{7}{\mega\hertz}$ et $\qty{14}{\mega\hertz}$ sur ce même dipôle).
