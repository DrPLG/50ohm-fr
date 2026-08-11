Dans la modulation de phase, la phase d'une onde porteuse est modifiée en fonction du signal de modulation. Cela signifie que le déphasage de l'onde porteuse varie directement proportionnellement à l'amplitude du signal de modulation. Cette variation de la phase se conserve au cours du signal et varie, par rapport à l'onde porteuse initiale, selon un motif déterminé. Le résultat est un signal sinusoïdal dont le « décalage » (phase) s'adapte en permanence, sans que l'amplitude du signal ne change.

On peut se représenter imagée la modulation de phase comme le décalage de la courbe sinusoïdale le long de l'axe du temps, chaque variation de la phase étant commandée par le signal de modulation. Plus l'amplitude du signal de modulation est forte, plus la phase du signal porteur se décale.

La modulation de phase et la modulation de fréquence appartiennent toutes deux au groupe des techniques de modulation angulaire, car elles influencent toutes deux l'angle de l'onde porteuse. La différence réside dans le fait qu'en modulation de fréquence, c'est la fréquence qui est directement influencée et, en modulation de phase, la phase.

Cela se manifeste particulièrement nettement avec un signal rectangulaire comme signal utile : en modulation de phase, chaque front du rectangle provoque un saut de phase immédiat du signal porteur, tandis qu'en modulation de fréquence, le front du signal ne déclenche qu'un changement de fréquence – la variation de phase qui en résulte n'apparaît qu'indirectement, en s'accumulant continûment au cours du temps.

<margin>
[picture:907:a_phasenmodulation:Modulation de phase avec inversion de la phase]
</margin>

<webonly>
<margin>
[include:applet_pm]
</margin>
</webonly>

<indepth>
Pour les personnes intéressées par les mathématiques : en modulation de phase, le signal utile $m(t)$ a une influence directe sur la phase, par ex. : 

$\varphi(t) = m(t)$

Le signal porteur est produit sous la forme d'une oscillation sinusoïdale de la forme

$s(t) = A_c \cos(2\pi f_c t + \varphi(t))$

où $A_c$ est l'amplitude, $f_c$ la fréquence porteuse et $\varphi(t)$ la phase modulée.

Les deux types de modulation FM et PM sont étroitement liés : la modulation de phase d'un signal entraîne indirectement une variation de la fréquence, et inversement la modulation de fréquence produit une variation de la phase. Mathématiquement, on peut exprimer la relation entre la fréquence et la phase par la relation suivante :

$f_i(t) = \frac{1}{2\pi} \cdot \frac{d\varphi(t)}{dt}$

Cela signifie que la fréquence est la dérivée temporelle de la phase.

Il est donc possible de réaliser la modulation de fréquence par la modulation de phase, en intégrant le signal utile $m(t)$ :

$\varphi(t) = 2\pi \int m(t) \, dt$

Le résultat est ensuite introduit comme $\varphi(t)$ dans la fonction porteuse.
</indepth>

[question:AE313]