Pour calculer la distance de sécurité, il existe une formule approchée. Nous la trouvons dans le recueil de formules : 

$ E = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{d} $

On peut rapidement la réarranger pour obtenir la distance de sécurité $d$ : 

$ d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{E} $

Le recueil de formules contient encore une remarque indiquant que la formule ci-dessus n'est valable que pour les calculs en champ lointain (respectivement en champ proche rayonnant), à partir de $ d > \frac{\lambda}{2\pi} $.

Cela tient à ce que ce n'est qu'en champ lointain que le champ électrique et le champ magnétique présentent une relation de phase fixe et constante l'un avec l'autre. Dans le champ proche réactif, en revanche, de fortes surélévations locales aussi bien du champ électrique que du champ magnétique peuvent se produire. Ces effets ne peuvent pas être saisis de manière fiable avec les formules approchées pour le champ lointain. Pour les calculs en champ proche réactif, c'est-à-dire pour des distances $d \le \frac{\lambda}{2\pi}$, des simulations numériques sont donc en règle générale nécessaires. Avec des restrictions (pas pour les antennes magnétiques, pas pour les antennes très courtes), les résultats sont aussi utilisables dans le champ proche rayonnant.

<indepth>
Le champ lointain d'une source de rayonnement est la région dans laquelle les vecteurs de l'intensité de champ électrique ($E$) et de l'intensité de champ magnétique ($H$) sont perpendiculaires l'un à l'autre et ne présentent pas de différences de phase. 

La limite entre champ lointain et champ proche dépend en premier lieu de la longueur d'onde. Le champ lointain se forme, selon les [explications relatives à la BEMFV](https://50ohm.de/ebemfv), à une distance d'environ $4\cdot\lambda$. 

Le champ proche se subdivise en champ proche *réactif* et champ proche *rayonnant*. Ce qui est pratique, c'est que dans le champ proche rayonnant, la formule pour le champ lointain peut malgré tout être utilisée. Cela tient au fait que la formule approchée fournit ici des estimations très conservatrices, c'est-à-dire que les intensités de champ réelles sont inférieures aux valeurs calculées. On est du côté sûr. 
  
Avec la formule $ d > \frac{\lambda}{2\pi} $, nous nous assurons donc d'être en dehors du *champ proche réactif*.
</indepth>

%TODO Applet basteln: https://www.leifiphysik.de/elektrizitaetslehre/elektromagnetische-wellen/versuche/dipolstrahlung-animation

C'est sur ce point que porte la question suivante :

[question:EK105]

Pour $\qty{3,5}{\mega\hertz}$, le champ lointain (champ proche rayonnant) ne commence qu'à $\qty{13,64}{\meter}$.

 $\begin{split} d &> \frac{\lambda}{2 \cdot \pi}\\ d &> \frac{\qty{85,7}{\meter}}{2 \cdot \pi}\\ d &> \qty{13,64}{\meter}\end{split}$
 
La distance de $\qty{3,65}{\meter}$ obtenue se situe nettement dans le champ proche réactif et est donc invalide. Au lieu de la formule approchée pour le champ lointain, il faut choisir une autre méthode. Entrent en ligne de compte des mesures des composantes de champ E et H, des simulations ou des calculs de champ proche.

Pour pouvoir répondre à la question suivante, il faut calculer où commence le champ lointain (champ proche rayonnant) pour les bandes des $\qty{160}{\meter}$ et des $\qty{80}{\meter}$.

[question:EK106]

Pour $\qty{160}{\meter}$ : $d > \frac{\qty{160}{\meter}}{2\pi} = \qty{25,5}{\meter}$
 
Pour $\qty{80}{\meter}$ : $d > \frac{\qty{80}{\meter}}{2\pi} = \qty{12,7}{\meter}$

Le calcul est invalide si la distance est inférieure à $\qty{25,5}{\meter}$ pour les $\qty{160}{\meter}$ et à $\qty{12,7}{\meter}$ pour les $\qty{80}{\meter}$.

%%%%

Dans la question suivante, il faut maintenant, pour la première fois, calculer une véritable distance de sécurité. 

[question:EK108]

Nous devons d'abord calculer la puissance rayonnée en $P_\textrm{EIRP}$. Nous remarquons en outre que le gain d'antenne est indiqué en $\unit{\dBd}$. Pour cela, nous utilisons de nouveau la formule du recueil de formules :

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{100}{\watt} \cdot 10^{\frac{\qty{7,5}{\dBd}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{653}{\watt}$

La somme des gains et des atténuations de l'ensemble du système d'antenne est le gain d'antenne de $\qty{7,5}{\dBd}$, moins l'atténuation de câble de $\qty{1,5}{\dB}$ et plus le gain de $\qty{2,15}{\dBi}$ pour le radiateur isotrope (le gain d'antenne est rapporté au dipôle).

Alternativement, nous pouvons, comme dans les chapitres précédents, déterminer les facteurs respectifs pour les gains et l'atténuation.
$\qty{7,5}{\dB} - \qty{1,5}{dB} = \qty{6}{\dB}$, ce qui correspond à un facteur de $\num{4}$. Le facteur pour $\qty{2,15}{\dBi}$ est $\num{1,64}$.

$P_\textrm{EIRP} = \qty{100}{\watt} \cdot 4 \cdot 1,64 = \qty{656}{\watt}$

---

Les résultats des deux méthodes de calcul devraient en principe être identiques. Ils s'écartent pourtant légèrement l'un de l'autre. C'est le résultat des arrondis sur les deux facteurs. La puissance calculée avec arrondis est toutefois suffisamment précise pour résoudre correctement la question. Nous insérons donc cette valeur dans la formule de distance :

$ d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_\text{EIRP}}}{E} = \frac{\sqrt{\qty{30}{\ohm}\cdot \qty{656}{\watt}}}{\qty{28}{\volt\per\meter}} \approx \qty{5}{\meter}  $

La distance de sécurité de $\qty{5}{\meter}$ a été déterminée avec la formule pour le champ lointain. Elle n'est donc valable que si elle se situe elle-même dans le champ lointain (respectivement le champ proche rayonnant). Cela peut se vérifier rapidement, comme ci-dessus.

$\begin{split} d &> \frac{\lambda}{2\pi}\\ d &> \frac{\qty{10}{\meter}}{2\pi}\\ d &> \qty{1,6}{\meter} \end{split}$

La distance de sécurité calculée de $\qty{5}{\meter}$ est supérieure à $\qty{1,6}{\meter}$ et se situe clairement dans le champ lointain (respectivement le champ proche rayonnant). Le calcul est donc valide. La bonne réponse est $\qty{5}{\meter}$.

<indepth>
Dans le tableau figure, pour $\qty{6}{\dB}$, un facteur de $\num{4}$. C'est une valeur arrondie, qui vaut en réalité $\num{3,981071706}$. C'est de là que vient l'erreur d'arrondi.
</indepth>
