De nombreux procédés de modulation numérique utilisent plus de deux symboles. Au lieu de deux amplitudes seulement (faible et forte), la modulation par déplacement d'amplitude fonctionne aussi avec quatre amplitudes différentes, voire davantage, par exemple $\qty{25}{\percent}$, $\qty{50}{\percent}$, $\qty{75}{\percent}$, $\qty{100}{\percent}$ du maximum. Deux bits ou plus peuvent ainsi être regroupés en un symbole et transmis simultanément.

[picture:701:4ask:Modulation par déplacement d'amplitude quaternaire (Quaternary Amplitude-shift Keying)]

Ce principe se transpose lui aussi à la modulation par déplacement de fréquence et de phase. Une modulation par déplacement de phase simple (Binary Phase-Shift Keying, BPSK) n'utilise que deux positions de phase différentes et ne peut donc émettre qu'un seul bit à la fois. La modulation par déplacement de phase en quadrature (Quadrature Phase-Shift Keying, QPSK) utilise en revanche déjà quatre positions de phase différentes ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ et $\qty{270}{\degree}$). La QPSK transmet ainsi deux bits à chaque pas.

[question:AE402]

Comme les procédés tels que la QPSK transmettent plus d'un bit par symbole, il nous faut faire attention aux unités. Tandis que, pour le flux de données, nous parlons d'un débit de données en $\unit{\bit\per\second}$, la cadence de succession des différents symboles se note en symboles par seconde, avec l'unité baud.

[question:AA104]

Si seuls deux symboles sont utilisés et que chaque bit est donc émis isolément, la rapidité de modulation en bauds ($\unit{\baud}$) correspond au débit de données en bits par seconde ($\unit{\bit\per\second}$). Si davantage de symboles sont utilisés et que plusieurs bits sont donc transmis simultanément, le débit de données est supérieur à la rapidité de modulation. La relation est la suivante : le débit de données en $\unit{\bit\per\second}$ est égal à la rapidité de modulation en $\unit{\baud}$ multipliée par le nombre de bits transmis par symbole :

$C=R_\mathrm{S}\cdot n$

$C$ débit de données en $\unit{\bit\per\second}$

$R_\mathrm{S}$ rapidité de modulation en $\unit{\baud}$

$n$ taille du symbole en $\unit{\bit\per\text{Symbol}}$

[question:AE405]
[question:AE406]
