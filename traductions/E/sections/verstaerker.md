Dans le chapitre sur les transistors, nous avons déjà appris qu'un petit courant de base $I_\text{B}$ permet de commander un courant de collecteur $I_\text{C}$ nettement plus grand. Ce principe peut être mis à profit pour construire un amplificateur de signaux électriques. Selon le type de montage, les transistors permettent d'amplifier des signaux de toute nature — qu'il s'agisse de signaux numériques, de signaux basse fréquence (BF) ou haute fréquence (HF). Une amplification signifie que la puissance de sortie d'un signal est supérieure à sa puissance d'entrée, ce qui constitue la caractéristique fondamentale d'un amplificateur.

---

La figure [ref:e_nf_verstaerker] montre un amplificateur basse fréquence (amplificateur BF) destiné à amplifier les signaux audio de l'appareil radio pour un haut-parleur. Cela se reconnaît facilement au symbole du haut-parleur dans le circuit. Les amplificateurs de puissance HF sont employés, par exemple, pour rehausser le signal d'émission.

<margin>
[picture:763:e_nf_verstaerker:Schéma d'un amplificateur BF]  
</margin>

[question:ED402]
[question:ED403]

Comme la puissance de sortie est plus élevée que la puissance d'entrée, il faut toujours apporter de l'énergie à un amplificateur. Une source de tension de capacité suffisante est donc nécessaire.

[question:ED401]

---

Pour qu'un amplificateur puisse être qualifié de *linéaire*, il doit posséder la propriété suivante : lorsque le signal d'entrée double, le signal de sortie de l'amplificateur double lui aussi.
Les écarts de linéarité sont en règle générale indésirables et ne sont tolérables que pour des modes comme la FM (dans lesquels l'information du signal n'est pas transmise par l'amplitude, mais uniquement par la fréquence). Si un amplificateur ne travaille pas linéairement, son signal de sortie contient des fréquences qui n'existent pas dans le signal d'entrée (ce qu'on appelle le splatter). Dans le domaine BF, ce comportement se manifeste par de la distorsion. Dans le domaine HF, des harmoniques du signal amplifié apparaissent. Les deux sont indésirables. La figure [ref:e_verstaerker_linearitaet] montre à titre d'exemple comment un signal sinusoïdal est déformé par un comportement non linéaire. 

<margin>
[picture:828:e_verstaerker_linearitaet:Le signal d'entrée est amplifié. En cas d'écrêtage dû au manque de linéarité, le signal de sortie est déformé.]
</margin>

[question:EF403]

Pour la linéarité d'un émetteur, une alimentation stabilisée et découplée des autres étages est également nécessaire, afin d'éviter les réactions parasites indésirables.

[question:EF405]

On ne trouve pas des amplificateurs BF uniquement au niveau du haut-parleur de l'appareil radio, mais aussi dès le microphone. Ils servent alors, par exemple, à amplifier le signal du microphone. Habituellement, les composantes de fréquence plus basses (en dessous de $\qty{300}{\hertz}$) et plus hautes (au-dessus de $\qty{3}{\kilo\hertz}$) du signal du microphone sont déjà supprimées à l'intérieur de l'amplificateur de microphone par une caractéristique de type passe-bande, afin de limiter la largeur de bande du signal BF et de supprimer les composantes de fréquence plus basses telles que le ronflement secteur (cf. figure [ref:e_frequenzgang_mikrofonverstaerker]). Pour une bonne intelligibilité de la parole, une largeur de bande BF d'environ $\qtyrange{2,5}{3}{\kilo\hertz}$ est nécessaire en communication vocale.

<margin>
[picture:246:e_frequenzgang_mikrofonverstaerker:Réponse en fréquence typique d'un amplificateur de microphone radioamateur]
</margin>

[question:EF308]
[question:EF307]