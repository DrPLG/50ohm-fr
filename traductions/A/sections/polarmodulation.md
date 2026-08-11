Un procédé connu depuis des décennies trouve depuis quelque temps un usage croissant dans le service amateur : la *modulation polaire*. La figure [ref:polar_modulator] montre le schéma fonctionnel du procédé. Les deux composantes du signal $I(t)$ et $Q(t)$, telles que décrites au chapitre précédent, y sont converties en une amplitude instantanée $A(t)$ et une phase $\varphi(t)$ :

$A(t)=\sqrt{I^2(t)+Q^2(t)}$

$\varphi(t)=\operatorname{atan2}\left(Q(t),I(t)\right)$

L'information de phase $\varphi(t)$ module ensuite une porteuse HF d'amplitude constante. Le signal obtenu contient donc déjà l'information de phase complète, tout en conservant une enveloppe constante. Il n'a de ce fait pas besoin d'être amplifié par un amplificateur de puissance linéaire. On peut au contraire employer un amplificateur à commutation particulièrement efficace, par exemple un amplificateur de classe E. De tels amplificateurs atteignent souvent, en pratique, des rendements supérieurs à $\qtyrange{80}{90}{\percent}$.

L'information d'amplitude $A(t)$ est appliquée à la tension d'alimentation de l'amplificateur de puissance au moyen d'un amplificateur d'enveloppe rapide. L'amplitude de sortie varie ainsi conformément à l'enveloppe souhaitée. On retrouve en sortie le signal complet, modulé en amplitude et en phase :

$s(t)=A(t)\cos\left(\omega_\mathrm{p}t+\varphi(t)\right)$

Pour que le signal reste aussi peu distordu que possible, le trajet d'amplitude et le trajet de phase doivent être accordés dans le temps avec une grande précision.

Le rendement élevé de l'amplificateur de puissance fait qu'une moindre part de la puissance électrique est convertie en chaleur. Cela économise du courant, réduit le besoin de refroidissement et permet des appareils radio plus petits et plus légers, sans gros dissipateur métallique. La modulation polaire convient donc particulièrement aux appareils radio QRP alimentés par batterie, mais elle est désormais également employée dans des émetteurs-récepteurs commerciaux plus puissants. Ce sujet ne fait l'objet d'aucune question d'examen directe, mais c'est un procédé passionnant, qui sera de plus en plus utilisé à l'avenir dans les équipements radioamateurs.

<margin>
[picture:1117:polar_modulator:Modulateur polaire]
</margin>
