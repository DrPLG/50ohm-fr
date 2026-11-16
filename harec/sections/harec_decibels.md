Gains d'amplificateurs, pertes de câbles, gains d'antennes : la radio manie des rapports qui vont de un millième à un million de millions. Le **décibel** [index:Décibel] (dB) les ramène à des nombres maniables, et transforme les multiplications en additions. Pour deux puissances $P_1$ (entrée) et $P_2$ (sortie) :

$g = 10 \cdot \log_{10}\left(\dfrac{P_2}{P_1}\right)~\unit{\dB}$

Un gain positif amplifie, un gain négatif atténue : $\qty{-3}{\dB}$ divise la puissance par deux. Pour un rapport de **tensions** sur une même résistance, la puissance variant comme le carré de la tension, on multiplie par 20 :

$g = 20 \cdot \log_{10}\left(\dfrac{U_2}{U_1}\right)~\unit{\dB}$

| c: dB | c: rapport de puissance | c: rapport de tension |
| $\num{0}$ | $\num{1}$ | $\num{1}$ |
| $\num{3}$ | $\num{2}$ | $\num{1,41}$ |
| $\num{6}$ | $\num{4}$ | $\num{2}$ |
| $\num{10}$ | $\num{10}$ | $\num{3,16}$ |
| $\num{20}$ | $\num{100}$ | $\num{10}$ |
| $\num{-3}$ | $\num{0,5}$ | $\num{0,71}$ |
| $\num{-10}$ | $\num{0,1}$ | $\num{0,32}$ |
[table:harec_db_rapports:Décibels à connaître par cœur]

<tip>
**Méthode — calculer de tête.** On décompose en briques connues, et on **ajoute** les décibels quand on **multiplie** les facteurs. $\qty{9}{\dB} = 6 + 3$, soit $4 \times 2 = 8$. $\qty{17}{\dB} = 20 - 3$, soit $100 \div 2 = 50$. $\qty{30}{\dB}$ : on cache le zéro, il reste 3, soit un facteur à trois zéros, $\num{1000}$. Dans l'autre sens, un facteur 40 vaut $4 \times 10$, soit $6 + 10 = \qty{16}{\dB}$.
</tip>

<attention>
Puissance ou tension ? Le même rapport de 2 vaut $\qty{3}{\dB}$ en puissance et $\qty{6}{\dB}$ en tension. Toujours se demander de quelle grandeur parle l'énoncé.
</attention>

---

Un décibel suivi d'une lettre exprime un **niveau absolu**, par rapport à une référence fixe : $\unit{\dBm}$ par rapport à $\qty{1}{\milli\watt}$, $\unit{\dBW}$ par rapport à $\qty{1}{\watt}$, $\unit{\dB\micro\volt}$ par rapport à $\qty{1}{\micro\volt}$. Ainsi $\qty{20}{\dBm} = 100 \times \qty{1}{\milli\watt} = \qty{100}{\milli\watt}$, et $\qty{0}{\dBW} = \qty{30}{\dBm}$. Le $\unit{\dBi}$ et le $\unit{\dBd}$ des antennes sont vus au chapitre *Antennes et lignes*.

<margin>
[picture:1053:harec_chaine_db:Chaîne de signal — amplificateurs et atténuateur]
</margin>

Dans une chaîne d'étages, on part du niveau d'entrée et on **additionne** gains et pertes. Exemple : $\qty{0}{\dBm}$ à l'entrée, un amplificateur de $\qty{10}{\dB}$, un atténuateur de $\qty{20}{\dB}$, un amplificateur de $\qty{10}{\dB}$ : $0 + 10 - 20 + 10 = \qty{0}{\dBm}$, soit $\qty{1}{\milli\watt}$ à la sortie.
