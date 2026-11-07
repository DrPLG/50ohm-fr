Une onde radio associe un champ électrique et un champ magnétique, perpendiculaires entre eux et à la direction de propagation. La **polarisation** [index:Polarisation] est, par convention, l'orientation du **champ électrique** par rapport au sol.

<margin>
[picture:326:harec_polarisation_h:Antenne à polarisation horizontale]
</margin>

* **Horizontale** : champ électrique parallèle au sol.
* **Verticale** : champ électrique perpendiculaire au sol.
* **Circulaire** : le champ électrique tourne d'un tour par période, à droite ou à gauche selon le sens.

Pour un dipôle ou une Yagi, le champ électrique suit les éléments : une antenne aux éléments **horizontaux** polarise **horizontalement**, une verticale polarise verticalement. La règle ne vaut pas pour toutes les antennes : une petite boucle magnétique posée à plat polarise verticalement, et la polarisation d'un cadre dépend de l'endroit où on l'alimente.

---

En **VHF et au-delà**, l'onde arrive en ligne directe et garde sa polarisation : les deux stations doivent utiliser **la même**. Une antenne horizontale face à une antenne verticale perd beaucoup de signal, souvent plus de $\qty{20}{\dB}$ ; une antenne circulaire face à une antenne linéaire en perd environ $\qty{3}{\dB}$. L'usage : verticale pour le trafic FM et les relais, horizontale pour la BLU et la télégraphie à grande distance.

En **ondes courtes**, l'ionosphère fait tourner la polarisation pendant le trajet : elle compte beaucoup moins.

<margin>
[picture:51:harec_polarisation_v:Antenne à polarisation verticale]
</margin>

La polarisation circulaire s'obtient avec deux dipôles croisés alimentés avec un déphasage de $\qty{90}{\degree}$, ou avec une antenne hélice. Elle évite les pertes dues à la rotation de l'onde, d'où son emploi pour les satellites.
