Une antenne n'a pas besoin d'être résonante pour rayonner : il suffit de l'**adapter**. C'est le rôle de la **boîte d'accord** [index:Boîte d'accord] (ou coupleur d'antenne), un réseau réglable de bobines et de condensateurs qui transforme l'impédance présentée par la ligne en $\qty{50}{\ohm}$ pour l'émetteur. On l'emploie pour faire travailler une antenne sur plusieurs bandes, ou une antenne de longueur quelconque.

Le montage classique est le **filtre en pi** [index:Filtre en pi] : deux condensateurs vers la masse, une bobine en série entre eux. Son nom vient de la forme de la lettre $\pi$ dans le schéma. C'est aussi un **passe-bas** : en plus d'adapter, il affaiblit les **harmoniques** de l'émetteur, et on le retrouve à la sortie des amplificateurs. Beaucoup de boîtes du commerce emploient plutôt un montage en **T** (deux condensateurs en série, une bobine vers la masse), plus souple à régler, mais sans cet effet passe-bas.

<margin>
[picture:1100:harec_filtre_pi:Filtre en pi]
</margin>

---

Il faut bien voir **où** agit la boîte.

* Placée **près de l'émetteur**, elle présente $\qty{50}{\ohm}$ à l'émetteur, et le ROS-mètre placé entre les deux affiche 1. Mais **entre la boîte et l'antenne, rien ne change** : le ROS de la ligne reste le même, et ses pertes aussi. C'est acceptable avec une ligne bifilaire à faibles pertes, beaucoup moins avec un long coaxial.
* Placée **au pied de l'antenne**, souvent en version automatique, elle adapte à l'endroit même de la désadaptation : la ligne travaille alors à un ROS voisin de 1.

<attention>
La boîte d'accord **ne rend pas l'antenne résonante** et n'augmente pas son rendement : elle permet seulement à l'émetteur de délivrer sa puissance. On la règle à **puissance réduite**, puis on contrôle au ROS-mètre.
</attention>

Le réglage se fait sur le ROS-mètre, placé **entre l'émetteur et la boîte** : on cherche le minimum, au plus près de 1.
