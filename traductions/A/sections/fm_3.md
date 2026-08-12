Comme nous l'avons déjà appris dans les classes N et E, en modulation de fréquence, l'information du signal modulant ne se trouve pas dans l'amplitude, mais uniquement dans la variation de fréquence du signal porteur. C'est pourquoi seuls les passages par zéro du signal porteur doivent être exploités dans le récepteur.

Les fluctuations d'amplitude sont ici masquées par un amplificateur limiteur. La modulation de fréquence est donc, de par sa nature, insensible aux perturbations impulsionnelles de l'amplitude, provoquées par ex. par des étincelles d'allumage, des moteurs électriques ou similaires. La FM convient donc bien au fonctionnement en véhicule automobile.

[question:AE302]

Nous allons maintenant examiner comment une modulation de fréquence peut être produite dans un émetteur, et comment la largeur de bande d'un signal FM peut être calculée.

---

Par la variation de la capacité du condensateur déterminant la fréquence, à l'intérieur d'un oscillateur, une modulation de fréquence peut être produite (voir [ref:fm_modulation_schaltung]). Une modulation de fréquence peut par exemple être produite au moyen d'une diode à capacité variable placée en série avec un circuit oscillant ou un quartz. L'amplitude de la basse fréquence (BF), produite par ex. par un microphone et présente aux bornes de la diode à capacité variable, détermine ici directement la variation de fréquence de l'oscillateur.

[question:AE303]

<margin>
[picture:155:fm_modulation_schaltung:Montage simple pour la modulation de fréquence d'un oscillateur par diode à capacité variable]
</margin>

La fréquence de modulation influence ici la fréquence à laquelle la fréquence de l'oscillateur varie.

[question:AE301]

L'*excursion de fréquence* indique de quelle valeur la fréquence instantanée du signal FM est écartée de la fréquence porteuse par le signal modulant. Plus l'amplitude du signal modulant est grande, plus cette excursion de fréquence est grande elle aussi.

Lors de la démodulation dans le récepteur FM, cette excursion de fréquence est reconvertie en une amplitude correspondante du signal démodulé. Une excursion plus grande conduit donc, toutes choses égales par ailleurs, à une amplitude plus grande du signal BF démodulé.

Une excursion plus grande augmente la largeur de bande nécessaire au signal FM. Si les valeurs prévues sont dépassées, le signal émis peut de ce fait déborder sur les canaux voisins et y provoquer des perturbations.

[question:AE305]
[question:AE306]
[question:AE307]
[question:AE304]

---

À strictement parler, la largeur de bande occupée d'une émission FM n'est pas déterminée seulement par l'excursion, mais aussi par la fréquence de modulation maximale (voir la figure [ref:fm_modulation]). En première approximation, pour une faible excursion et une basse fréquence de modulation, la formule de Carson peut être appliquée. Elle indique dans quelle largeur de bande se situent $\qty{99}{\percent}$ de la puissance d'émission.

$B\approx2 \cdot \left(\Delta f_{\textrm{p}} + f_{\textrm{mod max}} \right)$

<margin>
[picture:910:fm_modulation:Largeur de bande en modulation de fréquence]
</margin>

Au moyen de la formule de Carson, la largeur de bande occupée d'une émission FM peut être calculée lorsque les valeurs de l'excursion et de la fréquence de modulation sont connues. Par une transformation appropriée de la formule, les autres grandeurs peuvent également être calculées.

[question:AE309]
[question:AE308]
[question:AE311]
[question:AE312]
[question:AE310]
