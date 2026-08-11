Les circuits intégrés sont des circuits complexes réalisés sur un substrat semi-conducteur. Ils constituent ainsi une simplification essentielle pour la construction de circuits électroniques.

[question:AC601]

<margin>
[photo:334:a_ic:Émetteur ondes courtes TinyWhisper de la JKU Linz et de la JMU Würzburg, réalisé comme circuit intégré en technologie CMOS 130 nm]
</margin>

Comme classe particulière des circuits intégrés, il existe les Monolithic Microwave Integrated Circuits (MMIC). Ils réunissent des composants aussi bien actifs que passifs sur le même substrat. Ils sont typiquement conçus pour une impédance d'entrée et de sortie de $\qty{50}{\ohm}$. Ils permettent une amplification large bande élevée avec peu de composants.

[question:AC602]
[question:AC603]
[question:AC604]

---

Pour le calcul des exercices de l'examen, il est utile d'examiner d'abord de plus près le circuit de la figure [ref:a_mmic].

Les condensateurs $C_1$ et $C_3$ servent de condensateurs de liaison. Ils laissent passer les signaux HF, mais bloquent la tension continue. On empêche ainsi que des tensions continues soient transmises entre les différents étages du circuit et influencent le point de fonctionnement.

La self de choc dans la ligne d'alimentation $U_\mathrm{CC}$ empêche que des signaux HF puissent s'écouler par l'alimentation en tension. Pour la haute fréquence, la self possède une résistance élevée et agit donc comme un barrage. Le condensateur $C_2$ sert au découplage HF de la tension d'alimentation. Il dérive vers la masse les composantes HF restantes et veille à ce que la tension d'alimentation reste stable du point de vue HF. Avec la self, il forme un découplage HF de la tension d'alimentation. Nous ferons plus tard la connaissance de ce circuit sous le nom de « bias-T ».

Une particularité de nombreux MMIC est que la tension d'alimentation est amenée par la sortie. La résistance $R_\text{BIAS}$ règle alors le point de fonctionnement du MMIC.

<margin>
[picture:773:a_mmic:Circuit MMIC]
</margin>

Selon l'énoncé, on peut d'abord déterminer, à partir de la chute de tension aux bornes du MMIC, la chute de tension aux bornes de la résistance $R_\text{BIAS}$. Avec la valeur connue de la résistance, le courant traversant le circuit peut ensuite être calculé. Le même courant circule aussi à travers le MMIC, de sorte qu'on peut par exemple en déterminer la puissance dissipée thermique.

Les exercices suivants se résolvent donc de manière très semblable aux circuits à transistors bipolaires déjà connus.

[question:AF425]
[question:AF426]
[question:AF427]

% Eine wesentliche Erleichterung bei dem Aufbau von elektronischen Schaltung 
% ist die Verwendung von integrierten Schaltungen.
% Eine integrierte Schaltung enthält in einem Gehäuse eine komplexe elektronische Schaltung, 
% die auf einem Chip hergestellt wurde.

% "Zusatzinfo" Praktische Anwendungen:
% Operationsverstärker: siehe Abschnitt ...
% Niederfrequenzverstärker: siehe Abschnitt ...
% Mikrowellenverstärker MMIC: siehe Abschnitt ...
% Kombinierte Mischer- und Oszillatorschaltung: siehe Abschnitt ...
% Komplette Empfänger: siehe Abschnitt ...
% Digitale Schaltkreise: siehe Abschnitt ...
% PLL-Schaltungen: siehe Abschnitt ...

% Durch wenige externe Bauteile kann z.B. ein Audioverstärker, ein Oszillator mit Mischer oder sogar ein kompletter % Kurzwellenempfänger realisiert werden.
% Bild eines IC mit Typenbezeichnung und Blockschaltbild z.B. LM386
% Für Frequenzen ab ca. 100 MHz werden sogenannte Monolithic Microwave Integrated Circuit (MMIC) eingesetzt.
% Bild MMIC MSA 0686 oder ERA 3
% Hierbei handelt es sich um einen Verstärker. der breitbandig den Frequenzbereich von 100 MHz bis 2 GHz um  20dB verstärken kann
% und eingangs- und ausgangsseitug für 50 Ohm Last angepasst ist.
% Es muss lediglich der Strom für den Arbeitspunkt laut Datenblatt eingestellt werden, damit der MMIC auch nicht % thermisch überlastet wird. 
% Dazu ist bei vorgegebener Betriebsspannung ein Widerstand und dessen elektrische Belastung zu berechnen.

% Da der MMIC ein Gehäuse für SMD-Technik besitzt, ist es notwendig, auch die äußere Beschaltung in SMD- Technik auszuführen.
% Der Gesamtaufbau des Verstärkers wird so deutlich kleiner sein als früher in diskreter Schaltungstechnik.
% Bild Vergleich diskrete Schaltung und MMIC


