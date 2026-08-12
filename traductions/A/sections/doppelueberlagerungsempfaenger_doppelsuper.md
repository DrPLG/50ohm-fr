Dans la classe E, nous avons déjà fait connaissance avec le récepteur superhétérodyne. Dans cette classe, nous allons maintenant nous intéresser au récepteur à double changement de fréquence (double superhétérodyne). Contrairement au superhétérodyne simple, le double superhétérodyne utilise 2 fréquences intermédiaires, comme le montre la figure [ref:doppelsuper_blockschaltbild].

<margin>
[picture:810:doppelsuper_blockschaltbild:Schéma fonctionnel d'un double superhétérodyne]
</margin>

L'emploi d'une première FI élevée permet une bonne réjection de la fréquence image. Les deux points de réception possibles sont ainsi très éloignés l'un de l'autre, et la suppression du point de réception indésirable (fréquence image) est facilement réalisable par des filtres d'entrée placés avant le premier mélangeur. L'emploi d'une 2e FI basse permet, dans un deuxième temps, d'obtenir une sélectivité élevée du récepteur, car aux basses fréquences les filtres à facteur de qualité élevé et à flancs raides sont techniquement très bien réalisables.
Dans un récepteur décamétrique, la première FI et la plus haute fréquence de réception souhaitée devraient également être aussi éloignées que possible l'une de l'autre, selon le concept de récepteur, afin d'éviter une réception directe de la FI par l'antenne. La 1re FI devrait donc valoir le double de la fréquence de réception maximale.

<tip>
Une extension du concept de double superhétérodyne serait le triple superhétérodyne, dans lequel une 3e FI basse est formée. Cela peut être utile pour des procédés de démodulation particuliers ou pour la réalisation de procédés de réjection des perturbations (filtre notch). Le calcul des fréquences intermédiaires et des fréquences d'oscillateur s'effectue ici de la même manière que pour le double superhétérodyne.
</tip>

[question:AF112]
[question:AF113]

Après le premier mélangeur, on peut employer un filtre très étroit accordé sur la 1re FI, afin d'améliorer la tenue aux forts signaux.  Ce filtre est appelé *filtre roofing*. La largeur de bande du filtre roofing doit ici être au moins aussi grande que la plus grande largeur de bande nécessaire aux modes de fonctionnement prévus.

[question:AF114]
[question:AF116]

Le double superhétérodyne se compose des blocs fonctionnels suivants :
1. Partie HF avec présélection
2. Premier mélangeur avec VFO pour former la première FI. La fréquence du VFO peut ici se situer aussi bien au-dessus qu'en dessous de la fréquence de réception souhaitée (décalée chaque fois de la 1re FI)
3. Premier amplificateur FI avec filtre (filtre roofing)
4. Deuxième mélangeur avec CO (oscillateur à quartz) pour former la deuxième FI. La fréquence du CO peut ici se situer aussi bien au-dessus qu'en dessous de la 1re FI (décalée chaque fois de la 2e FI)
5. Deuxième amplificateur FI avec filtre (filtre FI selon le type de modulation ou le mode de fonctionnement, le plus souvent commutable).
6. Détecteur de produit ou démodulateur (selon le mode de fonctionnement), le cas échéant avec BFO. Cet étage sert aussi à produire une tension de régulation pour la commande de la sensibilité d'entrée de la chaîne de réception (AGC)
7. Amplificateur BF avec sortie haut-parleur ou prise casque

[question:AF209]
[question:AF117]
[question:AF210]

Pour calculer les fréquences d'oscillateur nécessaires en fonction d'une fréquence de réception souhaitée, il faut bien se représenter que les fréquences d'oscillateur peuvent se situer chaque fois au-dessus ou en dessous de la fréquence d'entrée souhaitée du mélangeur. Il existe donc, pour chaque étage mélangeur, deux solutions possibles.
1. Fréquence d'oscillateur = fréquence d'entrée + fréquence de sortie
2. Fréquence d'oscillateur = fréquence d'entrée - fréquence de sortie

Fort de ces connaissances, on peut répondre aux questions suivantes.

[question:AF120]
[question:AF118]
[question:AF119]