Un dipôle simple ne sert que sur une bande et ses multiples impairs. Pour couvrir plusieurs bandes avec un seul fil, on insère dans chaque brin un **circuit bouchon** [index:Circuit bouchon] : un circuit résonant **parallèle**, bobine et condensateur, appelé **trappe** (*trap* en anglais). C'est le **dipôle à trappes** [index:Dipôle à trappes].

<margin>
[picture:1036:harec_circuit_bouchon:Réponse d'un circuit résonant parallèle autour de sa fréquence de résonance]
</margin>

Un circuit parallèle présente une **impédance très élevée à sa fréquence de résonance** $f_\mathrm{res}$. Son effet sur le dipôle dépend de la fréquence de travail $f$ :

| l: fréquence de travail | l: la trappe se comporte comme | l: effet sur le dipôle |
| $f = f_\mathrm{res}$ | un **circuit bouchon** | le courant s'arrête à la trappe, le dipôle s'arrête là |
| $f < f_\mathrm{res}$ | une **bobine** | le dipôle entier travaille, électriquement allongé |
| $f > f_\mathrm{res}$ | un **condensateur** | électriquement raccourci |
[table:harec_trappes:Comportement d'une trappe selon la fréquence]

---

Exemple d'un dipôle bibande $\qty{40}{\meter}$ et $\qty{80}{\meter}$ : les trappes sont accordées sur $\qty{7}{\mega\hertz}$.

* Sur $\qty{7}{\mega\hertz}$, elles bloquent : seule la partie **entre les deux trappes** travaille, et sa longueur est celle d'un demi-onde pour $\qty{7}{\mega\hertz}$.
* Sur $\qty{3,5}{\mega\hertz}$, elles agissent comme des bobines d'allongement : **tout le fil** travaille, et il peut donc être un peu plus court qu'un demi-onde pour $\qty{80}{\meter}$.

Avec plusieurs paires de trappes, on couvre davantage de bandes. La paire **la plus proche du centre** est accordée sur la fréquence **la plus haute**, car c'est elle qui demande le dipôle le plus court ; chaque paire suivante, vers l'extérieur, sur la bande immédiatement inférieure.

Les trappes servent aussi sur les éléments des antennes Yagi multibandes.
