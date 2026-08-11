En classe N, nous avons déjà fait connaissance avec les émissions non désirées. De telles émissions doivent absolument être évitées, ce qui peut être obtenu par diverses mesures techniques — nous les approfondissons dans cette leçon. Les émissions non désirées des émetteurs radio résultent souvent d'*harmoniques* (Oberwellen), c'est-à-dire de multiples entiers de la fréquence fondamentale, ainsi que d'*émissions parasites* (Nebenaussendungen), comme le montre la figure [ref:e_unerwuenschte_aussendungen_uebersicht]. Nous nous occupons d'abord des harmoniques, car elles peuvent gêner ou perturber d'autres services radio. On parle de perturbation lorsqu'une station radioamateur rayonne des composantes de fréquence non désirées avec une intensité telle que les valeurs limites admissibles sont dépassées. Un exemple typique est l'émission d'une harmonique d'un émetteur-récepteur dans la bande de radiodiffusion VHF, comme le montre la figure [ref:e_unerwuenschte_aussendungen_oberwelle]. Ici, le quadruple de la fréquence fondamentale ($\qty{145,9}{\mega\hertz}\cdot 4 = \qty{583,6}{\mega\hertz}$) conduit à une perturbation. Nous examinerons les émissions parasites à la fin de cette leçon.

<margin>
[picture:1008:e_unerwuenschte_aussendungen_uebersicht:Émissions non désirées — harmoniques (OW) et émissions parasites (NA)]
</margin>

<margin>
[picture:745:e_unerwuenschte_aussendungen_oberwelle:Perturbation de la réception DVB-T2 d'un téléviseur par l'harmonique d'une émission radioamateur]
</margin>

---

La mesure des émissions non désirées d'un émetteur s'effectue — contrairement à la mesure de la PEP — toujours à la sortie de l'émetteur, en incluant le SWR-mètre éventuellement utilisé, les boîtes d'accord supplémentaires et les filtres passe-bas éventuellement mis en œuvre (cf. figure [ref:e_unerwuenschte_aussendungen_trx]).
On garantit ainsi que seules sont mesurées les émissions non désirées qui peuvent effectivement atteindre l'antenne. L'appareil de mesure le mieux adapté est un analyseur de spectre. La façon exacte de réaliser un tel contrôle, l'allure du spectre de fréquences des harmoniques et les prescriptions légales applicables ne seront examinées en détail qu'en classe A.

<margin>
[picture:917:e_unerwuenschte_aussendungen_trx:Mesure des émissions non désirées]
</margin>

[question:EJ209]

Un signal d'émission idéal, qui n'émet que sur une fréquence souhaitée, devrait être une sinusoïde idéale. Celle-ci ne contient aucune composante de fréquence autre que la fréquence fondamentale.

[question:EJ201]

<indepth>
Les formes de signaux qui ne sont pas sinusoïdales, et qui présentent notamment des « angles et arêtes » prononcés, se composent de nombreuses composantes sinusoïdales de fréquences différentes et contiennent beaucoup de composantes harmoniques. En particulier, lorsque des émetteurs sont saturés, des signaux auparavant sinusoïdaux sont souvent déformés ou écrêtés en amplitude. Il en résulte aussi des composantes harmoniques massives. Tout écart par rapport à la forme sinusoïdale idéale est donc à éviter pour des signaux d'émission idéaux. Nous examinerons ce sujet plus en détail en classe A. Avec cet applet, on peut cependant déjà expérimenter la chose.

[include:fourier]
</indepth>

---

Pour la suppression des harmoniques, on utilise habituellement dans le domaine des ondes courtes des *filtres d'harmoniques*. Leur caractéristique est conçue de telle sorte que les fréquences inférieures à une certaine fréquence de coupure traversent le filtre pratiquement sans atténuation, tandis que les fréquences supérieures à cette limite ne passent pas, ou seulement fortement atténuées. Un *filtre d'harmoniques* est donc un *filtre passe-bas*, comme nous l'avons déjà vu au chapitre sur les circuits oscillants. La réponse en fréquence d'un tel passe-bas est représentée à la figure [ref:e_ua_tiefpass]. La figure [ref:e_ua_tiefpass_selbstbau] montre un filtre passe-bas de construction personnelle, composé de condensateurs et de bobines enroulées sur des tores. Lorsqu'on change de bande sur un émetteur multibande, un filtre d'harmoniques approprié est en règle générale sélectionné en même temps. On entend alors souvent le clic d'un relais qui effectue cette commutation.

L'importance de ce sujet se voit au grand nombre de questions d'examen qui s'y rapportent. Avec les connaissances sur les harmoniques et les passe-bas, elles se laissent toutefois résoudre très facilement.

<margin>
[picture:591:e_ua_tiefpass:Réponse en fréquence d'un filtre passe-bas]
</margin>

<margin>
[photo:320:e_ua_tiefpass_selbstbau:Filtre passe-bas de construction personnelle]
</margin>

---

[question:EJ202]
[question:EJ204]
[question:EJ205]
[question:EJ206]
[question:EJ207]
[question:EJ208]
[question:EJ203]

<indepth>
[picture:593:bandpass:Réponse en fréquence d'un filtre passe-bande]
  
Une autre possibilité de supprimer les harmoniques est l'emploi d'un filtre passe-bande. Les filtres passe-bande sont fréquemment utilisés dans les émetteurs monobandes ainsi que dans les émetteurs pour les domaines VHF/UHF/SHF. Il faut alors souvent supprimer aussi des composantes de signal qui naissent au sein de l'élaboration du signal d'émission et peuvent également se trouver en dessous de la fréquence d'émission.
</indepth>

Comme mentionné précédemment, des signaux sinusoïdaux sont essentiels pour éviter les composantes harmoniques. On y parvient notamment en faisant travailler sans distorsion les étages de l'émetteur, en particulier les étages finaux de puissance. Si le point de fonctionnement d'un étage final d'émission est réajusté, il faut ensuite impérativement vérifier sa linéarité et contrôler que l'émission est de qualité et pauvre en harmoniques.

[question:EF404]

Des émissions non désirées peuvent aussi apparaître au voisinage immédiat du signal d'émission proprement dit (cf. figure [ref:e_unerwuenschte_aussendungen_uebersicht]) et concernent alors souvent d'autres radioamateurs sur la même bande. De telles perturbations ne peuvent être supprimées par des filtres que difficilement, voire pas du tout, et devraient donc être évitées dès le début de l'élaboration du signal par des mesures appropriées. Ces *émissions parasites* — appelées aussi produits parasites et, familièrement, « splatter » — résultent fréquemment d'un réglage trop élevé de l'amplificateur de microphone dans l'émetteur, ce qui élargit involontairement le signal d'émission.

[question:EJ213]
[question:EJ214]

Il en va de même pour les procédés de transmission numériques, comme par exemple le Packet Radio. Pour éviter les émissions parasites et les dépassements de la largeur de bande admissible, on peut, en particulier pour les émetteurs FM modulés en AFSK, soit limiter l'excursion, soit réduire le niveau BF.

[question:EJ212]

La stabilité de l'oscillateur utilisé dans l'émetteur peut elle aussi conduire à des émissions situées en dehors des limites de bande ou perturbant les stations voisines. Cela est possible en particulier avec des appareils anciens de construction personnelle sans oscillateurs stabilisés par quartz. Les émetteurs-récepteurs décamétriques modernes, mais aussi les appareils de construction personnelle et les kits actuels, disposent en règle générale d'oscillateurs de référence très stables.

[question:EJ216]
