Dans la section précédente, nous avons vu que l'information contenue dans un symbole peut être représentée par exemple par des amplitudes ou des fréquences différentes. Une autre possibilité consiste à modifier la phase d'un signal. Pour représenter clairement des états du signal d'amplitude et de phase différentes, on utilise fréquemment ce que l'on appelle la *représentation I/Q*.

Considérons d'abord un état du signal à l'instant $t=0$. Une amplitude $A$ et une phase $\varphi$ sont fixées pour le symbole. Dans une représentation vectorielle, l'amplitude détermine la longueur du vecteur et la phase son angle par rapport à l'axe horizontal.

Le vecteur peut être décomposé en une composante horizontale et une composante verticale. La composante horizontale est désignée par $I$, pour *In-Phase Component*, et la composante verticale par $Q$, pour *Quadrature Component*. Pour l'état du signal représenté, on a :

$I=A\cdot\cos(\varphi)$

$Q=A\cdot\cos(\varphi-\qty{90}{\degree})=A\cdot\sin(\varphi)$

Si nous laissons le temps s'écouler, le vecteur associé à l'oscillation tourne. Ses projections sur les deux axes sont sinusoïdales et déphasées de $\qty{90}{\degree}$ l'une par rapport à l'autre. L'applet montre ce lien entre l'oscillation et sa représentation I/Q.

[include:applet_iq_zeiger]

[question:AF633]

On peut se représenter intuitivement qu'au début de chaque intervalle de symbole, la valeur du symbole à transmettre fixe un point dans le plan I/Q, et donc l'amplitude et la phase initiale de l'oscillation pour ce symbole. Au symbole suivant, on passe en conséquence à l'état du signal correspondant au point suivant.

Pour la représentation des symboles, ce n'est donc pas la rotation continue du vecteur qui nous intéresse, mais l'état de départ fixé pour chaque symbole. Lorsque les états de départ possibles sont portés comme points dans le plan I/Q (cf. [ref:a_iq_ebene]), on parle de *diagramme de constellation* (cf. figure [ref:a_konstellationsdiagramm]). Chaque point correspond à un symbole possible. La distance d'un point à l'origine décrit l'amplitude du signal. Son angle par rapport à l'axe I décrit la phase.

<margin>
[picture:1060:a_iq_ebene:Plan I/Q avec un point de signal]
[picture:1059:a_konstellationsdiagramm:Diagramme de constellation à 4 points de constellation]
</margin>

<indepth>
Pour ceux que les mathématiques intéressent : une oscillation sinusoïdale peut aussi être décrite mathématiquement comme un *vecteur complexe* tournant à la pulsation $\omega_\mathrm{c}$ :

$s(t) = \Re\left\{A \cdot e^{j(\omega_\mathrm{c}t+\varphi)}\right\} = A\cos(\omega_\mathrm{c}t+\varphi)$

$A$ décrit ici l'amplitude et $\varphi$ la phase initiale du signal. L'expression complexe peut être décomposée en deux parties :

$A \cdot e^{j(\omega_\mathrm{c}t+\varphi)} = \underbrace{A \cdot e^{j\varphi}}_{\text{Amplitude et phase}} \cdot \underbrace{e^{j\omega_\mathrm{c}t}}_{\text{Porteuse}}$

Dans un diagramme de constellation, c'est la première partie $A \cdot e^{j\varphi}$ qui nous intéresse. Elle décrit l'amplitude et la phase de l'état du signal. La rotation continue de la porteuse proprement dite n'y est pas représentée.
</indepth>

Nous utiliserons cette représentation à maintes reprises dans les sections suivantes : elle permet de représenter clairement les symboles possibles des procédés de modulation numériques, et plus tard aussi de décrire l'association des combinaisons de bits à ces symboles.
