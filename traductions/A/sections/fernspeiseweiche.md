Les préamplificateurs déportés ou les convertisseurs de réception montés sur les antennes nécessitent une alimentation en tension continue. Afin d'économiser une ligne d'alimentation en tension continue supplémentaire, la tension d'alimentation peut aussi être transmise via le câble coaxial, parallèlement au signal HF, sans que les deux signaux se perturbent mutuellement. Pour injecter la tension continue dans le câble coaxial, on utilise donc un séparateur d'alimentation à distance, ou en anglais BIAS-T. La figure [ref:a_qo100_bias_t] montre une station QO-100 avec séparateur d'alimentation à distance pour l'alimentation du préamplificateur (LNB).

<margin>
[picture:1080:a_qo100_bias_t:Station QO-100 avec séparateur d'alimentation à distance pour l'alimentation du LNB]
</margin>

[question:AD322]

Techniquement, ce montage peut être réalisé, comme représenté sur la figure [ref:a_bias_t], avec un circuit très simple. Le séparateur d'alimentation à distance (BIAS-T) se compose, outre les connecteurs, uniquement de deux condensateurs et d'une inductance. Nous avons déjà rencontré ce montage avec le MMIC, dont la tension d'alimentation est injectée via la sortie au moyen d'un BIAS-T.

<margin>
[picture:399:a_bias_t:Séparateur d'alimentation à distance (BIAS-T)]
</margin>

[question:AD323]

On reconnaît un BIAS-T au fait que, d'un côté, le signal HF est acheminé vers le récepteur (RX), tandis que de l'autre côté est raccordé un préamplificateur ou un convertisseur de réception (LNA). De plus, une tension continue d'alimentation est injectée via le raccordement DC. Cette tension continue parvient, via l'inductance, sur le conducteur intérieur du câble coaxial et alimente ainsi le LNA raccordé. L'inductance agit ce faisant comme une haute impédance pour la haute fréquence, de sorte que le signal HF ne s'écoule pas dans l'alimentation.

Le condensateur de liaison $C_1$ empêche que la tension continue injectée ne parvienne à l'entrée du récepteur. Sans le condensateur $C_1$, la tension d'alimentation pourrait donc être court-circuitée à la masse.

[question:AD324]

---

L'inductance sert à injecter la tension continue d'alimentation dans la ligne, tout en constituant une résistance élevée pour la haute fréquence. La tension continue peut ainsi parvenir au LNA sans que le signal HF ne s'écoule dans l'alimentation. Le condensateur $C_2$ dérive les composantes haute fréquence restantes vers la masse. Cela empêche que des signaux HF ne se couplent dans l'alimentation.

<indepth>
[photo:288:a_Bias T Platine:Circuit imprimé BIAS - T - réalisé avec KiCAD]
Voici à quoi pourrait ressembler la mise en œuvre pratique du schéma représenté sur un circuit imprimé. $C_2$ et $C_3$ sont des condensateurs de découplage pour différentes plages de fréquences, afin que la fonction soit assurée sur une large plage de fréquences. $L_1$ sert à l'acheminement de la tension continue et doit être dimensionnée spécifiquement pour le courant de charge. Le condensateur de découplage $C_2$ du côté tension continue doit supprimer la tension HF. Il doit être choisi de telle sorte qu'il présente, à la fréquence HF utile, une réactance inférieure à 1 ohm.
</indepth>

La bobine entre le côté DC (côté tension continue, par ex. $\qty{12}{\volt}$) et le côté HF (par ex. signal de réception à $\qty{10}{\giga\hertz}$) ne doit pas laisser passer les composantes haute fréquence vers le côté DC. Il s'agit donc d'une self de choc, qui doit présenter une haute impédance à la fréquence utile (par ex. $X_L = \qty{10}{\kilo\ohm}$). Le courant d'alimentation du préamplificateur ou du convertisseur (LNA) traverse cette self de choc. Le diamètre du fil de la self de choc doit être suffisamment grand pour que le courant continu d'alimentation ne provoque pas d'échauffement de la self de choc. Autrement dit : la bobine doit présenter une tenue en courant correspondante. 

[question:AD325]