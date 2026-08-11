Les condensateurs sont utilisés dans de nombreuses applications en montage série, en montage parallèle ou encore en montage mixte. Le montage en parallèle est plus facile à comprendre ; nous l'examinons donc en premier.

Avec le montage en parallèle, davantage de plaques se font face et la surface des plaques augmente donc proportionnellement. La capacité de l'ensemble du montage augmente en conséquence.

<margin>
[picture:822:e_3C-parallel: Montage en parallèle de 3 condensateurs]
</margin>

---

Pour un montage en parallèle de condensateurs de même valeur, la capacité double, la tenue en tension reste identique. On peut bien sûr calculer la capacité totale. Nous trouvons la formule dans le formulaire :

$C_{\mathrm{ges}} = C_{1} + C_{2} + C_{3} + \dots$

<tip>
La capacité totale est, dans un montage en parallèle, toujours supérieure à la plus petite des capacités individuelles.
</tip>

Dans l'exercice suivant se présente une difficulté supplémentaire, car les préfixes des valeurs de capacité sont différents. Il faut d'abord convertir toutes les valeurs vers un préfixe commun. Les nombres ne doivent devenir ni trop grands ni trop petits ; il est donc recommandé de choisir le préfixe nano ($\unit{\nano}$). 

$\begin{split} \qty{0,1}{\micro\farad} &= \qty{100}{\nano\farad} \\ \qty{50000}{\pico\farad} &= \qty{50}{\nano\farad}\end{split}$

Il ne reste plus qu'à additionner toutes les valeurs en $\unit{\nano\farad}$.

[question:ED117]

<margin>
[photo:262:a_Netzteil BEKO PA $7 \times \qty{10000}{\micro\farad}$ parallel: Montage en parallèle de $7 \times \qty{10000}{\micro\farad}$ dans une alimentation d'étage de puissance]
</margin>

L'exercice suivant peut servir de test de compréhension.

[question:ED118]


---

Pour un montage en série de condensateurs, comme le montre la figure [ref:e_3C-parallel], la tenue en tension augmente, mais la capacité diminue. On peut bien sûr, là encore, calculer la capacité totale. Celle-ci est très similaire au montage en parallèle de résistances :

$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{C_{1}} + \frac{1}{C_{2}} + \frac{1}{C_{3}}$

<margin>
[picture:823:e_3C-parallel:Montage en série de 3 condensateurs] 
</margin>

<tip>
La capacité totale est, dans un montage en série, toujours inférieure à la plus petite des capacités individuelles.
</tip>

<tip>
Pour la résolution des exercices, la démarche suivante est recommandée :
  
1. Esquisse le montage
2. Inscris les valeurs de capacité à côté des composants.
3. Convertis vers des préfixes identiques.
4. Simplifie le montage en regroupant les groupes de montage de même nature
5. Calcule pas à pas la capacité totale
</tip>

Si tous les condensateurs ont la même valeur de capacité, on peut calculer facilement la capacité totale en divisant une capacité individuelle par 3. Dans l'exercice suivant, on calcule $\qty{0,33}{\micro\farad} / 3 = \qty{0,11}{\micro\farad}$.

[question:ED119]

Dans le montage en série de condensateurs de l'exercice suivant, on trouve comme préfixes $\unit{\micro\farad}$ et $\unit{\nano\farad}$. Il est très judicieux de convertir d'abord $\qty{200000}{\nano\farad}$ en $\qty{200}{\micro\farad}$. Pour un montage en série, on peut alors appliquer la formule du formulaire.


$C_{\mathrm{ges}} =\frac{1}{\frac{1}{\qty{100}{\micro\farad}} + \frac{1}{\qty{50}{\micro\farad}} + \frac{1}{\qty{100}{\micro\farad}}}$

[question:ED120]

---
  
Dans la question suivante, 3 condensateurs sont combinés en montage série et parallèle. 

[question:ED121]

Quelle partie du montage peut être simplifiée en premier ? Exact : le montage en série.
Ce sous-groupe a pour capacité totale la moitié de $\qty{10}{\nano\farad}$, soit $\qty{5}{\nano\farad}$. Il est maintenant plus facile de poursuivre le calcul, car dans un montage en parallèle les valeurs de capacité s'additionnent. Félicitations pour le résultat de $\qty{10}{\nano\farad}$.

Les autres exercices sont similaires et faciles à résoudre.

[question:ED122]
[question:ED123]
[question:ED124]

%<margin>
%
%Lösungshilfen:
%
%*ED 118:* Reihenschaltung von $\qty{22}{\nano\farad}$, $\qty{0,033}{\micro\farad} = \qty{33}{\nano\farad}$ und $\qty{15000}{\pico\farad} = \qty{15}{\nano\farad}$.
%$\frac{1}{C_{\mathrm{ges}}} = \frac{1}{\qty{22}{\nano\farad}} + \frac{1}{\qty{33}{\nano\farad}} + \frac{1}{\qty{15}{\nano\farad}}$
%Eigentlich muss man nicht rechnen, denn es gibt nur ein Ergebnis, das kleiner als $\qty{15}{\nano\farard}$ ist.
%*ED 120:* $\qty{50}{\micro\farad}$ 
%*ED 122:* $C_2 = \qty{1}{\micro\farad}$ und $C_3 = \qty{1}{\micro\farad}$ in Parallelschaltung ergibt zusammen $\qty{2}{\micro\farad}$. Dazu $C_1 = \qty{2}{\micro\farad}$ in Reihe %ergibt die Hälfte , also $\qty{1}{\micro\farad}$.
% 
%*ED 123:* $C_2 = \qty{4}{\nano\farad}$ und $C_3 = \qty{4}{\nano\farad}$ in Parallelschaltung ergibt zusammen $\qty{8}{\nano\farad}$. Dazu $C_1 = \qty{8}{\nano\farad}$ in Reihe %ergibt die Hälfte , also $\qty{4}{\nano\farad}$.
%  
%*ED 124:* $C_2 = \qty{100}{\nano\farad}$ und $C_3 = \qty{100000}{\pico\farad} = \qty{100}{\nano\farad}$ in Parallelschaltung ergibt zusammen $\qty{200}{\nano\farad}$. Dazu %$C_1 = \qty{200}{\nano\farad}$ in Reihe ergibt die Hälfte , also $\qty{100}{\nano\farad}$.
%</margin>
