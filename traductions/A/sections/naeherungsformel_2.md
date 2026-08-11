Dans la classe E, nous avons déjà rencontré une formule approchée permettant de calculer la distance de sécurité par rapport à une antenne :

$d = \frac{\sqrt{\qty{30}{\ohm}\cdot P_{\textrm{EIRP}}}}{E}$

Cette formule peut s'appliquer à de nombreuses formes d'antennes lorsque la condition

$d > \frac{\lambda}{2\pi}$

est remplie, c'est-à-dire lorsque nous nous trouvons en dehors du champ proche réactif. Nous allons voir maintenant d'où viennent cette restriction et la valeur de $\qty{30}{\ohm}$ qui apparaît dans la formule.

Sous sa forme générale, la formule approchée s'écrit :

$d = \frac{\sqrt{\frac{Z_0}{4\pi}\cdot P_{\textrm{EIRP}}}}{E}$

où $Z_0$ désigne l'impédance d'onde de l'espace libre. Comme nous l'avons vu au chapitre précédent, celle-ci se rapproche, à mesure que l'on s'éloigne de l'antenne, de la valeur du champ lointain

$Z_0 \approx \qty{120\pi}{\ohm} \approx \qty{377}{\ohm}$

(voir figure [ref:a_feldwellenwiderstand]). En reportant cette valeur dans l'expression $\frac{Z_0}{4\pi}$, nous obtenons :

$\frac{Z_0}{4\pi} \approx \frac{\qty{120\pi}{\ohm}}{4\pi} = \qty{30}{\ohm}$

Nous retrouvons ainsi la formule approchée connue depuis la classe E. On comprend du même coup pourquoi elle ne doit pas être utilisée dans le champ proche réactif : l'impédance d'onde n'y est pas constante, mais dépend fortement de la distance, de la forme de l'antenne et de la direction considérée. Pour des calculs dans le champ proche réactif, c'est-à-dire pour des distances $d \le \frac{\lambda}{2\pi}$, il faut donc en règle générale recourir à des calculs plus détaillés, à des simulations numériques ou à des mesures.

<margin>
[picture:1116:a_feldwellenwiderstand:Évolution de l'impédance d'onde sur les zones de champ proche et de champ lointain (échelle logarithmique).]
</margin>

Lorsque la formule approchée du champ lointain est appliquée à une antenne dipôle dès le champ proche rayonnant, on obtient en règle générale une distance de sécurité plus grande que celle réellement nécessaire. L'impédance d'onde y est inférieure à $\qty{377}{\ohm}$, alors que la formule approchée calcule avec la valeur, plus élevée, du champ lointain. Le résultat est donc conservateur et se situe du côté de la sécurité. Cette manière de procéder est acceptée par la Bundesnetzagentur.

Il n'en va toutefois pas de même pour les antennes magnétiques et pour les antennes électriquement très courtes. La figure [ref:a_feldwellenwiderstand] montre par exemple que l'impédance d'onde d'une antenne cadre magnétique peut, dans le champ proche rayonnant, dépasser nettement $\qty{377}{\ohm}$. La formule approchée du champ lointain donnerait dans ce cas une distance de sécurité trop faible. Pour de telles antennes, il faut donc employer d'autres procédés, par exemple des programmes spécialisés de calcul en champ proche (simulations) ou des mesures.

[question:AK103]

Pour le calcul des distances de protection des personnes, la formule approchée déjà connue peut être utilisée dans le champ lointain. Elle permet souvent d'éviter des mesures ou des simulations coûteuses. En trafic portable en particulier, elle rend possible une estimation rapide et approximative de la distance de sécurité nécessaire.
