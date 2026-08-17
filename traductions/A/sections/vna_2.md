Dans la classe E, nous avons déjà fait connaissance avec l'*analyseur de réseau vectoriel* (VNA) (cf. figure [ref:a_vna_swr]). Dans la classe A, nous voulons examiner son principe de fonctionnement d'un peu plus près.

Pour une mesure, le VNA produit d'abord un signal HF à une fréquence de départ fixée et le délivre à l'objet à mesurer, par exemple une antenne ou un circuit oscillant. Il mesure ensuite le signal qui revient de l'objet à mesurer, autrement dit le signal réfléchi. L'amplitude aussi bien que la phase de ce signal sont ici relevées. Afin de réduire l'influence des perturbations, plusieurs mesures peuvent aussi être effectuées puis moyennées pour un même point de fréquence.

Après la mesure, la fréquence est augmentée d'un pas fixé et l'opération est répétée. Le VNA parcourt ainsi pas à pas tout le domaine allant de la fréquence de départ à la fréquence d'arrêt. On désigne aussi cette opération sous le nom de *balayage en fréquence*, ou autrefois parfois de *wobbulation*.

À partir des valeurs mesurées aux différents points de fréquence, le VNA peut déterminer diverses grandeurs et les représenter en fonction de la fréquence. Il s'agit par exemple de l'impédance de l'objet à mesurer et du rapport d'ondes stationnaires (SWR). On peut ainsi reconnaître immédiatement à quelles fréquences une antenne est bien adaptée, ou présente une résonance.

<margin>
[photo:323:a_vna_swr:Mesure du SWR d'une antenne filaire alimentée par l'extrémité. Le SWR est proche de $1$ à $\qty{14}{\mega\hertz}$]
[picture:526:a_vna_swr_2:Évolution possible du SWR d'une antenne.]
</margin>

[question:AI201]
[question:AI202]
[question:AI203]

---

Une forme d'affichage possible du VNA est la décomposition de l'impédance en partie active et partie réactive (résistance active $R$ et réactance $X$). La résistance active est souvent indiquée en $\unit{\ohm}$ et la réactance parfois aussi sous la forme $j\unit{\ohm}$. Les affichages des différents appareils ne sont pas uniformes. Le $j$ provient d'une notation de l'électrotechnique, où il représente ce que les mathématiques appellent l'unité imaginaire ($i$). Les réactances positives correspondent à un comportement inductif et les réactances négatives à un comportement capacitif.

<indepth>
Les *nombres imaginaires* sont un outil apprécié en électrotechnique et en mathématiques. Afin de pouvoir résoudre des équations telles que $x^2 = -1$, on a imaginé un nombre dit imaginaire ($i$), qui, multiplié par lui-même, donne un nombre négatif : $i^2 = -1$. Aucun nombre réel ne satisfait une telle équation, car un nombre négatif multiplié par un nombre négatif donne un nombre positif. C'est pourquoi on qualifie $i$ d'« imaginaire ». Ce nombre « imaginé » donne, multiplié par lui-même, un nombre négatif, à savoir $-1$. Si l'on additionne des nombres réels (p. ex. $54$) et un nombre imaginaire (p. ex. $-12i$), on obtient un nombre complexe : $54 - 12i$. Un nombre complexe peut p. ex. servir à décrire la partie active et la partie réactive d'une résistance. On peut également convertir les nombres complexes en une amplitude et une phase. Au lieu de la lettre $i$, on utilise en électrotechnique la lettre $j$, afin d'éviter toute confusion avec le symbole $i$ (utilisé pour les courants).
</indepth>

[question:AI204]
[question:AI205]
[question:AI206]

---

De nombreux VNA offrent la possibilité de représenter graphiquement l'évolution du SWR en fonction de la fréquence. Si la fréquence de résonance d'une antenne est trop basse, on sait qu'il faut la raccourcir. Si elle est trop haute, l'antenne devrait être rallongée.

[question:AI207]
[question:AI208]
