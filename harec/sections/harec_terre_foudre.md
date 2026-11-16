**Liaison équipotentielle et terre.** Conduites d'eau, radiateurs, boîtiers, blindages de coaxiaux : un défaut, une charge statique ou la foudre peuvent porter ces conducteurs à des potentiels différents, et le contact entre deux d'entre eux devient dangereux. On les relie donc tous entre eux par des liaisons courtes et de faible impédance : c'est la **liaison équipotentielle** [index:Liaison équipotentielle]. Puis on raccorde l'ensemble à la **borne principale de terre** du bâtiment, pour évacuer les courants de défaut : c'est la **mise à la terre** [index:Mise à la terre]. Les appareils de la station portent à cet effet une borne à vis à l'arrière.

<attention>
**Le boîtier « chaud ».** Une liaison de terre séparée dont la longueur vaut $\lambda/4$, ou un multiple impair, sur une bande utilisée est **résonante**. Son bout à la terre est un nœud de tension ; le ventre de tension se trouve donc… au boîtier de l'émetteur, qui brûle ou électrise au toucher. Remède : changer la longueur de la liaison pour qu'elle ne résonne sur aucune bande.
</attention>

---

**La foudre.** Une antenne n'attire pas la foudre, mais si la foudre tombe, une antenne dégagée en sera probablement le point d'impact. Les antennes placées sur un bâtiment sont donc **mises à la terre**, ou intégrées au système de protection contre la foudre s'il en existe un. Un coup de foudre **voisin** suffit déjà à détruire les appareils par surtension.

Pour protéger la station :

* un **parafoudre** sur le coaxial, à tube à décharge de gaz, qui dérive la surtension vers la terre ;
* ou, plus simplement, **débrancher** et mettre à la terre la descente d'antenne après le trafic ;
* un conducteur de terre **massif**, de section suffisante, et non un fil souple fin.

Les **règles de l'art** sont données en France par les normes : **NF C 15-100** pour l'installation électrique, série **NF EN 62305** pour la protection contre la foudre. Toute intervention sur un système de protection contre la foudre revient à un **spécialiste**, et un pylône se signale à l'assureur.

**Charges statiques.** La pluie, la neige ou la grêle chargent une antenne isolée : craquements à la réception, et parfois danger. Une **résistance d'écoulement** de forte valeur (par exemple $\qty{100}{\kilo\ohm}$) entre la descente et la terre les évacue sans gêner l'antenne.

---

**Lignes électriques.** Une antenne se monte **loin des lignes aériennes**, et de façon qu'aucun élément ne puisse les toucher en tombant, même par tempête. Un contact avec une ligne d'énergie met toute l'installation sous une tension mortelle.

<attention>
**On ne touche jamais une antenne d'émission en service.** Les ventres de tension, aux extrémités d'un dipôle, portent des tensions HF élevées même à quelques watts : brûlures, choc, chute.
</attention>
