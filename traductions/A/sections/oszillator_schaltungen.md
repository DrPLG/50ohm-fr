Les oscillateurs sont l'un des éléments de montage les plus importants en radioamateurisme. Ils sont pour ainsi dire le cœur de chaque appareil radio. Les oscillateurs servent à produire des oscillations haute fréquence dans les émetteurs et les récepteurs.

Le cœur d'un oscillateur est un élément amplificateur dont le *signal de sortie est réinjecté sur son entrée*.

Pour qu'un oscillateur puisse produire des oscillations non amorties, *deux conditions fondamentales* doivent être remplies.
D'une part, le *signal de sortie doit être réinjecté en phase sur le point d'entrée du montage*.
D'autre part, l'*amplitude du signal réinjecté doit avoir au moins la même valeur* que celle du signal d'entrée. On dit aussi que le *gain de boucle doit être supérieur à 1* pour qu'une auto-excitation, qui entretient l'oscillation, soit possible.

[question:AD613]

<margin>
[picture:760:a_oszillator_schaltungen_oszillator:Montage d'un oscillateur à réaction capacitive]  
</margin>

%TODO: Evtl. Bild 760 ableiten und noch um die 3 Punkte der Dreipunktschaltung ergänzen (am kapazitiven Spannungsteiler - oben, in der Mitte und unten)

Le montage représenté sur la figure [ref:a_oszillator_schaltungen_oszillator] constitue un oscillateur à trois points à réaction capacitive. Le signal de sortie est réinjecté depuis l'émetteur du montage sur la base du transistor via un diviseur de tension capacitif. La fréquence de l'oscillateur est principalement déterminée par le circuit oscillant situé dans la base (constitué d'une bobine et d'un condensateur ajustable) ainsi que par le diviseur de tension capacitif monté en parallèle sur le circuit oscillant.
Le montage est un oscillateur en montage collecteur commun, car le collecteur est à la masse du point de vue des tensions alternatives.

[question:AD614]
[question:AD616]

Pour augmenter la stabilité de fréquence d'un oscillateur, son composant déterminant la fréquence (circuit oscillant) peut être remplacé par un quartz. Les quartz peuvent être excités à osciller aussi bien sur leur fréquence fondamentale que sur leurs fréquences harmoniques (harmoniques/partiels). Pour qu'un quartz puisse cependant être exploité sur une harmonique, l'amplificateur doit être conçu de façon sélective en fréquence (par ex. par l'utilisation d'un circuit oscillant). Si celui-ci n'est pas présent, on peut en déduire que le quartz est exploité sur sa fréquence fondamentale (voir figure [ref:a_oszillator_schaltungen_quarzoszillator] ).

<margin>
[picture:497:a_oszillator_schaltungen_quarzoszillator:Montage d'un oscillateur à quartz en montage collecteur commun avec le quartz exploité sur sa fréquence fondamentale]  
</margin>

[question:AD617]

Le signal de l'oscillateur devrait toujours être prélevé au point de plus basse impédance d'un oscillateur, afin de le charger le moins possible. Dans un montage collecteur commun, il s'agit de l'émetteur du transistor.

[question:AD610]

Un oscillateur devrait toujours être suivi d'un étage dit tampon, qui fait en sorte que l'oscillateur soit découplé des autres parties du montage et que sa fréquence ne soit pas influencée par la charge de la sortie. Un étage tampon est le plus souvent conçu en montage collecteur commun (émetteur suiveur) et a une impédance d'entrée élevée, qui ne charge l'oscillateur que de façon minimale. À sa sortie, le signal de l'oscillateur peut ensuite être traité en basse impédance.

Les mesures sur les oscillateurs devraient toujours être effectuées après l'étage tampon, faute de quoi l'oscillateur est chargé par des capacités parasites et sa fréquence en est influencée.

[question:AD615]
[question:AD619]
[question:AD618]










