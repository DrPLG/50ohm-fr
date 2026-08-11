Une alimentation secteur (Netzgerät) convertit la tension alternative de $\qty{230}{\volt}$ de la prise de courant en une tension continue plus faible. Dans le radioamateurisme, nous utilisons souvent des alimentations qui fournissent à leur sortie une tension continue de $\qty{13,8}{\volt}$, pour alimenter par exemple un émetteur-récepteur.

<margin>
[picture:740:n_netzgeraet:Alimentation secteur]
</margin>

<indepth>
Pour le *contrôle de l'état de fonctionnement* d'une alimentation secteur, il existe des interrupteurs lumineux, des diodes électroluminescentes de contrôle ou des instruments d'affichage éclairés. Les instruments d'affichage peuvent indiquer séparément la tension de service en volts et l'intensité du courant circulant actuellement en ampères. Il existe aussi des affichages numériques commutables à cet effet.
</indepth>

[question:ND101]
[question:ND102]

---

Une alimentation secteur est souvent raccordée à la prise de courant au moyen d'une *fiche à contact de protection* (en abrégé fiche Schuko). Avec la fiche à contact de protection, le sens d'insertion n'a pas d'importance, car la polarité change constamment en tension alternative. La fiche et la prise ont chacune 3 pôles, comme on peut le voir dans la figure [ref:n_schutzkontakt]. Les broches de la fiche s'insèrent dans les ouvertures de la prise et permettent la liaison avec les conducteurs dits L et N, entre lesquels est présente la dangereuse tension alternative de $\qty{230}{\volt}$.

<margin>
[photo:86:n_schutzkontakt:Contact de protection sur une prise de courant et fiche Schuko]
</margin>

Le contact frotteur extérieur de la fiche Schuko s'appelle *contact de protection* (marqué en rouge dans la figure [ref:n_schutzkontakt]). Lors de l'insertion, le contact de protection se relie au conducteur dit *PE* de la prise. « PE » est l'abréviation du terme anglais « protective earth », qui signifie terre de protection. Lors de l'insertion de la fiche, le boîtier métallique de l'alimentation est donc mis à la terre. Une tension dangereuse sur le boîtier est ainsi exclue.

[question:ND109]

---

La sortie de l'alimentation et le câble de liaison vers l'émetteur-récepteur sont bipolaires, afin qu'un circuit électrique fermé puisse s'établir. C'est la condition pour que le courant puisse circuler de l'alimentation vers l'émetteur-récepteur, le traverser et revenir à l'alimentation. 

<webmargin>
[picture:680:n_Netzgeraet_TRX:Raccordement de l'alimentation et du TRX]
</webmargin>

Les bornes de sortie de la tension continue sont colorées : rouge pour le plus et noir pour le moins. Lors du raccordement du câble de liaison vers l'émetteur-récepteur, cette polarité doit impérativement être respectée. Sinon, un court-circuit peut se produire, voire, dans le cas extrême, la destruction de l'émetteur-récepteur. Ce n'est qu'une fois tous les câbles raccordés et la polarité vérifiée que l'alimentation devrait être mise en marche. 

[question:ND104]
[question:ND103]
[question:ND105]
[question:ND106]
[question:ND107]

---

Dans l'alimentation et dans le câble de liaison vers l'émetteur-récepteur se trouvent des fusibles miniatures (Feinsicherungen). Ceux-ci peuvent détecter un défaut (court-circuit ou surcharge) et interrompre le passage du courant. Il s'agit fréquemment de fusibles à fil fusible, dans lesquels un fil fin fond lorsqu'un courant trop important circule. Le circuit électrique n'est alors plus fermé et le courant ne peut plus circuler. On parle alors de *fusible grillé* ou, dans le langage technique, de *coupure thermique*.

<margin>
[photo:88:n_feinsicherungen:Fusibles miniatures]
</margin>

<indepth>
*Approfondissement :* les fusibles miniatures mesurent $\qty{5}{\milli\meter} \times \qty{20}{\milli\meter}$ et sont disponibles en différentes versions. Ils se distinguent par leur intensité et leur caractéristique de déclenchement. Les fusibles temporisés sont utilisés chaque fois que le courant d'enclenchement est nettement supérieur au courant nominal, par exemple dans les alimentations secteur. Le temps de déclenchement du fusible dépend de l'intensité du courant et de la durée de son passage. Le tableau [ref:n_feinsicherung] rassemble les valeurs usuelles du temps de déclenchement. Les fabricants fournissent des indications plus précises au moyen de courbes caractéristiques dans leurs fiches techniques.
</indepth>

Après qu'un fusible a fondu et que l'on a identifié et corrigé la cause, il faut le remplacer. Mais les fusibles défectueux ne doivent être remplacés que par des fusibles de même type ! Il faut veiller à la fois à l'intensité et à ce qu'on appelle la caractéristique de déclenchement, qui indique la rapidité avec laquelle un fusible se déclenche (rapide, semi-temporisé, temporisé).

<webmargin>
| l: Caractéristique de déclenchement | l: Marquage | X: Temps de coupure |
| rapide | F | max. $\qty{30}{\milli\second}$ |
| semi-temporisé | MT | max. $\qty{90}{\milli\second}$ |
| temporisé | T | max. $\qty{300}{\milli\second}$ |
[table:n_feinsicherung:Caractéristiques des fusibles miniatures, temps de coupure à dix fois le courant nominal]
</webmargin>

<danger>
*ATTENTION :* le pontage d'un fusible défectueux, parfois pratiqué, par exemple avec du papier aluminium, est interdit et très dangereux. Il y a risque d'incendie !
</danger>

Les alimentations de qualité possèdent souvent aussi une limitation électronique des courants. En cas de court-circuit, celle-ci veille à ce que l'intensité soit limitée. Cela s'appelle la *limitation du courant de court-circuit*. Une fois le défaut éliminé, aucun fusible ne doit être remplacé.

[question:ND108]
[question:NK305]
