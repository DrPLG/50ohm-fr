La **ligne de transmission** [index:Ligne de transmission] (ou ligne d'alimentation) porte la puissance de l'émetteur à l'antenne. Deux familles sont d'usage courant.

Le **câble coaxial** [index:Câble coaxial] : une **âme** centrale, un **isolant** (le diélectrique), un **blindage** en tresse ou en feuillard, une **gaine** de protection. Bien employé, il ne rayonne pas et ne capte rien : le champ reste enfermé entre l'âme et le blindage. On peut donc le poser le long d'un mur ou dans un fourreau.

La **ligne bifilaire** [index:Ligne bifilaire] : deux conducteurs parallèles maintenus à distance constante par des entretoises, ou noyés dans un ruban isolant (« échelle à grenouille », ruban $\qty{300}{\ohm}$). Ses pertes sont **bien plus faibles**, car elle contient peu d'isolant, et elle supporte des **tensions plus élevées**. En revanche, elle doit être tenue à l'écart des objets métalliques et des murs, qui la perturbent.

<margin>
[picture:657:harec_station_ligne:Station, ligne d'alimentation et antenne]
</margin>

---

| l: | l: câble coaxial | l: ligne bifilaire |
| tensions par rapport à la terre | **asymétrique** : seule l'âme | **symétrique** : égales et opposées |
| impédance caractéristique | $\qty{50}{\ohm}$, $\qty{75}{\ohm}$ en télévision | $\num{300}$ à $\qty{600}{\ohm}$ |
| pertes | plus élevées, croissent avec la fréquence | faibles |
| pose | facile, insensible à l'entourage | à distance des masses métalliques |
[table:harec_coax_bifilaire:Câble coaxial et ligne bifilaire]

L'**impédance caractéristique** [index:Impédance caractéristique] d'une ligne ne dépend que de sa géométrie et de son isolant, **pas de sa longueur** ; la sortie d'antenne des émetteurs d'amateur est presque toujours prévue pour $\qty{50}{\ohm}$. Son calcul, le **coefficient de vélocité** et l'**affaiblissement linéique** sont traités au chapitre *Propagation et antennes*.

Aux puissances et aux fréquences élevées, on choisit un connecteur adapté : la **fiche N**, étanche et à impédance constante, convient jusqu'à plusieurs gigahertz.
