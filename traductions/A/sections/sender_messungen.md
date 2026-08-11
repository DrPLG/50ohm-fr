Les mesures importantes pour le radioamateur sur les émetteurs sont les mesures de puissance de sortie des émetteurs ou la mesure des tensions HF dans les parties HF d'un montage.

Lors de la mesure des puissances de sortie d'un émetteur, celui-ci doit être fermé sur une impédance définie, correspondant à l'impédance de sortie de l'émetteur. En radioamateurisme, l'impédance usuelle (terminaison de l'émetteur) est de $\qty{50}{\ohm}$. La terminaison peut aussi se faire directement dans le montage de mesure, ce qui n'a toutefois de sens que pour de faibles puissances.

La mesure des tensions HF s'effectue au moyen d'une sonde HF, par redressement à diode puis lissage de la tension continue obtenue à l'aide d'un condensateur placé en aval.

Sur les sondes HF à une seule diode, on peut mesurer à la sortie de mesure la tension de crête de la tension HF appliquée, diminuée de la tension directe de la diode utilisée et, le cas échéant, de l'effet d'un diviseur de tension placé en amont.

[question:AI608]

Pour améliorer la précision de mesure, en particulier pour les faibles puissances dans le domaine VHF/UHF, on utilise souvent un double redressement par 2 diodes, de sorte que les deux alternances de la HF sont redressées (double tension de crête) et sont disponibles, diminuées de 2 fois la tension directe des diodes utilisées, sous forme de tension de mesure additionnée à la sortie de mesure.

[question:AI605]
[question:AI604]

Pour les puissances HF plus élevées, il faut placer en amont un atténuateur de puissance admissible suffisante, qui absorbe une grande partie de la puissance de sortie de l'émetteur à mesurer. L'atténuateur est à prendre en compte dans le calcul de la puissance.

[question:AI609]

Pour pouvoir mesurer exactement les puissances et les tensions HF avec les montages précités, ceux-ci doivent être étalonnés, afin d'établir les valeurs de correction correspondantes pour les mesures.

[question:AI612]

Examinons maintenant en détail le calcul de ces montages.
Une sonde HF à redressement simple suivi d'un lissage se calcule comme suit :

Le signal HF d'entrée est fermé, avec l'impédance correcte, par la résistance présente à l'entrée (ou la combinaison de résistances individuelles). Dans le montage représenté, la tension HF est divisée par deux par le diviseur de tension qui suit (lequel agit également du point de vue de l'impédance). Vient ensuite le redressement de la valeur de crête par la diode, dont la tension de sortie se calcule comme la valeur de crête diminuée de la tension directe de la diode, et est mémorisée dans le condensateur placé en aval.

Pour $\qty{1}{\watt}$ de puissance d'entrée dans un système à $\qty{50}{\ohm}$, on obtient une tension d'entrée de $\qty{7,07}{\volt}$ efficaces et de $\qty{10}{\volt}$ de crête.
Le diviseur de tension placé en aval divise cette tension par deux, soit $\qty{5}{\volt}$ de tension de crête, laquelle, après redressement par la diode et déduction de la tension directe de celle-ci de $\qty{0,23}{\volt}$, vaut encore $\qty{4,77}{\volt}$. On mesure alors, arrondi, environ $\qty{4,8}{\volt}$ à la sortie du montage.

[question:AI610]

Inversement, la puissance fournie au montage peut être calculée à partir de la tension continue mesurée.

On mesure à la sortie du montage $\qty{14,9}{\volt}$ de tension de crête. En raison de la tension directe de la diode, la valeur de crête HF avant la diode est de $\qty{15,6}{\volt}$. Compte tenu du diviseur de tension placé en amont, cela donne une tension de crête HF de $\qty{31,2}{\volt}$.  Cela correspond, dans un système à $\qty{50}{\ohm}$, à une puissance d'entrée de $\qty{9,73}{\watt}$, soit environ $\qty{9,7}{\watt}$.

[question:AI611]

Sur les sondes HF et les wattmètres à double redressement de la valeur de crête (2 diodes), le calcul s'effectue comme pour le redressement simple, mais il faut tenir compte de la double tension de crête à la sortie et de la double chute de tension due aux 2 diodes.

[question:AI607]
[question:AI606]

Pour indiquer qu'un émetteur rayonne de la puissance par son antenne, on peut utiliser un indicateur de champ. La HF reçue par une antenne de mesure y est appliquée à une diode et redressée par celle-ci. La tension redressée est ensuite appliquée, à travers des selfs de choc HF, à un condensateur qui la mémorise. L'affichage se fait par un ampèremètre sensible. Plus la déviation de l'aiguille de l'instrument de mesure est grande, plus l'intensité du champ HF mesurée à l'antenne est élevée. Pour pouvoir effectuer des mesures exactes, tant l'antenne de mesure que le mesureur de champ doivent être étalonnés.

[question:AI613]