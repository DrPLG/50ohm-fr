Contrairement à la modulation, qui a lieu du côté de l'émetteur, la démodulation des signaux dans le récepteur fait qu'un signal modulé est par exemple reconverti en BF et devient ainsi audible, ou qu'une suite de bits est restituée dans le cas d'une transmission numérique.

Selon le type de modulation utilisé du côté de l'émetteur, une démodulation correspondante doit avoir lieu du côté du récepteur. Il existe pour cela différents concepts de montage qui permettent la démodulation. La façon dont fonctionne la modulation dans le domaine numérique sera examinée dans un chapitre ultérieur. Dans ce chapitre, nous nous occuperons d'abord de la démodulation des signaux analogiques.

La forme la plus simple de démodulation d'un signal haute fréquence est celle de la modulation d'amplitude (AM).
Les signaux AM peuvent être démodulés au moyen de ce qu'on appelle un démodulateur d'enveloppe, comme le montre la figure [ref:demodulator_huellkurvendemodulator_am]. Le signal haute fréquence est pour cela d'abord sélectionné selon la fréquence de réception souhaitée, par exemple au moyen d'un circuit oscillant accordé, puis redressé par une diode. Un condensateur placé après la diode se charge à la valeur de crête instantanée du signal et se décharge en même temps, à travers une résistance montée en parallèle sur lui, avec une constante de temps appropriée. Cette constante de temps est nettement supérieure à la période du signal HF, mais nettement inférieure à la période du signal BF.

