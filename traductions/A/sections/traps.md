Nous avons déjà fait connaissance avec les antennes multibandes, délibérément résonantes sur plusieurs bandes, p. ex. l'antenne alimentée par l'extrémité avec son transformateur 1:49. Revenons à notre exemple de la section « Alimentation en courant et en tension II » : un dipôle demi-onde alimenté au centre peut, outre sa fréquence fondamentale, être en principe résonant aussi aux multiples impairs de cette fréquence. Ainsi, un dipôle prévu pour la bande des $\qty{80}{\meter}$, de fréquence fondamentale $\qty{3,5}{\mega\hertz}$, présente d'autres résonances approximativement à $\qty{10,5}{\mega\hertz}$ et $\qty{17,5}{\mega\hertz}$.

Aux multiples pairs de la fréquence fondamentale, p. ex. à $\qty{7}{\mega\hertz}$ ou $\qty{14}{\mega\hertz}$, on trouve en revanche au point d'alimentation central un minimum de courant, et donc une impédance élevée. Ces fréquences ne sont de ce fait pas directement utilisables sur un simple dipôle alimenté au centre. Une possibilité de produire délibérément des résonances supplémentaires sur de telles fréquences est le *dipôle à circuits bouchons*, que l'on désigne aussi comme *dipôle à traps*.

Dans un dipôle à circuits bouchons, chaque moitié de dipôle comporte au moins un circuit oscillant parallèle formé d'une bobine et d'un condensateur. Un tel circuit oscillant est appelé *trap* (de l'anglais « piège »). Un circuit oscillant parallèle est à haute impédance à sa fréquence de résonance (cf. figure [ref:a_sperrkreis]). Il agit alors comme un *circuit bouchon* et empêche très largement le courant de circuler dans la partie du dipôle située plus à l'extérieur. Un même dipôle peut ainsi présenter des longueurs électriques différentes selon les bandes de fréquences.

<margin>
[picture:1036:a_sperrkreis:Réponse en fréquence qualitative d'un circuit oscillant parallèle (circuit bouchon)]
</margin>

[question:AG109]
[question:AG110]

---

La manière dont un trap agit sur le dipôle dépend de la position de la fréquence de travail par rapport à sa fréquence de résonance $f_\mathrm{res}$.

* À $f=f_\mathrm{res}$, le circuit oscillant parallèle est à haute impédance et agit en circuit bouchon. La partie extérieure du dipôle se trouve ainsi très largement séparée de la partie intérieure.
* À $f<f_\mathrm{res}$, l'effet inductif du trap prédomine. Il agit à la manière d'une bobine d'allongement et allonge électriquement le brin rayonnant.
* À $f>f_\mathrm{res}$, l'effet capacitif du trap prédomine. Le brin rayonnant s'en trouve électriquement un peu raccourci.

<margin>
Cet applet permet d'étudier l'effet d'un trap sur un dipôle pour différentes fréquences :

[include:applet_traps]
</margin>

Le cas de la résonance est d'abord particulièrement parlant. Lorsque le dipôle est exploité à la fréquence de résonance du trap (p. ex. $\qty{7.05}{\mega\hertz}$ sur notre figure), le circuit oscillant parallèle est à haute impédance. Il ne circule donc que peu de courant dans la partie extérieure du dipôle. Le dipôle se comporte approximativement comme s'il se terminait à l'emplacement du trap.

[question:AG112]

Cette relation peut être mise à profit pour concevoir un dipôle bibande. Pour la bande la plus haute en fréquence, c'est la distance entre les deux traps qui détermine pour l'essentiel la longueur utile du dipôle. À cette fréquence, les tronçons de fil extérieurs sont très largement séparés par l'effet de blocage des traps, comme s'ils n'étaient pas là, et le dipôle se comporte comme un dipôle plus court.

[question:AG116]

---

Si le dipôle est en revanche exploité à une fréquence *inférieure* à la fréquence de résonance du trap (p. ex. $\qty{3.5}{\mega\hertz}$ sur notre figure), le circuit oscillant n'est plus à haute impédance. Son effet inductif prédomine. Le trap agit de ce fait à la manière d'une bobine d'allongement et allonge électriquement le dipôle. Le dipôle tout entier, tronçons de fil extérieurs compris, peut ainsi être utilisé pour une bande de fréquences plus basse.

[question:AG111]

---

À une fréquence *supérieure* à la fréquence de résonance, c'est en revanche l'effet capacitif du trap qui prédomine. Le trap agit alors en raccourcissant électriquement, et il peut même être résonant à p. ex. $\qty{14}{\mega\hertz}$. Cet effet doit lui aussi être pris en compte lors du dimensionnement d'un dipôle à circuits bouchons.

[question:AG113]

---

Des paires de traps multiples permettent de construire des dipôles pour davantage de bandes de fréquences encore. Les traps destinés aux fréquences les plus élevées sont alors placés le plus à l'intérieur, car c'est pour elles qu'est requise la plus courte longueur utile de dipôle.

Le trap le plus intérieur est donc accordé sur la fréquence la plus haute prévue. La paire de traps immédiatement plus extérieure est accordée sur la fréquence immédiatement inférieure, et ainsi de suite. Plus la fréquence de travail est basse, plus les portions du dipôle qui deviennent actives sont grandes.

[question:AG115]
[question:AG114]

Les traps ne sont pas employés uniquement dans les antennes dipôles. Sur les antennes directives comme les antennes Yagi, des circuits bouchons peuvent également être utilisés dans les différents éléments, afin de rendre l'antenne utilisable sur plusieurs bandes de fréquences.
