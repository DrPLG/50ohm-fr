Un oscilloscope est un appareil de mesure de tension capable de visualiser l'évolution des tensions au cours du temps. Comme les autres voltmètres, les oscilloscopes possèdent une forte résistance interne. La plupart du temps, deux tensions ou plus peuvent être mesurées simultanément. L'appareil de la figure [ref:e_oszilloskop_digital] est par exemple réglé de manière à ce que deux signaux se partagent l'écran.

<margin>
[photo:212:e_oszilloskop_digital: Oscilloscope doté de nombreuses fonctions supplémentaires]
</margin>

Examinons maintenant d'un peu plus près l'affichage de l'oscilloscope de la figure [ref:e_oszilloskop_bildschirmfoto_sinus]. Un oscilloscope permet par exemple de déterminer les grandeurs caractéristiques d'une tension alternative sinusoïdale ($T$, $\hat{U}$, $U_\text{SS}$ et $U_\text{eff}$). À côté du tracé du signal sont affichées une indication de temps et une indication de tension — dans l'exemple $\qty{50,0}{\nano\second}$ et $\qty{500}{\milli\volt}$. Cela signifie qu'un carreau correspond, horizontalement, à 50 nanosecondes et, verticalement, à 500 millivolts. Ces carreaux sont souvent appelés divisions ou graduations, d'où aussi la notation $\qty{500}{\milli\volt\per\oszidiv}$.

<margin>
[photo:214:e_oszilloskop_bildschirmfoto_sinus:une tension sinusoïdale représentée sur un oscilloscope numérique]
</margin>

---

Nous pouvons nous représenter cela comme un système de coordonnées et y lire la période ($T$) et l'amplitude ($\hat{U}$). Dans l'exemple, une période fait 5 carreaux ou divisions de long. Multiplié par $\qty{50,0}{\nano\second}$ par division, cela donne une période de $\qty{250,0}{\nano\second}$. L'amplitude, c'est-à-dire l'écart maximal par rapport à la position de repos, vaut $\qty{1500}{\milli\volt}$ ou $\qty{1,5}{\volt}$, car elle mesure 3 divisions de haut et chaque division correspond à $\qty{500}{\milli\volt}$.

[question:EI301]

<tip>
Pour les mesures simples, beaucoup d'oscilloscopes numériques disposent d'une touche AUTO. Lorsqu'on l'actionne, certains réglages sont effectués automatiquement et une image stable des signaux appliqués apparaît le plus souvent. L'affichage peut être déplacé horizontalement. Un bouton rotatif remplissant cette fonction porte souvent l'inscription X-Position. Pour lire la période, on amène un point remarquable comme un passage par zéro sur une ligne verticale du quadrillage et l'on compte combien de divisions correspondent à une période.
</tip>
 
---

Dès que la période d'une oscillation est connue, on peut aussi en déduire la fréquence. En classe N, nous avons déjà découvert la relation qualitative : la fréquence indique le nombre d'oscillations par seconde. Si la période vaut une seconde, il en résulte une fréquence de $\qty{1}{\hertz}$. Si nous divisons la période par deux, à une demi-seconde, deux oscillations tiennent dans une seconde — la fréquence est alors de $\qty{2}{\hertz}$.

En classe E, nous considérons désormais cette relation sous forme de formule :
  
$f=\dfrac{1}{T}$ ou $T=\dfrac{1}{f}$

La fréquence en hertz est l'inverse de la période en secondes.

Le signal de la figure [ref:e_oszilloskop_bildschirmfoto_sinus] a donc la fréquence

$f = \dfrac{1}{\qty{250}{\nano\second}} = \qty{4}{\mega\hertz}$.
 
[question:EB408]
[question:EB409]
[question:EB411]
[question:EB410]
[question:EI302]

---

Il arrive que des signaux soient déformés involontairement. Cela se produit par exemple lorsqu'on injecte une tension d'entrée trop élevée dans un amplificateur. On dit alors que l'amplificateur est saturé et que son signal de sortie est distordu. Les distorsions fortes, comme sur la figure [ref:e_oszilloskop_verzerrt], se repèrent à l'oscilloscope. Pour l'appréciation des signaux audio en radioamateurisme, cela suffit le plus souvent.

<margin>
[photo:215:e_oszilloskop_verzerrt:signal d'entrée sinusoïdal (en haut) et signal de sortie distordu d'un amplificateur saturé]
</margin>

<indepth>
Savoir si un signal haute fréquence est exempt de distorsions susceptibles d'affecter d'autres plages de fréquences ne peut pas s'apprécier suffisamment bien avec un oscilloscope. Pour cela, l'appareil de mesure approprié est l'analyseur de spectre.
</indepth>

% EI304 NF-Verzerrungen 
[question:EI304]
