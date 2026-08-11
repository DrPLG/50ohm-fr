Pour établir une liaison radio entre deux lieux par l'onde d'espace, il faut choisir une fréquence que l'ionosphère réfracte de manière fiable vers la Terre. En règle générale, cela ne concerne pas une seule fréquence, mais toute une plage de fréquences. On choisit alors souvent la bande radioamateur la plus haute à l'intérieur de cette plage.

Cette plage de fréquences est limitée vers le haut par la *MUF* (*maximum usable frequency*), c'est-à-dire la fréquence la plus élevée que l'ionosphère peut encore tout juste réfracter vers la Terre pour la distance entre l'émetteur et le récepteur.

[question:EH204]

La MUF dépend de la densité des électrons libres dans la région réfractante (ici : la région F2) ainsi que de l'angle d'incidence de l'onde radio dans l'ionosphère. La figure [ref:e_muf_luf] montre la prévision de la MUF pour une journée d'été de juillet 2025. On y voit clairement que la MUF dépend de l'heure de la journée : de jour, l'ionisation plus forte conduit à une MUF plus élevée ; la nuit, l'ionisation diminue et la MUF baisse en conséquence. La figure [ref:e_muf_luf2] montre un autre exemple. La MUF s'y situe à environ $\qty{7,5}{\mega\hertz}$. Cela signifie que les fréquences $\qty{3,5}{\mega\hertz}$ et $\qty{7}{\mega\hertz}$ sont encore réfractées vers la Terre, tandis que les fréquences au-dessus de $\qty{7,5}{\mega\hertz}$ sont déviées vers l'espace. C'est aussi la raison pour laquelle nous communiquons avec la station spatiale ISS sur la bande des $\qty{2}{\meter}$ : avec $\qty{145,800}{\mega\hertz}$, nous sommes nettement au-dessus d'une MUF typique.

<margin>
[picture:991:e_muf_luf:Prévision de la MUF et de la LUF en juillet 2025]
</margin>

<margin>
[picture:997:e_muf_luf2:Simulation des distances de saut pour différentes fréquences et une MUF d'env. $\qty{7,5}{\mega\hertz}$, une nuit d'août 2024, avec un angle de rayonnement de $\qty{45}{\degree}$]
</margin>

Les relations exactes de la MUF, par exemple avec l'angle de rayonnement, ne sont traitées qu'en classe A. Pour la classe E, il faut retenir : plus l'ionisation de l'ionosphère est forte, plus la MUF est en règle générale élevée.

[question:EH207]
[question:EH206]

Nous avons déjà fait connaissance avec la région D dans le chapitre Ionosphère II. Elle détermine une autre fréquence limite — la LUF (*Lowest Usable Frequency*), c'est-à-dire la fréquence utilisable la plus basse, au-dessous de laquelle l'atténuation est trop forte.
Vers le bas, c'est donc la LUF qui constitue la limite. Elle est déterminée en premier lieu par l'ionisation de la *région D*, mais dépend aussi de l'équipement (puissance d'émission, antennes, sensibilité du récepteur).

[question:EH209]

En particulier lors d'une activité solaire très faible ou pendant de fortes tempêtes magnétiques, un cas particulier peut se produire : pour un trajet de signal donné, la LUF se situe au-dessus de la MUF. Dans ce cas, aucun trafic radio par l'onde d'espace n'est possible entre les lieux concernés. La figure [ref:e_muf_luf] montre aussi une prévision de la LUF pour juillet 2025. On y voit clairement qu'entre 6 h et 12 h, la LUF se situe au-dessus de la MUF et qu'aucun trafic en ondes courtes n'est donc possible.

