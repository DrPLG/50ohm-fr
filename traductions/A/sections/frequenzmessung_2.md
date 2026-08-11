L'affichage de fréquence d'un récepteur peut lui aussi être vérifié. À la différence d'un émetteur, la fréquence de réception affichée ne se laisse cependant normalement pas mesurer simplement au fréquencemètre sur une sortie de l'appareil. Le signal HF reçu est traité très tôt dans le récepteur et transposé, par exemple, sur une fréquence intermédiaire.

Pour vérifier l'affichage de fréquence, on utilise donc un signal de référence aussi précis que possible. Un générateur de fréquence ou un oscillateur de référence précis, de fréquence connue, est raccordé à l'entrée d'antenne du récepteur. Le récepteur est ensuite accordé sur ce signal et son affichage de fréquence est comparé à la fréquence connue du signal de référence.

Plus la référence utilisée est précise, plus l'affichage de fréquence du récepteur peut être vérifié, voire étalonné, avec précision. Les oscillateurs disciplinés par GPS ou les oscillateurs à quartz thermostatés de qualité (OCXO) conviennent par exemple particulièrement bien.

<attention>
Un générateur de fréquence raccordé directement peut facilement endommager une entrée de récepteur. Dans le doute, la mesure devrait être commencée avec la tension la plus basse du générateur et un atténuateur.
</attention>

[question:AI511]
[question:AI504]

---

Sur les émetteurs, la mesure de fréquence est plus simple. Un fréquencemètre est raccordé à la prise d'antenne par l'intermédiaire d'un atténuateur. Cette mesure n'a naturellement de sens que sur une porteuse non modulée, c'est-à-dire sur une sinusoïde aussi pure que possible.

<indepth>
Les émetteurs SSB ne produisent aucun signal en l'absence de modulation. Pour mesurer leur fréquence d'émission, on peut injecter dans la prise micro un signal audio de fréquence connue. En USB, la fréquence audio est retranchée de la valeur mesurée par le fréquencemètre à la sortie de l'émetteur, afin d'obtenir la fréquence de la porteuse non émise. En LSB, elle est ajoutée.
</indepth>

[question:AI502]
[question:AI501]

Une fréquence peut aussi être déterminée à l'oscilloscope. Pour des mesures de fréquence précises, un oscilloscope est cependant le plus souvent moins adapté qu'un fréquencemètre dédié, car la base de temps et le procédé de mesure de ce dernier sont spécialement conçus pour une exactitude et une résolution de fréquence élevées.

[question:AI503]

---

Les fréquencemètres simples travaillent fréquemment avec ce qu'on appelle un *temps de porte*. Pendant ce temps, l'appareil compte les périodes, ou encore les fronts ou les passages par zéro du signal d'entrée. La fréquence est ensuite calculée à partir du nombre d'oscillations comptées et du temps de porte connu. Exemple — avec un temps de porte d'une seconde, la détermination de la fréquence est particulièrement simple : si l'on compte par exemple $\num{1000}$ périodes, la fréquence mesurée vaut $\qty{1000}{\hertz}$.

<margin>
[picture:1126:a_frequenzmessung_torzeit:Comptage d'un signal de fréquence $\qty{1,1}{\kilo\hertz}$ pendant des temps de porte très courts]
</margin>

La *résolution en fréquence* $\Delta f$ indique quel est le plus petit écart de fréquence entre deux valeurs mesurées que le fréquencemètre peut encore distinguer, ou afficher. Sur un fréquencemètre simple à comptage direct, la résolution en fréquence est déterminée par le temps de porte $T_\mathrm{G}$ :

$\Delta f = \frac{1}{T_\mathrm{G}}$

L'effet du temps de porte, et donc de la résolution en fréquence, sur le résultat de mesure est montré par la figure [ref:a_frequenzmessung_torzeit]. Dans les deux cas, c'est le même signal, de fréquence réelle $\qty{1,1}{\kilo\hertz}$, qui est mesuré.

Avec un temps de porte de $\qty{1}{\milli\second}$ seulement, une seule période est comptée. Le fréquencemètre en déduit une valeur mesurée de $\qty{1}{\kilo\hertz}$. Le temps de porte court ne permet donc ici qu'une résolution en fréquence de $\qty{1}{\kilo\hertz}$.

Si le temps de porte est porté à $\qty{10}{\milli\second}$, ce sont déjà $\num{11}$ périodes qui peuvent être comptées. Il en résulte une valeur mesurée de $\qty{1,1}{\kilo\hertz}$. La résolution en fréquence vaut maintenant $\qty{100}{\hertz}$, de sorte que le chiffre supplémentaire de la fréquence peut lui aussi être affiché.

Plus le temps de porte est long, plus il est compté de périodes et plus la résolution en fréquence devient fine. Un temps de porte court a en revanche l'avantage de permettre une actualisation plus fréquente de l'affichage. Le choix du temps de porte constitue ainsi un compromis entre rapidité d'actualisation et finesse de résolution en fréquence. L'exactitude de la mesure de fréquence est à distinguer de la résolution : elle dépend en particulier de l'exactitude de la base de temps du fréquencemètre.

[question:AI505]
