Les mesures importantes pour le radioamateur sur les émetteurs sont les mesures de puissance de sortie des émetteurs ou la mesure des tensions HF dans les parties HF d'un montage. Lors de la mesure des puissances de sortie d'un émetteur, celui-ci doit être fermé sur une impédance définie, correspondant à l'impédance de sortie de l'émetteur. En radioamateurisme, l'impédance usuelle (terminaison de l'émetteur) est de $\qty{50}{\ohm}$. La terminaison peut aussi se faire directement dans le montage de mesure, ce qui n'a toutefois de sens que pour de faibles puissances.

La mesure des tensions HF s'effectue au moyen d'une sonde HF, par redressement à diode puis lissage de la tension continue obtenue à l'aide d'un condensateur placé en aval. La figure [ref:hf_messkopf_0] montre le principe d'une sonde HF à redressement simple et lissage de la tension continue. La tension HF est fermée, avec l'impédance correcte, par une résistance (ou une combinaison de résistances) placée à l'entrée. Le redressement s'effectue ensuite par une diode, dont la tension de sortie se calcule comme la valeur de crête diminuée de la tension directe de la diode, et est mémorisée dans le condensateur placé en aval. La figure [ref:hf_messkopf_1] montre une sonde HF construite par DL3JOP, la figure [ref:hf_messkopf_2] son schéma.

<margin>
[picture:576:hf_messkopf_0:Principe d'une sonde HF à redressement simple et lissage de la tension continue]
[photo:338:hf_messkopf_1:Sonde HF construite par DL3JOP]
[photo:339:hf_messkopf_2:Schéma de la sonde HF de DL3JOP]
</margin>

[question:AI608]

Pour les puissances HF plus élevées, il faut placer en amont un atténuateur de puissance admissible suffisante, qui absorbe une grande partie de la puissance de sortie de l'émetteur à mesurer. L'atténuateur est à prendre en compte dans le calcul de la puissance.

[question:AI609]

---

Pour mesurer les tensions et puissances HF avec la meilleure précision possible, le montage de mesure utilisé doit d'abord être étalonné. Pour cela, on injecte des signaux de référence connus et l'on détermine les écarts entre la valeur réelle et la valeur mesurée. Ces écarts permettent de déterminer des valeurs de correction dépendant de la fréquence et du niveau, qui peuvent par exemple être conservées dans un tableau tel que [ref:a_frequenzgang_messwerte].

Lors d'une mesure ultérieure, la valeur affichée est corrigée à l'aide de la valeur de correction correspondante. Si les valeurs mesurées sont exprimées en $\unit{\dBm}$, l'écart déterminé lors de l'étalonnage pour la fréquence correspondante peut par exemple être ajouté à la valeur mesurée comme valeur de correction en $\unit{\dB}$.

<margin>
| c: Fréquence en MHz | c: Puissance d'émission $\qty{-40}{\dBm}$ | c: Puissance d'émission $\qty{-20}{\dBm}$ |
| 10   | $\qty{-40,24}{\dBm}$ | $\qty{-20}{\dBm}$    |
| 50   | $\qty{-40,24}{\dBm}$ | $\qty{-20}{\dBm}$    |
| 100  | $\qty{-40,26}{\dBm}$ | $\qty{-20,12}{\dBm}$ |
| 200  | $\qty{-40,26}{\dBm}$ | $\qty{-20,2}{\dBm}$  |
| 300  | $\qty{-40,51}{\dBm}$ | $\qty{-20,32}{\dBm}$ |
| 400  | $\qty{-40,46}{\dBm}$ | $\qty{-20,28}{\dBm}$ |
| 500  | $\qty{-40,84}{\dBm}$ | $\qty{-20,64}{\dBm}$ |
| 600  | $\qty{-40,7}{\dBm}$  | $\qty{-20,41}{\dBm}$ |
| 700  | $\qty{-40,7}{\dBm}$  | $\qty{-20,53}{\dBm}$ |
| 800  | $\qty{-40,8}{\dBm}$  | $\qty{-20,55}{\dBm}$ |
| 900  | $\qty{-40,37}{\dBm}$ | $\qty{-20,2}{\dBm}$  |
| 1000 | $\qty{-40,33}{\dBm}$ | $\qty{-20,09}{\dBm}$ |
| 1100 | $\qty{-40,12}{\dBm}$ | $\qty{-19,85}{\dBm}$ |
| 1200 | $\qty{-39,94}{\dBm}$ | $\qty{-19,62}{\dBm}$ |
| 1300 | $\qty{-39,69}{\dBm}$ | $\qty{-19,49}{\dBm}$ |
| 1400 | $\qty{-40,18}{\dBm}$ | $\qty{-19,79}{\dBm}$ |
| 1500 | $\qty{-40,13}{\dBm}$ | $\qty{-19,97}{\dBm}$ |
| 1600 | $\qty{-40,95}{\dBm}$ | $\qty{-20,62}{\dBm}$ |
| 1700 | $\qty{-41,55}{\dBm}$ | $\qty{-21,64}{\dBm}$ |
| 1800 | $\qty{-41,47}{\dBm}$ | $\qty{-20,92}{\dBm}$ |
| 1900 | $\qty{-43,1}{\dBm}$  | $\qty{-23,27}{\dBm}$ |
| 2000 | $\qty{-42,34}{\dBm}$ | $\qty{-21,89}{\dBm}$ |
[table:a_frequenzgang_messwerte:Niveaux mesurés en fonction de la fréquence pour la sonde HF de DL3JOP]
</margin>

[question:AI612]

Examinons maintenant en détail le calcul des montages. Sur les sondes HF à une seule diode, on peut mesurer à la sortie de mesure la tension de crête de la tension HF appliquée, diminuée de la tension directe de la diode utilisée et, le cas échéant, de l'effet d'un diviseur de tension placé en amont. Une sonde HF à redressement simple suivi d'un lissage se calcule comme suit :

Le signal HF d'entrée est fermé, avec l'impédance correcte, par la résistance présente à l'entrée (ou la combinaison de résistances individuelles). Dans le montage représenté (cf. figure [ref:hf_messkopf_0]), la tension HF est divisée par deux par le diviseur de tension qui suit (lequel agit également du point de vue de l'impédance). Vient ensuite le redressement de la valeur de crête par la diode, dont la tension de sortie se calcule comme la valeur de crête diminuée de la tension directe de la diode, et est mémorisée dans le condensateur placé en aval.

