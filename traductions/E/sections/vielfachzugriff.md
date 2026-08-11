Dans la communication sans fil, différents procédés d'accès jouent un rôle central pour permettre à plusieurs utilisateurs d'exploiter simultanément un spectre de fréquences commun. Les procédés courants sont le multiplexage fréquentiel (FDMA), le multiplexage temporel (TDMA) et le multiplexage par code (CDMA). Chacun de ces procédés répartit le spectre de fréquences d'une manière différente, afin de minimiser les interférences et de garantir une transmission efficace. Le choix du procédé dépend des exigences spécifiques en matière de largeur de bande, de nombre d'utilisateurs et de sensibilité aux perturbations. Les différences entre ces procédés sont décrites ci-après.

---

Dans le procédé de multiplexage fréquentiel (FDMA — Frequency Division Multiple Access), la bande de fréquences disponible est divisée en plusieurs canaux de fréquence séparés les uns des autres (cf. figure [ref:e_fdma]). Chacun de ces canaux est attribué de façon fixe à un utilisateur individuel, de sorte que l'utilisation simultanée du système par plusieurs participants est possible. La séparation des utilisateurs s'effectue exclusivement par des fréquences différentes, ce qui fait que les signaux des différents participants ne se perturbent pas mutuellement tant que les espacements entre canaux sont respectés. Le FDMA est un procédé techniquement simple et établi depuis de nombreuses années, qui convient particulièrement aux systèmes comptant peu d'utilisateurs et présentant de faibles exigences en matière d'interférences. Un inconvénient réside toutefois dans l'efficacité spectrale relativement médiocre lorsque le nombre d'utilisateurs est grand, puisqu'une plage de fréquences propre reste réservée en permanence à chaque participant, même lorsque celui-ci ne transmet temporairement aucune donnée. Des exemples d'application typiques du FDMA sont les premiers systèmes de téléphonie mobile analogiques comme l'AMPS, ainsi que diverses formes de communication par satellite.

[question:EE410]

<margin>
[picture:845:e_fdma:Multiplexage fréquentiel]
</margin>

---

Dans le procédé de multiplexage temporel (TDMA — Time Division Multiple Access), plusieurs participants utilisent le même canal de fréquence, l'accès leur étant réparti dans le temps. Chaque utilisateur reçoit des intervalles de temps définis de façon fixe, appelés créneaux temporels (time slots), pendant lesquels il peut émettre et recevoir (cf. figure [ref:e_tdma]). Cette séparation temporelle des transmissions empêche que les signaux des différents participants ne se superposent ou ne se perturbent mutuellement.

Le TDMA permet une utilisation relativement efficace des ressources de fréquences disponibles, en particulier dans les systèmes comptant de nombreux utilisateurs et un volume de données élevé. Un fonctionnement sans accroc suppose toutefois une synchronisation temporelle très précise de tous les participants, ce qui augmente la complexité technique du système. Des exemples d'application connus du TDMA sont le système de téléphonie mobile GSM de deuxième génération, le système de téléphonie sans fil DECT et, dans le service radioamateur, le DMR.

[question:EE409]

<margin>
[picture:844:e_tdma:Multiplexage temporel]
</margin>

---

Dans le procédé de multiplexage par code (CDMA — Code Division Multiple Access), tous les participants utilisent simultanément le même domaine de fréquences et le même temps. La séparation des différents utilisateurs ne s'effectue pas par la fréquence ou le temps, mais par des codes d'étalement individuels (cf. figure [ref:e_cdma]). Un code propre est attribué à chaque utilisateur, avec lequel son signal est modulé. Ces codes sont choisis de telle sorte que les signaux superposés peuvent être à nouveau séparés les uns des autres au niveau du récepteur, bien qu'ils soient transmis simultanément dans la même bande de fréquences. Le CDMA se distingue par une grande flexibilité et une grande capacité de système, puisque de nombreux utilisateurs peuvent être actifs en même temps. De plus, le procédé est très robuste face aux perturbations et à la propagation par trajets multiples. En contrepartie, il exige un traitement du signal relativement complexe et des exigences accrues envers le matériel, en particulier lorsque le nombre de participants actifs est grand. Des exemples d'application typiques du CDMA sont les systèmes de téléphonie mobile de troisième génération comme l'UMTS, ainsi que le système de navigation par satellite GPS.

[question:EE411]

<margin>
[picture:846:e_cdma:Multiplexage par code]  
</margin>

En résumé, on peut dire que le FDMA est la méthode la plus simple, tandis que le TDMA et le CDMA deviennent de plus en plus efficaces et complexes, en particulier pour l'exploitation de largeurs de bande limitées et de grands nombres d'utilisateurs. Le CDMA offre la plus grande flexibilité, mais exige aussi la technologie la plus élaborée pour sa mise en œuvre.