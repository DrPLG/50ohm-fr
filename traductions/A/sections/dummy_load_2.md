Dans la classe E, nous avons déjà fait connaissance avec la *charge fictive (dummy load)*. Une charge fictive est une résistance de charge qui transforme en chaleur la puissance HF délivrée par l'émetteur. Elle permet par exemple de tester un émetteur ou de déterminer sa puissance de sortie sans qu'un signal soit rayonné par une antenne. Dans la classe A, nous allons maintenant examiner plus en détail comment une telle charge fictive peut être construite.

Une charge fictive pour le domaine HF est souvent composée de plusieurs résistances élémentaires. La puissance dissipée qui en résulte peut ainsi être répartie sur plusieurs composants, ce qui permet d'atteindre une puissance admissible totale plus élevée. Les résistances peuvent être montées en parallèle, en série, ou selon une combinaison des deux. Si l'on utilise des résistances identiques, de même puissance admissible, et que le montage est réalisé de façon symétrique, la puissance dissipée se répartit uniformément sur chacune des résistances. Le nombre nécessaire de résistances et leur montage peuvent être déterminés à l'aide des règles connues pour les montages en série et en parallèle. Pour une charge fictive HF, il importe en outre que le montage se comporte, même aux fréquences élevées, le plus possible comme une résistance purement ohmique de $\qty{50}{\ohm}$. C'est pourquoi on utilise des résistances adaptées, aussi peu inductives que possible, et des connexions aussi courtes que possible.

La figure [ref:dummy_load_aufbau1] montre une charge fictive de 50ohm.de entièrement assemblée. On y trouve par exemple $\num{20}$ résistances de $\qty{1}{\kilo\ohm}$ chacune, montées en parallèle. Pour $n$ résistances identiques montées en parallèle, on a :

$R_\mathrm{tot} = \frac{R}{n}$

On obtient ainsi :

$R_\mathrm{tot} = \frac{\qty{1}{\kilo\ohm}}{20} = \qty{50}{\ohm}$

<warning>
La puissance dissipée maximale admissible de l'ensemble de la charge fictive résulte approximativement de la somme des puissances admissibles de toutes les résistances, à condition que la puissance se répartisse uniformément entre elles. La charge fictive 50ohm.de ne disposant ni de refroidissement ni de blindage, elle ne doit être utilisée que pour des émetteurs QRP de faible puissance de sortie. Pour des puissances plus élevées, une charge fictive dotée d'un refroidissement et d'un blindage, adaptée également au fonctionnement continu, est nécessaire !
</warning>

La charge fictive 50ohm.de comporte en outre un redresseur de valeur de crête, constitué d'une diode et d'un condensateur. Celui-ci permet de produire, à partir de la tension HF présente, une tension continue qui peut par exemple être mesurée avec un multimètre. En tenant compte du diviseur de tension et de la tension de seuil de la diode, on peut en déduire la puissance HF de sortie de l'émetteur.

[question:AI602]

<margin>
[photo:340:dummy_load_aufbau1:La charge fictive 50ohm.de terminée]
[photo:341:dummy_load_aufbau2:Montage de la charge fictive 50ohm.de]

*Publicité :* Toi aussi, tu as envie de construire une chouette charge fictive QRP 50ohm.de ? Tu peux alors la commander sous forme de kit auprès du [DARC-Verlag](https://darcverlag.de/50Ohm-Dummy-Load-DIY-Kit-Bausatz).
</margin>

Dans la question d'examen suivante, la charge fictive est constituée d'une combinaison de montages en série et en parallèle. Si l'on monte dans chaque branche $N_\mathrm{S}$ résistances identiques en série, puis que l'on monte $N_\mathrm{P}$ branches de ce type en parallèle, la résistance totale vaut :

$R_\mathrm{tot} = \frac{N_\mathrm{S}}{N_\mathrm{P}} \cdot R$

Le nombre total de résistances utilisées vaut alors :

$n = N_\mathrm{S} \cdot N_\mathrm{P}$

Si toutes les résistances sont chargées de façon identique, leurs puissances dissipées admissibles s'additionnent. On peut ainsi réaliser une charge fictive présentant la résistance souhaitée tout en offrant une puissance admissible élevée.

[question:AI601]

Une autre possibilité pour déterminer la puissance HF de sortie consiste à équiper la charge fictive d'une prise sur son réseau de résistances. Si cette prise se trouve par exemple près de la connexion de masse, seule une partie de la tension HF totale y est présente.

Les résistances forment alors un diviseur de tension. Si son rapport de division est connu, on peut, à partir de la tension HF mesurée à la prise, en déduire par calcul la tension totale présente aux bornes de la charge fictive. Cette tension partielle peut par exemple être mesurée avec une sonde HF et un multimètre numérique. La puissance HF peut ensuite être calculée à partir de la tension totale ainsi déterminée.

[question:AI603]
