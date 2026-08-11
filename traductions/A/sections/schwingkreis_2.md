Dans le recueil de formules, nous trouvons la formule suivante pour le calcul de la fréquence de coupure des cellules RC, par ex. des filtres passe-haut ou passe-bas :

$f_g = \frac{1}{2 \pi \cdot R \cdot C}$

Avec cette formule, nous pouvons résoudre une série de questions d'examen.

<indepth>
Pour les lecteurs intéressés par les mathématiques : la formule de la fréquence de coupure d'une cellule RC peut aussi être établie par l'examen des impédances complexes de la résistance et du condensateur. Nous considérons le passe-bas RC comme un diviseur de tension dépendant de la fréquence.

[picture:175:a_rc_tiepass:Passe-bas RC comme diviseur de tension dépendant de la fréquence]

Pour le rapport entre la tension de sortie et la tension d'entrée, on a :

$\frac{|U_A|}{|U_E|} = \frac{|X_C|}{|R + X_C|}$

La réactance capacitive du condensateur s'écrit :

$X_C = \frac{1}{j\omega C}$

Il en résulte :

$\frac{|U_A|}{|U_E|} = \frac{\left|\frac{1}{j\omega C}\right|}{\left|R + \frac{1}{j\omega C}\right|}$

Pour les modules, nous obtenons :

$\frac{|U_A|}{|U_E|} = \frac{\frac{1}{\omega C}}{\sqrt{R^2 + \frac{1}{\omega^2 C^2}}}$

En multipliant le numérateur et le dénominateur par $\omega C$, l'expression se simplifie en :

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{1 + R^2\omega^2 C^2}}$

La fréquence de coupure est définie de telle sorte que la tension de sortie est retombée au facteur $\frac{1}{\sqrt{2}} \approx 0{,}707$ de la valeur initiale. Cela correspond à environ $\qty{70}{\percent}$ de la tension de sortie, soit une chute de niveau de $\qty{3}{\dB}$.

$\frac{|U_A|}{|U_E|} = \frac{1}{\sqrt{2}}$

Il s'ensuit :

$\frac{1}{\sqrt{1 + R^2\omega^2 C^2}} = \frac{1}{\sqrt{2}}$

Il faut donc que :

$R^2\omega^2 C^2 = 1$

et donc :

$\omega R C = 1$

Avec $\omega = 2\pi f$, il vient :

$2\pi f_g R C = 1$

Il en résulte pour la fréquence de coupure :

$f_g = \frac{1}{2\pi R C}$
</indepth>

[question:AD201] 
[question:AD202] 
[question:AD203] 

---

La réponse en fréquence en module d'un circuit oscillant série composé d'une résistance, d'une bobine et d'un condensateur, comme représenté sur la figure [ref:a_serienschwingkreis], se calcule d'après la formule suivante :
  
$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$

<margin>
[picture:181:a_serienschwingkreis:Circuit oscillant série]
</margin>

---

Lorsque la réactance de la bobine est exactement aussi grande que la réactance du condensateur, c'est-à-dire $X_\text{L} = X_\text{C}$, il en résulte pour l'impédance :

$Z=\sqrt{R^2+\left(0\right)^2}=\sqrt{R^2}=R$

Dans ce cas, il s'agit de ce qu'on appelle la *fréquence de résonance* $f_0$ du circuit oscillant, à laquelle l'impédance n'est plus déterminée que par la résistance ohmique. Aux fréquences supérieures et inférieures à la fréquence de résonance, l'impédance est plus grande que la résistance ohmique, car soit la bobine, soit le condensateur présente une réactance plus élevée. La figure [ref:a_serienschwingkreis_frequenzgang] montre la réponse en fréquence en module d'un circuit oscillant série, sur laquelle la fréquence de résonance se reconnaît nettement. Aux fréquences supérieures et inférieures à la fréquence de résonance, nous avons donc, pour le circuit oscillant série, une résistance totale (impédance) élevée dans les deux cas. À fréquence élevée, la bobine présente une résistance élevée. À basse fréquence, le condensateur présente une résistance élevée. 

