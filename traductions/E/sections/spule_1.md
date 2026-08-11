Le troisième composant passif en radiotechnique — après la résistance et le condensateur — est la *bobine*. Différents types de bobines et leurs symboles sont représentés sur les figures [ref:e_spulen] et [ref:e_schaltsymbole_spulen]. Comme nous l'avons déjà appris dans le chapitre sur le champ magnétique, un champ magnétique est créé dans une bobine dès qu'un courant électrique la traverse. La forme la plus simple d'une bobine est le *solénoïde* droit (bobine cylindrique), comme le montre la figure [ref:e_spule_Aufbau].

<margin>
[photo:207:e_spulen:Différentes formes de bobines]
[picture:942:e_schaltsymbole_spulen:Symboles de différents types de bobines]
[picture:948:e_spule_Aufbau:Constitution d'une bobine]
</margin>

---

Une bobine cylindrique possède une *inductance* $L$, qui se calcule selon la formule suivante :

$L = \frac{\mu_0 \cdot \mu_r \cdot N^2 \cdot A_S}{l}$

En examinant la constitution d'une bobine, on retrouve donc les grandeurs suivantes :
1. $\mu_0$ est la constante magnétique (perméabilité du vide), une constante universelle de valeur $\qty{1,2566e-6}{\henry\per\meter}$. On peut toujours en retrouver la valeur dans le formulaire.
2. $\mu_r$ est une constante de matériau, car le noyau de la bobine peut être constitué d'un matériau particulier capable de renforcer les champs magnétiques.
3. Le nombre $N$ de spires de la bobine, en fil de cuivre émaillé ou en fil de cuivre argenté.
4. $A_S$ désigne l'aire de la section du noyau de la bobine.
5. La longueur $l$ de la bobine.

[question:EA102]

<indepth>
La lettre $L$ a été choisie en l'honneur du professeur Emil Lenz (1804–1864) de Saint-Pétersbourg, qui a formulé la loi de Lenz qui porte son nom.
</indepth>

<unit>
Une bobine possède une inductance $L$ dont l'unité est le $\qty{1}{\volt\second\per\ampere}$, habituellement exprimée en *henry* ($\unit{\henry}$). Cette unité est nommée d'après le physicien américain *Joseph Henry* (1797–1878). Une inductance de $\qty{1}{\henry}$ correspond au cas où une variation de courant de $\qty{1}{\ampere}$ en une seconde provoque une tension d'auto-induction de $\qty{1}{\volt}$. En pratique, les valeurs d'inductance sont le plus souvent nettement inférieures et sont typiquement exprimées en $\unit{\milli\henry}$, $\unit{\micro\henry}$ ou $\unit{\nano\henry}$.
</unit>

---

À l'aide de la formule et des relations qualitatives suivantes, on peut déjà résoudre une série de questions d'examen :

1. L'inductance croît avec le carré du nombre de spires. Si le nombre de spires est doublé, l'inductance est multipliée par quatre.
2. Si la bobine est comprimée, l'inductance $L$ augmente.
3. Si l'aire de la section est augmentée, l'inductance $L$ augmente.
4. Si le champ magnétique dans la bobine est renforcé par un matériau approprié, conducteur du magnétisme (par exemple du fer), l'inductance $L$ augmente.

[question:EC305]

Si l'on comprime la bobine, $l$ diminue. L'inductance $L$ augmente donc.

[question:EC306]

Si l'on double la longueur $l$ de la bobine, l'inductance $L$ doit se réduire de moitié.

[question:EC307]

Si le nombre de spires $N$ est doublé, l'inductance $L$ est multipliée par quatre.

Si le nombre de spires est réduit, l'inductance diminue, mais même avec une demi-spire ou un quart de spire, et même avec un simple morceau de fil droit, il subsiste encore une faible inductance parasite.

[question:EC304]

---

On qualifie de *ferromagnétique* une certaine classe de matériaux qui contiennent, à l'échelle atomique, de petits aimants élémentaires qui s'orientent sous l'influence d'un champ magnétique extérieur et augmentent ainsi fortement la *densité de flux magnétique* (dont nous ne nous occupons toutefois pas encore ici). Parmi les éléments chimiques purs, seuls le fer, le cobalt et le nickel sont ferromagnétiques.

<indepth>
$\mu_r$, que l'on appelle aussi perméabilité relative, est très grande pour les matériaux ferromagnétiques (pour le fer par exemple, dans la plage de $300\dots\num{10000}$).
</indepth>


[question:EB204]

Si l'on introduit un matériau ferromagnétique comme le fer dans la bobine, le champ magnétique est renforcé et l'inductance augmente.

Si en revanche nous introduisons dans un solénoïde un noyau constitué d'un métal bon conducteur (non ferromagnétique) comme l'aluminium ou le cuivre, l'inductance de la bobine diminue. Cela tient au fait que le champ magnétique haute fréquence de la bobine crée (« induit ») dans les noyaux des courants, appelés courants de Foucault. Ces courants secondaires engendrent à leur tour des champs magnétiques qui s'opposent au champ magnétique de la bobine. C'est pourquoi l'inductance diminue. Le champ magnétique à l'intérieur du noyau s'en trouve réduit.

Dans la question suivante, la réponse considérée comme correcte est que le champ magnétique ne peut pas pénétrer dans le noyau et réduit donc la section du champ. Ce n'est cependant pas tout à fait ce qui se passe physiquement. Il suffit de retenir la « bonne » réponse.

[question:EB205]

---

Comme pour le condensateur, examinons d'abord le comportement de la bobine en courant continu : la bobine est reliée à une source de tension continue à travers une résistance série, comme le montre la figure [ref:e_spule_einschalten]. À l'instant de la mise sous tension, la montée du courant est d'abord retardée, si bien que le courant n'augmente pas brusquement, mais seulement progressivement jusqu'à sa valeur maximale.

La cause en est la loi de Lenz : lors de la montée du courant, la bobine engendre une tension d'auto-induction qui s'oppose à la variation du courant — donc à sa cause. La montée du courant s'en trouve limitée. Comme au début aucun courant ne circule encore, la quasi-totalité de la tension appliquée chute d'abord aux bornes de la bobine. À mesure que le courant croît, cette tension d'induction diminue, tandis que le courant continue d'augmenter.

Une fois l'état stationnaire atteint, la bobine se comporte en courant continu approximativement comme un morceau de fil. La tension à ses bornes est alors pratiquement nulle. L'évolution dans le temps de la tension aux bornes de la bobine est représentée sur la figure [ref:e_spule_einschalten_spannung].

<margin>
[picture:1016:e_spule_einschalten:Circuit pour l'étude d'une bobine]
</margin>
<margin>
[picture:186:e_spule_einschalten_spannung:Évolution de la tension à la mise sous tension]
</margin>

[question:EC301]

---

À l'instant de la coupure, la tension d'auto-induction cherche à maintenir le passage du courant. La bobine agit alors comme un générateur, dont la tension d'induction apparaît en sens inverse de la polarité précédente. La bobine se comporte ainsi exactement à l'opposé du condensateur. On peut bien observer ces phénomènes à l'aide d'un oscilloscope, comme sur la figure [ref:e_Spulenstrom].

<margin>
[photo:257:e_Spulenstrom:Comportement de la tension et du courant de la bobine à la mise sous et hors tension]
</margin>

On peut donc aussi utiliser les bobines pour temporiser. Dans la question suivante, le courant qui traverse la lampe 2 croît plus lentement que celui qui traverse la lampe 1, car une bobine est placée en amont, dont la tension d'auto-induction ne laisse le courant d'enclenchement croître que lentement.

[question:EC302]

De même que pour le condensateur, une bobine se comporte différemment selon qu'elle est raccordée en tension continue ou en tension alternative. En radiotechnique, c'est surtout le comportement en tension alternative qui importe. Examinons donc à présent le comportement en courant alternatif.

La bobine présente, comme un condensateur, une résistance en courant alternatif $X_{\textrm{L}}$, c'est-à-dire que, bien que le fil de la bobine n'ait qu'une très faible résistance ohmique (résistance du conducteur), il circule un courant qui devient toutefois plus petit à mesure que la fréquence de la tension alternative augmente :

$X_{L} = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$

La formule montre que cette résistance en courant alternatif croît avec la fréquence et diminue lorsque la fréquence baisse.

[question:EC303]
