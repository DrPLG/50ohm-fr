À l'aide d'un mélangeur, une fréquence donnée (ou une plage de fréquences de largeur de bande définie) peut être transposée vers une fréquence plus haute ou plus basse. Pour cela, les signaux sont multipliés entre eux. 

<indepth>
Une multiplication de signaux dans le domaine temporel conduit à une addition (ou une soustraction) dans le domaine fréquentiel. Cette relation s'explique de manière parlante avec l'identité trigonométrique suivante (un peu simplifiée : les facteurs $2\pi\cdot t$ ont été omis pour plus de clarté) :  
  
$\sin(f_1)\cdot\sin(f_2) = \frac{1}{2}\left(\cos(f_1-f_2)-\cos(f_1+f_2)\right)$
  
Lorsque deux signaux sinusoïdaux sont multipliés entre eux — l'un à la fréquence $f_1$ et l'autre à la fréquence $f_2$ —, deux nouveaux signaux en cosinus apparaissent dans le domaine fréquentiel (ce qui n'est rien d'autre qu'un sinus déphasé). Ils se situent aux fréquences $f_1 - f_2$ et $f_1 + f_2$. On peut se représenter cela comme une composante de fréquence décalée vers le bas et une autre décalée vers le haut. C'est exactement ce principe que le mélangeur met à profit.

Il en résulte fondamentalement toujours deux composantes de fréquence. En pratique, une seule d'entre elles est cependant le plus souvent souhaitée, raison pour laquelle des filtres appropriés sont placés à la suite du mélangeur pour sélectionner le produit de mélange voulu. À strictement parler, des fréquences négatives peuvent aussi apparaître lors de la différence, raison pour laquelle on considère en général la valeur absolue $| f_1 \pm f_2 |$.
</indepth>

---

Un mélangeur utilise des composants non linéaires, par exemple des diodes, pour multiplier des signaux entre eux. Il en résulte ce qu'on appelle des produits de mélange, dont les fréquences correspondent mathématiquement à la somme et à la différence des fréquences des signaux d'entrée.

Grâce à cette propriété, les mélangeurs sont employés de façon ciblée pour transposer des signaux vers d'autres plages de fréquences souhaitées — par exemple pour la transposition vers le haut ou vers le bas dans les émetteurs et les récepteurs. Dans les schémas synoptiques, un mélangeur est symbolisé, comme représenté sur la figure [ref:e_mischer], par un cercle contenant un signe de multiplication, qui rappelle l'effet multiplicatif de ce bloc fonctionnel.

<margin>
[picture:903:e_mischer:Mélangeur]
</margin>

---

Les fréquences produites à une sortie d'un mélangeur se composent principalement des deux produits de mélange des signaux appliqués : $f_\text{e}$, le signal d'entrée, et $f_\text{o}$, le signal provenant d'un oscillateur. Il en résulte deux produits de mélange souhaités, sous forme de somme et de valeur absolue de la différence des signaux appliqués :

$f_\text{z}=|f_\text{e}\pm f_\text{o}|$

À cause du $\pm$, il faut distinguer deux cas : on obtient ainsi $f_\text{z1} = f_\text{e}+f_\text{o}$ ainsi que $f_\text{z2}=|f_\text{e}-f_\text{o}|$.

Les barres de valeur absolue $|x|$ signifient que seule la valeur numérique, sans signe, est considérée. Si $x$ est négatif, il est rendu positif. Si $x$ est déjà positif, il reste inchangé.

Normalement, un seul des produits de mélange souhaités est utilisé pour le traitement ultérieur du signal. L'autre produit de mélange (ainsi que, le cas échéant, d'autres produits de mélange indésirables — voir l'approfondissement) doit ensuite être éliminé du mélange de signaux par filtrage.

<indepth>
Un mélangeur réel produit, outre les produits de mélange souhaités, des produits de mélange d'ordre supérieur, comme par exemple $2 * f_\text{in1} + f_\text{in2}$, etc. Ces produits de mélange indésirables doivent ensuite être également éliminés par des filtres appropriés. Dans les mélangeurs réels, les deux fréquences d'entrée ne sont pas non plus complètement supprimées dans le signal de sortie et doivent être prises en compte lors du traitement ultérieur du signal. L'utilisation d'un mélangeur en anneau équilibré (balance-mixer) permet de supprimer très fortement les deux signaux d'entrée dans le signal de sortie, raison pour laquelle ce type de mélangeur est fréquemment employé.
</indepth>

[question:EF201]

Pour cette question, il suffit d'additionner une fois la fréquence de l'oscillateur et de la soustraire une fois, en tenant compte de la valeur absolue.

$f_\text{z1} = f_\text{e}+f_\text{o} = \qty{21}{\mega\hertz} + \qty{31,7}{\mega\hertz} = \qty{52,7}{\mega\hertz}$

$f_\text{z2}=|f_\text{e}-f_\text{o}| =|\qty{21}{\mega\hertz} - \qty{31,7}{\mega\hertz}| = |\qty{-10,7}{\mega\hertz}| = \qty{10,7}{\mega\hertz}$

Les questions suivantes fonctionnent selon le même principe.

[question:EF202]
[question:EF203]
[question:EF204]
[question:EF205]

Comme les mélangeurs produisent les fréquences les plus diverses lors du processus de mélange, les *étages mélangeurs doivent toujours être très bien blindés*, afin qu'aucun rayonnement ne puisse se propager vers d'autres étages ou appareils et, en particulier, que d'autres services radio ne soient pas perturbés !

[question:EF206]