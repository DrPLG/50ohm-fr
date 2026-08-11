<margin>
[picture:1019:e_frequenzabhängiger_widerstand:Dépendance en fréquence du condensateur et de la bobine, comparée à une résistance classique]
[picture:1020:e_herleitung_tiefpass:Construction du circuit passe-bas à partir d'un diviseur de tension]
</margin>

Dans les chapitres consacrés aux condensateurs et aux bobines, nous avons déjà appris que ces deux composants possèdent une résistance dépendante de la fréquence. La figure [ref:e_frequenzabhängiger_widerstand] montre qualitativement que la résistance d'une résistance ohmique est indépendante de la fréquence, tandis que la résistance d'un condensateur diminue de façon hyperbolique lorsque la fréquence augmente et que la résistance d'une bobine croît linéairement avec la fréquence.

À partir de ces composants, on peut construire des filtres de fréquence dits passifs, que nous allons maintenant examiner de plus près. Dans la première partie de ce chapitre, nous nous intéressons aux filtres simples, à savoir les passe-haut et les passe-bas. Ces filtres permettent de supprimer les plages de fréquences indésirables au-dessus ou en dessous d'une fréquence de coupure. Dans la seconde partie, nous nous consacrerons ensuite à des filtres plus complexes, comme par exemple les passe-bande.

Nous commençons par la construction d'un passe-bas sous la forme d'une *cellule RC*. Le point de départ, à l'étape (1), est le circuit d'un diviseur de tension, tel qu'il est représenté sur la figure [ref:e_herleitung_tiefpass] et que nous avons déjà rencontré. Nous nous rappelons que pour un diviseur de tension, la relation suivante s'applique : 

$\frac{U_1}{U_2} = \frac{R_1}{R_2}$

Cela signifie par exemple : si la résistance $R_2$ est deux fois plus grande que la résistance $R_1$, alors la tension $U_2$ est elle aussi deux fois plus grande que la tension $U_1$.

À l'étape (2), nous remplaçons la résistance $R_2$ par le condensateur $C_1$. Ensuite, à l'étape (3), nous redessinons encore un peu le circuit, de manière à obtenir la représentation habituelle d'un passe-bas.

---

Retenons : un passe-bas n'est d'abord rien d'autre qu'un diviseur de tension. C'est pourquoi nous pouvons, dans la suite, le considérer exactement comme tel. La figure [ref:e_wiederstaende_tiefpass] présente à nouveau les courbes de résistance en fonction de la fréquence. Considérons d'abord les basses fréquences : dans ce cas, la résistance du condensateur est grande, de sorte qu'une tension élevée est présente en sortie. Si la fréquence augmente, la résistance du condensateur devient de plus en plus petite et, conformément au principe du diviseur de tension, la tension de sortie diminue elle aussi.

On obtient ainsi la courbe de tension telle qu'elle est montrée sur la figure [ref:e_tiefpass_frequenzgang]. L'idée centrale du passe-bas est ainsi expliquée : les hautes fréquences sont fortement atténuées, tandis que les basses fréquences traversent le filtre pratiquement sans entrave. Un exemple d'application d'un passe-bas est son utilisation derrière les amplificateurs d'émission, afin de filtrer les harmoniques apparaissant à cause des distorsions. 

<margin>
[picture:1021:e_wiederstaende_tiefpass:Comportement qualitatif des résistances dans le diviseur de tension passe-bas]
[picture:1024:e_tiefpass_frequenzgang:Évolution qualitative de la tension $U_\text{A}$ sur le passe-bas]
</margin>

[question:ED208]
[question:ED201]

<indepth>
La *fréquence de coupure* ($f_\text{g}$) d'un passe-bas est la fréquence à laquelle le signal de sortie commence tout juste à être affaibli de manière sensible. Elle marque donc la transition entre la plage de fréquences que le filtre laisse passer pratiquement sans entrave et la plage dans laquelle l'atténuation augmente nettement. Formellement, la fréquence de coupure est définie de telle sorte qu'à cette fréquence, la puissance de sortie est tombée à la moitié de la puissance d'entrée ($\qty{-3}{\dB}$). Comme la puissance est proportionnelle au carré de la tension, cela correspond à une diminution de la tension de sortie à environ $\qty{70}{\percent}$ de sa valeur initiale ($\frac{1}{\sqrt{2}}$). En pratique, on reconnaît donc souvent la fréquence de coupure au point où la tension de sortie devient nettement plus petite et où la réponse en fréquence commence à « fléchir ». En dessous de la fréquence de coupure, les basses fréquences sont transmises quasiment sans altération ; au-dessus de la fréquence de coupure, les fréquences plus élevées sont de plus en plus atténuées.
</indepth>

---

Dans un passe-haut, au contraire, les basses fréquences sont fortement atténuées, tandis que les hautes fréquences traversent ce filtre presque sans atténuation. On y parvient en échangeant le condensateur et la résistance, comme représenté sur la figure [ref:e_wiederstaende_hochpass]. La réponse en fréquence d'un passe-haut est montrée qualitativement en [ref:e_hochpass_frequenzgang]. Un exemple d'application d'un passe-haut est son utilisation dans un séparateur d'antenne, par exemple pour éliminer la gamme des ondes courtes en amont d'un récepteur VHF, afin d'éviter les perturbations dues au trafic en ondes courtes.

<margin>
[picture:1025:e_wiederstaende_hochpass:Comportement qualitatif des résistances dans le diviseur de tension passe-haut]
[picture:1022:e_hochpass_frequenzgang:Évolution qualitative de la tension $U_\text{A}$ sur le passe-haut]
</margin>

[question:ED211]
[question:ED202]

---

Les cellules RC simples ont l'inconvénient de présenter des flancs plutôt plats au voisinage de la fréquence de coupure. De plus, la plus petite impédance d'un passe-bas RC est déterminée par la résistance $R$. Or, la résistance $R$ peut être remplacée par une bobine, dont le comportement en fréquence est opposé à celui d'un condensateur. Il est donc naturel de combiner bobines et condensateurs pour former des passe-haut et des passe-bas. 
Aux *hautes fréquences, la résistance de la bobine est élevée*, celle du condensateur en revanche est petite.
Aux *basses fréquences, la résistance de la bobine est faible*, celle du condensateur en revanche est grande. 
Selon le composant aux bornes duquel la tension de sortie est mesurée, on obtient un passe-haut ou un passe-bas. Si l'on retient que la résistance de la bobine $X_\text{L}$ est elle aussi élevée à haute fréquence, on peut rapidement identifier un circuit comme passe-haut ou passe-bas en regardant aux bornes de quel composant la tension de sortie est mesurée.

<tip>
Pour les circuits comportant condensateur et bobine, la règle simple suivante s'applique également : si la branche supérieure du diviseur de tension contient un *H* dressé — comme dans passe-*H*aut —, il s'agit d'un passe-haut. Si la branche supérieure contient en revanche une résistance ou une bobine, il s'agit d'un passe-bas.
[picture:1023:e_hochpass_tipp:Astuce mnémotechnique]
</tip>

[question:ED209]
[question:ED212]

---

Les questions suivantes portent sur une application pratique de nos filtres. Il est bien sûr possible d'utiliser plusieurs composants dépendants de la fréquence dans un même circuit, de sorte que la transition au voisinage de la fréquence de coupure devienne plus raide. Grâce à l'astuce mentionnée, tu devrais maintenant reconnaître facilement quel circuit est utilisé dans les deux questions suivantes. 

[question:ED210]
[question:ED213] 

Un autre exemple pratique d'enchaînement de bobines et de condensateurs en tant que filtre est le diplexeur expliqué en marge. 

<indepth>
*Exemple pratique : le diplexeur.* Les passe-haut et passe-bas passifs sont aussi utilisés dans les répartiteurs de fréquences. Dans l'exemple ci-dessous, on voit le circuit d'un diplexeur pour $\qty{2}{\meter}$ et $\qty{70}{\centi\meter}$. Celui-ci peut être utilisé, par exemple, pour exploiter un poste $\qty{2}{\meter}$ et un poste $\qty{70}{\centi\meter}$ sur une antenne bibande commune. Inversement, on pourrait aussi utiliser des antennes séparées pour le $\qty{2}{\meter}$ et le $\qty{70}{\centi\meter}$ avec un appareil VHF/UHF bibande, par exemple une antenne omnidirectionnelle pour le trafic direct sur $\qty{2}{\meter}$ et une antenne directive pour le trafic via relais sur $\qty{70}{\centi\meter}$. 
Devant la sortie $\qty{2}{\meter}$ se trouve un passe-bas, devant la sortie $\qty{70}{\centi\meter}$ un passe-haut — chacun combinant 5 composants dépendants de la fréquence. 
[picture:939:e_circuit_diplexer:Schéma du diplexeur $\qty{2}{\meter}$/$\qty{70}{\centi\meter}$]
[photo:171:e_example_diplexer:Exemple de réalisation]
</indepth>

<indepth>
[photo:320:e_tiefpass_selbstbau:Filtre passe-bas de construction personnelle]
Les filtres mentionnés ci-dessus peuvent naturellement être calculés et construits soi-même pour toutes les gammes de fréquences. Le formulaire contient les formules nécessaires, et il existe bien sûr aussi de nombreux plans de montage et programmes de calcul. Les bobines nécessaires sont souvent faciles à fabriquer soi-même. Pour les petites valeurs d'inductance, une petite réserve de fil de cuivre émaillé de $\qty{0,8}{\milli\meter}$ suffit pour des bobines à air stables. Pour les grandes valeurs d'inductance, par exemple pour les bandes décamétriques, on s'en sort avec du fil de cuivre émaillé de $\qty{0,2}{\milli\meter}$ et du matériau de noyau présentant les valeurs $A_\text{L}$ appropriées, afin de pouvoir fabriquer soi-même à tout moment les bonnes valeurs. Les dimensions, nombres de spires, etc. nécessaires se trouvent également, la plupart du temps, facilement grâce au formulaire, aux plans de montage ou aux programmes de calcul.
</indepth>  

---

Nous avons maintenant fait connaissance avec les cellules RC et LC simples en tant que filtres passe-haut et passe-bas. À partir de condensateurs et de bobines, on peut cependant réaliser encore d'autres types de filtres, qui vont au-delà des simples passe-haut et passe-bas. Nous allons maintenant les examiner de plus près dans cette seconde partie : les *circuits oscillants* (Schwingkreise).

<margin>
[picture:1026:e_rp_schwingkreis:(a) Circuit oscillant série (b) circuit oscillant parallèle]
</margin>

Dans les circuits oscillants, la bobine et le condensateur sont disposés — selon l'effet de filtrage souhaité — de manière à ce qu'une résistance particulièrement élevée ou particulièrement faible apparaisse à une fréquence donnée. Les fréquences situées au-dessus ou en dessous de cette fréquence sont ainsi atténuées ou laissées passer de manière ciblée.

La disposition de la bobine et du condensateur peut se faire soit en série, soit en parallèle. On distingue en conséquence les circuits oscillants série (a) et les circuits oscillants parallèle (b), comme représenté sur la figure [ref:e_rp_schwingkreis]. 

---

Si l'on connecte la bobine et le condensateur en parallèle et que l'on applique par exemple une impulsion rectangulaire à cet ensemble, celui-ci entre en oscillation. Le condensateur chargé a maintenant emmagasiné de l'énergie dans son champ électrique, laquelle se décharge cependant à travers la bobine. Le courant qui traverse la bobine y fait naître un champ magnétique, qui oppose d'abord une résistance au passage du courant. Mais dès que le champ magnétique est établi, le condensateur se décharge complètement. L'énergie est alors emmagasinée dans le champ magnétique de la bobine. Comme le condensateur ne peut toutefois pas se décharger davantage ni maintenir un courant, le champ magnétique ne peut pas être entretenu. Le champ magnétique de la bobine se dissipe et engendre une tension de sens inverse. Cette tension charge alors le condensateur en sens inverse, jusqu'à ce que le champ magnétique de la bobine soit dissipé et ne puisse plus opposer de résistance au champ électrique du condensateur. Le processus recommence ensuite. 

<margin>
[include:applet_schwingkreis]
</margin>

---

C'est pour cette raison que l'on parle de circuit oscillant. La fréquence à laquelle ce circuit oscille est appelée fréquence de résonance ($f_0$). Elle est comparable à la fréquence de résonance d'un diapason mis en vibration par un choc. À la résonance, les résistances de la bobine $X_\text{L}$ et du condensateur $X_\text{C}$ sont égales. De tels circuits oscillants peuvent d'une part servir à produire des oscillations, ce que nous étudierons plus en détail dans le chapitre sur les oscillateurs. D'autre part, ils peuvent aussi être employés comme filtres — et c'est précisément le sujet de ce chapitre.

<margin>
[picture:1037:e_rsk_frequenzgang:Réponse en fréquence qualitative d'un circuit oscillant série]
</margin>

---

Dans un *circuit oscillant série* (Serienschwingkreis ou Reihenschwingkreis), comme sur la figure [ref:e_rp_schwingkreis]a, la résistance totale est minimale à la résonance. La figure [ref:e_rsk_frequenzgang] montre la réponse en fréquence. Aux fréquences supérieures à la fréquence de résonance, la résistance de la bobine augmente, de sorte que la résistance totale du circuit oscillant série croît elle aussi. Il se passe la même chose aux fréquences inférieures à la fréquence de résonance, mais c'est alors la résistance du condensateur qui est grande. Dans les circuits oscillants série, la résistance est donc minimale à la fréquence de résonance. Du fait du montage en série, aux fréquences éloignées de la résonance, c'est le composant présentant la plus grande résistance qui détermine l'impédance du circuit oscillant.

<indepth>
Le module de la réponse en fréquence d'un circuit oscillant série composé d'une résistance, d'une bobine et d'un condensateur se calcule selon la formule suivante :
  
$Z = \sqrt{R^2+\left(X_\text{L} - X_\text{C}\right)^2}$
  
À la résonance, lorsque $X_\text{C}$ = $X_\text{L}$, il ne reste que la résistance $R$. Dans le cas idéal, lorsque la résistance $R=\qty{0}{\ohm}$, la résistance est même nulle. Si nous remplaçons $X_\text{L}$ et $X_\text{C}$ par leurs valeurs, nous obtenons :
  
$Z = \sqrt{R^2+\left(2\pi f \cdot L~-~\frac{1}{2\pi f \cdot C} \right)^2}$
  
Dans la formule, on retrouve très bien la réponse en fréquence de la figure [ref:e_rsk_frequenzgang] : si l'on fait tendre la fréquence vers $\qty{0}{\hertz}$, la contribution de la bobine disparaît et seul le condensateur agit. Si l'on fait au contraire tendre la fréquence vers l'infini, seule la bobine agit et la contribution du condensateur s'évanouit.
  
On peut même calculer la fréquence de résonance. Lorsque $X_\text{L} = X_\text{C}$, on peut résoudre la formule par rapport à $f$ :
  
$2\pi f \cdot L = \frac{1}{2\pi f \cdot C}$
  
On obtient ainsi la formule : 
  
$f_0 = \frac{1}{2\pi \sqrt{L\cdot C}}$
  
La dérivation exacte des formules peut par exemple être consultée sur [Wikipedia](https://50ohm.de/schwk). Il convient de mentionner ici que toutes les réponses en fréquence sont tracées de manière qualitative et peuvent, dans la réalité, avoir un aspect quelque peu différent.
</indepth>

[question:ED205]

---

Si l'on assemble le condensateur et la bobine en un *circuit oscillant parallèle* (Parallelschwingkreis), comme sur la figure [ref:e_rp_schwingkreis]b, le comportement est exactement inverse : la résistance *$Z$* est très élevée à la fréquence de résonance, cf. figure [ref:e_psk_frequenzgang]. Aux fréquences supérieures à la fréquence de résonance, le condensateur présente cependant une faible résistance, de sorte que la résistance de ce circuit oscillant diminue. Aux fréquences inférieures à la fréquence de résonance, c'est en revanche la bobine qui présente une faible résistance, de sorte que la résistance du circuit oscillant diminue également aux fréquences plus basses. 
Dans les circuits oscillants parallèle, la résistance est donc maximale à la fréquence de résonance. Aux fréquences éloignées de la résonance, c'est le composant présentant la résistance la plus faible qui détermine l'impédance du circuit oscillant parallèle. 

<margin>
[picture:1036:e_psk_frequenzgang:Réponse en fréquence qualitative d'un circuit oscillant parallèle]
</margin>

[question:ED206] 
[question:ED207]

% TODO ////

Selon la façon dont les circuits oscillants parallèle et série sont insérés sur le trajet du signal, on peut alors soit atténuer, soit extraire des plages de fréquences. Pour cela, nous voulons de nouveau utiliser notre approche du diviseur de tension.

---

Commençons d'abord par les circuits réalisant des *filtres coupe-bande* (Bandsperren). Il existe deux façons de les construire sous forme de diviseur de tension : premièrement le *circuit d'absorption* (Saugkreis, cf. figure [ref:e_saugkreis]) et deuxièmement le *circuit bouchon* (Sperrkreis, cf. figure [ref:e_sperrkreis]). Les figures représentent chaque fois la résistance dépendante de la fréquence ainsi que la tension de sortie. À l'aide de nos règles bien connues sur le diviseur de tension, ces relations se déduisent et se comprennent de manière tout à fait analogue aux cellules RC traitées précédemment. Comme les circuits oscillants parallèle présentent une résistance élevée à la résonance, ils se prêtent bien à une utilisation en circuit bouchon, en série sur le trajet du signal. Ou bien l'on utilise la faible résistance à la résonance d'un circuit oscillant série, en parallèle du trajet du signal, comme circuit d'absorption. Souvent, on emploie d'ailleurs les deux en combinaison. Une application des filtres coupe-bande est par exemple la suppression de certaines portions de bande, par exemple lorsqu'un émetteur de radiodiffusion FM proche perturbe la réception.

[question:ED204]
[question:ED214] 
[question:ED215]

<margin>
[picture:1038:e_saugkreis:Réponses en fréquence qualitatives d'un circuit d'absorption]
[picture:1040:e_sperrkreis:Réponses en fréquence qualitatives d'un circuit bouchon]
</margin>

---

La seconde catégorie de circuits que l'on peut développer à partir de circuits oscillants est celle des *passe-bande* (Bandpässe). Là encore, il existe deux façons de les construire sous forme de diviseur de tension : premièrement le *circuit passant* (Leitkreis, cf. figure [ref:e_leitkreis]) et deuxièmement le *passe-bande* (cf. figure [ref:e_bandpass]). Ici aussi, la construction s'effectue comme d'habitude à partir du comportement d'un diviseur de tension. Pour un passe-bande, on place des circuits oscillants parallèle en parallèle du trajet du signal, car ceux-ci présentent une faible résistance pour les fréquences éloignées de la résonance et les « court-circuitent » pour ainsi dire. Un circuit oscillant série, placé en série sur le trajet du signal, apporte une atténuation supplémentaire en dehors de la résonance, tandis qu'il présente une faible résistance à la fréquence souhaitée.

[question:ED203]

<margin>
[picture:1039:e_leitkreis:Réponses en fréquence qualitatives d'un circuit passant]
[picture:1041:e_bandpass:Réponses en fréquence qualitatives d'un passe-bande]
</margin>

Un exemple d'application évident des passe-bande est leur emploi dans les récepteurs, où un préfiltrage de certaines bandes de fréquences est nécessaire. Dans ce cas, on utilise un filtre qui ne laisse passer que la bande de fréquences souhaitée, tandis que toutes les autres fréquences sont atténuées. De tels passe-bande se trouvent donc dans presque tous les récepteurs, souvent même séparément pour chacune des bandes décamétriques. Dimensionnés pour des puissances suffisamment élevées, les passe-bande sont aussi utilisés à l'émission, par exemple lors de contests en commun ou de fielddays, afin de minimiser les perturbations mutuelles entre stations voisines.

Pour construire des passe-bande et des filtres coupe-bande, on peut donc utiliser aussi bien des circuits oscillants série que parallèle. L'essentiel est de tenir compte du comportement de chaque circuit oscillant à la résonance. Selon leur comportement, ils peuvent être placés en série sur le trajet du signal ou en parallèle de celui-ci — éventuellement même combinés plusieurs fois entre eux. 

Dans les filtres, seuls certains types de condensateurs appropriés peuvent être utilisés.
Les condensateurs électrolytiques, par exemple, ne conviennent pas aux circuits HF, d'une part parce que leur capacité dépend fortement de la fréquence, d'autre part parce qu'ils présentent une résistance interne élevée aux hautes fréquences. Les condensateurs à film ne conviennent pas non plus, car leurs enroulements (inductance propre) les rendent fortement dépendants de la fréquence, en particulier à partir des bandes décamétriques, et leur confèrent un mauvais facteur de qualité. 
Les condensateurs céramiques, en revanche, ne présentent que de faibles pertes et leur capacité ne dépend que peu de la fréquence et de la température. De plus, ils sont faciles à se procurer, même pour des tensions élevées.
Conviennent également les condensateurs constitués de plaques avec l'air comme isolant, que l'on rencontre le plus souvent sous forme de condensateurs variables. Pour les tensions élevées, les condensateurs variables sont également employés dans les boîtes d'accord d'antenne.

[question:ED216]