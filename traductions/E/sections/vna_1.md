Un simple multimètre ne convient pas pour mesurer des résistances dépendantes de la fréquence. On peut utiliser à la place un analyseur de réseau vectoriel (VNA). Il s'agit d'un appareil de mesure actif qui détermine, pour une multitude de fréquences (une plage de fréquences réglable), comment le courant et la tension se comportent l'un par rapport à l'autre (rapport des amplitudes et déphasage entre la tension et le courant).

<margin>
[photo:201:e_vna_tiefpassmessung:Mesure d'un filtre passe-bas de $\qty{0}{\mega\hertz}$ à $\qty{100}{\mega\hertz}$ avec une fréquence de coupure à $\qty{30}{\mega\hertz}$]
</margin>

---

On peut ainsi déterminer, par exemple, à quelle fréquence un circuit oscillant ou un filtre présente une résistance (respectivement une impédance) particulièrement élevée ou particulièrement basse (cf. figure [ref:e_vna_tiefpassmessung]). On peut de même déterminer à quelle fréquence une antenne est en résonance, en observant le SWR sur une plage de fréquences, comme représenté sur la figure [ref:e_vna_swr].

<margin>
[photo:323:e_vna_swr:Mesure du SWR d'une antenne filaire alimentée en extrémité. Le SWR est presque de $1$ à $\qty{14}{\mega\hertz}$]
</margin>

[question:EI201]
[question:EI202]
[question:EI203]
[question:EI204]

Beaucoup de VNA devraient être calibrés avant utilisation, afin d'obtenir un résultat de mesure aussi précis que possible.

[question:EI205]

---

Pour le calibrage comme pour le test de fonctionnement, on mesure souvent les états « ouvert » (résistance infinie), « court-circuit » (résistance proche de zéro) et « adapté » (résistance de charge correspondant à la résistance de sortie de l'appareil de mesure).

<margin>
[photo:327:e_vna_solt:Kit de calibrage SOL(T). De gauche à droite — Load, Open, Closed]
</margin>

Avec une terminaison de ligne raccordée (par exemple une résistance de terminaison de $\qty{50}{\ohm}$), le VNA devrait afficher un SWR proche de $\num{1}$, puisqu'aucune puissance n'est réfléchie. Si rien n'est raccordé à la prise de mesure ou si celle-ci est court-circuitée, on obtient un SWR proche de l'infini (réflexion totale).

[question:EI206]
