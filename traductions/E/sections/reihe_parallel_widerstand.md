Nous sommes souvent confrontés au problème qu'une valeur de résistance souhaitée ne figure pas dans la « série normalisée de résistances ». Il se peut aussi qu'une résistance doive dissiper une grande puissance, impossible à atteindre avec des résistances individuelles du commerce — pour ne citer que deux exemples. Nous allons maintenant voir comment obtenir d'autres valeurs de résistance par montage en série ou en parallèle de résistances.

À partir de la loi d'Ohm, nous pouvons établir les règles des montages en série et en parallèle de résistances :

$U=R \cdot I$

<margin>
[picture:819:e_spannungsteiler:Diviseur de tension]
</margin>

La figure [ref:e_spannungsteiler] montre deux résistances $R_1$ et $R_2$ montées l'une derrière l'autre. Elles sont parcourues par le même courant *I*. Aux bornes des résistances chutent alors les tensions

$U_1 = R_1 \cdot I$ et  $U_2 = R_2 \cdot I$. 
La tension totale $U_g$ est simplement la somme de ces deux tensions :

$U_g = U_1 + U_2 = R_{\mathrm{ges}} \cdot {I} = R_1 \cdot I + R_2 \cdot I$

Nous pouvons maintenant calculer la résistance vue entre les bornes extérieures :
$R_{\mathrm{ges}} = \frac{U_g}{I} = R_1 + R_2$, car le courant $I$ se simplifie des deux côtés de l'équation.

Le tout fonctionne aussi avec plus de deux résistances, comme indiqué dans le formulaire :

$R_{\mathrm{ges}} = R_1 + R_2 + R_3 + R_4 + \dots$

---

Mais qu'en est-il si nous montons deux résistances $R_1$ et $R_2$ en parallèle, comme le montre la figure [ref:e_parallelschaltung] ? 

À présent, la même tension $U$ est appliquée aux deux résistances, ce qui fait circuler dans les résistances les courants

$I_1 = \frac{U}{R_1}$ et $I_2 = \frac{U}{R_2}$

.

<margin>
[picture:945:e_parallelschaltung:Dans ce montage, on voit toutes les tensions et tous les courants.]
</margin>

Le courant qui circule dans le circuit extérieur est la somme de ces deux courants :

$I = I_1 + I_2 = \frac{U}{R_1} + \frac{U}{R_2}$

Nous cherchons de nouveau une résistance totale $R_{\mathrm{ges}}$, pour laquelle on doit alors avoir : $I=\frac{U}{R_{\mathrm{ges}}}$ et par conséquent :

$\dfrac{1}{R_{\mathrm{ges}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$

---

L'inverse de la résistance totale est donc la somme des inverses des résistances individuelles. Une conséquence est que, pour un montage en parallèle d'une série de résistances identiques, il suffit de diviser la valeur d'une résistance individuelle par le nombre de résistances.

Ici aussi, nous pouvons effectuer le calcul pour un nombre quelconque de résistances en parallèle (cf. formulaire) :

$\dfrac{1}{R_{\mathrm{ges}}} = \dfrac{1}{R_1} + \dfrac{1}{R_2} + \dfrac{1}{R_3} + \dfrac{1}{R_4} + \dots$

L'expression pour deux résistances en parallèle peut aussi, selon les règles du calcul fractionnaire, s'écrire :

$R_{\mathrm{ges}} = \dfrac{R_1 \cdot R_2}{R_1 + R_2}$

<tip>
Dans un montage en série, la valeur de la résistance totale est toujours supérieure à la plus grande des résistances individuelles. Dans un montage en parallèle, la résistance totale est toujours inférieure à la plus petite des résistances individuelles.
</tip>

---

[question:ED104]
[question:ED105]
[question:ED106]

<tip>
Veiller précisément à ce que les résistances utilisées dans le calcul aient toujours les mêmes unités. Nous recommandons toujours de se ramener autant que possible à l'unité de base ($\unit{\ohm}$). Si nous montons par exemple une résistance de $\qty{1}{\kilo\ohm}$ et une de $\qty{10}{\ohm}$ en série, nous calculons $\qty{1000}{\ohm} + \qty{10}{\ohm} = \qty{1010}{\ohm}$.
</tip>

---

Certains exercices comportent des réseaux de résistances où figurent à la fois un montage en série et un montage en parallèle. Nous procédons alors ainsi : nous convertissons d'abord par exemple le montage en parallèle en une résistance équivalente, que nous regroupons ensuite avec la troisième résistance montée en série. Ou l'inverse, selon ce qui se prête le mieux au schéma.

<tip>
[picture:305:e_tipp_aufgabe:Montage exemple]

Une méthode de résolution importante est la « méthode du coup d'œil avisé »… il y a par exemple un montage comportant une résistance $R_1$ en série avec deux résistances $R_2$ et $R_3$ montées en parallèle. Les valeurs sont $R_1 = \qty{1}{\kilo\ohm}$, $R_2 = \qty{2000}{\ohm}$ et $R_3 = \qty{2}{\kilo\ohm}$. Or $\qty{2}{\kilo\ohm} = \qty{2000}{\ohm}$. Le montage en parallèle de $R_2$ et $R_3$ donne une résistance deux fois plus petite : $\qty{1000}{\ohm} = \qty{1}{\kilo\ohm}$. Nous la montons en série avec $R_1$ et obtenons le résultat : $R_{\mathrm{ges}} = \qty{2}{\kilo\ohm}$.
</tip>

[question:ED111]
[question:ED110]
[question:ED112]
[question:ED113]
[question:ED108]
[question:ED109]

Pour les considérations de puissance, le mieux est de partir de l'expression connue de la puissance :

$P = U \cdot I$

Pour un montage en série de trois résistances identiques par exemple, toutes les résistances sont parcourues par le même courant, mais aux bornes de chaque résistance ne chute qu'un tiers de la tension extérieure. Pour un montage en parallèle, la même tension est appliquée à toutes les résistances, mais le courant se répartit sur trois chemins. Dans les deux cas, le montage supporte donc le triple de la puissance d'une résistance individuelle.

[question:ED107]
