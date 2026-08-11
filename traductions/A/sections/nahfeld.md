Le champ électromagnétique d'une antenne se divise, comme le montre la figure [ref:a_nahfernfeld], en un *champ proche* situé dans l'environnement immédiat de l'antenne et un *champ lointain* plus éloigné. Le champ proche se subdivise en outre en *champ proche réactif* et *champ proche rayonnant*.

<tip>
Dans l'[explication des procédés d'évaluation selon la BEMFV](https://50ohm.de/bemfv) la BNetzA a expliqué les notions et les procédés pour la détermination des distances de sécurité.
[photo:80:n_Bewertungsverfahren:Ce document décrit les procédés d'évaluation]
</tip>

[picture:1113:a_nahfernfeld:Définitions des distances pour le champ proche et le champ lointain selon la Bundesnetzagentur (BNetzA).]

---

Selon la définition de la Bundesnetzagentur (BNetzA) utilisée dans la figure, le champ proche réactif s'étend jusqu'à une distance de

$d \le \dfrac{\lambda}{2 \cdot \pi}$

de l'antenne, où $\lambda$ désigne la longueur d'onde. Au-delà commence le champ proche rayonnant. La distance de cette limite dépend donc de la longueur d'onde. Pour une longueur d'onde de $\qty{20}{\meter}$ par exemple, il vient :

$d = \frac{\qty{20}{\meter}}{2 \cdot \pi} \approx \qty{3,18}{\meter}$

Dans cet exemple, le champ proche réactif s'étend donc jusqu'à une distance d'environ $\qty{3,18}{\meter}$ de l'antenne.

Dans le champ proche réactif d'une antenne, l'intensité de champ électrique et l'intensité de champ magnétique ne présentent entre elles aucune relation de phase constante. Ce que cela signifie exactement est expliqué plus en détail dans l'approfondissement ci-contre.

[question:AK101]

Si l'on observe l'évolution des champs électrique et magnétique d'une antenne dipôle sur ces différentes zones, figure [ref:a_dipol_feld_e_h], on constate que les deux grandeurs de champ n'ont pas les mêmes valeurs. Le champ électrique est nettement plus fort que le champ magnétique. Pour une antenne cadre magnétique, figure [ref:a_loop_feld_e_h], c'est exactement l'inverse : le champ magnétique est nettement plus fort que le champ électrique.

<margin>
[picture:1114:a_dipol_feld_e_h:Évolution des intensités de champ électrique et magnétique d'une antenne dipôle sur les zones de champ proche et de champ lointain (échelle logarithmique).]
[picture:1115:a_loop_feld_e_h:Évolution des intensités de champ électrique et magnétique d'une antenne cadre sur les zones de champ proche et de champ lointain (échelle logarithmique).]
</margin>

<indepth>
Pour les lecteurs intéressés par les mathématiques et déjà familiers des nombres complexes, on explique ici de façon simplifiée pourquoi les intensités de champ électrique et magnétique ne possèdent pas, dans le champ proche réactif, de relation de phase indépendante du lieu.
Pour un dipôle électriquement court, les champs se composent, de façon simplifiée, de plusieurs contributions :

$ \underline{E}(r)~=~\left( \underbrace{\frac{A}{r^3}}_{\text{quasistatique}} + \underbrace{j\,\frac{B}{r^2}}_{\text{inductif}} + \underbrace{\frac{C}{r}}_{\text{rayonnement}} \right) e^{-jkr}$

$ \underline{H}(r)~=~\left( \underbrace{j\,\frac{D}{r^2}}_{\text{inductif}} + \underbrace{\frac{F}{r}}_{\text{rayonnement}} \right) e^{-jkr}. $

Les grandeurs soulignées sont complexes et décrivent, outre l'amplitude, la phase de chacune des contributions. Les facteurs tels que $j$ ou $-j$ dans les équations complètes des champs correspondent à des déphasages de $\qty{90}{\degree}$ et de $\qty{-90}{\degree}$ respectivement.

Comme les différentes contributions décroissent plus ou moins vite avec la distance $r$, leur rapport évolue. La différence de phase entre intensité de champ électrique et intensité de champ magnétique dépend de ce fait, dans le champ proche, de la distance, de la direction et de la forme de l'antenne.

Une compréhension complète suppose d'examiner chacune des composantes vectorielles des équations des champs. Ces relations dépassent nettement le programme de la classe A et ne sont pas exigibles à l'examen.
</indepth>

Dans le champ proche réactif en particulier, de fortes intensités de champ locales peuvent apparaître, en raison des contributions électriques ou magnétiques élevées qui décroissent rapidement avec la distance. Cette zone est qualifiée de *réactive* parce qu'une grande partie de l'énergie du champ n'est pas rayonnée, mais oscille entre l'antenne et le champ. Exactement comme dans un condensateur (champ électrique) ou une bobine (champ magnétique), l'énergie emmagasinée dans le champ proche réactif n'est pas consommée mais restituée à l'antenne avec un déphasage — ce va-et-vient entre le champ et l'antenne correspond à la partie réactive de l'impédance d'antenne, tandis que seule la partie active (résistance de rayonnement) décrit la puissance effectivement rayonnée.

Dans le *champ proche rayonnant*, dans la zone

$\frac{\lambda}{2\pi} < d < 4\cdot\lambda$

les contributions rayonnées passent progressivement au premier plan. Le rapport entre intensité de champ électrique et intensité de champ magnétique se rapproche de plus en plus de celui du champ lointain. L'antenne ne commence toutefois pas à rayonner seulement dans cette zone, elle rayonne par principe dès le départ ; ce sont seulement les contributions réactives du champ qui perdent de leur importance à mesure que la distance augmente. Pour bien des considérations simplifiées, le champ proche rayonnant peut déjà être traité comme le champ lointain. Nous y reviendrons plus en détail.

Le *champ lointain* commence, selon la définition retenue ici, à une distance de

$d \ge 4\cdot\lambda$

de l'antenne. Dans cette zone, l'intensité de champ électrique et l'intensité de champ magnétique décroissent chacune proportionnellement à $\frac{1}{d}$. En outre, les deux composantes du champ sont dans un rapport fixe l'une par rapport à l'autre et présentent une relation de phase constante.

---

Le rapport des modules de l'intensité de champ électrique et de l'intensité de champ magnétique est appelé *impédance d'onde* :

$Z_\mathrm{F}(d)=\left|\frac{E(d)}{H(d)}\right|$

La figure [ref:a_feldwellenwiderstand] montre comment l'impédance d'onde varie à mesure que l'on s'éloigne de l'antenne. Dans le champ proche réactif, elle dépend fortement de la forme de l'antenne, de la direction considérée et de la distance. Elle peut y être nettement plus grande ou nettement plus petite que l'impédance d'onde de l'espace libre.

Dans le champ proche rayonnant, le rapport de l'intensité de champ électrique à l'intensité de champ magnétique se rapproche progressivement de la valeur de l'espace libre. Dans le champ lointain, elle est enfin constante et vaut approximativement :

$Z_0 = \sqrt{\dfrac{\mu_0}{\varepsilon_0}} \approx \qty{120\pi}{\ohm} \approx \qty{377}{\ohm}$

L'impédance d'onde de l'espace libre relie entre elles les grandeurs de champ électrique et magnétique. Elle mesure l'importance de l'intensité de champ électrique par rapport à l'intensité de champ magnétique.

[question:AK102]

Cette valeur est à retenir, car elle nous servira à établir la formule approchée.

Résumons :

* Le champ lointain d'une source de rayonnement est la région dans laquelle les vecteurs de l'intensité de champ électrique (E), de l'intensité de champ magnétique (H) ainsi que la direction de propagation sont perpendiculaires entre eux et ne présentent aucune différence de phase. De plus, l'impédance d'onde doit correspondre à celle de l'espace libre.
* La limite entre champ lointain et champ proche dépend en premier lieu de la longueur d'onde. Toutefois, le type d'antenne utilisé et son environnement jouent bel et bien un rôle. Pour les antennes filaires majoritairement utilisées en radioamateur (par ex. les dipôles), le champ lointain se forme à une distance d'environ $4\cdot\lambda$.

<margin>
[picture:1116:a_feldwellenwiderstand:Évolution de l'impédance d'onde sur les zones de champ proche et de champ lointain (échelle logarithmique).]
</margin>
