Si le récepteur détecte une erreur de transmission, par exemple à l'aide de bits de contrôle, il peut demander à l'émetteur une nouvelle transmission des données. Avec la *correction d'erreurs directe*, en revanche, une retransmission n'est fréquemment pas nécessaire. Pour cela, des informations supplémentaires sont ajoutées aux données utiles, par exemple plusieurs bits de contrôle. Le récepteur peut ainsi, sous certaines conditions, non seulement détecter qu'une erreur est survenue, mais aussi déterminer quel bit est erroné et le corriger. En anglais, ce procédé est appelé *Forward Error Correction* (FEC).

Le détail du fonctionnement possible est montré dans l'encadré d'approfondissement ci-contre, à l'exemple d'un code de Hamming. Le procédé exact n'est pas au programme de l'examen.

[question:AE413]
[question:AE414]

<indepth>
Le code de Hamming est un procédé de correction d'erreurs qui utilise plusieurs bits de parité. Supposons que nous voulions transmettre les $\num{11}$ bits de données suivants :

[picture:683:hamming1: ]

Pour qu'une erreur portant sur un seul bit ne soit pas seulement détectée, mais aussi corrigée, nous devons pouvoir établir à quel endroit l'erreur est survenue. Nous examinons pour cela d'abord les positions des différents bits et les désignons par des lettres :

[picture:682:hamming2: ]

Nous disposons maintenant les bits de données un peu autrement et ajoutons quatre bits de parité supplémentaires, $p_1$ à $p_4$ :

[picture:684:hamming3: ]

Les quatre bits de parité contrôlent des groupes de bits différents, qui se recouvrent partiellement :

[picture:685:hamming4: ]

Chaque bit de parité protège ainsi un groupe déterminé :

[picture:686:hamming5: ]

Pour chacun de ces groupes, nous calculons maintenant le bit de parité correspondant en *parité paire* :

[picture:687:hamming6: ]

Si une erreur portant sur un seul bit survient lors de la transmission, certains contrôles de parité échouent. La combinaison des contrôles ayant échoué permet de déterminer à quelle position l'erreur est survenue. Le bit erroné peut ensuite être inversé, et donc corrigé.

Si, par exemple, le bit $k$ devient un $\num{0}$ lors de la transmission, les quatre contrôles de parité $p_1$ à $p_4$ échouent. Seul le bit $k$ appartient aux quatre groupes contrôlés. L'erreur se situe donc forcément sur le bit $k$.

Si en revanche une erreur survient sur le bit $a$, seuls les contrôles de parité de $p_1$ et $p_2$ échouent, tandis que ceux de $p_3$ et $p_4$ réussissent. Ce motif permet au récepteur de reconnaître que le bit $a$ est erroné.

Une erreur portant sur un bit de parité lui-même peut elle aussi être détectée et corrigée. Si par exemple $p_1$ est erroné, seul le contrôle de parité correspondant à $p_1$ échoue, tandis que les contrôles de $p_2$, $p_3$ et $p_4$ réussissent. L'erreur se situe donc forcément sur $p_1$.

Le code de Hamming présenté ici est conçu pour la correction d'une erreur portant sur un seul bit. Si plusieurs erreurs binaires surviennent simultanément, les contrôles de parité ne permettent plus de conclure de façon fiable à la position réelle de l'erreur. Les codes de Hamming étendus peuvent en outre détecter de façon sûre, par exemple, deux erreurs binaires survenant simultanément.
</indepth>
