Afin de réduire la largeur de bande maximale d'un signal SSB émis et d'utiliser efficacement le spectre de fréquences disponible, la largeur de bande de modulation BF maximale d'un signal SSB ne devrait pas dépasser $\qty{2,7}{\kilo\hertz}$. Cela permet un écart minimal entre signaux SSB de $\qty{3}{\kilo\hertz}$, pour un fonctionnement sans perturbation.

[question:AE208]
[question:AE209]

Lorsqu'un signal SSB est saturé dans le modulateur de l'émetteur, il en résulte des distorsions qui conduisent à des émissions parasites. Ces émissions parasites sont aussi appelées familièrement « splatter » et peuvent perturber les émissions voisines, car la largeur de bande du signal émis dépasse dans ce cas les $\qty{2,7}{\kilo\hertz}$ requis.
[question:AE205]

La voix de chaque personne a un spectre de fréquences individuel. Pour la meilleure intelligibilité possible lors des émissions SSB, les fréquences vocales de la partie supérieure du spectre devraient être rehaussées et celles des plages de fréquences plus basses atténuées. C'est à cela que sert un égaliseur dans l'amplificateur de microphone de l'émetteur, qui permet un réglage individuel de la réponse en fréquence du signal de modulation. La réponse en fréquence du microphone est ainsi adaptée de façon optimale à l'opérateur concerné.
[question:AE213]

---

Pour pouvoir apprécier la forme de l'enveloppe d'un émetteur SSB du point de vue de la qualité et de la linéarité, un signal à deux tons peut être utilisé pour moduler l'émetteur SSB. L'émetteur SSB est alors modulé par un signal BF constitué de deux fréquences BF superposées. Ces fréquences BF ne doivent pas être dans un rapport entier l'une par rapport à l'autre. Par la superposition apparaissent, dans la HF émise, des maxima et des minima (passages par zéro) du signal HF. Pour la modulation, on peut par ex. utiliser un ton de $\qty{700}{\hertz}$ et un ton de $\qty{1200}{\hertz}$. Il en résulte, lors de la mesure du signal HF au moyen d'un oscilloscope (sur une résistance de charge), un battement de la HF de $\qty{500}{\hertz}$, qui devrait dans le cas idéal être sinusoïdal. Le signal à deux tons permet aussi la mesure de la puissance d'enveloppe (PEP) d'un émetteur SSB par la représentation de la forme de la courbe sur l'oscilloscope.

[question:AI304]

<margin>
[picture:1092:a_ssb_zweiton:Signal à deux tons pour apprécier la forme de l'enveloppe d'un émetteur SSB]
</margin>

La figure [ref:a_ssb_zweiton] montre en 1. un signal à un ton, c'est-à-dire un simple ton BF sinusoïdal. En 2. et 3. est représentée la façon dont ce signal à un ton est transposé sur la HF en AM respectivement en SSB. Le signal SSB en 3. se compose d'une unique composante HF d'amplitude constante et apparaît donc comme une porteuse HF non modulée sur une fréquence décalée par rapport à la porteuse supprimée. Sur un tel signal à un ton, la qualité et la linéarité d'un émetteur SSB ne peuvent cependant être appréciées que de façon limitée ; en particulier, aucun produit d'intermodulation significatif entre plusieurs signaux utiles n'apparaît.

En 4. est visible un signal utile à deux tons, constitué de la superposition de deux tons sinusoïdaux de $\qty{700}{\hertz}$ et $\qty{1200}{\hertz}$. En 5. et 6. est montrée la façon dont ce signal à deux tons est transposé sur la HF en AM respectivement en SSB. Dans le signal SSB à deux tons en 6. apparaissent deux composantes HF écartées de $\qty{500}{\hertz}$. Par leur superposition apparaît un battement périodique de l'enveloppe HF à la fréquence différence de $\qty{500}{\hertz}$. Cette enveloppe permet la mesure de la puissance de crête d'enveloppe (PEP) et sert en même temps à apprécier la linéarité de l'émetteur, car les non-linéarités conduisent à des produits d'intermodulation supplémentaires dans le spectre.

[question:AE207]

Pour les exercices suivants, il faut déterminer la puissance de sortie de l'émetteur en tant que puissance de crête d'enveloppe (PEP). La PEP décrit la puissance efficace que l'émetteur délivre pendant la crête de l'enveloppe de modulation. Elle ne se rapporte donc pas à la puissance moyenne sur l'ensemble de la modulation, mais à la valeur de puissance au maximum de l'enveloppe, comme représenté sur la figure [ref:a_pep_hüllkurve]. La tension de crête servant au calcul de la puissance efficace peut être relevée sur l'oscillogramme. Il faut alors prêter attention au rapport de la sonde de mesure.

<margin>
[picture:875:a_pep_hüllkurve:Enveloppe de modulation pour le calcul de la puissance]
</margin>

% Tastkopf 1:1 PEP
[question:AI305]

% Tastkopf 10:1 PEP
[question:AI306]