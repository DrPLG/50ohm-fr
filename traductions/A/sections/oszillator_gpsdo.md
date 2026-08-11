Dans le chapitre précédent, nous avons vu qu'il existe différents types d'oscillateurs, de stabilité et de précision de fréquence différentes. Les oscillateurs à quartz sous forme de TCXO, et surtout d'OCXO, atteignent une stabilité particulièrement élevée. Les appareils radio modernes atteignent par exemple, avec un TCXO, une précision de fréquence de $\pm\qty{0,5}{\ppm}$. Pour une fréquence souhaitée de $\qty{10}{\mega\hertz}$, la fréquence réelle se situe donc dans la plage de $\qtyrange{9,999995}{10,000005}{\mega\hertz}$, soit au plus $\pm\qty{5}{\hertz}$ à côté de la fréquence nominale. Cet écart est faible et, en règle générale, plus que suffisant pour le trafic en ondes courtes.

Si nous travaillons cependant non pas à $\qty{10}{\mega\hertz}$ mais à $\qty{10}{\giga\hertz}$, l'écart possible passe à $\pm\qty{5000}{\hertz}$. Il peut ainsi déjà être supérieur à la largeur de bande d'un filtre SSB usuel. Lors d'une liaison radio sur une fréquence convenue à l'avance, le signal peut donc se situer en dehors de la plage de réception. Pour de telles applications, par exemple avec le satellite géostationnaire QO-100 qui émet sur $\qty{10}{\giga\hertz}$, des références de fréquence encore plus précises sont donc nécessaires. 

<margin>
[picture:1081:a_gpsdo:GPS-Disciplined Oscillator (GPSDO) dans le contexte d'une station QO-100]
</margin>

On pourrait consacrer beaucoup d'efforts à stabiliser davantage un OCXO, ou utiliser d'autres types d'oscillateurs comme les étalons de fréquence au rubidium, qui atteignent une stabilité plus élevée que les oscillateurs à quartz, en particulier sur de longues durées. De tels étalons de fréquence présentent cependant souvent des inconvénients, comme une consommation de courant plus élevée, des dimensions plus grandes et un prix plus élevé, car ils sont avant tout développés pour des applications professionnelles.

Heureusement, il existe une autre possibilité : les systèmes de navigation par satellite, en anglais Global Navigation Satellite Systems (GNSS), comme le GPS ou Galileo, ont besoin de références de temps très précises. La position du récepteur est déterminée à partir des temps de propagation des signaux transmis par plusieurs satellites vers le récepteur. Comme toute horloge précise a besoin d'un oscillateur stable comme base de temps, nous pouvons utiliser la référence de temps tirée des signaux satellites pour stabiliser notre propre TCXO ou OCXO. Un tel oscillateur est appelé oscillateur synchronisé par GPS, ou en anglais GPS-Disciplined Oscillator (GPSDO). Comment cette régulation fonctionne techniquement, nous le verrons dans un chapitre ultérieur consacré aux boucles à verrouillage de phase (PLL). La figure [ref:a_gpsdo] représente un GPSDO dans le contexte d'une station QO-100, qui fournit au Software Defined Radio (SDR) une fréquence de référence stable. Un module construit soi-même est visible sur la figure [ref:a_gpsdo_homebrew].

---

On pourrait maintenant se demander pourquoi nous n'utilisons pas directement comme signal d'oscillateur la référence de temps fournie par le GPS. Le récepteur GPS tire habituellement des signaux satellites, faibles et modulés, un signal de temps précis, par exemple une impulsion par seconde. L'instant exact de cette impulsion peut cependant fluctuer à court terme du fait du bruit, de la propagation par trajets multiples, des influences atmosphériques et des retards dans le récepteur. Considérée sur de longues durées, la fréquence qui en est dérivée est en revanche très précise.

Un TCXO ou un OCXO possède quant à lui une bonne, voire une très bonne stabilité à court terme, mais peut s'écarter lentement de la fréquence nominale à long terme, du fait des influences résiduelles de la température et du vieillissement de ses composants. Dans un GPSDO, ces deux propriétés sont donc combinées : le TCXO ou l'OCXO local fournit un signal de sortie stable à court terme et peu bruité, tandis qu'une boucle de régulation lente corrige son écart à long terme à l'aide de la référence de temps GPS. De cette manière, un GPSDO atteint à la fois une très bonne stabilité à court terme et une stabilité à long terme ainsi qu'une précision de fréquence élevées.

[question:AD606]

<margin>
[photo:335:a_gpsdo_homebrew:GPSDO construit soi-même, avec TCXO]
</margin>
