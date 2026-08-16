Un montage en série de deux résistances est fréquemment utilisé comme diviseur de tension. En classe E, nous considérons d'abord le *diviseur de tension à vide* (non chargé), tel qu'il apparaît aussi dans les exercices suivants. Dans un diviseur de tension à vide, les tensions sont proportionnelles aux résistances. Cela signifie par exemple qu'une tension plus grande chute aux bornes d'une résistance de forte valeur, tandis qu'une tension d'autant plus petite est mesurable aux bornes d'une résistance de faible valeur.

<margin>
[picture:819:E 63. Spannungsteiler:Diviseur de tension]
</margin>

<indepth>
On trouve un diviseur de tension important, par exemple, à la base d'un transistor dans un montage amplificateur.
On parle alors du diviseur de tension de base. Nous examinerons cela de plus près dans le chapitre sur les amplificateurs.
</indepth>

Cette relation peut être représentée par différentes formules, que nous trouvons dans le formulaire :

$\frac{U_{1}}{U_{2}} = \frac{R_{1}}{R_{2}}$

ou

$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$

% TODO implementiere Attention in CSS!
<danger>
Pour un diviseur de tension chargé, ces formules ne s'appliquent pas. Des questions à ce sujet suivront en classe A.
</danger>

Dans les questions suivantes, le terme « diviseur de tension » n'est pas mentionné directement, mais le choix des mots — « Comment la tension se répartit-elle sur deux résistances montées en série… » — doit permettre de reconnaître qu'il s'agit d'un diviseur de tension.

[question:ED101]

Aucune valeur concrète de résistance n'est indiquée ; le résultat doit donc être présenté sous forme de formule générale.
D'après l'énoncé, $R_1$ est 5 fois plus grande que $R_2$ ; on doit donc aussi pouvoir mesurer à ses bornes une tension 5 fois plus grande, soit $R_1 = 5 \cdot R_2$

Cette relation peut s'exprimer par une formule.

$\frac{U_{1}}{U_{2}} = \frac{5 \cdot R_2}{R_2}$

Les $R_2$ se simplifient et il en résulte :

$\frac{U_{1}}{U_{2}} = \frac{5}{1}$

Après quelques transformations, nous obtenons le résultat :

$U_{1} = U_{2} \cdot \frac{5}{1}$

$U_{1} = 5 \cdot U_{2}$

[question:ED102]

Pour cette question, la relation est inverse de celle de la question ED 101. D'après l'énoncé, $R_1$ est 6 fois plus petite que $R_2$ ; on doit donc aussi pouvoir mesurer à ses bornes une tension 6 fois plus petite.

Cette relation, exprimée par une formule, s'écrit alors :

$\frac{U_{1}}{U_{2}} = \frac{1}{6}$
  
$U_{1} = U_{2} \cdot {\frac{1}{6}}$
  
$U_1 = \frac{U_2}{6}$

[question:ED103]

Pour cette question, des valeurs concrètes de résistance sont indiquées, qui servent à déterminer le rapport du diviseur de tension. $R_1$ est à $R_2$ comme $\qty{10}{\kilo\ohm}$ est à $\qty{20}{\kilo\ohm}$, soit $1$ à $2$. $U_2$ doit donc être deux fois plus grande que $U_1$. Mais c'est la tension totale $U_g$ qui est indiquée. Celle-ci est appliquée à une résistance totale de $\qty{30}{\kilo\ohm}$ et se répartit donc dans le rapport $30$ à $20$ (ou $3$ à $2$) par rapport à $R_2$. Aux bornes de $R_2$, on doit donc pouvoir mesurer la tension $2/3$ de $U_g$.

Bien entendu, ce résultat peut aussi se calculer avec la formule du formulaire :

$\frac{U_{2}}{U_g} = \frac{R_{2}}{R_{1} + R_{2}}$

puis en la transformant pour isoler $U_2$ :

$U_{2} = \frac{R_{2}}{R_{1} + R_{2}} \cdot U_g$