<margin>
[picture:1037:a_serienschwingkreis_frequenzgang:Réponse en fréquence en module d'un circuit oscillant série]
</margin>

[question:AD206]
[question:AD207] 
[question:AD204] 

Pour les circuits oscillants parallèles et série, la relation suivante est donc vérifiée à la résonance, comme montré ci-dessus :

$X_\text{C} = X_\text{L}$

Si nous introduisons maintenant les formules des réactances de la bobine et du condensateur dans l'équation ci-dessus, nous obtenons :

$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$
  
On obtient ainsi la formule : 
  
$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$

---

Cette formule s'appelle la formule de Thomson et vaut aussi bien pour les circuits oscillants parallèles que série. Dans le recueil de formules, nous la trouvons au thème « Circuits oscillants ». Elle indique que la fréquence de résonance d'un circuit oscillant ne dépend que de l'inductance de la bobine et de la capacité du condensateur. Les résistances ohmiques et les pertes n'ont aucune influence sur la fréquence de résonance. Avec cette formule, nous pouvons calculer la fréquence de résonance des circuits oscillants. 

<indepth>
Les résistances ohmiques dans les circuits oscillants parallèles et série influent cependant sur le facteur de qualité ($Q$) et donc sur la bande passante ($B$) du circuit oscillant - nous y reviendrons plus précisément par la suite.
</indepth>


[question:AD208] 
[question:AD209]
[question:AD210] 

---

La fréquence de résonance des circuits oscillants parallèles se calcule exactement comme pour les circuits oscillants série avec la formule de Thomson mentionnée précédemment. 

[question:AD211] 
[question:AD212] 

---

Pour modifier la fréquence de résonance des circuits oscillants, on peut modifier soit l'inductance de la bobine, soit la capacité du condensateur du circuit oscillant.
Comme il ressort de la formule de Thomson, les grandeurs $L$ et $C$ se trouvent chacune sous la barre de fraction. De ce fait, une augmentation de $L$ ou de $C$ provoque une diminution de la fréquence du circuit oscillant, car le dénominateur de la formule devient plus grand. Pour une diminution de $L$ et de $C$, on a inversement que la fréquence de résonance du circuit oscillant augmente.

<indepth>
La racine carrée n'a aucune influence sur cette relation, car la racine d'un nombre plus grand est également un nombre plus grand. La relation n'est cependant pas linéaire.
</indepth>

L'inductance d'une bobine peut être augmentée en augmentant le nombre de spires, en resserrant les spires ou en introduisant un noyau de ferrite.
Inversement, l'inductance d'une bobine peut être diminuée en réduisant le nombre de spires, en écartant les spires, en retirant un noyau de ferrite ou en introduisant un noyau de cuivre. La capacité des condensateurs peut être influencée par remplacement ou par l'utilisation de condensateurs ajustables ou variables.

Fort de ces connaissances, nous pouvons maintenant répondre aux questions suivantes.

[question:AD213] 
[question:AD214] 
[question:AD215] 
[question:AD216] 
[question:AD217] 

Une combinaison de circuits oscillants parallèles et série peut, avec une disposition appropriée, être utilisée comme filtre passe-bande. À la résonance, les circuits oscillants parallèles se comportent comme des résistances de haute impédance et le circuit oscillant série comme une résistance de basse impédance.

[question:AD205]

La bande passante des filtres et des passe-bande est souvent indiquée par rapport à une certaine valeur d'atténuation. L'atténuation décrit alors dans quelle mesure un signal est affaibli par rapport au maximum de transmission.

Habituellement, la *bande passante* d'un filtre est définie par le point dit $\qty{-3}{\dB}$.

Au point $\qty{-3}{\dB}$, on a :

- Seule la moitié de la puissance passe encore le filtre
- La tension du signal représente encore environ $0{,}7$ fois la valeur maximale

La bande passante résulte de la différence entre la fréquence de coupure haute et la fréquence de coupure basse à $\qty{-3}{\dB}$ :

$ B = f_\mathrm{o} - f_\mathrm{u} $

[question:AD220]

Avec :

- $f_\mathrm{o}$ : fréquence de coupure haute
- $f_\mathrm{u}$ : fréquence de coupure basse

La bande passante à $\qty{-3}{\dB}$ est utilisée pour décrire l'aptitude d'un filtre à certains modes de trafic :

- Filtre à bande étroite d'environ $\qty{500}{\hertz}$ de bande passante : adapté à la CW (télégraphie)
- Filtre à bande plus large d'environ $\qty{2,7}{\kilo\hertz}$ de bande passante : adapté à la transmission de la parole en SSB

[question:AD221] 
[question:AD222]

Dans la question suivante, ce n'est pas le point $\qty{-3}{\dB}$ qu'il faut relever, mais la bande passante au point $\qty{-60}{\dB}$.

[question:AD219]

Le facteur de qualité d'un circuit oscillant (en anglais Q-Faktor) est déterminé par le rapport entre les réactances de la capacité et de l'inductance à la résonance et la résistance de pertes ohmique. Si un circuit oscillant ne comportait aucune résistance de pertes ohmique, son facteur Q serait infini. Les composants réels sont cependant toujours affectés de pertes. Les inductances ont toujours une résistance de pertes ohmique, les capacités ont des pertes diélectriques, qui se traduisent elles aussi par une résistance ohmique. Plus les résistances ohmiques dans un circuit oscillant sont élevées, plus son facteur Q est faible. Pour les filtres à facteur de qualité élevé et à flancs raides, on utilise fréquemment des filtres à quartz.

Pour le calcul du facteur Q, nous utilisons les formules correspondantes du recueil de formules, selon qu'il s'agit d'un circuit oscillant parallèle ou série :

Pour le circuit oscillant série, on a à la résonance ($X_\text{L} = X_\text{C}$) :

$Q = \frac{f_0}{B} = \frac{X_\text{L}}{R_\text{S}}$

Pour le circuit oscillant parallèle, on a à la résonance ($X_\text{L} = X_\text{C}$) :

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD225]


