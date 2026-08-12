Un signal idéal, purement sinusoïdal, ne se compose que de son *onde fondamentale, également appelée 1re harmonique*. Dès qu'un signal ne correspond plus à la forme sinusoïdale et ne s'en écarte serait-ce que légèrement, il contient des *multiples entiers* de son oscillation fondamentale, que l'on appelle aussi *harmoniques supérieures ou oscillations supérieures*. Il importe ici de bien différencier les deux notions d'harmonique supérieure et d'harmonique.
La figure [ref:zusammenhang_oberwellen_harmonische] et le tableau [ref:a_harmonische] montrent la relation entre harmoniques supérieures et harmoniques, qu'il suffit de mémoriser une fois pour toutes. La 1re harmonique supérieure correspond ici à la 2e harmonique de l'oscillation fondamentale et se situe au double de la fréquence de l'oscillation fondamentale. La 2e harmonique supérieure correspond à la 3e harmonique de l'oscillation fondamentale et se situe au triple de la fréquence de l'oscillation fondamentale. Selon ce principe, toutes les harmoniques et harmoniques supérieures sont rapportées à l'onde fondamentale et numérotées par un rang $N$.

<margin>
[picture:869:zusammenhang_oberwellen_harmonische:Relation entre harmoniques supérieures et harmoniques]

| l: Multiple de la fréquence fondamentale | l: Harmonique | l: Harmonique supérieure |
| $f_0$ | 1 | ~ |
| $2 \cdot f_0$ | 2 | 1 |
| $3 \cdot f_0$ | 3 | 2 |
| $4 \cdot f_0$ | 4 | 3 |
[table:a_harmonische:Harmoniques et harmoniques supérieures]
</margin>

<indepth>
Selon la nature de la distorsion d'un signal, il apparaît proportionnellement plus d'harmoniques supérieures de rang pair ou de rang impair dans son spectre de fréquences. Les signaux de forme rectangulaire, qui naissent par exemple de la saturation d'étages amplificateurs (les crêtes des amplitudes y sont limitées et aplaties), contiennent principalement des harmoniques de rang impair, c'est-à-dire des harmoniques supérieures de rang pair.

<webonly>
[include:applet_rectangle]

Aux points de discontinuité, l'approximation de Fourier présente ce qu'on appelle le *phénomène de Gibbs* : même avec un très grand nombre d'harmoniques, il subsiste un léger dépassement au-dessus et en dessous du signal.
</webonly>

Les signaux en dents de scie contiennent principalement des harmoniques de rang pair, c'est-à-dire des harmoniques supérieures de rang impair.
</indepth>

[question:AB403]
[question:AB401]
[question:AB402]

Si la fréquence fondamentale d'un signal est connue, la fréquence de la $N$-ième harmonique s'obtient en multipliant la fréquence fondamentale par le rang $N$ :

$f_N = N \cdot f_0$

Pour la $N$-ième harmonique supérieure, on a en revanche :

$f_\mathrm{HS,N} = (N+1)\cdot f_0$

[question:AJ201]
[question:AJ205]
[question:AJ202]
[question:AJ206]

Même lorsqu'un signal apparaît d'abord sinusoïdal à l'oscilloscope, il peut néanmoins contenir des composantes notables d'harmoniques supérieures (c'est-à-dire d'harmoniques de l'onde fondamentale). Pour pouvoir apprécier quantitativement et qualitativement la teneur en harmoniques supérieures d'un signal, on a besoin d'un *analyseur de spectre*, capable de représenter le signal dans le domaine fréquentiel (frequency domain) et d'y représenter logarithmiquement les valeurs d'amplitude des différentes harmoniques supérieures, de sorte que leurs parts dans le signal total soient mesurables.

[question:AI615]
[question:AI614]