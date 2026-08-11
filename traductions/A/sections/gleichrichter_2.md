Comme cela a déjà été montré au chapitre « Redresseurs I » de la classe E, une diode seule ne laisse passer que l'alternance positive. Pour qu'il en résulte une tension continue utilisable, il faut en plus au moins un condensateur qui lisse la tension de sortie pulsée (voir le montage [ref:a_einweggleichrichtung_c]).

<margin>
[picture:795:a_einweggleichrichtung_c:Redressement simple alternance avec condensateur]
</margin>

---

Lors de l'alternance positive, la diode $D$ conduit et laisse circuler le courant. Pendant ce temps, le condensateur $C_L$ se charge à la valeur de crête de la tension alternative. Au moment de l'alternance négative, la diode $D$ bloque le courant et le condensateur $C_L$ se décharge à travers la résistance de charge $R_L$.

Il s'établit ainsi aux bornes de la résistance de charge $R_L$ une tension continue légèrement pulsée $U_L$ (cf. fig.[ref:a_Restwelligkeit]). Plus la capacité du condensateur est grande, plus la tension continue aux bornes de la résistance de charge est lissée de façon régulière.

<margin>
[picture:75:a_Restwelligkeit:Ondulation de la tension continue de sortie $U_L$]
</margin>

Lors du dimensionnement de la diode et du condensateur, nous devons toutefois savoir que les tensions du transformateur sont indiquées en tensions efficaces $U_{\mathrm{eff}}$. Nous devons donc déterminer au préalable la tension de crête $\hat{U}$.

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}}$

Si par exemple la tension $U_a = \qty{15}{\volt}$ est indiquée sur un transformateur, nous calculons :

$\hat{U} = \sqrt{2} \cdot U_{\mathrm{eff}} = \sqrt{2} \cdot \qty{15}{\volt} = \qty{21,21}{\volt}$

Il s'établira donc à vide une tension de crête à vide d'environ $\qty{21}{\volt}$.

[question:AD302]

Pour la question suivante, nous devons appliquer le rapport de transformation du transformateur afin de déterminer notre tension de sortie. Nous prenons donc, pour la tension d'entrée efficace $U_{\mathrm{eff}}$, un vingtième de la tension d'entrée du transformateur de $\qty{230}{\volt}$. Nous pouvons ensuite ajouter encore à la tension de crête la moitié de la tension afin de tenir compte de la marge de sécurité.

[question:AD303]

Pour résoudre l'exercice suivant, nous devons reconnaître que la valeur de crête de l'alternance négative et la tension du condensateur s'additionnent et sollicitent la diode en sens inverse. C'est la tension la plus élevée qui peut apparaître aux bornes de la diode en sens inverse.

Nous calculons : $U_{\mathrm{inv}} = 2 \cdot \hat{u}$
Il faut ensuite encore tenir compte du rapport de transformation $5 : 1$  du transformateur d'alimentation et de la marge de sécurité de $\qty{20}{\percent}$.

[question:AD304]

%TODO Simulation einbauen: https://tinyurl.com/22m65xlw