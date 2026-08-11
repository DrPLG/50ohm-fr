Dans la classe N, nous avons déjà rencontré la *puissance apparente rayonnée* (ERP). Contrairement à l'EIRP, elle ne se rapporte pas à un radiateur isotrope, mais à un dipôle demi-onde. Pour le calcul, seule compte la puissance qui parvient réellement au point d'alimentation de l'antenne. Les pertes dans la ligne d'alimentation, dues par exemple à l'atténuation du câble, doivent donc être retranchées de la puissance de sortie de l'émetteur.

La puissance apparente rayonnée résulte de la puissance fournie à l'antenne et du gain d'antenne dans la direction considérée :

$P_\mathrm{ERP}=P_\mathrm{Ant}\cdot G_\mathrm{d}$

où $G_\mathrm{d}$ est le gain d'antenne rapporté à un dipôle demi-onde, exprimé comme facteur linéaire.

[question:AG501]

La puissance au point d'alimentation de l'antenne se détermine à partir de la puissance de sortie de l'émetteur et de l'atténuation de la ligne d'alimentation. Pour cela, l'atténuation est convertie en un facteur d'atténuation linéaire $D$. Pour une atténuation de $\qty{10}{\dB}$ par exemple, ce facteur vaut $\num{0,1}$, de sorte qu'un dixième seulement de la puissance de l'émetteur parvient à l'antenne :

$P_\mathrm{Ant}=D\cdot P_\mathrm{TX}$

C'est seulement cette puissance réellement fournie qui est ensuite multipliée par le gain d'antenne pour calculer l'ERP.

[question:AK104]

Pour la question suivante, il faut absolument faire attention aux signes des opérations. Les pertes sont soustraites de la puissance d'émission, puis le résultat est multiplié par le facteur de gain ($G_\mathrm{Antenne}$).
Comme c'est l'ERP qui doit être calculée, la référence doit être prise par rapport à un dipôle demi-onde.

[question:AG502]

Une indication sur la bonne solution de la question suivante figure déjà dans l'[annexe 1 de l'AFUV](https://50ohm.de/a1). Il y est prescrit, comme puissance maximale pour la bande des $\qty{630}{\meter}$, $\qty{1}{\watt}$ ERP. Un dipôle demi-onde pour cette fréquence aurait une longueur d'environ $\qty{315}{\meter}$ et n'est donc guère réalisable pour la plupart des radioamateurs. En pratique, on a donc le plus souvent recours à des antennes fortement raccourcies, dont le rendement est nettement plus faible que celui d'un dipôle demi-onde non raccourci. Un gain d'antenne de $\qty{-20}{\dBd}$ est donc tout à fait plausible. Comme le câble coaxial utilisé est court, son atténuation peut être négligée dans cette gamme de fréquences. Essaie maintenant de résoudre la question suivante.

[question:AG503]

Pour résoudre cette question, on peut recourir au tableau des rapports de puissance du recueil de formules. Pour $\qty{-20}{\dB}$, le facteur $\num{0,01}$ y est indiqué.

$\qty{50}{\watt}\cdot 0,01 = \qty{0,5}{\watt}$

La bonne réponse est $\qty{0,5}{\watt}$.

<tip>
Ce tableau figure dans le recueil de formules et est disponible pendant l'examen.

| r:   | r: Rapport de puissance | r: Rapport de tension |
| $\qty{-20}{\dB}$ | $\num{0,01}$ | $\num{0,1}$ |
| $\qty{-10}{\dB}$ | $\num{0,1}$ | $\num{0,32}$ |
| $\qty{-6}{\dB}$ | $\num{0,25}$ | $\num{0,5}$ |
| $\qty{-3}{\dB}$ | $\num{0,5}$ | $\num{0,71}$ |
| $\qty{-1}{\dB}$ | $\num{0,79}$ | $\num{0,89}$ |
| $\qty{0}{\dB}$ | $\num{1}$ | $\num{1}$ |
| $\qty{1}{\dB}$ | $\num{1,26}$ | $\num{1,12}$ |
| $\qty{3}{\dB}$ | $\num{2}$ | $\num{1,41}$ |
| $\qty{6}{\dB}$ | $\num{4}$ | $\num{2}$ |
| $\qty{10}{\dB}$ | $\num{10}$  | $\num{3,16}$ |
| $\qty{20}{\dB}$ | $\num{100}$ | $\num{10}$ |
[table:Pegel_Verhältnis:Rapports de puissance et de tension pour des valeurs importantes d'atténuation et de gain]

</tip>
