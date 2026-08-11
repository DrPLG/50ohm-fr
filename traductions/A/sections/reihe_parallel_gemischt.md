Dans la classe E, nous avons déjà appris comment se comportent les condensateurs en montage série et parallèle. Le montage en série de bobines a en outre été traité au chapitre précédent. Dans ce chapitre, nous examinons maintenant le montage en parallèle de bobines et de condensateurs. Mais nous répétons d'abord encore une fois les relations fondamentales des montages en parallèle et en série de capacités.

Dans les circuits oscillants parallèles, bobines et condensateurs sont combinés. Or une bobine réelle possède elle aussi une certaine capacité propre. Celle-ci provient par exemple des enroulements de la bobine et des couplages de champ électrique existant de ce fait entre les spires.

Pour un calcul aussi précis que possible de la fréquence de résonance, ces capacités « invisibles » doivent être prises en compte. Dans l'exercice suivant, les capacités des condensateurs et la capacité propre de la bobine peuvent être additionnées directement, car elles sont en parallèle les unes des autres.

Il est particulièrement important de faire attention aux différentes unités. Avant le calcul, toutes les valeurs devraient donc être converties dans la même unité, afin que les capacités puissent être additionnées correctement.

[question:AD103]

Dans l'exercice suivant, trois condensateurs sont montés en série. Dans la classe E, nous avons appris que, pour des condensateurs en montage série, ce sont les inverses des capacités qui s'additionnent :

$\frac{1}{C_{\mathrm{tot}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

Ici aussi, les capacités doivent être converties dans la même unité avant le calcul, afin que les inverses puissent être additionnés correctement.

[question:AD101]

---

Dans les circuits en courant alternatif apparaissent, à côté des résistances ohmiques bien connues, aussi des réactances, comme nous les avons déjà rencontrées avec les condensateurs et les bobines. La résistance ohmique normale est désignée comme résistance active $R$. Les réactances sont décrites par $X$. Les deux types de résistances influencent simultanément le passage du courant dans le circuit.

Comme résistance active et réactance agissent différemment, elles ne peuvent pas être simplement additionnées. Elles sont au contraire composées géométriquement. On peut se représenter cela comme un triangle rectangle, comme sur la figure [ref:a_dreieck] :

---

- La résistance active $R$ forme le côté horizontal.
- La réactance $X$ forme le côté vertical.
- La résistance totale qui en résulte est désignée comme impédance apparente $|Z|$.

<margin>
[picture:1067:a_dreieck:Triangle rectangle illustrant le calcul de l'impédance apparente $|Z|$ à partir de la résistance active $R$ et de la réactance $X$]
</margin>

L'impédance apparente peut se calculer avec le théorème de Pythagore (cf. recueil de formules) :

$ |Z| = \sqrt{R^2 + X^2} $

La lettre $Z$ est utilisée pour ce qu'on appelle l'impédance. Pour les calculs de ce chapitre, il suffit toutefois de considérer le module $|Z|$ comme la résistance totale en courant alternatif du circuit.

<indepth>
Pour les personnes intéressées par les mathématiques : l'impédance $Z$ est une grandeur complexe qui contient la résistance active $R$ comme partie réelle et la réactance $X$ comme partie imaginaire :

$Z = R + jX$

Le module $|Z|$ correspond alors à la longueur du vecteur dans le plan complexe qui résulte de la combinaison de $R$ et $X$.
</indepth>

Pour la question suivante, avant de pouvoir appliquer le théorème de Pythagore, il faut calculer la réactance $X_C$ du condensateur à $\qty{1}{\mega\hertz}$. Nous utilisons pour cela la formule de la réactance d'un condensateur.

[question:AD104]

La question suivante porte sur le calcul de l'impédance apparente d'un montage en série d'une résistance et d'une bobine. Nous calculons d'abord $X_L$, puis nous appliquons de nouveau le théorème de Pythagore. Ici aussi, il faut faire attention aux puissances de dix pour que le calcul soit effectué correctement.

[question:AD105]
