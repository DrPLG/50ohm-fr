Lors de la numérisation d'un signal analogique, deux propriétés doivent être examinées : à quels instants le signal est-il mesuré, et avec quelle exactitude les valeurs mesurées peuvent-elles être représentées ? Les deux étapes correspondantes sont appelées *échantillonnage* et *quantification*.

Les termes *à temps continu*, *à temps discret*, *continu en valeur* et *discret en valeur* décrivent ici deux propriétés indépendantes l'une de l'autre. D'une part, on peut examiner si le signal est défini à tout instant quelconque. D'autre part, on peut examiner s'il peut prendre des valeurs quelconques.

Un signal analogique idéal est à la fois *à temps continu* et *continu en valeur*. Il est défini à tout instant quelconque et peut prendre, à l'intérieur de sa plage de valeurs, des valeurs intermédiaires quelconques. La figure [ref:a_wertkont_zeitkont] montre un tel signal.

---

Les signaux analogiques ne possèdent pas de plus petite résolution temporelle et sont continus dans le temps. On les qualifie donc de signaux *à temps continu*. Lors de l'échantillonnage, un tel signal n'est en revanche mesuré, autrement dit échantillonné, qu'à certains instants. Les différentes valeurs prélevées sont appelées *échantillons*.

Les échantillons ne représentent chacun que l'état instantané du signal à l'instant de l'échantillonnage. Entre deux instants d'échantillonnage, le signal analogique peut continuer de varier. Comme, après l'échantillonnage, seules subsistent des valeurs isolées, séparées les unes des autres dans le temps, on qualifie le signal échantillonné de signal *à temps discret*.

La figure [ref:a_wertkont_zeitdisk] montre un tel signal idéalement échantillonné. Il est *à temps discret*, puisque des valeurs ne sont disponibles qu'à certains instants d'échantillonnage. Les différents échantillons peuvent cependant encore prendre, dans un premier temps, des valeurs quelconques et sont donc *continus en valeur*.

<margin>
[picture:408:a_wertkont_zeitkont:Signal continu en valeur et à temps continu]
[picture:409:a_wertkont_zeitdisk:Signal continu en valeur et à temps discret]
</margin>

[question:AF601]
[question:AF603]

Le processus par lequel un signal à temps continu est échantillonné à certains instants et de ce fait transformé en un signal à temps discret est appelé *échantillonnage*.

[question:AF606]

La vitesse à laquelle l'échantillonnage d'un signal analogique est effectué est appelée *fréquence d'échantillonnage*. Elle indique combien d'échantillons sont prélevés par unité de temps, par exemple par seconde.

Les signaux sonores analogiques sont par exemple échantillonnés, sur les supports de données numériques comme les CD, à une fréquence d'échantillonnage de $\num{44100}$ samples par seconde (unité $\unit{\sps}$), ou en abrégé $\qty{44,1}{\kilo\sps}$.

[question:AF615]

---

Outre la résolution temporelle, la résolution des valeurs mesurées joue elle aussi un rôle lors de la numérisation. Les signaux analogiques peuvent prendre des valeurs de tension quelconques et varier entre celles-ci sans paliers intermédiaires fixes. On les qualifie pour cette raison de *continus en valeur*.

Lors de la numérisation, on ne dispose en revanche que d'un nombre limité de valeurs numériques possibles. Une valeur de tension mesurée doit donc être rattachée à l'un de ces échelons fixes. Le signal est ensuite *discret en valeur*.

Si une valeur de signal analogique se situe entre deux échelons possibles, il faut décider à quel échelon la valeur mesurée est rattachée. Ce processus est appelé *quantification*. Le signal, jusqu'alors continu en valeur, est ainsi représenté sur un nombre fini de valeurs possibles.

[question:AF605]

La figure [ref:a_wertdisk_zeitkont] montre, à titre d'illustration, un *signal discret en valeur, mais à temps continu*. Le signal reste défini à tout instant, mais ne peut prendre que certaines valeurs fixées d'avance. Les valeurs possibles sont donc déjà quantifiées, tandis que le temps n'est pas encore discrétisé.

Lorsque échantillonnage et quantification sont combinés, il en résulte un *signal discret en valeur et à temps discret*, tel qu'il est représenté à la figure [ref:a_wertdisk_zeitdisk]. Des échantillons ne sont disponibles qu'à certains instants, et leurs valeurs possibles sont elles aussi limitées à des échelons fixes. Cela correspond à la représentation numérique d'un signal auparavant analogique.

<tip>
Pour illustrer cela, on peut comparer un variateur analogique à un commutateur à crans. Un variateur analogique permet de régler la luminosité d'une lampe de façon aussi fine que l'on veut. Avec un commutateur à crans comportant par exemple $\num{5}$ crans, on ne dispose en revanche que de $\num{5}$ valeurs de luminosité différentes. Les valeurs intermédiaires ne sont pas possibles.

Si l'on veut reproduire avec le commutateur à crans une luminosité réglée au variateur analogique, il faut choisir le cran qui convient le mieux. C'est exactement ce qui correspond au principe de la quantification : une valeur continue est rattachée à l'une de plusieurs valeurs fixées d'avance.
</tip>

<margin>
[picture:410:a_wertdisk_zeitkont:Signal discret en valeur et à temps continu]
[picture:411:a_wertdisk_zeitdisk:Signal discret en valeur et à temps discret]
</margin>

[question:AF602]
[question:AF604]

<indepth>
Voici la possibilité d'expérimenter le tout une nouvelle fois. Un signal sinusoïdal à temps continu est numérisé par un convertisseur A/N, puis reconverti par un convertisseur N/A en un signal analogique à temps continu, mais toujours discret en valeur. Les curseurs permettent de régler la quantification temporelle et la quantification en valeur des convertisseurs A/N et N/A.

[include:quantisierung_und_sampling]
</indepth>
