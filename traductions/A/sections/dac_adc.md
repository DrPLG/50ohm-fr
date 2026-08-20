Cette section montre comment des signaux analogiques sont convertis en valeurs numériques, et les valeurs numériques de nouveau en signaux analogiques. On emploie pour cela des *convertisseurs A/N* (convertisseurs analogique-numérique) et des *convertisseurs N/A* (convertisseurs numérique-analogique). La figure [ref:a_adc_dac] montre les schémas fonctionnels d'un convertisseur A/N et d'un convertisseur N/A.

<margin>
[picture:1130:a_adc_dac:Convertisseurs A/N et N/A]
</margin>

Un convertisseur A/N échantillonne un signal d'entrée analogique à des instants déterminés et en produit des valeurs numériques, qui peuvent ensuite être traitées numériquement par d'autres parties d'un montage.

Comme un convertisseur A/N ne travaille qu'avec un nombre limité de valeurs numériques possibles, il ne peut saisir l'amplitude d'un signal d'entrée analogique que par échelons déterminés. Souvenons-nous à ce sujet de l'exemple, déjà employé, du variateur et du commutateur à crans. Si la valeur réelle se situe entre deux échelons possibles, elle doit être rattachée à l'un des deux. Il en résulte une *erreur de quantification*.

[question:AF607]

---

Le nombre d'échelons possibles d'un convertisseur A/N est appelé sa *résolution*. On l'indique souvent en bits (unité $\unit{\bit}$). Si un convertisseur peut par exemple distinguer $\num{256}$ valeurs différentes, il possède une résolution de $\qty{8}{\bit}$, car $\qty{8}{\bit}$ permettent de représenter $\num{256}$ valeurs différentes. Un convertisseur de $\qty{16}{\bit}$ peut déjà distinguer $\num{65536}$ valeurs différentes.

Pour les signaux susceptibles de prendre aussi bien des valeurs positives que négatives, une partie de ces valeurs est typiquement utilisée pour la plage de signal positive, et une autre partie pour la plage négative.

La figure [ref:a_adc_4bit] montre un signal sinusoïdal numérisé par un convertisseur A/N d'une résolution de $\qty{4}{\bit}$, puis reconverti en signal analogique. La figure [ref:a_adc_12bit] montre le même signal sinusoïdal, mais numérisé par un convertisseur A/N d'une résolution de $\qty{12}{\bit}$, puis reconverti en signal analogique. On reconnaît nettement que les $\qty{8}{\bit}$ supplémentaires conduisent à une résolution bien plus fine (meilleure d'un facteur 256), de sorte que le signal reconstitué se rapproche déjà beaucoup du signal sinusoïdal d'origine.

<margin>
[picture:300:a_adc_4bit:Signal sinusoïdal numérisé par un convertisseur A/N de 4 bits, puis reconverti par un convertisseur N/A]
[picture:299:a_adc_12bit:Signal sinusoïdal numérisé par un convertisseur A/N de 12 bits, puis reconverti par un convertisseur N/A]
</margin>

[question:AF608]

Une autre propriété importante d'un convertisseur A/N est l'exactitude temporelle de l'échantillonnage. Les différents échantillons doivent être prélevés le plus exactement possible aux intervalles de temps prévus. Cela exige un générateur d'horloge d'échantillonnage aussi stable que possible.

En pratique, les instants d'échantillonnage réels peuvent toutefois s'écarter légèrement des instants idéaux. Ces fluctuations temporelles sont appelées *jitter* (soit, en gros, la gigue). Le jitter peut conduire à des erreurs supplémentaires, et donc à un bruit supplémentaire dans le signal numérisé. Le même mécanisme se produit du côté du convertisseur N/A. Le jitter y conduit à un bruit supplémentaire dans le signal analogique.

[question:AF621]

---

Le pendant du convertisseur A/N est le *convertisseur N/A*. Il produit de nouveau un signal analogique à partir d'un flux de données numériques, autrement dit à partir d'échantillons numériques.

Un convertisseur N/A ne peut pas non plus produire un nombre quelconque de valeurs de sortie différentes. Comme le convertisseur A/N, il possède une résolution déterminée en bits, et donc un nombre fini de valeurs de sortie possibles.

Un convertisseur N/A ne peut en outre produire que des tensions comprises dans une plage de valeurs déterminée, par exemple de $\qty{0}{\volt}$ à $\qty{1}{\volt}$, ou de $\qty{-2}{\volt}$ à $\qty{2}{\volt}$.

Dans un convertisseur N/A à fonctionnement linéaire, les valeurs de sortie possibles sont réparties uniformément sur cette plage de tension. Si un convertisseur N/A possède par exemple une résolution de $\qty{4}{\bit}$, on dispose de

$\num{2^4}=\num{16}$

échelons possibles.

[question:AF609]

Si ceux-ci se répartissent sur une plage de tension de $\qty{0}{\volt}$ à $\qty{1}{\volt}$, il y a au total $\num{15}$ pas intermédiaires entre les $\num{16}$ échelons. Le pas vaut donc

$\frac{\qty{1}{\volt}}{16-1}\approx\qty{67}{\milli\volt}.$

[question:AF611]
[question:AF610]

---

Les convertisseurs A/N et N/A sont employés par exemple dans les récepteurs et les émetteurs-récepteurs SDR. Les signaux d'entrée analogiques sont d'abord numérisés par un convertisseur A/N, puis traités numériquement. S'il faut en produire de nouveau un signal analogique, les valeurs numériques sont reconverties en valeurs de tension analogiques au moyen d'un convertisseur N/A.

Il peut arriver qu'un signal d'entrée n'exploite qu'une petite partie de la plage de valeurs disponible d'un convertisseur A/N. Dans ce cas, une partie seulement des échelons numériques disponibles est utilisée.

Inversement, un signal d'entrée peut dépasser la plage de valeurs maximale d'un convertisseur A/N. Les valeurs supérieures à la tension d'entrée maximale saisissable ne peuvent alors plus être représentées correctement et ne sont plus rendues que par la valeur maximale possible. Cet effet est appelé *clipping* (en français : écrêtage). Les zones concernées apparaissent de ce fait tronquées dans l'allure du signal.

Un convertisseur N/A ne peut pas non plus produire de tension de sortie en dehors de sa plage de valeurs prévue.

Plus la résolution d'un convertisseur A/N ou N/A est élevée, plus les différentes valeurs d'amplitude peuvent être représentées numériquement de façon fine, ou reconverties de façon fine en valeurs de tension analogiques. Une résolution faible ne met en revanche à disposition que peu d'échelons possibles, de sorte que l'échelonnement devient nettement visible.

[question:AF613]
[question:AF612]
[question:AF614]
