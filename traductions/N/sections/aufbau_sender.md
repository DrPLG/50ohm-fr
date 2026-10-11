<margin>
[picture:735:aufbau_sender:Schéma-bloc d'un émetteur simple]
</margin>

La figure [ref:aufbau_sender] montre à partir de quels composants on peut construire un émetteur AM. Certains blocs nous sont déjà connus du récepteur, d'autres sont nouveaux. Les numéros du tableau sont ceux de la figure.

| c: Nº | X: Bloc et rôle |
| 1 | **Microphone** — Le microphone convertit les ondes sonores de la parole en oscillations électriques basse fréquence. On peut aussi, à la place, utiliser le signal basse fréquence issu de la sortie audio d'un ordinateur, par exemple pour les procédés de transmission numériques. |
| 2 | **Amplificateur basse fréquence** — Le signal provenant du microphone ou de l'ordinateur est d'abord amplifié. |
| 3 | **Mélangeur** — Le mélangeur combine la porteuse haute fréquence produite par l'oscillateur (4) avec l'oscillation basse fréquence provenant du microphone ou de l'ordinateur. Il en résulte que la porteuse haute fréquence est modulée en amplitude par le signal vocal ou le signal de données. |
| 4 | **Oscillateur** — L'oscillateur produit l'oscillation haute fréquence à la fréquence sur laquelle on souhaite émettre, par exemple $\qty{29,5}{\mega\hertz}$. |
| 5 | **Filtre passe-bande** — Comme le mélangeur, de par son principe de fonctionnement, produit non seulement les fréquences souhaitées mais aussi d'autres fréquences indésirables, celles-ci doivent être bloquées par un filtre de bande. |
| 6 | **Amplificateur haute fréquence** — Le signal haute fréquence est maintenant amplifié afin d'atteindre la puissance d'émission souhaitée. |
| 7 | **Filtre passe-bas** — Comme l'amplification peut elle aussi produire des fréquences indésirables, un nouveau filtrage est nécessaire. |
| 8 | **Antenne** — Le signal haute fréquence est enfin transmis à l'antenne, qui le rayonne sous forme d'onde radio. |

%[class:N]
<indepth>
Lorsqu'un mélangeur combine deux signaux, cela correspond mathématiquement à une multiplication des deux signaux. C'est pourquoi on retrouve le signe de multiplication dans le symbole de bloc du mélangeur. Le fonctionnement précis d'un mélangeur fait partie du cours de la classe A.
</indepth>
%[/class]

[question:NF401]
[question:NF403]

Pour la question suivante, il est important de se rappeler qu'un émetteur a besoin d'un oscillateur et d'un mélangeur.

[question:NF402]

Une installation radioamateur doit être construite et exploitée selon les règles de l'art généralement reconnues. Cela vaut naturellement tout particulièrement pour les émetteurs.

[question:VD106]