<margin>
[picture:141:demodulator_huellkurvendemodulator_am:Démodulateur d'enveloppe pour la démodulation des signaux AM]
</margin>

[question:AD501]

Au point de connexion X de la figure [ref:demodulator_huellkurvendemodulator_am_2] apparaît à chaque fois la tension de crête redressée du signal HF, qui décroît légèrement entre les crêtes du signal HF selon la constante de temps de la résistance montée en parallèle sur le condensateur. L'enveloppe du signal correspond ainsi à la BF modulée, laquelle est, en raison de la constante de temps du condensateur, superposée à un signal en dents de scie (fréquence porteuse), et correspond au signal de la figure [ref:demodulator_huellkurvendemodulator_am_abbx]. Dans les étages de traitement BF suivants (non représentés), les restes de cette fréquence porteuse sont ensuite filtrés, de sorte qu'il ne subsiste que la BF pure comme signal de sortie (cf. figure [ref:demodulator_huellkurvendemodulator_am_clean]).

<margin>
[picture:607:demodulator_huellkurvendemodulator_am_2:Démodulateur d'enveloppe pour la démodulation des signaux AM, avec représentation du signal d'entrée FI présent à l'entrée du démodulateur]
[picture:146:demodulator_huellkurvendemodulator_am_abbx:Signal démodulé au point X du démodulateur d'enveloppe]
[picture:147:demodulator_huellkurvendemodulator_am_clean:Signal filtré à la sortie du démodulateur d'enveloppe]
</margin>

[question:AD502]

---
<margin>
[picture:841:demodulator_flankendiskriminator:Circuit oscillant utilisé comme discriminateur à flanc]

[picture:149:demodulator_flankendiskriminator_schaltung:Discriminateur à flanc FM]
</margin>

Un montage très semblable au démodulateur d'enveloppe précédent peut être utilisé pour démoduler les signaux FM.
Partant de la fréquence intermédiaire du récepteur FM, le signal parvient, comme le montre la figure [ref:demodulator_flankendiskriminator], dans un circuit oscillant dont la fréquence de résonance $f_\text{res}$ est accordée légèrement au-dessus ou en dessous de la fréquence intermédiaire $f_\text{ZF}$. Le signal FM à démoduler se situe de ce fait sur le flanc du circuit oscillant, et celui-ci convertit les variations de fréquence de la FM en variations d'amplitude. Au moyen du démodulateur AM placé en aval, le signal FM, désormais converti en signal AM, est alors démodulé et rendu audible. Ce montage, présenté à la figure [ref:demodulator_flankendiskriminator_schaltung], est appelé discriminateur à flanc.

[question:AD504]

---

Les signaux modulés en FM peuvent également être démodulés au moyen d'une PLL (Phase Locked Loop), cf. figure [ref:demodulator_pll]. Dans une PLL, un oscillateur commandé en tension (VCO) est couplé, par une boucle de régulation de phase, à un signal d'entrée dont il suit la fréquence. Lorsque la fréquence du signal d'entrée varie (modulation FM), la tension de régulation du VCO suit la modulation FM. Cette tension de régulation correspond alors exactement à la modulation du signal FM, et donc à la BF modulée, et peut être prélevée sur la PLL pour la suite du traitement.

<margin>
[picture:77:demodulator_pll:PLL pour la démodulation des signaux FM]
</margin>

[question:AD505]

---

Pour démoduler les signaux modulés en SSB, on utilise ce qu'on appelle un détecteur de produit. Celui-ci est pour l'essentiel un mélangeur en anneau, déjà rencontré au chapitre consacré aux récepteurs, qui utilise comme signaux d'entrée la FI du récepteur ainsi qu'un BFO (Beat Frequency Oscillator). Par le mélange (produit) de ces deux signaux d'entrée naît, comme l'un des produits de mélange, le signal BF souhaité (signal SSB), qui peut être prélevé à la sortie pour la suite du traitement. Pour une intelligibilité optimale de la BF démodulée, le BFO doit être accordé sur la fréquence de la porteuse supprimée du signal SSB.


<indepth>
[picture:153:demodulator_produktdetektor:Détecteur de produit pour la démodulation des signaux SSB]
[picture:1125:a_produktdetektor_spannung:Exemple de tensions au détecteur de produit]

Pour démoduler un signal SSB, on emploie fréquemment ce qu'on appelle un *détecteur de produit*. Celui-ci peut par exemple être réalisé sous forme de mélangeur en anneau. Il reçoit comme signaux d'entrée le signal SSB sur la fréquence intermédiaire (FI) et le signal d'un *Beat Frequency Oscillator (BFO)*.

Le fonctionnement s'explique de façon simplifiée avec un mélangeur commutant. Le signal du BFO fait basculer le mélangeur en anneau entre deux états. De façon simplifiée, on peut donc se représenter le BFO comme un signal qui commute entre les valeurs $+1$ et $-1$, comme le représente la courbe supérieure de la figure [ref:a_produktdetektor_spannung].

Le signal FI est de ce fait tantôt transmis inchangé, tantôt inversé en polarité. Dans la représentation simplifiée, le signal FI peut donc être considéré comme le produit du signal BF par le signal de commutation du BFO :

$u_\mathrm{FI}(t)=u_\mathrm{BF}(t)\cdot s_\mathrm{BFO}(t)$

Dans le détecteur de produit, ce signal est de nouveau multiplié par le signal du BFO :

$u_\mathrm{FI}(t)\cdot s_\mathrm{BFO}(t)=u_\mathrm{BF}(t)\cdot s_\mathrm{BFO}(t)\cdot s_\mathrm{BFO}(t)$

Comme le signal de commutation simplifié du BFO ne prend que les valeurs $+1$ et $-1$, on a :

$s_\mathrm{BFO}^2(t)=1$

Il subsiste donc, comme composante basse fréquence, le signal BF d'origine :

$u_\mathrm{BF}(t)=u_\mathrm{FI}(t)\cdot s_\mathrm{BFO}(t)$

Outre le signal BF souhaité, le processus de mélange fait naître d'autres produits de mélange haute fréquence. Ceux-ci sont supprimés à la sortie du détecteur de produit par un filtre passe-bas.

Pour que le signal BF d'origine soit restitué à la bonne hauteur de son, la fréquence du BFO doit être réglée en accord avec la fréquence de la porteuse supprimée du signal SSB.
</indepth>

[question:AD506]
