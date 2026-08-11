Les *convertisseurs* (Konverter) et les *transverters* sont employés dans le radioamateurisme pour donner accès, avec des appareils radio existants, à des gammes de fréquences supplémentaires que ces appareils ne couvrent pas à l'origine. Un *convertisseur* ne transpose le signal que dans une seule direction, soit sur le trajet d'émission, soit sur le trajet de réception. Un *transverter*, en revanche, dispose d'une commutation émission/réception interne et assure la transposition de fréquence aussi bien à l'émission qu'à la réception. La transposition de fréquence dans les convertisseurs et les transverters s'effectue toujours par mélange dans un ou plusieurs mélangeurs.

Par exemple, avec un transverter approprié et un émetteur-récepteur décamétrique existant, on peut aussi trafiquer dans les gammes VHF/UHF/SHF. On transposerait par exemple la bande des $\qty{10}{\meter}$ de l'émetteur-récepteur décamétrique, au moyen d'un transverter, vers le $\qty{2}{\meter}$/$\qty{70}{\centi\meter}$ ou le $\qty{23}{\centi\meter}$, dans les deux directions.

[question:EF501]
[question:EF502]

---

Considérons dans un premier temps le schéma synoptique d'un convertisseur sur la figure [ref:e_konverter]. Un tel convertisseur pourrait par exemple être utilisé pour transposer un signal issu d'un appareil VHF à destination du satellite radioamateur QO-100, qui nécessite une fréquence d'entrée dans la bande des $\qty{2,4}{\giga\hertz}$. Un transverter n'est ici pas forcément nécessaire, car la réception s'effectue via une clé SDR et un LNB.

Le schéma synoptique fait apparaître qu'une plage de fréquences d'entrée définie est transposée vers une autre plage de fréquences de sortie à l'aide d'au moins un mélangeur. Aucune commutation émission/réception n'est prévue. Un convertisseur ne peut donc transposer un signal que dans une seule direction, soit sur le trajet de réception (RX), soit sur le trajet d'émission (TX). Les convertisseurs destinés à l'émission comportent souvent une commande PTT, qui active les étages amplificateurs du convertisseur en cas d'émission.

La bande de fréquences vers laquelle un convertisseur transpose le signal peut se déterminer par calcul à partir de la fréquence d'oscillateur appliquée au mélangeur ainsi que de la fréquence d'entrée ou de sortie. Dans l'exemple concret, la fréquence cible résulte du produit de mélange de
$\qty{144}{\mega\hertz} + \qty{2,256}{\giga\hertz} = \qty{2,4}{\giga\hertz}$,
le produit souhaité étant ensuite sélectionné par des filtres appropriés.

<margin>
[picture:651:e_konverter:Circuit convertisseur, par ex. pour QO-100]
</margin>

[question:EF504]

---

Le circuit d'un transverter se distingue bien de celui d'un convertisseur. Les figures [ref:e_transverter_rx] et [ref:e_transverter_tx] montrent le schéma synoptique d'un transverter qui permet de trafiquer sur la bande des $\qty{2}{\meter}$ avec un émetteur-récepteur décamétrique $\qty{10}{\meter}$. On utilise pour cela une commutation émission/réception ainsi que deux mélangeurs et deux trajets de signal séparés — un pour la réception (RX) et un pour l'émission (TX).

En émission, la branche TX transpose le signal de sortie de l'émetteur-récepteur vers la bande de fréquences supérieure souhaitée, tandis qu'en réception, la branche RX abaisse par mélange le signal provenant de l'antenne vers la bande de fréquences adaptée à l'émetteur-récepteur. Les bandes de fréquences entre lesquelles le transverter travaille peuvent se déterminer par calcul, en connaissant la fréquence de l'oscillateur appliquée aux mélangeurs ainsi que les fréquences d'entrée et de sortie respectives. Ces relations sont représentées sur les figures.

L'oscillateur stabilisé par quartz ($G$) produit une fréquence de $\qty{38,666}{\mega\hertz}$, qui est portée à $\qty{116}{\mega\hertz}$ à l'aide d'un multiplicateur de fréquence 1:3. En réception, comme représenté sur la figure [ref:e_transverter_rx], le signal d'entrée de la plage $\qtyrange{144}{146}{\mega\hertz}$ est abaissé par mélange vers la plage $\qtyrange{28}{30}{\mega\hertz}$. En émission, comme montré sur la figure [ref:e_transverter_tx], le signal de sortie de l'appareil radio, dans la plage $\qtyrange{28}{30}{\mega\hertz}$, est élevé par mélange vers la plage $\qtyrange{144}{146}{\mega\hertz}$. Comme d'habitude, des filtres appropriés sont employés dans les deux trajets de signal pour sélectionner les produits de mélange souhaités ; ils ne sont pas représentés ici par souci de lisibilité.

[question:EF503]

<margin>
[picture:842:e_transverter_rx:Transverter sur le trajet RX]
[picture:843:e_transverter_tx:Transverter sur le trajet TX]
</margin>

Les transverters et convertisseurs conçus pour des fréquences d'entrée ou de sortie élevées (dans le domaine des GHz) doivent disposer d'un oscillateur très stable. À cause de la multiplication de fréquence interne, les erreurs de la fréquence d'oscillateur conduisent, du fait des fréquences de sortie élevées, à des écarts inacceptables sur la fréquence cible pour les modes à bande étroite ou la SSB. Un écart de la fréquence d'oscillateur est en effet multiplié lui aussi par la multiplication de celle-ci. On utilise souvent un TCXO ou un OCXO, qui peut en outre être synchronisé par une source de référence externe (par exemple GPS), afin de stabiliser au mieux la fréquence de l'oscillateur et de maintenir faibles les écarts sur la fréquence cible.

[question:EF505]