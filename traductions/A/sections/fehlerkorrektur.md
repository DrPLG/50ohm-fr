Si le récepteur détecte une erreur, par exemple au moyen de bits de contrôle, il peut demander à l'émetteur une nouvelle transmission des données afin de corriger l'erreur. Avec la correction d'erreurs directe, en revanche, une retransmission n'est souvent pas nécessaire. Pour cela, de la redondance supplémentaire est ajoutée aux données, p. ex. plusieurs bits de contrôle. On ne détecte ainsi pas seulement qu'une erreur est présente, mais aussi où elle se trouve. Le procédé peut donc corriger l'erreur en rectifiant le bit reconnu comme erroné. Le fonctionnement détaillé est expliqué dans l'encadré bonus. Il n'est cependant pas au programme de l'examen. En anglais, on parle de Forward Error Correction (FEC).

[question:AE413]
[question:AE414]

<indepth>

Le code de Hamming est un procédé de correction d'erreurs qui utilise plusieurs bits de parité. Supposons que nous voulions transmettre les 11 bits suivants :

[picture:683:hamming1: ]

L'objectif est qu'une erreur sur un bit ne soit pas seulement détectée, mais aussi corrigée. Pour cela, il est utile d'examiner de plus près les positions des différents bits. Nous désignons donc les positions par des lettres :

[picture:682:hamming2: ]

Nous disposons maintenant les bits un peu autrement et ajoutons quelques bits supplémentaires :

[picture:684:hamming3: ]

Au lieu d'un unique bit de contrôle, nous en utilisons désormais quatre ($p_1$-$p_4$), qui couvrent différentes zones de nos bits de données, à la manière d'une grille de mots croisés :

[picture:685:hamming4: ]

Chaque bit de contrôle protège une certaine zone :

[picture:686:hamming5: ]

Reprenons l'ensemble avec nos données. Pour chaque zone, nous calculons le bit de contrôle en parité paire :

[picture:687:hamming6: ]

Si une erreur survient lors de la transmission, elle peut être localisée et corrigée grâce à la combinaison des différentes zones. 

Si, par exemple, le bit $k$ devient un $\num{0}$ du fait de la transmission, tous les contrôles de parité ($p_1$-$p_4$) échouent. L'erreur se situe donc forcément sur le bit $k$.

Si l'erreur survient p.\,ex. sur le bit $a$, les contrôles de parité de $p_1$ et $p_2$ échouent, tandis que ceux de $p_3$ et $p_4$ réussissent. L'erreur se situe donc forcément sur le bit $a$.

Même des erreurs portant sur les bits de parité peuvent être détectées et corrigées. Si l'erreur survient p.\,ex. sur le bit $p_1$, le contrôle de parité de $p_1$ échoue, tandis que ceux de $p_2$, $p_3$ et $p_4$ réussissent. L'erreur se situe donc forcément sur le bit $p_1$.

Si plus de 1 erreur survient, le code de Hamming ne peut plus les détecter ni les corriger correctement. Il existe cependant des extensions du code de Hamming, capables de détecter également les erreurs portant sur plusieurs bits.
</indepth>
