Voyons d'abord comment est constitué un récepteur. Dans la figure [ref:aufbau_empfaenger_blockdiagramm], nous ne descendons pas, par souci de simplification, au niveau des composants individuels : nous considérons des blocs remplissant chacun une fonction déterminée. Cette représentation s'appelle un schéma-bloc (Blockdiagramm). Elle sert, en électrotechnique, à présenter des appareils complexes sous forme d'une vue d'ensemble simplifiée. On omet pour cela les détails qui ne sont pas nécessaires à la compréhension de l'appareil dans son ensemble.

<margin>
[picture:736:aufbau_empfaenger_blockdiagramm:Schéma-bloc d'un récepteur simple]
</margin>

<indepth>
Le récepteur représenté ici est appelé récepteur à amplification directe (Geradeausempfänger). Ce nom vient du fait que la fréquence du signal capté par l'antenne n'est pas modifiée jusqu'au démodulateur.
</indepth>

---

Examinons en détail, de gauche à droite, les différents blocs du récepteur :

1. Antenne : l'antenne capte une multitude d'ondes radio et les transmet sous forme d'oscillations électriques.
2. Filtre passe-bande : pour extraire le signal souhaité, un filtre passe-bande suit l'antenne. Il ne laisse passer que la plage de fréquences désirée et bloque toutes les autres fréquences indésirables.
3. Amplificateur HF : vient ensuite un amplificateur qui amplifie le signal ainsi filtré. Il s'agit ici d'un amplificateur haute fréquence (amplificateur HF), car le signal présente une fréquence élevée, par exemple $\qty{144,3}{\mega\hertz}$.
4. Démodulateur : le signal amplifié est ensuite traité par le démodulateur. La démodulation est l'opération inverse de la modulation. Alors que la modulation consiste à moduler un signal (par exemple un signal vocal) sur une porteuse haute fréquence, la démodulation fait exactement l'inverse : le signal d'origine est récupéré à partir de la porteuse haute fréquence modulée. On retrouve alors, par exemple, le signal vocal qui a été prononcé dans le microphone du côté de l'émetteur. On parle aussi de signal basse fréquence, en abrégé signal BF (NF en allemand), car il présente des fréquences relativement basses — pour un signal vocal, par exemple, des fréquences inférieures à $\qty{20}{\kilo\hertz}$.
5. Amplificateur BF : le signal démodulé est ensuite amplifié. Il s'agit cette fois d'un amplificateur basse fréquence (amplificateur BF) destiné à amplifier le signal pour le haut-parleur. Le symbole de l'amplificateur BF est le même que celui de l'amplificateur haute fréquence.
6. Haut-parleur : le signal est enfin converti par le haut-parleur d'une oscillation électrique en une onde sonore, et redevient ainsi audible.

<indepth>
Sur le symbole du *filtre passe-bande*, les deux ondes barrées symbolisent le blocage des fréquences situées au-dessus et au-dessous de la plage de fréquences souhaitée. L'onde du milieu signifie que la plage de fréquences souhaitée est laissée passer.
</indepth>

<indepth>
Le *démodulateur* est représenté par le symbole de la diode, qui est le composant essentiel de nombreux démodulateurs. Le fonctionnement d'une diode sera expliqué plus loin, dans le chapitre « Composants et circuits ».
</indepth>

[question:NF201]

Selon sa constitution exacte, un récepteur présente des propriétés différentes. Une propriété importante est la sensibilité. Elle désigne la capacité du récepteur à recevoir des signaux faibles. Plus un récepteur est sensible, plus les signaux qu'il peut recevoir sont faibles.

[question:NF303]
