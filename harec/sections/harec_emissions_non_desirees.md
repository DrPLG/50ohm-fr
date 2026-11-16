Un émetteur idéal ne produirait qu'une sinusoïde pure, sur sa seule fréquence. Un émetteur réel produit aussi des **émissions non désirées** [index:Émissions non désirées], qui tombent souvent hors des bandes d'amateur, dans la radiodiffusion, l'aéronautique ou la téléphonie.

<margin>
[picture:1008:harec_harmoniques_parasites:Émissions non désirées — harmoniques et émissions parasites]
</margin>

* Les **harmoniques** [index:Harmonique] sont les multiples entiers de la fréquence d'émission : $2f$, $3f$… Elles naissent de toute déformation du signal, en particulier quand un étage final est **saturé** ou mal réglé. Une émission sur $\qty{145,9}{\mega\hertz}$ a sa quatrième harmonique à $\qty{583,6}{\mega\hertz}$, en pleine bande de télévision.
* Les **émissions parasites** proches de la porteuse élargissent le signal et gênent les voisins de bande : en BLU, le *splatter*, dû surtout à un gain micro trop élevé ; en FM ou en AFSK, une excursion ou un niveau BF trop forts.
* Un **oscillateur instable** peut faire sortir l'émission de la bande, surtout sur un montage ancien sans quartz.

Le terme réglementaire est **rayonnements non essentiels** : leur niveau maximal, fixé par renvoi à l'appendice 3 du RR, est donné au chapitre *Réglementation nationale*.

---

<margin>
[picture:591:harec_passe_bas:Réponse d'un filtre passe-bas]
</margin>

Contre les harmoniques, on place un **filtre passe-bas** [index:Filtre passe-bas] à la sortie de l'émetteur : il laisse passer la fréquence d'émission et affaiblit tout ce qui est au-dessus de sa **fréquence de coupure**. Un émetteur multibande commute un filtre par bande ; c'est le « clic » de relais qu'on entend en changeant de bande. Les émetteurs monobandes, en VHF et au-delà, emploient plutôt un **filtre passe-bande**, qui affaiblit aussi les produits situés sous la fréquence d'émission.

Les émissions parasites proches de la porteuse, en revanche, ne se filtrent pas : on les évite à la source, par un réglage correct du micro, de la modulation et des étages, et par un étage final travaillant **sans distorsion**. Après tout réglage du point de fonctionnement d'un étage final, on revérifie sa linéarité.

Les émissions non désirées se contrôlent à l'**analyseur de spectre**, en aval de tout ce qui est intercalé entre l'émetteur et l'antenne.
