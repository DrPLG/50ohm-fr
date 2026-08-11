Les oscillateurs présentent toujours, du fait de la dépendance à la température des composants qui les constituent, une dépendance de la fréquence produite vis-à-vis de la température ambiante. Les transistors et les diodes présentent une dépendance relativement forte de leur caractéristique et de leur comportement vis-à-vis de la température ambiante (facteur d'amplification, tension de seuil, capacités). De même, les paramètres électriques des composants passifs comme les condensateurs, les résistances et en particulier les quartz dépendent de leur température ambiante.
Pour maintenir les oscillateurs aussi stables que possible en fréquence, il existe différentes possibilités techniques et physiques :
1. Tous les oscillateurs devraient toujours être aussi bien isolés thermiquement que possible des autres sources de chaleur des appareils.
2. Plutôt qu'un oscillateur RC, LC ou VCO, il faut privilégier un oscillateur à quartz, car celui-ci est nettement plus stable en fréquence en raison du facteur de qualité (Q) élevé du quartz. Ce type d'oscillateur est appelé *XO* - Crystal oscillator. 
3. Utilisation d'un oscillateur à quartz et compensation des influences thermiques par la mise en œuvre de composants dans le montage de l'oscillateur, de telle sorte que les influences de température se compensent mutuellement dans la plage des températures de service usuelles. Ce type d'oscillateur est appelé *TCXO* - Temperature compensated crystal oscillator
4. Stabilisation artificielle de la température ambiante d'un oscillateur à quartz par une régulation de température au moyen d'un circuit à thermostat et d'un montage dans un boîtier isolé thermiquement, ainsi que d'une isolation vis-à-vis des sources externes de chaleur et de froid. Ce type d'oscillateur est appelé *OCXO* - Oven controlled crystal oscillator. L'OCXO a, par rapport aux autres types d'oscillateurs, la plus grande stabilité de fréquence.

Fondamentalement, les oscillateurs stables en fréquence devraient toujours être aussi bien isolés thermiquement que possible des sources de chaleur et de froid internes et externes à l'appareil. Cela peut par ex. être obtenu par une distance aussi grande que possible aux sources de chaleur et de froid internes et externes ainsi qu'aux courants d'air.

[question:AF215]
[question:AD602]
[question:AD603]
[question:AD605]

En particulier lors du fonctionnement sur les fréquences élevées, la stabilité de fréquence de l'oscillateur de référence des transceivers, transverters et convertisseurs est très importante lors de l'utilisation de modes de trafic sensibles aux écarts de fréquence. Pour atteindre les fréquences élevées d'émission ou de réception, une multiplication de fréquence de l'oscillateur de référence a lieu à l'intérieur de l'appareil. De ce fait, les écarts de fréquence de l'oscillateur de référence se répercutent de façon multiplicative sur les fréquences d'émission ou de réception, ce qui peut conduire à des écarts de fréquence importants et à des instabilités de fréquence (par ex. dérive du signal d'émission ou de réception).
C'est pourquoi il faudrait toujours utiliser le meilleur type d'oscillateur disponible (par ex. TCXO ou OCXO).

[question:AD604]