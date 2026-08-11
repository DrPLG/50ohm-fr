%TODO ggf. das Kapitel wo anders hinschieben 

Dans le chapitre sur le décibel, il a déjà été évoqué que les suffixes $\unit{\dBd}$ et $\unit{\dBi}$ sont utilisés dans l'indication des gains d'antenne. Dans ce cas, la valeur en décibels ne se rapporte pas à une puissance ou à une tension, mais à un radiateur de référence déterminé. Sont usuels le $\unit{\dBi}$, rapporté au radiateur sphérique isotrope, ainsi que le $\unit{\dBd}$, rapporté au dipôle demi-onde.

Le *radiateur isotrope* (cf. figure [ref:e_Kugelstrahler]) est une antenne imaginaire, hypothétique, qui rayonne avec la même intensité dans toutes les directions. Si une antenne réellement existante présente une directivité, le rayonnement est plus fort dans certaines directions et plus faible dans d'autres qu'il ne le serait pour le radiateur isotrope hypothétique. 

<margin>
[picture:751:e_Kugelstrahler:Radiateur isotrope au centre d'une sphère, produisant la même puissance rayonnée en tous les points de la surface de la sphère]
</margin>

Le gain dans une direction (par exemple la direction principale de rayonnement, qui est la direction du gain d'antenne maximal) par rapport à un radiateur isotrope peut s'indiquer en décibels $\unit{\dB}$. Au lieu de $\unit{\dB}$, on écrit $\unit{\dBi}$ pour indiquer clairement que l'on se rapporte au radiateur isotrope.

[question:EG220]

Même un simple dipôle demi-onde a un gain, car il rayonne, perpendiculairement au conducteur, $\qty{2,15}{\dB}$ plus fort que ne le ferait un radiateur isotrope. Un dipôle demi-onde a en conséquence un gain de $\qty{2,15}{\dBi}$.

On s'intéresse parfois au gain qui dépasse le gain d'un dipôle demi-onde, c'est-à-dire au gain rapporté à un dipôle demi-onde. On l'indique en $\unit{\dBd}$, le $\text{d}$ signifiant dipôle. Un dipôle demi-onde a en conséquence un gain de $\qty{0}{\dBd}$. Les antennes qui présentent plus de gain qu'un dipôle demi-onde ont un gain supérieur à $\qty{0}{\dBd}$ et les antennes de gain inférieur à celui d'un dipôle demi-onde, en conséquence, moins de $\qty{0}{\dBd}$.

Comparons encore une fois le gain d'un dipôle demi-onde indiqué en $\unit{\dBi}$ et indiqué en $\unit{\dBd}$ : le dipôle demi-onde a, dans la direction principale de rayonnement, un gain de $\qty{2,15}{\dBi}$, car il rayonne $\qty{2,15}{\dB}$ plus fort que le radiateur isotrope. Indiqué en $\unit{\dBd}$, cela fait toutefois $\qty{0}{\dBd}$. L'indication en $\unit{\dBi}$ est toujours supérieure de $\qty{2,15}{\dB}$ à l'indication en $\unit{\dBd}$.

Cela figure aussi dans le recueil de formules : 

$g_i = g_d + \qty{2,15}{\dB}$

[question:EG221]
