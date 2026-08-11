Contrairement à la transmission de la parole, beaucoup de procédés de transmission numériques (digimodes) n'ont besoin que d'une très faible largeur de bande. Alors que les signaux de parole en SSB occupent typiquement une largeur de bande d'environ $\qty{2,4}{\kilo\hertz}$, les digimodes se contentent de plages de fréquences nettement plus étroites. Ainsi, par exemple, le BPSK31 n'a besoin que d'environ $\qty{31,25}{\hertz}$ de largeur de bande, tandis que le FT8 se contente d'environ $\qty{50}{\hertz}$. Les signaux produits par les digimodes sont habituellement, sur les ondes courtes, également modulés en SSB. La largeur de bande HF du signal rayonné correspond alors exactement à la largeur de bande BF du digimode.

[question:EE402]
[question:EE403]

À l'intérieur de la largeur de bande de réception SSB usuelle d'environ $\qty{2,4}{\kilo\hertz}$, plusieurs de ces signaux digimodes à bande étroite peuvent être reçus simultanément.

<margin>
[picture:718:e_digimode_ssb_empfang_mehrerer_digimodes:Diagramme en cascade de la réception de plusieurs signaux digimodes à l'intérieur de la largeur de bande SSB de 2,4 kHz. Chaque colonne est la transmission d'un signal différent]
</margin>

[question:EE404]

Par un simple calcul, on peut loger dans une largeur de bande SSB de $\qty{2,4}{\kilo\hertz}$ jusqu'à 48 signaux FT8 ($\frac{\qty{2400}{\hertz}}{\qty{50}{\hertz}}$), voire jusqu'à 76 signaux BPSK31 ($\frac{\qty{2400}{\hertz}}{\qty{31,25}{\hertz}}$). Sur l'ordinateur, on peut ensuite soit sélectionner de manière ciblée un seul signal digimode, soit — selon le logiciel — décoder simultanément une multitude de ces signaux. C'est précisément cette haute efficacité spectrale qui rend les digimodes à bande étroite particulièrement attractifs pour le trafic radioamateur.

---

La Slow-Scan Television (SSTV) désigne la transmission d'images fixes à l'aide de données d'image numérisées. Les images y sont transmises ligne par ligne, ce qui autorise une vitesse de transmission relativement faible. Il existe différents procédés SSTV, qui se distinguent notamment par la résolution, la profondeur de couleur et la durée de transmission. Un avantage essentiel de la SSTV est la faible largeur de bande nécessaire : elle est typiquement inférieure à $\qty{3}{\kilo\hertz}$ et correspond ainsi à peu près à la largeur de bande d'un signal de parole SSB. La SSTV peut de ce fait être employée aussi dans les bandes décamétriques et convient particulièrement bien aux transmissions d'images à l'échelle mondiale dans le service radioamateur. La figure [ref:e_digimode_ssb_sstv] montre une image SSTV typique.

À l'opposé se trouve l'Amateur Television (ATV), qui transmet des images animées — donc de la véritable télévision. En raison de la quantité d'information nettement plus grande, l'ATV exige une largeur de bande considérablement plus importante, typiquement plusieurs mégahertz, souvent $\qty{6}{\mega\hertz}$ ou plus. Pour cette raison, l'ATV n'est pas réalisable dans les bandes décamétriques et n'est employée que dans les gammes de fréquences plus élevées, la plupart du temps à partir de la bande des $\qty{70}{\centi\meter}$, ou par exemple dans le domaine $\unit{\giga\hertz}$ via QO-100. Des plages de fréquences suffisamment larges y sont disponibles pour fournir la largeur de bande nécessaire aux transmissions d'images animées.

[question:EE415]

<margin>
[photo:84:e_digimode_ssb_sstv:Confirmation d'une liaison SSTV à F1BIB par ON1GA avec le RST 575 et, en plus, l'image reçue à l'origine]
</margin>
