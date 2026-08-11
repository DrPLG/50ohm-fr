En de nombreux points de la technique haute fréquence, les rapports de puissance jouent un rôle important, par exemple pour le gain d'une antenne ou d'un amplificateur, ou pour l'atténuation d'un câble. En classe N, nous avons encore découvert ces relations sous la forme de simples facteurs, par exemple : « L'antenne a un gain de facteur $2$ ».

Ces rapports peuvent prendre des valeurs numériques très grandes ou très petites. Ainsi, un récepteur d'ondes courtes possède par exemple un facteur d'amplification total de $\num{1000000000000}$, soit un un suivi de douze zéros. Avec de tels nombres, le calcul devient vite peu lisible, et l'on se met inévitablement à compter les zéros.

En simplifiant, il existe toutefois un outil mathématique pour ce « comptage des zéros » : les logarithmes. Grâce à eux, on peut en outre transformer les multiplications en additions et les divisions en soustractions. Cela rend très simple le calcul avec de grands nombres.

---

Il est donc devenu d'usage d'indiquer les rapports de puissance sur une échelle logarithmique.
Le logarithme est l'opération inverse de l'élévation à une puissance. En radioamateurisme, nous utilisons en règle générale le logarithme décimal (« logarithme en base dix ») de base $10$ :

---

$a =\log_{10} (b)$, si $b=10^{a}$

Le logarithme de $100$ vaut $\log_{10}(100)=2$, car $10^2 = 100$. Autrement dit : le nombre $100$ possède deux zéros.

<warning>
Une calculatrice technique et scientifique propose, à côté du logarithme décimal (inscription $\lg$ ou $\log$), aussi le logarithme naturel *$\ln$*, qui a pour base le nombre d'Euler *$e=\num{2,7182818}\dots$*. À ne pas confondre !
</warning>	

<margin>
| c:dB | c:≈ facteur de puissance |
| $0$ | $1$ |
| $1,5$ | $\sqrt{2} = 1,41$ |
| $2,15$ | $1,64$ |
| $3$ | $2$ |
| $5$ | $\sqrt{10} = 3,16$ |
| $6$ | $4$ |
| $10$ | $10$ |
| $20$ | $100$ |
[table:e_dezibel_leistungsfaktoren:Facteurs de puissance importants en $\unit{\dB}$]
</margin>

Du logarithme décimal est dérivé le *bel* ($\unit{\bel}$). Ce nom rend hommage à l'enseignant américain pour sourds et pionnier du téléphone, *Alexander Graham Bell*. Dans l'exemple ci-dessus, nous aurions aussi pu écrire :

$\log_{10}(b)=\qty{a}{\bel}$

En règle générale, on utilise plutôt le *décibel* (symbole d'unité $\unit{\dB}$) que le bel, c'est-à-dire le dixième d'un bel :

$10 \cdot \log_{10}(b) = \qty{a}{\dB}$

---

Le formulaire donne, pour convertir un rapport de puissance, la formule suivante :

$g = 10\cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$

où $P_1$ correspond à la puissance d'entrée et $P_2$ à la puissance de sortie. Supposons maintenant que nous ayons un amplificateur qui amplifie la puissance d'entrée $P_1=\qty{50}{\watt}$ jusqu'à $P_2=\qty{100}{\watt}$, c'est-à-dire qui la double. D'après notre formule, il en résulte le facteur d'amplification suivant en $\unit{\dB}$ :

$g = 10\cdot \log_{10}\left(\frac{\qty{100}{\watt}}{\qty{50}{\watt}}\right)\unit{\dB} = 10\cdot \log_{10}\left(2\right)\unit{\dB} = 10\cdot \qty{0.301}{\dB} \approx \qty{3}{\dB} $

Pour la classe E, il suffit dans un premier temps de connaître la valeur en décibels correspondant au facteur de puissance $2$. Le formulaire contient à ce sujet un tableau, également reproduit dans le tableau [ref:e_dezibel_leistungsfaktoren]. On peut y lire qu'un facteur de puissance de $2$ correspond à une valeur de $\qty{3}{\dB}$. Le calcul détaillé avec des valeurs en décibels n'est traité qu'en classe A.

<tip>
On peut estimer sans aucune calculatrice les valeurs en décibels qui se terminent par « $0$ » : il suffit de cacher le dernier zéro ; le chiffre indique alors le nombre de zéros du facteur de rapport. Exemple : $\qty{30}{\dB} \rightarrow 3 \rightarrow 3~\text{zéros} \rightarrow \text{facteur de rapport}~1000$ !
</tip>

[question:EA107]

Outre l'unité $\unit{dB}$, on rencontre souvent en pratique des indications comme $\unit{\dBi}$, $\unit{\dBm}$, $\unit{\dBW}$ ou $\unit{\dBu}$. Ces compléments indiquent la grandeur de référence à laquelle se rapporte la valeur en décibels concernée. En classe E, ce sont surtout les indications $\unit{\dBi}$ et $\unit{\dBd}$ que nous rencontrerons dans le chapitre sur les antennes. Les autres grandeurs comme $\unit{\dBm}$ et $\unit{\dBW}$ ne seront nécessaires qu'en classe A.
