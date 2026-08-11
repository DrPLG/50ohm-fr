[question:AC401]

La diode pn se compose de deux régions semi-conductrices qui, par le procédé du dopage, ont soit un excès d'électrons libres (n), soit un excès de trous libres (p). À droite et à gauche de la surface de séparation naît ce qu'on appelle une zone de charge d'espace, qui ne contient pratiquement aucun porteur de charge libre. La zone n constitue la cathode, la zone p l'anode. 

Si l'on applique à la diode une tension directe (positif sur l'anode, négatif sur la cathode), des électrons sont envoyés de la zone dopée n vers la zone p et des trous de la zone p vers la zone n. Ainsi s'obtient la bonne réponse.

Ce qui peut éventuellement prêter à confusion, c'est que le sens conventionnel du courant est opposé au sens du flux d'électrons. La flèche du courant pointe donc de l'anode vers la cathode, bien que le flux d'électrons aille de la cathode vers l'anode.

[question:AC403]

Les diodes pn présentent une dépendance exponentielle du courant de diode à la tension de diode. Le courant de saturation augmente quand la température augmente. Cela fait que la tension de diode nécessaire pour un courant de diode donné devient plus petite quand la température augmente. La « tension directe » diminue donc (en règle empirique de $\qty{-2}{\milli\volt\per\kelvin}$ d'élévation de température).
<indepth>

Le courant de diode est :
  
$I_D(T) = I_S(T) \cdot e^{\frac{U_D}{U_T}}$
  
$I_S$ est le courant de saturation, $U_T = k T/q$ ce qu'on appelle la tension thermique. Ici, $k$ est la constante de Boltzmann, $q$ la charge élémentaire.
  
Quand la température augmente, le courant de saturation augmente et la fonction exponentielle diminue. C'est toutefois la dépendance en température du courant de saturation qui l'emporte.

</indepth>

[question:AC404]

---

La diode à capacité variable (cf. figure [ref:a_diode_kapazitaet]) exploite la capacité entre les zones n et p par-dessus la zone de charge d'espace, de manière analogue à un condensateur plan. Mais aucun courant continu notable ne doit alors circuler, la diode doit donc être polarisée en sens inverse.

<margin>
[picture:1068:a_diode_kapazitaet:Symbole de la diode à capacité variable]
</margin>

Plus la tension de diode est négative (ou plus la tension inverse est élevée), plus la zone de charge d'espace s'étend et plus la capacité de la diode diminue.

Dans les questions AC405 et AC406, des *diodes antiparallèles* sont employées pour limiter l'amplitude d'une tension alternative. De tels circuits sont utilisés p. ex. pour protéger les entrées de récepteurs contre des tensions qui pourraient détruire les transistors d'entrée.

[question:AC405]

Il s'agit ici de diodes au silicium, qui ont une tension de seuil d'environ $\qty{0,6}{\volt}$. Donc, quand la tension d'entrée dépasse $\qty{0,6}{\volt}$, la diode de droite devient passante. Quand elle descend en dessous de $\qty{-0,6}{\volt}$, la diode de gauche devient passante.

À la première demi-onde, la tension nécessaire n'est pas encore atteinte, elle est donc transmise inchangée. Les deux demi-ondes suivantes ont en revanche des amplitudes qui dépassent la tension de seuil. Les amplitudes sont « écrêtées » à $\qty{\pm 0,6}{\volt}$.

[question:AC406]

La solution se déroule de manière analogue à l'exercice précédent — mais les diodes sont ici des *diodes au germanium*, la tension de seuil est d'environ $\qty{0,3}{\volt}$. C'est pourquoi toutes les demi-ondes sont écrêtées.

[question:AC407]

Dans ce qui suit sont décrits des composants qui interagissent avec la lumière : la photorésistance et la photodiode.

La photorésistance est un composant qui dispose de deux contacts non bloquants. Elle se comporte comme une résistance ohmique conventionnelle — le courant croît linéairement avec la tension appliquée. La valeur de la résistance peut être diminuée par absorption de lumière — les photons absorbés augmentent la densité des porteurs de charge libres. Si aucune tension n'est appliquée, aucun courant ne circule.

---

La photodiode, en revanche, est une diode pn (cf. figure [ref:a_photodiode]). La lumière y est absorbée dans la zone de charge d'espace ; il se forme des paires électron-trou qui sont séparées dans le champ électrique de la zone de charge d'espace. Ce champ existe aussi sans polarisation externe. Un courant circule même pour $U_D=0$ (un courant de court-circuit). Ce courant a le sens opposé au courant de diode conventionnel. 

<margin>
[picture:1069:a_photodiode:Symbole de la photodiode]
</margin>

---

[question:AC408]

Les optocoupleurs réunissent une diode électroluminescente et une photodiode dans un même boîtier, le côté entrée (diode électroluminescente) et le côté sortie (photodiode) étant isolés l'un de l'autre (séparation galvanique).

Ces composants sont employés pour séparer galvaniquement des interfaces, par exemple pour empêcher des boucles de masse qui peuvent provoquer un ronflement secteur induit.

<margin>
[picture:1070:a_optokoppler:Symbole de l'optocoupleur]
</margin>