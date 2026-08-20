Dans les transmissions numériques, les informations sont transmises sous forme de symboles. Un symbole est ici un état du signal que l'on peut distinguer des autres et qui est transmis pendant une durée déterminée. Ces états du signal peuvent se distinguer par exemple par des amplitudes, des fréquences ou des phases différentes, ou encore par des combinaisons de ces propriétés. Nous examinons dans les sections suivantes comment de tels symboles sont produits. Selon le nombre de symboles différents qu'un procédé de transmission peut employer, un symbole isolé peut contenir un ou plusieurs bits d'information.

Si l'on ne dispose que de deux symboles différents, chaque symbole permet de transmettre exactement un bit. Avec quatre symboles possibles, deux bits peuvent déjà être transmis par symbole, puisque deux bits permettent de représenter quatre combinaisons différentes. De même, huit symboles différents peuvent transmettre trois bits, et $\num{16}$ symboles différents quatre bits simultanément.

De façon générale, le nombre $N$ de bits transmissibles par un symbole découle du nombre $M=2^N$ de symboles possibles :

$N = \log_2(M)$

La *rapidité de modulation* indique combien de symboles sont transmis par seconde. Son unité est le *baud*. Une rapidité de modulation de $\qty{1000}{\baud}$ signifie donc que $\num{1000}$ symboles sont transmis par seconde.

La rapidité de modulation n'est pas nécessairement identique au débit de données. Si plusieurs bits sont transmis par symbole, le débit de données est d'autant plus grand. Pour le débit de données $R_\mathrm{D}$ (d'unité $\unit{\bit\per\second}$) et la rapidité de modulation $R_\mathrm{S}$, on a :

$R_\mathrm{D} = R_\mathrm{S} \cdot N$

Si par exemple, à une rapidité de modulation de $\qty{1200}{\baud}$, deux bits sont transmis par symbole, il en résulte un débit de données de :

$R_\mathrm{D} = \qty{1200}{\baud} \cdot \qty{2}{\bit\per{symbole}} = \qty{2400}{\bit\per\second}$

Le nombre de symboles possibles et la rapidité de modulation sont ainsi des grandeurs importantes pour les procédés de transmission numériques. Nous examinons dans les sections suivantes comment les différents symboles peuvent être représentés par différentes propriétés d'un signal.

[question:AA104]

---

Un exemple simple de la façon dont différents symboles peuvent être représentés par différents états du signal est la *modulation par déplacement de fréquence* (*Frequency-Shift Keying*, FSK), déjà connue de la classe E.

En FSK, la fréquence du signal émis est commutée entre différentes valeurs. La figure [ref:a_fsk] montre une FSK binaire à deux fréquences de symbole possibles, en représentation temporelle. La fréquence la plus haute peut par exemple correspondre au symbole $1$, et la fréquence la plus basse au symbole $0$. Comme deux symboles différents sont disponibles, chaque symbole permet de transmettre un bit.

<margin>
[picture:703:a_fsk:FSK (Frequency-Shift Keying)]
</margin>

Un exemple en est le *RTTY*. On y commute entre deux fréquences de symbole, par exemple entre $\qty{14072,43}{\kilo\hertz}$ et $\qty{14072,60}{\kilo\hertz}$. Chaque symbole permet ainsi de transmettre un bit, soit $0$, soit $1$.

[question:AE405]

La FSK n'est cependant pas limitée à deux fréquences de symbole. Si l'on emploie par exemple quatre fréquences différentes, on dispose de quatre symboles différents. Chaque symbole peut alors se voir attribuer l'une des quatre combinaisons de bits possibles $00$, $01$, $10$ ou $11$. Chaque symbole permet ainsi de transmettre deux bits.

Le procédé de transmission *FT4* en est un exemple. On peut y commuter entre quatre fréquences de symbole, par exemple $\qty{14081,20}{\kilo\hertz}$, $\qty{14081,40}{\kilo\hertz}$, $\qty{14081,61}{\kilo\hertz}$ et $\qty{14081,83}{\kilo\hertz}$.

[question:AE406]
