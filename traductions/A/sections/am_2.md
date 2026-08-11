Plus une porteuse AM est fortement modulée, plus son amplitude varie au cours du temps. Sans modulation, seule la porteuse HF est émise, avec une amplitude constante (cf. figure [ref:modulationsgrad_0]). À mesure que la modulation augmente, l'amplitude de la porteuse HF suit de plus en plus fidèlement le signal BF modulant, ce qui donne l'enveloppe caractéristique (cf. figure [ref:modulationsgrad_10]).

Le rapport entre l'amplitude du signal BF modulant et l'amplitude de la porteuse non modulée détermine le *taux de modulation* $m$. Pour un taux de modulation $m=1$, c'est-à-dire $\qty{100}{\percent}$, la porteuse est excursionnée en totalité. L'enveloppe oscille alors entre zéro et le double de l'amplitude de la porteuse non modulée (cf. figure [ref:modulationsgrad_100]).

[question:AE201]

<margin>
[picture:27:modulationsgrad_0:Taux de modulation de $\qty{0}{\percent}$ d'un signal AM]
[picture:26:modulationsgrad_10:Taux de modulation de $\qty{10}{\percent}$ d'un signal AM]
[picture:24:modulationsgrad_100:Taux de modulation de $\qty{100}{\percent}$ d'un signal AM]
</margin>

---

Dès que le taux de modulation devient supérieur à $m=1$, c'est-à-dire à $\qty{100}{\percent}$ (cf. figure [ref:modulationsgrad_1000]), on parle de *surmodulation*. L'enveloppe n'atteint alors pas seulement la valeur zéro, mais changerait mathématiquement de polarité au-delà. De ce fait, le signal ne peut plus être restitué sans distorsion par un démodulateur d'enveloppe usuel.

Sur les émetteurs réels, la surmodulation peut en outre conduire à un écrêtage, et donc à des composantes spectrales indésirables supplémentaires, appelées *splatter de bande latérale*. Pour éviter cela, le taux de modulation ne doit pas dépasser $\qty{100}{\percent}$ en AM classique.

<margin>
[picture:28:modulationsgrad_1000:Taux de modulation supérieur à $\qty{100}{\percent}$ (surmodulation) d'un signal AM]
</margin>

[question:AE204]
[question:AE203]

---

Le taux de modulation se calcule d'après la formule suivante (avec la figure [ref:modulationsgrad] du recueil de formules) :

$m = \frac{\hat{U}_\mathrm{mod}}{\hat{U}_\mathrm{p}}$


<margin>
[picture:328:modulationsgrad:Taux de modulation d'un signal AM]
</margin>

Essaie maintenant, dans la question suivante, de relever les valeurs et de calculer le taux de modulation $m$ :

[question:AE202]
