Dans un câble, une partie de la puissance se perd en chaleur : c'est l'**affaiblissement linéique** [index:Affaiblissement linéique], donné en décibels pour $\qty{100}{\meter}$ sur la fiche du câble. Il **croît avec la fréquence** et il est **proportionnel à la longueur** : $\qty{25}{\meter}$ d'un câble qui perd $\qty{8}{\dB}$ aux $\qty{100}{\meter}$ perdent $\qty{2}{\dB}$. Les connecteurs ajoutent leurs propres pertes. Un amplificateur ou une antenne à gain compensent le signal perdu, mais ne diminuent pas les pertes du câble.

| c: dB | c: facteur de puissance |
| $\num{1}$ | $\num{1,26}$ |
| $\num{3}$ | $\num{2}$ |
| $\num{6}$ | $\num{4}$ |
| $\num{10}$ | $\num{10}$ |
| $\num{20}$ | $\num{100}$ |
[table:harec_decibels:Décibels et facteurs de puissance à retenir]

<tip>
**Méthode — pertes d'un câble.** Un émetteur de $\qty{100}{\watt}$ alimente $\qty{30}{\meter}$ d'un câble qui perd $\qty{10}{\dB}$ aux $\qty{100}{\meter}$ : $10 \times 30 \div 100 = \qty{3}{\dB}$, soit un facteur 2. Il reste $\qty{50}{\watt}$ à l'antenne. Les décibels s'additionnent quand les facteurs se multiplient : $\qty{6}{\dB}$, c'est deux fois $\qty{3}{\dB}$, donc un facteur 4.
</tip>

---

Même sans câble, une onde s'affaiblit en s'éloignant de l'émetteur, car sa puissance se répartit sur une sphère de plus en plus grande : c'est l'**affaiblissement en espace libre** [index:Affaiblissement en espace libre]. Pour une distance $d$ en kilomètres et une fréquence $f$ en mégahertz :

$A = \qty{32,45}{\dB} + 20\cdot\log_{10}(f) + 20\cdot\log_{10}(d)$

Deux règles suffisent souvent : **doubler la distance ajoute $\qty{6}{\dB}$** d'affaiblissement, et **décupler la distance en ajoute $\num{20}$**. Il en va de même pour la fréquence.

<tip>
**Méthode — sans touche « log ».** À $\qty{145}{\mega\hertz}$, l'affaiblissement vaut environ $\qty{76}{\dB}$ à $\qty{1}{\kilo\meter}$. À $\qty{10}{\kilo\meter}$, on ajoute $\qty{20}{\dB}$ : $\qty{96}{\dB}$. À $\qty{20}{\kilo\meter}$, encore $\qty{6}{\dB}$ : $\qty{102}{\dB}$.
</tip>
