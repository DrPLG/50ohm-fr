Dans chaque appareil radio sont présentes une ou plusieurs stabilisations de tension, car la tension d'entrée peut fluctuer, surtout dans les appareils alimentés par accumulateur, et des sous-ensembles sensibles, comme par ex. les oscillateurs, changeraient alors de fréquence.

Il existe 3 variantes de stabilisations de tension :
1. *Montage à diode Zener* 
2. *Régulateurs de tension linéaires* 
3. *Régulateurs de tension fixe* en circuit intégré

Le *montage à diode Zener* (cf. figure [ref:a_stab_z_diode]) constitue un montage très simple de stabilisation de la tension de sortie, car la diode Zener peut maintenir la tension de sortie stable dans certaines limites.

La diode Zener est toujours exploitée avec une résistance série et en sens inverse ($-U_Z$). Les diodes Zener dont la tension de claquage $U_Z$ est supérieure à $\qty{5}{\volt}$ présentent une allure de caractéristique très raide (cf. figure [ref:a_z_diode_kennlinie]) et conviennent donc très bien à la stabilisation de tension. Le rendement du montage est très faible, car il faut tenir compte des pertes dans la résistance série $R_V$ et dans la diode Zener. 

<margin>
[picture:323:a_stab_z_diode:Stabilisation de tension à diode Zener]
[picture:862:a_z_diode_kennlinie:Caractéristique d'une diode Zener]
</margin>

La résolution de l'exercice suivant est un peu plus laborieuse. On détermine d'abord la puissance de sortie à partir de la résistance de charge et du courant de charge. On calcule ensuite la puissance d'entrée absorbée à partir de la tension d'alimentation et de la somme du courant de charge et du courant de la diode Zener. Le rendement résulte alors du rapport entre la puissance délivrée et la puissance absorbée.

[question:AD321]

---

Les *régulateurs de tension linéaires* stabilisent la tension de sortie en exploitant un transistor de puissance comme résistance variable qui, avec la résistance de charge, forme un diviseur de tension.

<margin>
[picture:1079:a_diskrete_pannungsstabilisierung:Stabilisation de tension réalisée en composants discrets]
</margin>

Dans la question suivante est représentée une stabilisation de tension discrète avec transistor ballast. Une tension de référence de $\qty{5,6}{\volt}$ est produite à la base du transistor au moyen d'une diode Zener. Le potentiel d'émetteur est, en régime de fonctionnement d'un transistor au silicium, inférieur d'environ $\qty{0,6}{\volt}$ au potentiel de base. La tension de sortie régulée est alors d'environ $\qty{5}{\volt}$.

Le courant de charge traverse également le transistor, qui devient donc très chaud lorsque le courant de charge est élevé. Les transistors dits ballast se trouvent donc toujours, dans les stabilisations de tension à régulation linéaire, sur un dissipateur thermique. 

<margin>
[photo:246:a_Längstransistor 2N3055 auf Kühlkörper:Le transistor ballast d'une alimentation à régulation linéaire doit supporter de fortes puissances dissipées et est donc monté sur un dissipateur thermique.]
</margin>

[question:AD315]

La puissance dissipée $P_V$ résulte de la différence de  $P_{\mathrm{in}} - P_{\mathrm{out}}$. Avec la formule de la puissance $P = U \cdot I$, la puissance dissipée peut être calculée.

[question:AD319]

Avec les régulateurs de tension linéaires, le rendement est souvent très faible par nature. Il y a à ce sujet une question sur le rendement, qui peut être résolue avec la formule connue vue plus haut $\eta = \frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}$. 

[question:AD320]

---

Outre la diode Zener et le régulateur de tension linéaire, il existe aussi des *régulateurs de tension fixe* en circuit intégré. Les régulateurs de tension fixe fonctionnent comme les régulateurs de tension linéaires à transistor ballast et contiennent une source de tension de référence très précise ainsi qu'une régulation électronique optimale. Même si la tension d'entrée fluctue fortement (par ex. $\qty{\pm 2}{\volt}$), la variation de tension du côté de la charge n'est mesurable que dans le domaine du millivolt. Les condensateurs des deux côtés du régulateur de tension fixe doivent être choisis conformément aux prescriptions du fabricant, sinon des oscillations indésirables peuvent apparaître dans le comportement de régulation du montage.

<margin>
[picture:200:a_Festspannungsregler:Régulateur de tension fixe]
</margin>

---

Un régulateur de tension fixe maintient sa tension de sortie largement constante, tant que la tension d'entrée est suffisamment supérieure à la tension de sortie. La tension de sortie reste donc quasiment inchangée, même si la tension d'entrée fluctue.

[question:AD316]
[question:AD317]

<tip>
Pour que le circuit de régulation interne fonctionne de façon optimale, la tension d'entrée doit être, pour un régulateur de tension fixe standard (par ex. le type 7812 pour une tension fixe de $\qty{12}{\volt}$), supérieure d'env. $\qty{3}{\volt}$ à la tension de sortie, donc d'au moins $\qty{15}{\volt}$. Il existe des régulateurs de tension fixe pour lesquels la tension d'entrée ne doit être supérieure que de $\qty{1}{\volt}$ à la tension de sortie. Ces régulateurs sont appelés régulateurs de tension à faible chute (Low-Drop).
</tip>

---

Pour résoudre l'exercice suivant, nous utilisons à nouveau la relation connue : la puissance dissipée $P_V$ du régulateur de tension fixe résulte de la différence entre $P_{\mathrm{in}}$ et $P_{\mathrm{out}}$.

[question:AD318]

<tip>
La démarche de résolution commence par le calcul du courant de charge : $I_L$. Remarque : le courant dans la ligne de masse du régulateur de tension fixe est négligeable et n'est donc pas pris en compte.
</tip>

<margin>
[photo:245:a_Festspannungsregler:Régulateurs de tension fixe pour $\qty{5}{\volt}$, $\qty{12}{\volt}$ et $\qty{9}{\volt}$ sur dissipateur thermique]
</margin>
  