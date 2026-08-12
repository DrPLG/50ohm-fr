La *précision de fréquence* indique de combien une fréquence générée, réglée ou mesurée peut s'écarter de sa valeur réelle. Elle est fréquemment exprimée en pourcentage ($\unit{\percent}$), en *parties par million* ($\unit{\ppm}$) ou directement comme écart relatif.

On a alors :

$\qty{1}{\percent} = 1 \cdot 10^{-2}$

et

$\qty{1}{\ppm} = 1 \cdot 10^{-6}$

Pour un fréquencemètre, la précision atteignable dépend essentiellement de sa *base de temps*. Le fréquencemètre détermine la fréquence du signal d'entrée à l'aide d'une fréquence de référence interne. Si cette référence s'écarte de sa valeur nominale, cet écart se répercute directement sur le résultat de la mesure.

On utilise donc comme base de temps des oscillateurs aussi stables que possible. Les fréquencemètres de qualité emploient par exemple un TCXO ou un OCXO. Pour des mesures particulièrement précises, on peut aussi souvent raccorder une référence de fréquence externe, par exemple un oscillateur synchronisé par GPS (GPSDO).

Si la précision de fréquence relative est connue, on peut en calculer l'écart de fréquence maximal attendu :

$\Delta f = f \cdot a$

$f$ est ici la fréquence considérée et $a$ la précision de fréquence relative.

<indepth>
  Remarque concernant la conversion et l'écriture des puissances de dix :
  
  $1 \cdot {\num{10^{-2}}} = \frac{1}{\num{10^2}}$
  $1 \cdot {\num{10^{-6}}} = \frac{1}{\num{10^6}}$
  
  etc.
</indepth>
  
[question:AA115]

[question:AA116]

[question:AI508]

[question:AI509]

[question:AI510]

[question:AI506]

[question:AI507]
