% Halbleiter II
% DF2DR 2024-08-19

Le matériau de base de notre monde moderne, ce sont les matériaux semi-conducteurs. Raison suffisante pour s'y intéresser d'un peu plus près. Les semi-conducteurs ont une structure cristalline en réseau, c'est-à-dire que leurs atomes sont disposés de manière périodique. 

<margin>
[picture:854:a_silizium_halbleiter:Cristal semi-conducteur de silicium]
</margin>

Tous les matériaux semi-conducteurs ont deux propriétés en commun :

---

Il existe une *bande interdite* (Energiebandlücke), qui est une conséquence de la structure périodique. Cela signifie que les électrons dans le cristal ne peuvent pas prendre certaines énergies. L'énergie la plus élevée des électrons liés aux atomes, nous l'appelons *énergie de la bande de valence*. Mais comme les électrons sont tous liés aux atomes du réseau, ils ne peuvent pas contribuer au passage du courant. Il existe encore d'autres états d'énergie que les électrons peuvent atteindre — ils se situent dans la *bande de conduction*, qui se trouve au-dessus du bord de la bande de valence, à une distance égale à la largeur de la bande interdite. Les électrons de la bande de conduction peuvent contribuer au passage du courant si nous appliquons une tension à l'échantillon semi-conducteur. Ils ont pour cela besoin d'une énergie plus grande que la bande interdite. Ils peuvent absorber cette énergie sous forme d'énergie thermique, raison pour laquelle les semi-conducteurs de haute pureté sont de très bons isolants aux basses températures.

[question:AB104]

<margin>
L'énergie de la bande interdite est déterminée par la composition chimique du semi-conducteur. Comparé au Si, le Ge a une énergie de bande interdite nettement plus petite, le GaAs et l'InP une un peu plus grande et le GaN une beaucoup plus grande.
</margin>

Le silicium (Si) et le germanium (Ge) sont des *semi-conducteurs élémentaires* (comme d'ailleurs aussi le diamant, qui est du carbone cristallin). Mais il existe aussi des composés chimiques qui sont des semi-conducteurs (*semi-conducteurs composés*), comme l'arséniure de gallium (GaAs), le phosphure d'indium (InP) ou encore le nitrure de gallium (GaN). 

---

Les matériaux à bande interdite ne sont désignés comme semi-conducteurs que s'ils sont en plus *dopables*. Leur conductivité peut être modifiée dans de larges limites par une contamination ciblée du matériau semi-conducteur de haute pureté. Ainsi, l'arsenic (As) a, comparé aux semi-conducteurs élémentaires, un électron de plus dans la couche électronique externe. Cet électron peut très facilement et avec peu d'énergie devenir un électron libre dans la bande de conduction. Un tel dopage est appelé *dopage n*.

<margin>
[picture:855:a_n_dotierung:Dopage n]
</margin>

---

Mais que se passe-t-il si nous contaminons le semi-conducteur avec un matériau qui a un électron de moins dans la couche électronique externe ? Une telle lacune électronique est appelée un *trou*. Comme l'atome était neutre auparavant, la lacune électronique porte une charge positive. Les trous peuvent eux aussi se déplacer dans le cristal et contribuer à un passage de courant. Un tel dopage est appelé *dopage p*.

<margin>
[picture:856:a_p_dotierung:Dopage p]
</margin>

En résumé, nous pouvons constater :
* Le dopage n produit dans le semi-conducteur un excès d'électrons.
* Le dopage p produit dans le semi-conducteur un excès de trous.

[question:AB105]
[question:AB106]
[question:AB107]

---

Si l'on combine dans un cristal, mais séparées spatialement, des zones dopées p et dopées n, un échange de porteurs de charge a lieu dans le plan de contact : des électrons se déplacent de la zone dopée n vers la zone dopée p, des trous se déplacent de la zone dopée p vers la zone dopée n. Ce mouvement de porteurs de charge, provoqué par les différences de densité des électrons et des trous, est appelé courant de diffusion.

Cette séparation de charges produit d'autre part un champ électrique à l'effet opposé, qui conduit à un courant de champ. À l'équilibre (sans tension appliquée de l'extérieur), les effets de la diffusion et du champ électrique se compensent exactement. Entre les zones p et n naît une région sans porteurs de charge libres, que l'on appelle *zone d'appauvrissement* (Verarmungszone) ou *couche d'arrêt* (Sperrschicht). Une telle structure constitue une *diode pn*.

[question:AB108]

<margin>
[picture:857:a_pn_uebergang:Jonction PN]
</margin>

---

Appliquons maintenant de l'extérieur une tension qui est plus positive sur la zone p (*anode*) que sur la zone n (*cathode*). L'électrode positive attire des électrons par-dessus la zone d'appauvrissement, et l'électrode négative des trous. La zone d'appauvrissement se résorbe, un courant s'établit. Cela constitue le fonctionnement en *sens direct*.

<margin>
[picture:956:a_pn_uebergang_mit_spannung:Jonction PN avec tension externe]
</margin>

[question:AC402]

---

Si nous inversons maintenant la tension, la zone d'appauvrissement s'élargit, le passage du courant s'arrête. C'est le *fonctionnement en sens inverse* de la diode.

<margin>
[picture:957:a_pn_uebergang_mit_spannung:Jonction PN avec tension externe]
</margin>


[question:AB109]