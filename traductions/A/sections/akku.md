Outre les accumulateurs au plomb (Pb) et les accumulateurs nickel-hydrure métallique (NiMH) bien connus, nous recourons de plus en plus, en technique radio, par ex. en trafic portable, aux accumulateurs lithium-fer-phosphate (LiFePO4). Examinons pour cela d'abord un accumulateur et ses inscriptions sur la figure [ref:a_akku_lifepo4].

<margin>
[photo:175:a_akku_lifepo4:LiFePO4]
</margin>

<indepth>
* Capacité : $\qty{4200}{\milli\ampere\hour}$
* Tension : 4S1P / $\qty{13,2}{\volt}$
% * Entladung: 30C Constant / 40C Burst
% * Balance Stecker: JST-XH
% * Entlastung Stecker: $\qty{5.5}{\milli\meter}$ Kugel-Stecker

Les caractéristiques les plus importantes pour nous sont la tension nominale de $\qty{13,2}{\volt}$ et l'interconnexion 4S1P. Cela signifie que la tension nominale de $\qty{13,2}{\volt}$ résulte de 4 éléments en série et 1 fois en parallèle, donc les 4 sont montés en série. Habituellement, les LiFePO4 possèdent une tension nominale de cellule de $\qty{3,2}{\volt}$ à $\qty{3,3}{\volt}$. On obtient donc $\qty{3,3}{\volt} \cdot 4 = \qty{13,2 }{\volt} \cdot 1 = \qty{13,2}{\volt}$.

Dans un 4S2P, 8 cellules au total sont montées. 4 en série et cela 2 fois en parallèle. Cela donnerait alors une tension de $\qty{13,2}{\volt}$ mais une capacité de $\qty{8400}{\milli\ampere\hour}$.

</indepth>

Pour l'accumulateur pris en exemple, $\qty{4200}{\milli\ampere\hour}$ sont indiqués comme capacité nominale. La capacité nominale d'accumulateur $Q$ est aussi désignée comme la charge et s'exprime en $\unit{\ampere\hour}$ ou en $\unit{\milli\ampere\hour}$.

Pour notre accumulateur pris en exemple, cela correspond à $\qty{4,2}{\ampere\hour}$. Cela signifierait théoriquement que nous pouvons charger notre accumulateur pendant $\qty{1}{\hour}$ avec $\qty{4,2}{\ampere}$ ou pendant $\qty{2}{\hour}$ avec $\qty{2,1}{\ampere}$, etc.Cela se décrit par la formule :

$t=\frac{Q}{I}$

$t=\frac{\qty{4,2}{\ampere\hour}}{\qty{4,2}{\ampere}} = \qty{1}{\hour}$

[question:AB210]

Mais nous voulons maintenant aussi savoir quelle quantité d'énergie électrique est stockée dans l'accumulateur. L'énergie ($\unit{\watt\hour}$) est la charge $Q$ ($\unit{\ampere\hour}$) de l'accumulateur multipliée par la tension totale $U$ en volts.

$\qty{1}{\watt\hour} = \qty{1}{\ampere\hour} \cdot \qty{1}{\volt}$

Pour notre exemple, nous calculons $\qty{4,2}{\ampere\hour} \cdot \qty{13,2}{\volt} = \qty{55,44}{\watt\hour}$ comme énergie stockée.

[question:AB501]

%Die Entladung dieses Akkus kann mit einem konstanten Entladestrom von "30 C" erfolgen. Das bedeutet, dass der Akku mit 30 $\cdot$ Kapazität $Q$ entladen werden kann.
%
%Endladestrom: $I = 30 \cdot \qty{4200}{\milli\ampere} = \qty{126}{\ampere}$
%
%Das ist allerdings nur ein theoretisch möglicher Wert, da unser Akku somit innerhalb von $\qty{108}{\second}$ entladen wäre. Auch der Kabelquerschnitt ist dabei zu berücksichtigen.
%

Lors du montage en série d'accumulateurs, comme sur la figure [ref:a_akku_4S1P], les tensions s'additionnent et la capacité reste identique. 
Lors du montage en parallèle, comme sur la figure [ref:a_akku_4S2P], la tension reste identique et les capacités s'additionnent. 

<margin>
% TODO Bild Reihenschaltung liegt bei DG1HXJ als .tex
[photo:176:a_akku_4S1P:Montage en série]
</margin>

<margin>
% TODO Bild Parallelschaltung liegt bei DG1HXJ als .tex
[photo:177:a_akku_4S2P:Montage en parallèle]
</margin>

<attention>
Lors de l'utilisation d'un LiFePO4 monté en 4S1P, note que des tensions comprises entre $\qty{10}{\volt}$ et $\qty{14,4}{\volt}$ peuvent être présentes. Tous les appareils radio ne peuvent pas fonctionner avec ces tensions. Il est également important de ne monter ensemble que des cellules/accumulateurs de mêmes caractéristiques, car les cellules s'influencent mutuellement et peuvent sinon être endommagées. En particulier avec les accumulateurs au lithium actuels, il est judicieux d'installer un dispositif de surveillance (équilibreur, moniteur de batterie). Celui-ci assure entre autres l'équilibrage nécessaire des tensions de cellules et une charge optimale.
</attention>

---


% In der Abb. [ref:a_akku_lifepo4_anschluss]
% TODO Bild Infobox Anschluss Akku liegt bei DG1HXJ als .tex
%<margin>
%[photo:178:a_akku_lifepo4_anschluss:LiFePO4 Anschlüsse]
%</margin>

Pour résoudre la question suivante, il faut savoir que la tension totale correspond à la somme des tensions de cellules. La charge totale correspond en revanche à la charge d'une seule cellule.

[question:AB209]

Pour la question suivante, il faut d'abord déterminer la quantité de charge extractible de $\qty{90}{\percent}$.
Le temps de décharge $t$ s'obtient par : $t=\frac{Q}{I}$

[question:AB211]
