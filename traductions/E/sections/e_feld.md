Le phénomène physique qui rend les signaux radio possibles est le champ électromagnétique. Le fait que ce champ puisse se propager dans le vide, sans milieu porteur, fut l'une des découvertes les plus importantes du XIXe siècle.

<margin>
Longtemps, la physique a cru à l'existence d'un « éther », présent partout, dans lequel les ondes électromagnétiques se propageraient comme le son dans l'air. Cette conception était fausse, mais le terme s'est maintenu dans le langage courant : par exemple, nous sommes assis au récepteur et *à l'écoute de l'éther*.
</margin>

---

Comme son nom l'indique déjà, le champ électromagnétique se compose de deux composantes, le champ électrique et le champ magnétique. Lorsque le champ électrique et le champ magnétique varient dans le temps, les deux composantes de champ apparaissent toujours conjointement.

Commençons toutefois par le champ électrique invariable dans le temps, aussi appelé champ statique. Le champ électrique est généralement désigné par la lettre $E$.

<margin>
[picture:881:e_plattenkondensator: Un condensateur plan sous tension, avec un champ électrique homogène]
</margin>
  
---

La figure [ref:e_plattenkondensator] montre schématiquement un *condensateur plan*, aux bornes duquel une tension $U$ est appliquée. Les armatures sont isolées l'une de l'autre, aucun courant ne circule. La tension a pour effet d'accumuler des porteurs de charge positifs sur l'armature de gauche et négatifs sur l'armature de droite. Entre les deux armatures s'établit un champ électrique statique $E$. Si nous supposons que l'étendue des armatures en longueur et en largeur est très supérieure à leur écartement, alors l'intensité du champ est indépendante du lieu — nous parlons d'un champ *homogène*. L'intensité du champ électrique se calcule alors très simplement :

$E = \frac{U}{d}$

où $d$ est l'écartement des armatures.

<unit>
De l'équation $E = \frac{U}{d}$ découle aussi l'unité de l'intensité du champ électrique : $\unit{\volt\per\meter}$
</unit>

[question:EB101]
[question:EA103]

---

Pour calculer l'intensité du champ électrique dans un condensateur plan, nous devons connaître la tension appliquée et l'écartement des armatures. Les condensateurs plans se rencontrent souvent dans les boîtes d'accord d'antenne.

<danger>
Pour ces questions, il faut impérativement veiller à la bonne unité !
</danger>

[question:EB102]

Ici, on peut de nouveau calculer simplement avec la formule ci-dessus :

$E = \frac{\qty{9}{\volt}}{\qty{0,6}{\centi\meter}} = \frac{\qty{9}{\volt}}{\qty{0,006}{\meter}} = \qty{1500}{\volt\per\meter}$

Un *condensateur bobiné* peut se représenter comme un condensateur plan à armatures très larges qui ont été enroulées. Entre les armatures se trouve toutefois une couche isolante, le *diélectrique*. Il augmente la *capacité* du condensateur — l'aptitude à stocker des charges. Le diélectrique n'a cependant aucune influence sur le calcul de l'intensité du champ à l'intérieur.

[question:EB103]

Pour cette question aussi, nous faisons de nouveau appel à notre formule :

$E = \frac{\qty{300}{\volt}}{\qty{0,15}{\milli\meter}} = \frac{\qty{300}{\volt}}{\qty{0,00015}{\meter}} = \qty{2000000}{\volt\per\meter} = \qty{2000}{\kilo\volt\per\meter}$

Les diélectriques ne peuvent supporter qu'une intensité de champ électrique limitée avant de perdre leur pouvoir isolant. L'intensité de champ limite à laquelle cela se produit est aussi appelée *rigidité diélectrique*. Si nous connaissons la rigidité diélectrique et l'épaisseur du diélectrique, nous pouvons calculer la tension maximale que le condensateur peut supporter.

Si la rigidité diélectrique est $E_d$ et l'épaisseur du diélectrique *d*, alors la tension de claquage vaut :

$U_d =E_d \cdot d$

[question:EB104]

Ici, nous calculons avec la formule ci-dessus (attention aux unités !) :

$\begin{split} U_d &= \qty{400}{\kilo\volt\per\centi\meter} \cdot \qty{0,15}{\milli\meter} \\ &= \qty{40000000}{\volt\per\meter} \cdot \qty{0,00015}{m} \\ &= \qty{6000}{\volt} \\ &= \qty{6}{\kilo\volt} \end{split}$

---

Une autre compétence importante consiste à distinguer, sur des croquis, les lignes de champ électrique des lignes de champ magnétique traitées plus loin.

Avec une règle empirique simple, c'est assez facile : les lignes de champ électrique ont un début et une fin, les lignes de champ magnétique non ! Le sens du champ électrique va toujours du potentiel le plus positif vers le plus négatif.

[question:EB105]

<margin>
[picture:884:e_feldlinien_vertikalantenne:Lignes de champ sur une antenne verticale]
</margin>