---

[question:AI610]

<tip>
Pour tous les montages à sonde HF, on peut admettre de façon générale que la résistance d'entrée vaut $\qty{50}{\ohm}$. Il n'est pas nécessaire de le recalculer : cette étape peut être passée pour les questions d'examen.
</tip>

Inversement, la puissance fournie au montage peut être calculée à partir de la tension continue mesurée. Essaie de voir si tu trouves la solution !

[question:AI611]

Outre les sondes HF à une seule diode, il existe des montages à deux diodes. Leur avantage est de saisir à la fois la crête positive et la crête négative du signal HF. On dispose ainsi, à la sortie, d'une tension de mesure environ deux fois plus grande qu'avec un simple redressement de valeur de crête. Cela est particulièrement utile lorsque de faibles tensions HF doivent être mesurées avec un voltmètre à courant continu placé en aval.

[question:AI605]
[question:AI604]

La crête positive et la crête négative du signal HF sont ici saisies séparément et mémorisées dans des condensateurs. Les deux tensions s'additionnent à la sortie. Dans l'idéal, la tension de sortie correspond donc à la tension crête à crête du signal HF :

$U_\mathrm{S} \approx U_\mathrm{CC} = 2\hat U$

Dans le montage réel, il faut en outre tenir compte des tensions directes des deux diodes. On a donc approximativement :

$U_\mathrm{S} \approx 2\hat U - 2U_\mathrm{F}$

Si l'on souhaite déduire la tension HF à partir de la tension de sortie mesurée, on obtient :

$\hat{U} \approx \frac{U_\mathrm{S}+2U_\mathrm{F}}{2}$

À partir de la valeur de crête, on peut ensuite calculer la valeur efficace, puis, la résistance étant connue, la puissance HF.

[question:AI607]
[question:AI606]

Pour indiquer qu'un émetteur rayonne de la puissance par son antenne, on peut utiliser un indicateur de champ. La HF reçue par une antenne de mesure y est appliquée à une diode et redressée par celle-ci. La tension redressée est ensuite appliquée, à travers des selfs de choc HF, à un condensateur qui la mémorise. L'affichage se fait par un ampèremètre sensible. Plus la déviation de l'aiguille de l'instrument de mesure est grande, plus l'intensité du champ HF mesurée à l'antenne est élevée. Pour pouvoir effectuer des mesures exactes, tant l'antenne de mesure que le mesureur de champ doivent être étalonnés.

[question:AI613]
