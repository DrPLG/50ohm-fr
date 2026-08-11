Les transistors ont une *caractéristique* qui représente la *relation entre le signal d'entrée (tension base-émetteur ou grille-source) et le signal de sortie (courant de collecteur/de drain)*. Il existe ici, dans le domaine de la caractéristique, différentes portions dans lesquelles le transistor a une *caractéristique linéaire ou aussi non linéaire*.
Les portions droites de la caractéristique, dans lesquelles une variation de la grandeur de commande provoque une variation proportionnelle de la grandeur de sortie, sont dites linéaires.
D'autres portions de la caractéristique, dans lesquelles une variation de la grandeur de commande ne provoque **aucune** variation proportionnelle de la grandeur de sortie, sont dites non linéaires.

<margin>
[picture:377:a_kennlinien_transistor_arbeitspunkt:Caractéristique d'un transistor avec points de fonctionnement]  
</margin>

Pour un fonctionnement optimal de l'amplificateur du point de vue du rendement et de l'absence d'harmoniques dans le signal amplifié, il faut procéder à un choix optimal du point de fonctionnement de l'amplificateur sur sa caractéristique.
Ce point de fonctionnement est fixé par une tension continue auxiliaire appropriée (tension de polarisation) à la base ou à la grille.

L'amplification du signal d'entrée s'effectue alors autour du point de fonctionnement souhaité, qui définit le centre de la plage de fonctionnement.
Le choix du point de fonctionnement détermine un courant de repos correspondant du transistor. Celui-ci circule même en l'absence de signal d'entrée. Le courant de repos influence de façon déterminante l'efficacité d'un amplificateur, car il augmente sa puissance dissipée thermique et réduit donc son rendement.

Tous les signaux dont l'information de modulation se trouve dans leur amplitude doivent être amplifiés linéairement afin de transmettre sans distorsion l'information véhiculée (SSB, AM, etc.). Les signaux dont l'information de modulation ne se trouve pas dans l'amplitude mais uniquement dans la fréquence peuvent aussi être amplifiés dans la zone non linéaire d'un amplificateur (FM, etc.) puis filtrés.

Selon le mode de fonctionnement, on distingue différents points de fonctionnement possibles et leur désignation sur la caractéristique (voir figure [ref:a_kennlinien_transistor_arbeitspunkt] ) :

AP1 : fonctionnement de l'amplificateur en classe C
- sans tension de polarisation
- courant de repos nul
- rendement env. $\qtyrange{80}{87}{\percent}$
- taux d'harmoniques élevé

AP2 : fonctionnement de l'amplificateur en classe B
- faible tension de polarisation jusqu'à l'apparition du courant de collecteur
- courant de repos presque nul (faible)
- rendement env. jusqu'à $\qty{80}{\percent}$
- faible taux d'harmoniques

AP3 : fonctionnement de l'amplificateur en classe A/B
- tension de polarisation plus élevée qu'en classe B, mais plus faible qu'en classe A
- courant de repos plus élevé qu'en classe B, mais nettement plus faible qu'en classe A
- rendement entre $\qty{50}{\percent}$ et $\qty{80}{\percent}$
- faible taux d'harmoniques

AP4 : fonctionnement de l'amplificateur en classe A
- la valeur de la tension de polarisation est choisie de telle sorte que le courant de repos atteigne env. $\qty{50}{\percent}$ de la valeur maximale admissible
- rendement env. $\qty{40}{\percent}$
- très faible taux d'harmoniques

[question:AD416]
[question:AD419]
[question:AD420]
[question:AD421]

La puissance de sortie d'un amplificateur peut être calculée approximativement par la connaissance du point de fonctionnement et donc de son rendement approximatif. On calcule d'abord la puissance en courant continu fournie à l'amplificateur, à partir du produit de la tension et du courant. On multiplie ensuite cette puissance par le facteur numérique du rendement, $\qty{100}{\percent}$ correspondant à un rendement de $1$. Par exemple, un rendement de $\qty{40}{\percent}$ correspond alors à un facteur de $0,4$.

[question:AD424]
[question:AD425]
[question:AD418]
[question:AD417]

Pour qu'un amplificateur puisse être utilisé pour le trafic SSB (amplification linéaire), son point de fonctionnement doit se situer en classe A, AB ou B. Fondamentalement, la classe A est possible en raison de sa grande linéarité, mais elle n'est pas efficace aux puissances plus élevées. On monte ici 2 transistors ensemble dans un montage dit push-pull, de sorte que chacun des deux transistors n'amplifie qu'une seule alternance (positive ou négative). De ce fait, un fonctionnement en classe AB ou B avec un rendement accru de l'amplificateur est également possible.
En classe C, le signal est cependant toujours distordu. C'est pourquoi un émetteur SSB ne peut pas fonctionner en classe C.
En particulier lors du fonctionnement en classe AB ou B d'un amplificateur, il faut éviter la saturation, car celle-ci peut rapidement conduire à des distorsions du signal. Celles-ci se manifestent en SSB sous la forme de splatter sur les fréquences voisines.

[question:AD422]
[question:AJ218]
[question:AD423]

Les amplificateurs en classe C produisent, en raison de leur point de fonctionnement fortement non linéaire, des taux d'harmoniques élevés, qui doivent être supprimés plus loin sur le trajet du signal, par ex. par filtrage (passe-bas).
Comme, pour les amplificateurs de puissance en classe C, des composantes harmoniques de fortes amplitudes et puissances sont également présentes dans l'amplificateur ainsi que dans le filtre qui le suit, l'amplificateur comme le filtre doivent être exploités dans un boîtier métallique assurant un bon blindage, de sorte qu'ils ne provoquent aucune perturbation par les composantes harmoniques.

[question:AF402]
[question:AF403]


