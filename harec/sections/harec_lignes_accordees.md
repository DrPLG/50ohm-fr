L'onde met un certain temps à parcourir une ligne : entre ses deux bouts apparaît un **déphasage**, proportionnel à la longueur **électrique**. Une longueur d'onde correspond à $\qty{360}{\degree}$.

| l: Longueur électrique | l: Déphasage |
| $\lambda/4$ | $\qty{90}{\degree}$ |
| $\lambda/2$ | $\qty{180}{\degree}$ |
| $3\lambda/4$ | $\qty{270}{\degree}$ |
| $\lambda$ | $\qty{360}{\degree}$ |
[table:harec_dephasage:Déphasage selon la longueur de ligne]

---

Sur une ligne qui n'est pas fermée sur son impédance caractéristique, l'onde se réfléchit au bout. Onde directe et onde réfléchie forment des **ondes stationnaires** : des ventres et des nœuds de courant et de tension, fixes, qui alternent tous les $\lambda/4$. C'est le principe de la **ligne de Lecher** [index:Ligne de Lecher], deux conducteurs parallèles.

<margin>
[picture:1112:harec_lecher_ouverte:Ligne de Lecher à extrémité ouverte]
</margin>

* **Bout ouvert** : le courant y est nul et la tension maximale, l'impédance est infinie. À $\lambda/4$ du bout, c'est l'inverse : courant maximal, tension nulle, impédance quasi nulle.
* **Bout en court-circuit** : la tension y est nulle et le courant maximal, l'impédance est nulle. À $\lambda/4$ du bout, l'impédance devient très grande.

<margin>
[picture:1111:harec_lecher_court_circuit:Ligne de Lecher à extrémité court-circuitée]
</margin>

D'où trois règles à retenir :

* une ligne de $\lambda/2$ **répète** à son entrée l'impédance qui la termine ;
* une ligne de $\lambda/4$ **inverse** : un circuit ouvert devient un court-circuit, et un court-circuit un circuit ouvert ;
* une ligne $\lambda/4$ ouverte se comporte à son entrée comme un **circuit résonant série**, une ligne $\lambda/4$ en court-circuit comme un **circuit résonant parallèle**.

Ces lignes accordées servent de circuits résonants en VHF et UHF, et leur longueur fixe la fréquence de résonance : une ligne plus longue résonne plus bas.
