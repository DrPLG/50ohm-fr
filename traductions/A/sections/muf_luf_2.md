La *MUF* (*maximum usable frequency*), c'est-à-dire la fréquence la plus élevée que l'ionosphère peut encore renvoyer par réfraction pour la distance entre émetteur et récepteur, nous l'avons déjà rencontrée dans la classe E. Il y était apparu que la MUF dépend de la densité des électrons libres dans la région réfractante. Dans la classe A, nous allons maintenant examiner ce sujet de plus près, en particulier sous l'angle de l'angle de rayonnement.

[question:AH206]
[question:AH207]

Comme nous le savons aussi déjà, la portée des ondes d'espace dépend de l'angle de rayonnement. Plus l'onde frappe l'ionosphère de manière rasante, plus la réfraction se produit facilement. Cette relation vaut aussi pour la MUF : la fréquence tout juste encore renvoyée, la *MUF*, est d'autant plus élevée que notre signal pénètre dans l'ionosphère de manière rasante. La figure [ref:e_muf_winkel2] montre une simulation de la distance de saut pour un jour d'été de l'année 2024 pour un signal radioamateur autour de $\qty{7}{\mega\hertz}$. À $\qty{45}{\degree}$, la MUF était ce jour-là de $\qty{7,5}{\mega\hertz}$. Si l'on modifie l'angle de rayonnement, la MUF change elle aussi : si l'on rayonne plus haut (p. ex. $\qty{60}{\degree}$), la MUF baisse et l'onde radio n'est plus réfractée. Si l'on rayonne au contraire plus bas (p. ex. $\qty{30}{\degree}$), la MUF augmente. Nous allons examiner cette relation plus précisément dans ce qui suit.

<margin>
[picture:998:e_muf_winkel2:Distance de saut à 7 MHz à l'été 2024]
</margin>

---

Les stations de mesure ionosphérique mesurent ce qu'on appelle la fréquence critique $f_\text{c}$ (ou souvent aussi $f_\text{k}$, $f_\text{krit}$ ou $f_\text{oF2}$). C'est la fréquence la plus élevée pour laquelle l'onde d'espace pénétrant verticalement dans l'ionosphère est tout juste encore réfléchie (cf. figure [ref:e_muf_winkel]). Si nous rayonnons verticalement vers le haut, c'est-à-dire si notre signal pénètre dans l'ionosphère sous un angle de $\qty{90}{\degree}$, la MUF est à son minimum, car notre signal doit alors « faire complètement demi-tour » dans l'ionosphère, c'est-à-dire accomplir un virage à 180°. Cela signifie qu'à $\qty{90}{\degree}$, on a $f_\text{c} = MUF$. 

<indepth>
Comme symbole de grandeur, on utilise $f_o$ (petite lettre « O » en indice pour *ordinary wave*) suivie de la région ionosphérique à laquelle cette fréquence s'applique, donc p. ex. $f_\text{oF2}$ pour la région F2. Cependant, $f_\text{c}$, $f_\text{k}$ ou $f_\text{krit}$ sont aussi souvent utilisés comme symboles.
</indepth>

<margin>
[picture:870:e_muf_winkel:Les angles pour le calcul de la MUF]
</margin>

<indepth>
La fréquence critique est donc la fréquence la plus élevée qui revient de l'ionosphère lorsqu'on rayonne verticalement vers le haut. Une règle empirique dit que la fréquence la plus élevée encore renvoyée pour une incidence *rasante* vaut environ le triple de la fréquence critique.
</indepth>

[question:AH204]
[question:AH205]

---

La figure [ref:e_muf_fof2] montre l'évolution temporelle de la MUF et de $f_\text{c}$ le 08.09.2025, mesurée avec l'ionosonde de Juliusruh. MUF $\qty{3000}{\kilo\meter}$ signifie dans ce cas que l'on rayonne de façon très rasante pour atteindre une distance de saut de $\qty{3000}{\kilo\meter}$.

<margin>
[picture:999:e_muf_fof2:MUF et $f_\text{c}$ le 08.09.2025]
</margin>

Pour d'autres angles de rayonnement, la MUF peut se déterminer approximativement à partir de la $f_\text{c}$ à l'aide de la formule suivante du recueil de formules (valable pour $\alpha > \qty{40}{\degree}$) :

$MUF \approx \frac{f_\text{c}}{sin(\alpha)}$

où $\alpha$ désigne l'angle de rayonnement (cf. figure [ref:e_muf_winkel]). En regardant la formule de plus près, on reconnaît que la MUF est toujours plus élevée que la fréquence critique — et ce d'autant plus que l'antenne d'émission rayonne bas, ou que l'antenne de réception capte bas.

[question:AH208]

---

Pour la planification commerciale des fréquences, où il importe qu'une liaison radio réussisse avec une forte probabilité, il existe en outre la notion de *FOT* (*frequency of optimal transmission*, fréquence optimale de transmission), aussi notée $f_\text{opt}$. C'est la fréquence qui, sur un trajet de signal donné, permet statistiquement une liaison radio 90 % des jours ; elle se situe habituellement 15 % en dessous de la moyenne mensuelle de la MUF. Nous trouvons cette relation dans le recueil de formules sous la forme 

$f_\text{OPT} = MUF \cdot 0,85$

Avec ces informations, nous pouvons maintenant résoudre l'exercice suivant ; une calculatrice y est utile.

[question:AH209]

<indepth>
Pour les liaisons DX en radioamateurisme, la $f_\text{opt}$ ne joue aucun rôle, car on y choisit en règle générale la bande de fréquences la plus haute permettant encore une liaison (donc au plus près de la MUF), puisque c'est là que le plancher de bruit le plus faible, et donc le meilleur signal, est à attendre (rapport signal/bruit SNR le plus élevé).
</indepth>

Dans la classe E, nous avons déjà fait connaissance avec la LUF (Lowest Usable Frequency). Elle est déterminée par la région D et désigne la fréquence utilisable la plus basse, en dessous de laquelle l'atténuation est trop forte. La région D *atténue* en effet notre signal radio, et par saut, ce signal doit en plus traverser cette région D *deux* fois. En même temps, cette atténuation est d'autant plus élevée que la fréquence est basse (la relation est quadratique : si l'on divise la fréquence par deux, l'atténuation est multipliée par quatre). C'est pourquoi, en diminuant continuellement la fréquence, on finira également par atteindre le point où le signal renvoyé n'est plus utilisable ; c'est la LUF.

[question:AH210]
[question:AH211]
