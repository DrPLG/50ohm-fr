Les composants SMD ne mesurent que quelques millimètres. SMD signifie Surface-Mounted Device (en français : composant monté en surface). Contrairement aux composants classiques, ils ne possèdent pas de fils de connexion mais sont soudés directement sur le circuit imprimé — sans aucune traversée. Dans ce qui suit, nous nous intéressons au marquage des résistances SMD.

<margin>
[photo:318:e_platine_smd:Circuit imprimé avec des composants SMD]
</margin>

---

La figure [ref:e_smd] montre une résistance SMD. Pour indiquer la valeur de la résistance, des chiffres y sont imprimés — dans ce cas les chiffres 113. La valeur de la résistance se détermine alors ainsi : tous les chiffres sauf le *dernier* sont repris comme valeur numérique brute. Dans l'exemple 113, on obtient donc *11* comme valeur numérique. Le *dernier* chiffre indique la *puissance de dix* par laquelle il faut multiplier les autres chiffres. Un 1 correspond alors à la première puissance de dix $10^1$, un 2 à la deuxième puissance de dix $10^2$, et ainsi de suite.

<margin>
[picture:1006:e_smd:Composant SMD]
</margin>

Dans notre exemple, nous obtenons donc : $11 \cdot 10^3$, soit $\qty{11000}{\ohm}$ ohms ou $\qty{11}{\kilo\ohm}$.

[question:EC114]
[question:EC115]
[question:EC116]
[question:EC117]
