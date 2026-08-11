Un vieux proverbe de radioamateur dit que le meilleur amplificateur haute fréquence est l'antenne. Dans les premières années de la radiotechnique, elle était le seul « amplificateur » ; l'électronique amplificatrice n'existait pas. En 1907 apparut le tube électronique — un composant qui rencontra un grand succès, mais tout de même assez encombrant et peu performant. Dès les années 1920, la science rêvait de composants de fonction similaire, mais où tout se déroulerait à l'intérieur d'un solide (semi-conducteur), et non dans le vide. Le premier composant à y parvenir en pratique fut, en 1947/1948, le *transistor bipolaire*, qui fait aussi très majoritairement l'objet des questions de l'examen de la classe E.

[question:EC602]

<indepth>
Le *transistor bipolaire* est aussi appelé en anglais BJT : Bipolar Junction Transistor, soit transistor bipolaire à jonction.
</indepth>

La fonction idéale de tous les types de transistors, et aussi du tube électronique, est celle d'une *source de courant commandée en tension* : une variation de tension aussi petite que possible à l'entrée doit provoquer une variation de courant aussi grande que possible à la sortie.

Le transistor bipolaire a trois bornes, appelées émetteur, base et collecteur. L'émetteur envoie des porteurs de charge dans la base — dans le transistor bipolaire NPN, ce sont des *électrons*, dans le transistor bipolaire PNP des électrons déficitaires, aussi appelés *trous*. Nous n'aborderons la physique derrière ces notions que dans la formation à la classe A. Ces porteurs de charge traversent la base et sont récupérés par le collecteur.

---

La figure [ref:e_npn_pnp_symbol] montre les symboles des transistors NPN et PNP. On reconnaît l'électrode d'émetteur à une flèche qui, pour le transistor PNP, pointe vers la base et, pour le transistor NPN, s'éloigne de la base.

<margin>
[picture:864:e_npn_pnp_symbol:Symboles des transistors NPN et PNP]
</margin>

[question:EC605]
[question:EC606]
[question:EC607]
[question:EC608]
[question:EC609]

---

Les transistors bipolaires sont constitués de deux diodes — la diode émetteur-base et la diode base-collecteur.
En fonctionnement actif, la diode émetteur-base est toujours polarisée en sens direct. Pour le transistor NPN, le potentiel de la base doit alors être plus positif que celui de l'émetteur ; pour le transistor PNP, plus négatif. La diode base-collecteur est polarisée en sens inverse. Pour cela, le potentiel du collecteur doit être choisi plus positif que la base pour le transistor NPN, plus négatif pour le transistor PNP.

<tip>
La fonction de transistor ne s'établit toutefois que si la zone de base entre l'émetteur et le collecteur ne fait au maximum que quelques micromètres de largeur. Nous ne pouvons donc pas fabriquer un transistor en soudant deux diodes séparées l'une à l'autre.
</tip>

La tension minimale à la jonction émetteur-base dépend du semi-conducteur utilisé. Pour un transistor NPN au silicium, la base doit être environ $\qty{0,6}{\volt}$ plus positive que l'émetteur ; pour un transistor PNP au silicium, environ $\qty{0,6}{\volt}$ plus négative.

[question:EC610]
[question:EC612]
[question:EC613]
[question:EC614]
[question:EC615]

---

<margin>
[picture:863:e_npn_i_u:Courants et tensions sur un transistor NPN]
</margin>

---

Les courants et tensions sur un transistor NPN sont représentés sur la figure [ref:e_npn_i_u]. Nous connaissons déjà la tension base-émetteur $U_\mathrm{BE}$, de même que la tension collecteur-base $U_\mathrm{CB}$. Le courant de collecteur $I_\mathrm{C}$ dépend de façon exponentielle de la tension base-émetteur :

$I_\mathrm{C} = I_\mathrm{S}\ e^{\frac{U_\mathrm{BE}}{U_\mathrm{T}}}$

$U_\mathrm{T}$ vaut environ $\qty{26}{\milli\volt}$ à température ambiante.

<indepth>
$I_\mathrm{S}$ désigne le courant inverse de saturation d'un transistor bipolaire. C'est un paramètre caractéristique du composant, étroitement lié à la diode émetteur-base. Il s'agit d'un très faible courant de fuite qui circule à travers le transistor même lorsque la jonction base-émetteur n'est pas conductrice.
</indepth>

Le courant de base $I_\mathrm{B}$ présente, dans de larges plages de fonctionnement, la même dépendance en tension que le courant de collecteur, si bien que le rapport du courant de collecteur au courant de base est constant :

$\frac{I_\mathrm{C}}{I_\mathrm{B}} = B$

*$B$* est le gain en courant (plus précisément le gain en courant en montage émetteur commun). Il est souvent plus commode de se représenter le transistor comme un composant commandé en courant, même si physiquement ce n'est pas le cas. Le gain en courant vaut, dans les transistors réels, $50 \dots 350$.

<tip>
Pour la commande en courant du transistor bipolaire, il existe une très vieille analogie faisant intervenir un grand et un petit canal d'eau, une vanne dans le grand canal et un clapet de commande. Les plus âgés d'entre nous la connaissent peut-être encore du « Kleiner Radiomann » des éditions Kosmos…
  
[picture:835:e_transistor_wehr_geschlossen:Le canal de commande ferme complètement la vanne]
  
Au début, aucune eau ne circule dans le petit canal. La vanne du grand canal est fermée, aucune eau n'y circule donc non plus.
  
[picture:837:e_transistor_wehr_halb_offen:Le canal de commande ouvre la vanne à moitié]

Puis l'eau commence à circuler dans le petit canal, le canal de commande. L'eau soulève le clapet, qui à son tour actionne la vanne — l'eau commence aussi à circuler dans le canal principal.
  
[picture:836:e_transistor_wehr_geoeffnet:Le canal de commande ouvre complètement la vanne]

Maintenant, davantage d'eau circule dans le canal de commande, le clapet est soulevé davantage, la vanne du canal principal s'ouvre complètement.
</tip>

[question:EC603]

Le courant d'émetteur $I_E$ est la somme du courant de collecteur et du courant de base :

$I_\mathrm{E} = I_\mathrm{C} + I_\mathrm{B}$

[question:EC611]

Le point de fonctionnement en tension des transistors est généralement indiqué par la tension collecteur-émetteur :

$U_\mathrm{CE} = U_\mathrm{CB} + U_\mathrm{BE}$

Outre les transistors bipolaires traités ici principalement, il existe surtout aussi les *transistors à effet de champ*, qui fonctionnent différemment sur le plan physique, mais présentent extérieurement la même fonction de base (source de courant commandée en tension). Sous la forme des MOSFET, ils dominent notre électronique, car ils sont présents par millions, voire par milliards, dans les circuits intégrés de l'électronique numérique.

<indepth>
MOSFET signifie *metal-oxide-semiconductor field effect transistor*, soit transistor à effet de champ métal-oxyde-semi-conducteur.
</indepth>

[question:EC604]

Les transistors peuvent être utilisés non seulement comme amplificateurs, mais aussi comme interrupteurs (de courant) (courant on/off) ou encore, pour de faibles tensions en sortie, comme résistance commandable. Cette dernière fonction est surtout réalisée avec des transistors à effet de champ.

[question:EC601]
