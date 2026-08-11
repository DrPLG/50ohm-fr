Les débits de données atteignables en pratique diffèrent nettement selon le procédé de transmission et les conditions de propagation. Le WLAN et la 5G permettent, dans des conditions optimales, des débits de données allant jusqu'à l'ordre du gigabit par seconde. FT8, en revanche, peut être employé même dans des conditions défavorables, mais ne transmet que quelques bits par seconde.

Le débit de données atteignable dépend de la largeur de bande utilisable et du rapport signal sur bruit ($P_\text{S}/P_\text{N}$). À partir de ces deux grandeurs, la loi de Shannon-Hartley permet de calculer le débit de données théorique maximal atteignable pour un canal de transmission :

$C=B \cdot \log_2 \left(1+{\dfrac{P_\text{S}}{P_\text{N}}}\right) \unit{\bit\per\second}$

[question:AE416]

---

Une valeur facile à retenir apparaît pour un rapport signal sur bruit de $\qty{0}{\dB}$. Ici, la largeur de bande en $\unit{\hertz}$ correspond exactement au débit de données maximal atteignable en $\unit{\bit\per\second}$. Des rapports signal sur bruit moins bons permettent des débits plus faibles, de meilleurs rapports signal sur bruit des débits plus élevés. Ce moyen mnémotechnique permet de répondre rapidement aux questions d'examen correspondantes, sans long calcul.

<margin>
En posant $\frac{P_\text{S}}{P_\text{N}} = \qty{0}{\dB}$, c'est-à-dire le facteur $\num{1}$, on obtient :
  
$\begin{split} C&=B \cdot \log_2 \left(1+1\right) \unit{\bit\per\second}\\ C&=B \cdot \log_2 \left(2\right) \unit{\bit\per\second}\\C &= \qty{B}{\bit\per\second}\end{split}$
</margin>

---

Si l'on veut transmettre nettement plus de bits par seconde qu'il n'y a de hertz de largeur de bande disponibles, le rapport signal sur bruit nécessaire augmente fortement. Sur les liaisons à bande étroite en ondes courtes, il est donc pratiquement impossible d'atteindre des débits élevés. C'est ainsi que le Hamnet, en tant que réseau de données rapide, est en règle générale exploité dans le haut de la bande UHF et le bas de la bande SHF, où de plus grandes largeurs de bande sont disponibles.

<indepth>
On ne considère ici que l'énergie de bruit située à l'intérieur de la largeur de bande utilisée. Certains programmes informatiques utilisent en revanche l'énergie de bruit d'un canal de $\qty{2,4}{\kilo\hertz}$ de large, même lorsque le signal utile proprement dit est nettement plus étroit ; il s'agit cependant là d'une autre grandeur, qui ne peut pas être introduite directement dans la formule de la loi de Shannon-Hartley.
</indepth>

En abaissant le débit de données, on peut en revanche mettre au point des procédés qui non seulement nécessitent une faible largeur de bande, mais fonctionnent encore avec un rapport signal sur bruit extrêmement mauvais.  Les procédés de transmission numériques tels que WSPR ou FT8, qui n'échangent que peu de caractères par unité de temps, en sont des exemples. La transmission d'un court message reste ainsi possible, même dans de mauvaises conditions de propagation.

[question:AE417]
[question:AE418]
[question:AE420]
[question:AE419]

Il faut noter que la loi de Shannon-Hartley ne détermine qu'une borne supérieure du débit de données atteignable. Les débits réellement atteints se situent toujours en dessous. Ce n'est qu'au moyen de bons procédés de correction d'erreurs, que nous découvrirons plus loin, que l'on peut s'approcher de cette borne supérieure. 
