Par nature, le processus de mélange qui a lieu dans un récepteur superhétérodyne (cf. figure [ref:spiegelfrequenzen_mischen1]) fait toujours apparaître, avec la fréquence d'oscillateur du récepteur, deux fréquences de réception possibles :

$f_\text{ZF} = \left|f_\text{e} \pm f_\text{o}\right|$

Comme nous voulons, dans le récepteur superhétérodyne, abaisser le signal par mélange vers une fréquence intermédiaire plus basse, c'est ici en particulier la fréquence différence qui est intéressante :

$f_\text{ZF} = \left|f_\text{e} - f_\text{o}\right|$

La valeur absolue est ici déterminante — pour une fréquence d'oscillateur $f_\text{o}$ et une fréquence intermédiaire $f_\text{ZF}$ fixées, il existe deux fréquences de réception possibles qui produisent toutes deux la même fréquence intermédiaire. L'une est la fréquence de réception souhaitée, l'autre est appelée *fréquence image*.

<margin>
[picture:807:spiegelfrequenzen_mischen1:Processus de mélange avec la fréquence de réception $f_\text{e}$, la fréquence d'oscillateur $f_\text{o}$ et la fréquence intermédiaire $f_\text{ZF}$]
</margin>

---

<margin>
[picture:806:spiegelfrequenzen_fe1_fe2:Fréquences de réception conduisant toutes deux à la même $f_\text{ZF}$]
</margin>

Exemple — supposons que notre oscillateur oscille, comme le montre la figure [ref:spiegelfrequenzen_fe1_fe2], sur la fréquence $f_\text{o}=\qty{3,955}{\mega\hertz}$. La fréquence intermédiaire $f_\text{ZF}$ doit valoir $\qty{0,455}{\mega\hertz}$. En raison de la valeur absolue dans notre formule, il existe maintenant deux possibilités quant aux fréquences de réception que l'on peut entendre, à savoir $f_\text{e1} = \qty{3,500}{\mega\hertz}$ et $f_\text{e2} = \qty{4,410}{\mega\hertz}$. Pour ces deux valeurs, la formule donne la fréquence intermédiaire $f_\text{ZF}$.

Si $f_\text{e1}$ est la fréquence de réception souhaitée, alors $f_\text{e2}$ est appelée la *fréquence image* de $f_\text{e1}$. Si $f_\text{e2}$ est la fréquence de réception souhaitée, alors $f_\text{e1}$ est appelée la *fréquence image* de $f_\text{e2}$.

L'écart entre la fréquence de réception souhaitée et la fréquence image vaut ici toujours le double de la fréquence intermédiaire (FI), comme on peut aisément le voir sur la figure [ref:spiegelfrequenzen_fe1_fe2].

Si l'oscillateur oscille *au-dessus* de la fréquence de réception ($f_\mathrm{E} < f_\mathrm{OSC}$), alors la fréquence image se trouve elle aussi *au-dessus* de la fréquence de réception, au double de la FI ($f_\mathrm{S} = f_\mathrm{E} + 2\cdot f_\mathrm{ZF}$).

Si l'oscillateur se trouve en revanche *en dessous* de la fréquence de réception ($f_\mathrm{E} > f_\mathrm{OSC}$), alors la fréquence image se trouve elle aussi *en dessous* de la fréquence de réception, au double de la FI ($f_\mathrm{S} = f_\mathrm{E} - 2\cdot f_\mathrm{ZF}$). Cette relation figure également dans le recueil de formules.

Essaie maintenant, avec ces connaissances, de résoudre les questions suivantes.

[question:AF106]
[question:AF201]
[question:AF202]
[question:AF203]
[question:AF107]
[question:AF108]

---
<margin>
[picture:808:spiegelfrequenzen_mischen2:Filtre passe-bande supplémentaire pour la réjection de la fréquence image]
</margin>

Si elle est insuffisamment supprimée, la fréquence image peut provoquer des perturbations de réception, car les signaux qui se trouvent sur la fréquence image sont eux aussi transposés sur la même fréquence intermédiaire et peuvent de ce fait devenir audibles dans le récepteur. Pour éviter cela, la fréquence de réception souhaitée est sélectionnée par un filtre passe-bande dès avant le mélangeur, comme le montre la figure [ref:spiegelfrequenzen_mischen2]. La fréquence image doit alors être supprimée le plus fortement possible.

Pour une réjection efficace de la fréquence image, un écart aussi grand que possible entre la fréquence de réception souhaitée et la fréquence image est avantageux. Cet écart devient plus grand lorsqu'une fréquence intermédiaire plus élevée est choisie.

Cela se reconnaît également sur la figure [ref:spiegelfrequenzen_fe1_fe2] — à mesure que la FI augmente, les deux fréquences de réception possibles $f_\text{e1}$ et $f_\text{e2}$ s'écartent l'une de l'autre.

Plus cet écart de fréquence est grand, plus le passe-bande placé en amont peut facilement laisser passer la fréquence de réception souhaitée tout en atténuant fortement la fréquence image. Avec un écart très faible, le filtre devrait au contraire posséder des flancs nettement plus raides, ou encore une sélectivité plus élevée. Les exigences envers la présélection du récepteur en seraient sensiblement accrues.

[question:AF109]
[question:AF110]
[question:AF111]
[question:AF204]
