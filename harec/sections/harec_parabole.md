Au-delà d'environ $\qty{1}{\giga\hertz}$, dans le domaine des **micro-ondes**, la longueur d'onde ne mesure plus que quelques centimètres. On peut alors construire un réflecteur de plusieurs longueurs d'onde de diamètre : l'**antenne parabolique** [index:Antenne parabolique].

<margin>
[picture:850:harec_parabole_source:Réflecteur parabolique et sa source au foyer]
</margin>

Une surface métallique en forme de paraboloïde, pleine ou en grillage à mailles fines devant la longueur d'onde, renvoie les ondes parallèles vers un point, le **foyer**. On y place la **source**, ou antenne d'excitation : petit dipôle, **cornet** alimenté par un guide d'ondes, ou **antenne hélice** pour la polarisation circulaire. À l'émission, le chemin est inverse : la source éclaire le réflecteur, qui renvoie un faisceau étroit.

Le gain croît avec le diamètre **rapporté à la longueur d'onde** ; une parabole n'est utile qu'à partir de quelques longueurs d'onde de diamètre. Pour un diamètre $d$, une longueur d'onde $\lambda$ et un rendement d'éclairement $\eta$ (souvent $\num{0,5}$ à $\num{0,6}$) :

$g_\mathrm{i} = 10 \cdot \log_{10} \left[\left(\dfrac{\pi \cdot d}{\lambda}\right)^2 \cdot \eta \right]~\unit{\dBi}$

<tip>
**Méthode — gain d'une parabole.** Parabole de $\qty{1}{\meter}$ à $\qty{10}{\giga\hertz}$, $\eta = \num{0,6}$. Longueur d'onde : $300 \div 10000 = \qty{0,03}{\meter}$. Puis $\pi \times 1 \div \num{0,03} \approx 105$ ; au carré, $\approx \num{11000}$ ; fois $\num{0,6}$, $\approx \num{6600}$. Enfin $10 \cdot \log_{10}(6600) \approx \qty{38}{\dBi}$. Doubler le diamètre, ou la fréquence, ajoute $\qty{6}{\dB}$.
</tip>

Sur les ondes courtes, une parabole mesurerait des dizaines de mètres : elle est réservée aux bandes UHF et au-delà.
