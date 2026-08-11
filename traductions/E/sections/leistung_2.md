En classe N, nous avons déjà découvert la notion de puissance comme produit du courant et de la tension ($P = U \cdot I$). En classe E, nous approfondissons ce sujet, notamment en nous intéressant à la transformation de formules.

---

Pour cela, considérons le montage de la figure [ref:e_leistung_r]. Il montre comment, dans une résistance, la puissance électrique est transformée en chaleur. En supposant les grandeurs $P$ et $R$ connues, on peut déterminer la tension $U$ à l'aide de la formule de la puissance ($P = U \cdot I$) et de la loi d'Ohm ($U = R \cdot I$).

<margin>
[picture:1013:e_leistung_r:La puissance est transformée en chaleur dans la résistance $R$]
</margin>
  
---

<tip>
Les formules établies figurent aussi, de façon claire, dans le [formulaire](https://50ohm.de/hm).
</tip>
  
Pour commencer, transformons l'équation de la loi d'Ohm pour isoler le courant :

$\begin{align*} U &= R \cdot I &\quad\quad\quad &|~: R\\ \frac{U}{R} &= \frac{\cancel{R} \cdot I}{\cancel{R}}\\[1.5ex] I &= \frac{U}{R}.\end{align*}$

En reportant cette expression de $I$ dans notre formule de la puissance, on obtient :

$\begin{split} P &= U \cdot \frac{U}{R}\\P&=\frac{U^2}{R}.\end{split}$

Nous résolvons cette équation en $U^2$ en multipliant les deux membres par R :

$\begin{align*} P &= \frac{U^2}{R} &\quad\quad\quad &|~\cdot R\\ U^2 &= P \cdot R.\end{align*}$

Nous voulons maintenant déterminer la tension $U$. Pour cela, nous appliquons l'opération inverse de l'élévation au carré, à savoir l'extraction de la racine carrée. Nous obtenons ainsi :

$\begin{align*} U^2 &= P \cdot R &\quad\quad\quad &|~\sqrt{~~}\\ U &= \sqrt{P \cdot R}.\end{align*}$

Dans certaines questions d'examen, il est important de reconnaître les bonnes relations. À l'aide du formulaire, on peut toujours retrouver la solution correcte.

[question:EB504]
  
Pour le courant $I$ aussi, on peut établir la relation entre le courant $I$, la résistance $R$ et la puissance $P$ en reportant la loi d'Ohm dans la formule de la puissance.

Nous partons des deux équations $P = U \cdot I$ et $U = R \cdot I$. En reportant la seconde équation dans la première pour $U$, on obtient :

$\begin{split} P &= R \cdot I \cdot I\\ P &= I^2 \cdot R.\end{split}$

Nous résolvons en $I^2$ en divisant les deux membres par R :

$\begin{align*} P &= I^2 \cdot R &\quad\quad\quad &|~:~R\\ I^2 &= \frac{P}{R}.\end{align*}$

Dans la dernière étape, nous extrayons alors la racine :

$\begin{align*} I^2 &= \frac{P}{R} &\quad\quad\quad &|~\sqrt{~~}\\ I &= \sqrt{\frac{P}{R}}\end{align*}$

[question:EB505]

Si l'on connaît la puissance $P$ et le courant $I$ ou la tension $U$, on peut toujours en calculer la résistance $R$.

Nous connaissons déjà :

$P=\frac{U^2}{R}$

Nous résolvons en R en multipliant les deux membres de l'équation par R, puis en divisant par P :

$R = \frac{U^2}{P}$

D'autre part, $P = I^2 \cdot R$. Nous divisons les deux membres par $I^2$ et obtenons l'expression recherchée :

$R = \frac{P}{I^2}$

[question:EB506]

Toutes les relations présentées précédemment en technique du courant continu entre puissance, courant et tension valent aussi pour le courant alternatif. Il faut toutefois alors utiliser les valeurs efficaces du courant et de la tension. Dans un chapitre précédent, nous avons déjà découvert comment calculer la valeur efficace à partir de la valeur de crête :

$U_\text{eff} = \frac{\hat{U}}{\sqrt{2}}\text{ ou }\hat{U} = U_\text{eff} \cdot \sqrt{2}$

[question:EB503]

Cela signifie qu'avec toutes les formules établies précédemment, nous pouvons maintenant aussi calculer les exercices suivants issus du monde de la haute fréquence — c'est-à-dire de la tension alternative.

%%%%%

[question:EB507]

La valeur efficace est ici $U_\text{eff} = \qty{100}{\volt}$. La résistance de charge est de $\qty{50}{\ohm}$ (résistance purement active). On cherche la puissance dans la charge.

$P = \frac{U^2}{R} =\frac{(\qty{100}{\volt})^2}{\qty{50}{\ohm}} = \qty{200}{\watt}$

%%%%%

[question:EB508]

Lorsque le courant est connu lui aussi, on peut calculer avec la formule connue $P = I^2 \cdot R$. Nous reportons :
  
$P = (\qty{2}{\ampere})^2 \cdot \qty{50}{\ohm} = \qty{200}{\watt}$

%%%%%

[question:EB509]

Pour calculer la puissance dissipée dans une résistance de $\qty{100}{\ohm}$ aux bornes de laquelle chute une tension de $\qty{10}{\volt}$, nous utilisons de nouveau :

$P = \frac{U^2}{R} = \frac{(\qty{10}{\volt})^2}{\qty{100}{\ohm}} = \qty{1}{\watt} $

%%%%%

[question:EB510]

Répondre à cette question demande une certaine réflexion. On indique à la fois une tenue en tension maximale ($\qty{700}{\volt}$) et une puissance maximale ($\qty{1}{\watt}$). Reste à savoir quelle limite est atteinte en premier lorsqu'on augmente la tension.

Calculons d'abord la tension qui doit être appliquée à la résistance ($\qty{10}{\kilo\ohm}$) pour que la puissance admissible soit tout juste atteinte. Pour cela, nous calculons (démonstration plus haut) :

$U = \sqrt{P \cdot R} = \sqrt{\qty{1}{\watt} \cdot \qty{10000}{\ohm}} = \qty{100}{\volt}$

C'est déjà la tension continue maximale recherchée !

%%%%%

[question:EB511]

Ici, la démarche de calcul est la même que dans l'exercice précédent, seules les valeurs numériques diffèrent :

$U = \sqrt{P \cdot R} = \sqrt{\qty{6}{\watt} \cdot \qty{10^5}{\ohm}} \approx \qty{774,6}{\volt} \approx \qty{775}{\volt}$

%%%%%

[question:EB512]

Lorsque la valeur de la résistance et la charge maximale admissible sont données et que l'on cherche le courant maximal, nous utilisons la relation :

$I = \sqrt{\frac{P}{R}} =  \sqrt{\frac{\qty{23}{\watt}}{\qty{120}{\ohm}}} \approx \qty{0,4378}{\ampere} \approx \qty{438}{\milli\ampere}$

[question:EB513]

Dans cette question, un oscilloscope est utilisé pour mesurer la tension crête à crête dans la charge. Cette tension vaut $U_\text{SS} = \qty{25}{\volt}$. Cela signifie que la tension de crête vaut $\hat{U} = \qty{12,5}{\volt}$. Nous calculons d'abord la valeur efficace de la tension :

$U_\text{eff} = \frac{\hat{U}}{\sqrt{2}} = \frac{\qty{12,5}{\volt}}{\sqrt{2}} \approx \qty{8,84}{\volt}$

Le courant efficace vaut alors (loi d'Ohm) :

$I_\text{eff} = \frac{U_\text{eff}}{R} = \frac{\qty{8,84}{\volt}}{\qty{1000}{\ohm}} \approx \qty{8,8}{\milli\ampere}$

On pourrait aussi en déduire la puissance efficace, mais la question ne va pas jusque-là.

---

[question:EB514]

La réponse à cette dernière question se calcule très bien de tête. On monte ici 11 résistances identiques en parallèle, comme le montre la figure [ref:e_dummyload_11]. Autrement dit, le courant qui traverse chaque résistance est $1/11$ du courant total. La puissance dans chaque résistance n'est donc elle aussi que $1/11$ de la puissance totale.

La puissance totale admissible est donc $11 \cdot \qty{5}{\watt} =\qty{55}{\watt}$.

<margin>
[picture:1014:e_dummyload_11:Charge fictive constituée de 11 résistances de même valeur]
</margin>
