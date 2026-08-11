Les postes radio doivent parfois être réalignés, par exemple après une réparation ou lorsque des composants ont dérivé avec le vieillissement. Pour les récepteurs, l'alignement comprend le contrôle des fréquences des oscillateurs. On utilise habituellement pour cela un fréquencemètre (compteur de fréquence).

[question:EI501]

La figure [ref:e_frequenzzaehler1] montre l'afficheur d'un fréquencemètre. Le trois détaché tout à droite représente, comme sur certaines calculatrices, $\num{10^3}$. Le compteur mesure donc la fréquence $\qty{455}\cdot \qty{10^3}{\hertz}$, soit $\qty{455}{\kilo\hertz}$. Les appareils de mesure plus récents affichent directement le préfixe d'unité au lieu de la puissance de dix.

<margin>
[photo:187:e_frequenzzaehler1:Afficheur d'un fréquencemètre indiquant $\qty{455}\cdot \qty{10^3}{\hertz}$]
</margin>

% Ich hab das mal aus Platzgründen entfernt
%<margin> 
%[photo:189:e_frequenzzaehler2:Multimeter, das im Frequenzmessbereich $\qty{455}{\kilo\hertz}$ anzeigt. Darüber erscheinen ein Symbol für niedrige %Batteriespannung, die Luftfeuchtigkeit und die Temperatur. Diese Werte haben nichts mit der Frequenzmessung zu tun.]
%</margin>

<indepth>
La fréquence $\qty{455}{\kilo\hertz}$ est très courante comme fréquence intermédiaire des récepteurs superhétérodynes et peut être mesurée lorsque le récepteur est accordé sur un signal fort.
</indepth>

---

Dans les instructions d'alignement, il est souvent exigé de régler une fréquence avec une précision donnée, par exemple $\pm\qty{10}{\hertz}$. Dans de tels cas, il est utile de se représenter le poids de chacun des chiffres. La puissance de dix affichée par l'appareil de mesure, c'est-à-dire pour $\qty{455}{\kilo\hertz}$ la valeur $\num{10^3}$ ou $\num{1000}$, s'applique toujours au chiffre situé juste avant la virgule. Le chiffre à sa gauche vaut alors $\qty{10}{\kilo\hertz}$ ou $\qty{10^4}{\hertz}$, et le chiffre encore un cran plus à gauche, le quatre dans l'exemple, $\qty{100}{\kilo\hertz}$ ou $\qty{10^5}{\hertz}$. Vers la droite, on va dans l'autre sens.

 La figure [ref:e_frequenzzaehler_stellen] montre un exemple avec une fréquence plus élevée.
  
<margin>
[picture:793:e_frequenzzaehler_stellen:Cet affichage représente une fréquence en $\unit{\mega\hertz}$. C'est aussi le poids du chiffre situé avant la virgule.]
</margin>

<attention>
Les entrées des fréquencemètres peuvent avoir une résistance interne élevée. Nous connaissons cela des voltmètres et des oscilloscopes. Mais il existe aussi des entrées en $\qty{50}{\ohm}$. Elles sont le plus souvent particulièrement sensibles, et la valeur maximale de tension ou de puissance indiquée dans le manuel d'utilisation du compteur ne doit en aucun cas être dépassée.
</attention>

[question:EI502]
[question:EI503]

Les fréquencemètres sont construits pour une plage de valeurs déterminée, par exemple de $\qty{100}{\kilo\hertz}$ à $\qty{2}{\giga\hertz}$. En dehors de cette plage, ils mesurent de façon imprécise, ou pas du tout. Pour mesurer des fréquences plus élevées, il existe des diviseurs de fréquence. Ils divisent la fréquence d'un signal appliqué à leur entrée par une valeur fixe et restituent le résultat en sortie sous forme d'oscillation électrique. On les appelle aussi prédiviseurs, parce qu'ils s'intercalent entre l'objet mesuré et le compteur.

%TODO Bild Frequenzteiler

Souvent, les prédiviseurs divisent la fréquence par dix. Si l'on applique $\qty{2,4}{\giga\hertz}$ à l'entrée d'un tel diviseur 10:1, le fréquencemètre placé derrière affiche $\qty{240}{\mega\hertz}$.

[question:EI504]