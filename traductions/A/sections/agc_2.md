Dans la classe E, nous avons déjà fait connaissance avec l'AGC (Automatic Gain Control, régulation automatique de gain). Lorsque les signaux d'entrée sont forts, l'AGC réduit le gain des étages amplificateurs de la chaîne de réception ; lorsqu'ils sont faibles, elle l'augmente en conséquence. L'amplitude du signal démodulé, et donc le volume du signal BF, est ainsi maintenue constante.
Sans AGC, les signaux forts satureraient la BF et les signaux faibles ne seraient audibles en BF que très faiblement. Le volume BF devrait être réajusté en permanence à la main. L'AGC compense ainsi la dynamique du signal reçu et adapte dynamiquement la sensibilité de la chaîne de réception en fonction des signaux HF d'entrée.

[question:AF224]

<margin>
[picture:1055:e_agc:L'AGC dans le récepteur superhétérodyne]
</margin>

---

Pour que l'AGC puisse adapter automatiquement le gain à la force du signal reçu, elle a besoin d'une information sur l'amplitude de celui-ci. Pour cela, une partie du signal FI peut être redressée puis lissée, comme le montre la figure [ref:e_agc_regelspannung].

La diode redresse le signal FI haute fréquence. Une cellule RC placée en aval supprime les composantes alternatives rapides, de sorte qu'il en résulte une tension continue dont l'amplitude dépend de celle du signal FI. Plus le signal reçu est fort, plus la valeur de cette tension est grande.

Cette *tension de régulation* est réinjectée vers les étages amplificateurs HF ou FI réglables, où elle sert à commander leur gain. Il en résulte une boucle de régulation fermée : un signal reçu plus fort entraîne une action de régulation plus forte, et donc un gain plus faible.

<margin>
[picture:142:e_agc_regelspannung:Tension de régulation de l'AGC]
</margin>

[question:AD503]