Dans le calcul des distances de sécurité, l'atténuation angulaire des antennes directives joue un rôle important. La plus grande puissance rayonnée est émise au centre du lobe de rayonnement. Dans les autres directions, elle est plus faible. Si l'antenne est suffisamment haute, elle rayonne en grande partie au-dessus de la zone <u>non</u> contrôlable, c'est-à-dire la zone dans laquelle les valeurs limites doivent impérativement être respectées.

<margin>
[picture:950:a_richtantenne_personenschutz:À un angle de $\qty{40}{\degree}$ sous l'axe du lobe de rayonnement principal, la puissance rayonnée est inférieure de $\qty{6}{\decibel}$ à celle obtenue à l'angle $\qty{0}{\degree}$.]
</margin>

Sur la figure [ref:a_richtantenne_personenschutz], une zone non contrôlable, dans laquelle des personnes peuvent se trouver, est représentée à l'angle critique de $\qty{40}{\degree}$ sous l'antenne. La puissance rayonnée y est inférieure de $\qty{6}{\dB}$ à celle du centre du diagramme de rayonnement. La conséquence directe est que la distance de sécurité peut y être d'autant plus faible.

$\qty{6}{\dB}$ correspondent à un facteur de $\num{0,25}$ ou $\dfrac{1}{4}$ (recueil de formules).

$ E = \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{d}$
Réarrangement de la formule selon $d$ (distance de sécurité).
$ d = \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{E}$

La puissance rayonnée $P_\textrm{EIRP}$ n'est pas connue. Nous savons toutefois que, dans ce calcul, nous ne devons prendre en compte qu'un quart de la puissance rayonnée par rapport à la puissance rayonnée maximale.

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}\cdot \dfrac{1}{4}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{E}\cdot \sqrt{\dfrac{1}{4}}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_\textrm{EIRP}}}{E}\cdot \mathbf{\dfrac{1}{2}}\end{split}$

Si la puissance rayonnée est réduite à $\dfrac{1}{4}$, la distance de sécurité de $\qty{20}{\meter}$ est divisée par deux. Elle diminue à $\qty{10}{\meter}$ dans l'exemple concret.

[question:AK105]
