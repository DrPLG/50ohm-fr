L'alimentation d'une antenne s'effectue toujours avec une tension et un courant qui sont dans un rapport déterminé l'un avec l'autre. Ce rapport est appelé résistance d'alimentation.

Pour qu'une puissance puisse être délivrée, il faut toujours que la tension *et* le courant soient présents, car la puissance résulte de la multiplication de la tension par le courant. Si la tension ou le courant était nul, il n'y aurait pas non plus de puissance délivrée ou absorbée.

Nous parlons néanmoins, pour certaines antennes, d'antennes *alimentées en courant* et, pour certaines autres antennes, d'antennes *alimentées en tension*. On entend par là que, pour certaines antennes, un courant élevé est présent au point d'alimentation avec une tension comparativement faible, ou une tension élevée avec un courant comparativement faible.


---

Pour un dipôle demi-onde, la résistance d'alimentation dépend de l'endroit où s'effectue l'alimentation. Cela tient au fait que, dans le dipôle, les porteurs de charge oscillent d'avant en arrière, un nombre particulièrement grand de porteurs de charge étant déplacés au centre, ce que nous appelons un ventre de courant, tandis que des tensions particulièrement élevées apparaissent aux extrémités, ce que nous appelons un ventre de tension. Là où aucune charge n'est déplacée, nous parlons d'un nœud de courant, et là où la tension est nulle, nous parlons d'un nœud de tension. La figure [ref:e_strom_spannung_speisung_dipol] montre la répartition du courant et de la tension sur le dipôle. 

[question:EG203]

<margin>
[picture:787:e_strom_spannung_speisung_dipol:Dipôle demi-onde avec répartition de la tension et du courant]
</margin>

---

Si nous alimentons donc un dipôle demi-onde au centre, de nombreuses charges doivent être déplacées et nous parlons d'une antenne alimentée en courant (résistance d'alimentation basse). Un dipôle demi-onde alimenté en extrémité est en revanche une antenne alimentée en tension (résistance d'alimentation élevée). Pour l'alimentation en extrémité, comme montré sur la figure [ref:e_strom_spannung_speisung_dipol_ende], un dispositif d'adaptation est nécessaire. Nous ne l'aborderons en détail que dans la classe A. 

<margin>
[picture:851:e_strom_spannung_speisung_dipol_ende:Dipôle demi-onde alimenté en extrémité]
</margin>

---

Les antennes alimentées en courant présentent en conséquence une résistance basse et les antennes alimentées en tension une résistance élevée.

Cela s'illustre bien à l'aide de la loi d'Ohm :

$ R = \frac{U}{I} $

Si l'on alimente un dipôle au centre, on y trouve une tension comparativement faible avec en même temps un courant élevé. Le quotient de la tension par le courant est donc petit, et la résistance résultante est en conséquence basse. Si l'alimentation s'effectue en revanche à l'extrémité du dipôle, une tension élevée y est présente, tandis que le courant tend vers zéro. Le quotient devient alors très grand, et la résistance résultante prend en conséquence des valeurs élevées.

Pour les résistances basses, nous parlons aussi de comportement *à basse impédance* ($\downarrow\unit{\ohm}$) et pour les résistances élevées, en conséquence, de comportement *à haute impédance* ($\uparrow\unit{\ohm}$).

<indepth>
Un ordre de grandeur habituel pour la *résistance d'alimentation* d'une antenne alimentée en courant est par exemple de $\qty{36}{\ohm}$ à $\qty{100}{\ohm}$, et pour les antennes alimentées en tension de $\qty{1500}{\ohm}$ à $\qty{4000}{\ohm}$.
</indepth>

---

<indepth>
La répartition du courant sur un dipôle dépend de la fréquence à laquelle l'antenne est exploitée. La figure [ref:e_stromverteilungen] montre la répartition du courant pour des multiples entiers de la fréquence fondamentale $f$ dans le cas d'un dipôle alimenté au centre. On y reconnaît que, pour les multiples pairs de la fréquence fondamentale, un nœud de courant apparaît au point d'alimentation. Dans ce cas, le courant y est très petit, la tension en revanche élevée, et l'antenne apparaît à haute impédance au point d'alimentation. Pour cette raison, un dipôle alimenté au centre n'est résonant que pour les multiples entiers impairs de la fréquence fondamentale. Une utilisation de plusieurs bandes peut être obtenue en déplaçant le point d'alimentation, par exemple vers l'un des ventres de courant, comme sur la figure [ref:e_stromverteilungen]b (par exemple pour l'antenne Windom), ou vers l'extrémité de l'antenne (par exemple antenne EFHW ou Fuchs). Dans ces cas, des appareils d'adaptation sont toutefois nécessaires, sur lesquels nous ne reviendrons plus en détail que dans la classe A.
  
[picture:1050:e_stromverteilungen:Répartitions du courant pour différentes fréquences fondamentales]
</indepth>

[question:EG204]
[question:EG205]
[question:EG206]
