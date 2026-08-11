La fréquence d'un oscillateur dépend toujours de la température ambiante, car les propriétés des composants utilisés varient avec la température. Pour les transistors et les diodes, cela concerne par exemple le facteur d'amplification, la tension de seuil et les capacités. Les composants passifs comme les condensateurs, les résistances et en particulier les quartz présentent eux aussi des propriétés électriques dépendantes de la température.

Pour maintenir la fréquence d'un oscillateur aussi stable que possible, celui-ci devrait être bien isolé thermiquement, dans l'appareil, des autres sources de chaleur et de froid. Cela peut être obtenu par exemple par une distance aussi grande que possible aux sources de chaleur et de froid internes et externes ainsi qu'aux courants d'air. En outre, un oscillateur à quartz est à préférer à un oscillateur RC, LC ou VCO, car il présente une stabilité de fréquence nettement plus élevée en raison du facteur de qualité élevé du quartz.

[question:AF215]

Il existe différents types d'oscillateurs à quartz, qui se distinguent par leur stabilité de fréquence :

* L'oscillateur à quartz le plus simple (cf. figure [ref:a_xo]) est appelé *XO*, abréviation de Crystal Oscillator.
* Un *TCXO* (Temperature Compensated Crystal Oscillator) compense les influences de la température par des composants supplémentaires dans le montage de l'oscillateur, de telle sorte que leurs effets dépendants de la température se compensent largement les uns les autres dans la plage des températures de service usuelles.
* Un *OCXO* (Oven-Controlled Crystal Oscillator) stabilise la température de l'oscillateur à quartz au moyen d'un chauffage régulé. L'oscillateur se trouve pour cela dans un boîtier isolé thermiquement, qui le protège largement des influences extérieures de chaleur et de froid. Parmi les types d'oscillateurs cités, l'OCXO offre la stabilité de fréquence la plus élevée. 

<margin>
[photo:333:a_xo:Oscillateur à quartz XO à $\qty{433,75}{\mega\hertz}$]
[photo:337:a_ocxo:Oscillateur à quartz OCXO à $\qty{10}{\mega\hertz}$]
</margin>

[question:AD602]
[question:AD603]
[question:AD605]

En particulier lors du fonctionnement sur les fréquences élevées, la stabilité de fréquence de l'oscillateur de référence des émetteurs-récepteurs, transverters et convertisseurs est très importante lors de l'utilisation de modes de transmission sensibles aux écarts de fréquence. Pour atteindre les fréquences élevées d'émission ou de réception, une multiplication de fréquence de l'oscillateur de référence a lieu à l'intérieur de l'appareil. De ce fait, les écarts de fréquence de l'oscillateur de référence se répercutent de façon multiplicative sur les fréquences d'émission ou de réception, ce qui peut conduire à des écarts de fréquence importants et à des instabilités de fréquence (par ex. dérive du signal d'émission ou de réception). C'est pourquoi il faudrait utiliser au moins un TCXO, par exemple sur la bande des $\qty{3}{\centi\meter}$, c'est-à-dire la bande des $\qty{10}{\giga\hertz}$.

[question:AD604]
