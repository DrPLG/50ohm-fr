Contrairement à la modulation, qui a lieu du côté de l'émetteur, la démodulation des signaux dans le récepteur fait qu'un signal modulé est reconverti en BF et devient ainsi audible.

Selon le type de modulation utilisé du côté de l'émetteur, une démodulation correspondante doit avoir lieu du côté du récepteur.
Il existe pour cela différents concepts de montage qui permettent la démodulation.

La forme la plus simple de démodulation d'un signal haute fréquence est celle de la modulation d'amplitude (AM).
Les signaux AM peuvent être démodulés au moyen de ce qu'on appelle un démodulateur d'enveloppe, comme le montre la figure [ref:demodulator_huellkurvendemodulator_am]. Le signal haute fréquence est pour cela d'abord sélectionné selon la fréquence de réception souhaitée, par exemple au moyen d'un circuit oscillant accordé, puis redressé par une diode. Un condensateur placé après la diode se charge à la valeur de crête instantanée du signal et se décharge en même temps, à travers une résistance montée en parallèle sur lui, avec une constante de temps appropriée. Cette constante de temps est nettement supérieure à la période du signal HF, mais nettement inférieure à la période du signal BF.

<margin>
[picture:141:demodulator_huellkurvendemodulator_am:Démodulateur d'enveloppe pour la démodulation des signaux AM]
</margin>

[question:AD501]

Au point de connexion X de la figure [ref:demodulator_huellkurvendemodulator_am_2] apparaît à chaque fois la tension de crête redressée du signal HF, qui décroît légèrement entre les crêtes du signal HF selon la constante de temps de la résistance montée en parallèle sur le condensateur. L'enveloppe du signal correspond ainsi à la BF modulée, laquelle est, en raison de la constante de temps du condensateur, superposée à un signal en dents de scie (fréquence porteuse), et correspond au signal de la figure [ref:demodulator_huellkurvendemodulator_am_abbx]. Dans les étages de traitement BF suivants (non représentés), les restes de cette fréquence porteuse sont ensuite filtrés, de sorte qu'il ne subsiste que la BF pure comme signal de sortie.

<margin>
[picture:607:demodulator_huellkurvendemodulator_am_2:Démodulateur d'enveloppe pour la démodulation des signaux AM, avec représentation du signal d'entrée FI présent à l'entrée du démodulateur]
[picture:146:demodulator_huellkurvendemodulator_am_abbx:Signal démodulé au point X du démodulateur d'enveloppe]
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

Les signaux modulés en FM peuvent également être démodulés au moyen d'une PLL (Phase Locked Loop). Dans une PLL, un oscillateur commandé en tension (VCO) est couplé, par une boucle de régulation de phase, à un signal d'entrée dont il suit la fréquence. Lorsque la fréquence du signal d'entrée varie (modulation FM), la tension de régulation du VCO suit la modulation FM. Cette tension de régulation correspond alors exactement à la modulation du signal FM, et donc à la BF modulée, et peut être prélevée sur la PLL pour la suite du traitement.

[question:AD505]

Pour démoduler les signaux modulés en SSB, on utilise ce qu'on appelle un détecteur de produit. Celui-ci est pour l'essentiel un mélangeur en anneau, qui utilise comme signaux d'entrée la FI du récepteur ainsi qu'un BFO (Beat Frequency Oscillator). Par le mélange (produit) de ces deux signaux d'entrée naît, comme l'un des produits de mélange, le signal BF souhaité (signal SSB), qui peut être prélevé à la sortie pour la suite du traitement. Pour une intelligibilité optimale de la BF démodulée, le BFO doit être accordé sur la fréquence de la porteuse supprimée du signal SSB.

[question:AD506]