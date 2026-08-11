Nous autres humains sommes habitués à utiliser les dix chiffres de $\num{0}$ à $\num{9}$. On parle de système à base dix ou système décimal.

Pour les ordinateurs, il est en revanche plus simple de travailler avec seulement $\num{2}$ chiffres : le $\num{0}$ et le $\num{1}$. Cela correspond à deux états : par exemple éteint et allumé, « transistor bloqué » et « transistor passant », ou encore $\qty{0}{\volt}$ et $\qty{5}{\volt}$. Il en résulte un système de numération binaire ou système binaire.

[question:EA201]

Le comptage se fait de la même façon dans tous les systèmes de numération (voir tableau [ref:binaer_zahlensysteme]) : on commence à $\num{0}$ et on fait défiler les chiffres. Quand la réserve de chiffres est épuisée, on recommence depuis le début en écrivant un $\num{1}$ devant chaque nombre. C'est pourquoi, dans le système décimal, le $\num{10}$ vient après le $\num{9}$. Le chiffre le plus à droite a la valeur qu'il représente lui-même. On appelle cela le poids $\num{1}$. 

---

Dans le système décimal, le deuxième chiffre en partant de la droite vaut dix fois sa propre valeur, il a donc le poids $\num{10}$. Chaque position située plus à gauche vaut à chaque fois dix fois plus que celle située juste à sa droite. Par exemple, le nombre décimal $\num{5573}$ du tableau [ref:binaer_stellenwert_dezimal] signifie donc en réalité $5 \cdot 1000 + 5 \cdot 100 + 7 \cdot 10 + 3 \cdot 1$.

<margin>
|c: |c: |c: |c: |
|$\num{1000}$ | $\num{100}$ | $\num{10}$ | $\num{1}$ |
| $\num{5}$ | $\num{5}$ | $\num{7}$ | $\num{3}$ |
[table:binaer_stellenwert_dezimal:Poids des chiffres du nombre décimal à quatre chiffres $\num{5573}$]

|r: Décimal | r: Binaire |
| $\num{0}$ | $\num{0}$ |
| $\num{1}$ | $\num{1}$ |
| $\num{2}$ | $\num{10}$ |
| $\num{3}$ | $\num{11}$ |
| $\num{4}$ | $\num{100}$ |
| $\num{5}$ | $\num{101}$ |
| $\num{6}$ | $\num{110}$ |
| $\num{7}$ | $\num{111}$ |
| $\num{8}$ | $\num{1000}$ |
| $\num{9}$ | $\num{1001}$ |
| $\num{10}$ | $\num{1010}$ |
| $\num{11}$ | $\num{1011}$ |
| $\num{12}$ | $\num{1100}$ |
| $\num{13}$ | $\num{1101}$ |
| $\num{14}$ | $\num{1110}$ |
| $\num{15}$ | $\num{1111}$ |
[table:binaer_zahlensysteme:Nombres dans le système décimal et dans le système binaire]
</margin>

Dans le système binaire, il n'y a que deux chiffres, à savoir $\num{0}$ et $\num{1}$. Comme on le voit dans le tableau [ref:binar_stellenwert_dual], la première position en partant de la droite a le poids $\num{1}$, la deuxième $\num{2}$, la troisième $\num{4}$, la quatrième $\num{8}$ et ainsi de suite. Les poids doublent au lieu de décupler, parce qu'il n'y a que deux chiffres et non dix. Une position dans le système binaire s'appelle aussi un bit ($\unit{\bit}$).

|c: |c: |c: |c: |c: |c: |c: |c: |
| $\num{128}$ | $\num{64}$ | $\num{32}$ | $\num{16}$ | $\num{8}$ | $\num{4}$ | $\num{2}$ | $\num{1}$ |
| $\num{1}$ | $\num{0}$ | $\num{0}$ | $\num{0}$ | $\num{1}$ | $\num{1}$ | $\num{1}$ | $\num{0}$ |
[table:binar_stellenwert_dual:Poids des chiffres du nombre binaire à huit chiffres $\num{10001110}$]

Quand on connaît les poids des positions, la conversion des nombres binaires dans le système décimal est simple. Prenons un exemple du tableau [ref:binar_stellenwert_dual]. Le nombre binaire $\num{10001110}$ doit être converti en nombre décimal.

1. On écrit au-dessus de chaque chiffre du nombre binaire son poids.
2. On additionne tous les poids sous lesquels se trouve un $\num{1}$ : $128+8+4+2=142$

[question:EA206]
[question:EA207]
[question:EA208]

Sur le papier, on peut écrire des nombres binaires avec autant de bits qu'on en a besoin. En technique numérique, il en va autrement. Le matériel ou le logiciel impose un nombre de positions déterminé, qu'on appelle aussi la largeur. Par exemple, les microcontrôleurs ou les ordinateurs ont fréquemment des largeurs de $\num{8}$, $\num{16}$, $\num{32}$ ou $\qty{64}{\text{Bits}}$. Dans la représentation, les nombres binaires sont souvent complétés par des zéros en tête jusqu'à atteindre cette largeur. Cela ne change rien à la valeur du nombre.

[question:EA205]

Une largeur fixe limite la plage de valeurs. Avec un bit, deux valeurs sont possibles ($\num{0}$ et $\num{1}$), avec deux bits déjà quatre ($\num{00}$, $\num{01}$, $\num{10}$ et $\num{11}$), et avec chaque bit supplémentaire à chaque fois deux fois plus. Avec $n$ bits, on peut représenter $2^n$ nombres différents.

[question:EA204]
[question:EA202]
[question:EA203]
