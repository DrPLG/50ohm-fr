On a besoin d'un convertisseur de tension chaque fois qu'une tension électrique doit être transformée en une autre tension. En radioamateurisme, il peut s'agir par exemple de produire du $\qty{5}{\volt}$ pour un microcontrôleur à partir d'une alimentation en $\qty{13,8}{\volt}$, ou d'alimenter un ordinateur portable en $\qty{19}{\volt}$ à partir d'une batterie de $\qty{12}{\volt}$. De tels montages sont appelés convertisseurs DC/DC. Si la tension est élevée, on parle d'un convertisseur Step-UP (élévateur) ; si elle est abaissée, d'un convertisseur Step-DOWN (abaisseur).

Toute conversion de tension engendre des pertes. C'est pourquoi la puissance délivrée est toujours inférieure à la puissance fournie. Le rapport entre la puissance de sortie et la puissance d'entrée est appelé rendement $\eta$ :

$ \eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}} $

Pour les questions suivantes, il faut appliquer la formule de la puissance $P = U \cdot I$ afin de calculer la puissance d'entrée et la puissance de sortie. On peut ensuite déterminer le rendement.

[question:AB213]
[question:AB214]

<indepth>
[photo:300:StepUpWandler: Convertisseur abaisseur (Buck) et élévateur (Boost). Réglé ici comme convertisseur élévateur de $\qty{7,2}{\volt}$ à $\qty{24}{\volt}$]
Ce convertisseur Buck-Boost peut être réglé de $\qty{0,5}{\volt}$ à $\qty{25}{\volt}$ en sortie. La puissance maximale est de $\qty{25}{\watt}$. Comme le rendement est très élevé, les transistors de commutation se passent de dissipateur thermique.  Le mode de fonctionnement convertisseur abaisseur (Step Down = Buck Mode) ou convertisseur élévateur (Step Up = Boost Mode) peut être activé avec le mini-interrupteur de droite.
</indepth>