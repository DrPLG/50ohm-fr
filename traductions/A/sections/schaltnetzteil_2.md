L'alimentation à découpage a déjà été expliquée de façon introductive en classe N et E. Nous examinons maintenant plus précisément le schéma fonctionnel simplifié.

<margin>
[picture:35:a_schaltnetzteil:Schéma de principe d'une alimentation à découpage]
</margin>

L'important interrupteur électronique du bloc E sert aussi à la régulation d'une tension de sortie constante.
Comme il n'existe pas d'états intermédiaires entre transistor passant et transistor bloqué, il doit y avoir une autre possibilité de régulation. Le transport d'énergie du côté entrée vers le côté charge peut être varié par le temps de commutation. Si l'interrupteur est fermé plus longtemps, davantage d'énergie est transportée vers le côté charge et la tension de sortie augmente. Pour le constater, il faut un retour d'information de la tension de sortie vers le bloc de commande de l'interrupteur électronique. Cette contre-réaction manque dans le schéma simplifié représenté. La régulation de la tension de sortie s'effectue ainsi via le modulateur de largeur d'impulsion. Cela signifie que l'état passant de l'interrupteur est modifié, la fréquence de découpage restant quant à elle constante. 

---

[question:AD311]

La séparation galvanique du côté entrée et du côté sortie est également importante, afin de tenir les potentiels de la tension secteur éloignés de la sortie. Cette séparation du secteur est réalisée par le transformateur à noyau de ferrite. 
Voir figure [ref:a_innenansicht_eines_schaltnetzteils]. 

<margin>
[photo:264:a_innenansicht_eines_schaltnetzteils:Vue intérieure d'une alimentation à découpage]
</margin>

---

La variation du temps de commutation provoque des signaux perturbateurs supplémentaires, qui doivent impérativement être tenus éloignés du côté de la tension secteur, afin qu'ils ne se propagent pas via le réseau électrique et ne perturbent pas d'autres appareils électroniques. Le réseau électrique agit aussi comme une antenne et peut donc rayonner les signaux perturbateurs sous forme d'onde électromagnétique. Si l'interrupteur électronique est exploité avec une fréquence de découpage de $\qty{30}{\kilo\hertz}$, il en résulte un spectre perturbateur dans lequel un signal perturbateur apparaît tous les $\qty{30}{\kilo\hertz}$. La figure [ref:a_störspektrum] montre le spectre perturbateur d'une alimentation à découpage. Le spectre perturbateur a été reçu directement au-dessus du boîtier de l'alimentation à découpage. À $\qty{1}{\meter}$ de distance, le spectre perturbateur est à peine mesurable.

[question:AD312]

Lorsque les alimentations à découpage sont insuffisamment déparasitées, le spectre perturbateur nuit à la réception radio.

[question:AD313]

<margin>
[photo:277:a_störspektrum:Spectre perturbateur d'une alimentation à découpage]
</margin>

---

Pour empêcher que des perturbations ne parviennent dans le réseau électrique, un filtre passe-bas de qualité doit être intégré dans l'alimentation à découpage, du côté du raccordement au réseau de tension alternative $\qty{230}{\volt}$. La structure typique du filtre est visible sur la figure [ref:a-schaltnetzteilfilter].

<margin>
[picture:367:a-schaltnetzteilfilter:Filtre à l'entrée $\qty{230}{\volt}$ d'une alimentation à découpage]
</margin>

Compare aussi les filtres des figures [ref:a_EMV_Filter1] et [ref:a_EMV_Filter2]
*Retiens :* le conducteur PE ne doit pas être relié au conducteur L1 ni au conducteur N.
La self T ne doit pas produire de fonction de transformateur pour la tension alternative du secteur.

[question:AD314]


<margin>
Filtre CEM = filtre de déparasitage radio contre les perturbations conduites
[photo:242:a_EMV_Filter1: Filtre de déparasitage radio pour une alimentation à découpage]
[photo:243:a_EMV_Filter2: Filtre directement à l'entrée de tension AC $\qty{230}{\volt}$]
</margin>