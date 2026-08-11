Comme nous l'avons déjà appris à propos de l'émetteur, les mélangeurs comme les amplificateurs produisent des composantes de fréquence indésirables. Si de telles composantes indésirables parviennent à l'antenne, elles sont rayonnées par celle-ci. On parle alors d'*émissions non désirées* (unerwünschte Aussendungen).

Les fréquences de ces émissions non désirées se situent souvent en dehors des bandes radioamateur. Elles peuvent au contraire se trouver, par exemple, dans des plages de fréquences de la radio aéronautique ou de la radiodiffusion commerciale.

Afin de ne perturber ni les autres services radio ni nos voisins dans leur réception de la radiodiffusion, un émetteur devrait toujours être exploité de façon à ne produire aucune émission non désirée. Cela peut être obtenu, par exemple, au moyen d'un filtre passe-bande qui ne laisse passer que la plage de fréquences souhaitée, tout en bloquant toutes les fréquences supérieures et inférieures.

Comme les filtres réellement disponibles ne sont pas parfaits, les émissions non désirées ne peuvent pas être totalement évitées par ce moyen. En pratique, les émissions non désirées doivent donc être limitées au *niveau le plus faible possible*.

<indepth>
% TODO: Editionsspezifisch machen
Même si la loi allemande sur le radioamateurisme (Amateurfunkgesetz) exige seulement, de manière générale, que les émissions non désirées soient limitées au niveau le plus faible possible, d'autres dispositions légales fixent des valeurs limites concrètes. Celles-ci sont traitées dans le cours de la classe A.
</indepth>

[question:NJ201]
[question:NF404]

[question:VD110]

<france>
# Le niveau des rayonnements non essentiels

La réglementation française ne fixe pas elle-même de valeur : la décision ARCEP n° 2012-1241 renvoie à l'appendice 3 du Règlement des radiocommunications de l'UIT. Il faut donc aller y chercher le chiffre.

Cet appendice exprime une atténuation minimale par rapport à la puissance de l'émission fondamentale, en décibels sous la porteuse (dBc) :

$$43 + 10\,\log(P)$$

où **P** est la puissance en crête de l'émetteur exprimée en watts, si bien que $10\,\log(P)$ n'est autre que cette puissance exprimée en dBW.

L'appendice assortit cette formule d'un plafond, et retient la valeur la moins contraignante des deux : 50 dBc en dessous de 30 MHz, 70 dBc au-dessus.

Un exemple pour fixer les idées. Sur 144 MHz, à la puissance maximale autorisée de 120 W, soit environ 21 dBW, la formule donne 43 + 21 = 64 dBc. C'est cette valeur qui s'applique, puisqu'elle est moins contraignante que le plafond de 70 dBc.
</france>