---

Conformément à l'exemple de calcul ci-dessus, nous pouvons maintenant aussi calculer le facteur de qualité du circuit oscillant parallèle. La fréquence de résonance se calcule comme dans l'exemple précédent. Il faut cependant veiller à utiliser, pour le calcul de $Q$, la formule du circuit oscillant parallèle :

$Q = \frac{f_0}{B} = \frac{R_\text{P}}{X_\text{L}}$

[question:AD226]

La bande passante des circuits oscillants parallèles et série se calcule maintenant elle aussi simplement à partir de la fréquence de résonance du circuit oscillant et de son facteur de qualité, comme suit (formule dans le recueil de formules) :

$Q = \frac{f_0}{B}$

En transformant la formule, on obtient la bande passante $B$ :

$B = \frac{f_0}{Q}$

La formule précédente vaut aussi bien pour le circuit oscillant série que pour le circuit oscillant parallèle !

[question:AD224]

De la même façon, la question suivante peut maintenant être calculée pas à pas avec les connaissances décrites précédemment.
[question:AD223]

---

Pour la transmission de signaux entre étages de montage ainsi que dans les filtres des émetteurs et des récepteurs, on utilise fréquemment des circuits oscillants couplés. Deux circuits oscillants y sont couplés l'un à l'autre de façon inductive ou capacitive. La figure [ref:a_gekoppelte_schwingkreise] montre un couplage inductif. Ce couplage peut, selon l'application, être 

- *lâche* (d),
- *sous-critique* (c),
- *critique* (b) ou 
- *surcritique* (a)

Le degré de couplage détermine l'influence mutuelle et donc la bande passante et la courbe de transmission de l'ensemble du dispositif.

<margin>
[picture:184:a_gekoppelte_schwingkreise:Couplage de circuits oscillants]
</margin>

Pour un couplage lâche et sous-critique, il n'y a pratiquement pas d'influence mutuelle ; en revanche, l'atténuation d'insertion du dispositif est relativement élevée et la bande passante relativement faible.

Pour un couplage critique, les deux circuits oscillants s'influencent juste assez pour qu'il en résulte une courbe de transmission plate dans la bande passante, avec une faible atténuation, et parfaitement plane dans la bande passante souhaitée (plateau). La bande passante du dispositif est ici plus grande que pour un couplage lâche et sous-critique. C'est aussi à cela qu'un couplage critique se reconnaît bien.

Pour un couplage surcritique, l'influence mutuelle des deux circuits oscillants est très forte, ce qui conduit à une forte modification des deux fréquences de résonance et donc à une grande bande passante. De ce fait, la courbe de transmission est fortement déformée dans la bande passante et il se forme, à gauche et à droite de la fréquence centrale, deux points de résonance. La courbe de transmission présente un « creux ». C'est à cela que le couplage surcritique se reconnaît bien.

[question:AD227] 
[question:AD228] 
[question:AD229] 