On peut alimenter un dipôle demi-onde **à une extrémité** au lieu du centre : c'est l'antenne **alimentée en bout** [index:Antenne alimentée en bout], en anglais *end-fed half wave* (EFHW). Le fil est plus facile à tendre, et l'arrivée du câble se fait au bout, souvent près de la maison.

L'extrémité d'un demi-onde est un ventre de tension : l'impédance y est **très élevée**, de l'ordre de $\num{2000}$ à $\qty{2500}{\ohm}$. Il faut un **adaptateur** pour la ramener aux $\qty{50}{\ohm}$ du câble. Trois solutions classiques :

* le **circuit de Fuchs** [index:Circuit de Fuchs] : un circuit résonant parallèle accordé sur la fréquence de travail, qui élève l'impédance et compense la partie réactive ;
* un **transformateur 1:49** (unun) : un rapport de spires de $1:7$ donne un rapport d'impédances de $1:7^2 = 1:49$, soit $\qty{50}{\ohm}$ ramenés à $\qty{2450}{\ohm}$ ;
* une **ligne bifilaire $\lambda/4$** : c'est l'**antenne Zeppelin** [index:Antenne Zeppelin], qui doit son nom aux dirigeables, où elle éloignait la haute tension de l'enveloppe remplie de gaz.

<margin>
[picture:310:harec_circuit_fuchs:Circuit de Fuchs pour un demi-onde alimenté en bout]
</margin>

<attention>
Dans un transformateur, le rapport des **impédances** est le **carré** du rapport des spires. Les baluns et ununs sont presque toujours désignés par leur rapport d'impédances : un « unun 1:49 » a un rapport de spires de $1:7$.
</attention>

---

Comme tout dipôle, l'antenne alimentée en bout a besoin d'un **contrepoids**. Le courant au point d'alimentation étant faible, un fil court suffit, d'au moins un vingtième de longueur d'onde, ou un morceau du blindage du câble. Pour que le reste du câble ne rayonne pas, on place un **bloqueur d'ondes de gaine** à la distance voulue.

<margin>
[picture:315:harec_efhw_contrepoids:Demi-onde alimenté en bout avec court contrepoids]
</margin>

Il ne faut pas confondre cette antenne avec l'**antenne long fil** [index:Antenne long fil], alimentée en bout elle aussi, mais nettement plus longue qu'une longueur d'onde.
