Avant d'aborder la puissance rayonnée, nous avons vu que la preuve du respect des valeurs limites de protection des personnes n'est exigée qu'à partir d'une certaine puissance rayonnée. Maintenant que nous savons ce que signifie l'EIRP, nous pouvons la chiffrer : pour les stations radioamateur fixes, la procédure de justification ne doit être menée que si l'installation d'émission atteint une puissance rayonnée de $\qty{10}{\watt}$ EIRP ou plus.

[question:VE508]
[question:VE507]

---

% Da für Klasse N die Strahlungsleistung ohnehin auf $\qty{10}{\watt}$ EIRP beschränkt ist, spielt das Nachweisverfahren eigentlich erst für Inhaber der Klassen E und A eine praktische Rolle. Da aber der Bereich Vorschriften auch in Klasse N bereits komplett geprüft wird, können wir es in keinem Fall vermeiden, uns mit den folgenden Fragen zum Nachweisverfahren zu beschäftigen.

<indepth>
À y regarder *de près*, il faut relever que les radioamateurs de classe N peuvent exploiter des installations jusqu'à $\qty{10}{\watt}$ EIRP, et que la preuve du respect des valeurs limites de protection des personnes est exigée dès $\qty{10}{\watt}$ EIRP. Si l'on exploitait donc une installation à exactement $\qty{10}{\watt}$ EIRP, on serait tenu d'apporter la preuve à l'autorité. En pratique, il ne faut de toute façon pas pousser la valeur maximale à sa limite, mais rester au moins légèrement en dessous. On évite ainsi de dépasser par inadvertance la puissance rayonnée admissible du fait d'erreurs de mesure ou d'autres imprécisions. Et il n'y a alors pas non plus d'obligation de mener la procédure de justification.
</indepth>

---

<margin>
[photo:79:n_Deckblatt_Anleitung:Page de couverture du guide]
</margin>

La déclaration de respect des valeurs limites de protection des personnes pour une station radioamateur de plus de $\qty{10}{\watt}$ EIRP, dans le cadre de la procédure de justification de la limitation des champs électromagnétiques (BEMFV), doit être déposée auprès de l'antenne compétente de la BNetzA avant la mise en service de l'installation radioamateur.

<tip>
L'antenne compétente peut être trouvée sur le [site web de la Bundesnetzagentur](https://50ohm.de/so).
</tip>

Le cœur de la procédure de justification est le calcul de la *distance de sécurité pour la protection des personnes*, aussi appelée *distance de sécurité liée au site*. C'est la distance autour d'une antenne à l'intérieur de laquelle les valeurs limites de protection des personnes ne sont *pas* respectées. Il faut garantir qu'aucune personne non autorisée ne se trouve dans cette zone pendant l'émission. Cela est en principe considéré comme acquis lorsque cette zone se situe entièrement sur son propre terrain, dans la *zone contrôlable*.

Outre la déclaration, constituée de quelques formulaires, il faut joindre une représentation graphique *compréhensible* (nachvollziehbar) de la distance de sécurité liée au site et de la zone contrôlable par l'exploitant de la station. Pour établir la déclaration, la BNetzA met un guide à disposition en téléchargement.

[question:VE509]

---

<tip>
Le mot-clé de la bonne réponse, pour cette question et la suivante, est chaque fois le terme « compréhensible » (nachvollziehbar).
</tip>

[question:VE512]

D'autres documents techniques doivent être établis, p. ex. une documentation *compréhensible* du respect des exigences, des diagrammes d'antennes, des plans de situation, un dessin de construction ou un croquis coté. Ceux-ci ne sont toutefois pas à joindre à la déclaration, mais à tenir à disposition à la station radioamateur et à présenter à la demande de la Bundesnetzagentur.

[question:VE513]
[question:VD107]

Tous les documents établis doivent être régulièrement vérifiés quant à leur actualité. Si l'installation radioamateur a été modifiée au point de ne plus correspondre à la situation antérieure, une nouvelle déclaration doit être déposée. C'est le cas, p. ex., lors de l'érection d'un mât d'antenne supplémentaire, ou quand un changement d'antenne ou une puissance d'émission plus élevée rend nécessaire une distance plus grande qu'auparavant.

[question:VE514]
[question:VE510]

---

Le respect des valeurs limites et la distance de sécurité pour les personnes qui en résulte doivent être justifiés soit par des calculs, soit par des mesures d'intensité de champ, et documentés de façon compréhensible. Le calcul peut s'effectuer avec la procédure d'évaluation simplifiée, par calcul en champ lointain ou en champ proche, ainsi qu'avec le logiciel « [Watt Wächter](https://50ohm.de/ww) » publié par la Bundesnetzagentur. Les procédures de calcul sont décrites dans un document téléchargeable auprès de l'autorité.

<margin>
[photo:80:n_Bewertungsverfahren:Ce document décrit les procédures d'évaluation.]
</margin>

[question:VE506]
[question:VE515]

Il arrive que des radioamateurs émettent sur plusieurs fréquences en même temps. Le calcul de la distance de protection des personnes doit donc prendre en compte toutes les émissions simultanées d'une station radioamateur fixe. Si l'on émet avec plus d'une antenne à la fois, toutes les antennes doivent être considérées ensemble pour la distance de protection. C'est toujours le cas lorsque les distances de sécurité respectives se chevauchent.

[question:VE516]
[question:VE517]

<france>
# Une déclaration, pas une justification

La France a bien une formalité pour les stations fixes, mais elle n'a ni le même objet ni le même déclencheur que l'*Anzeige* allemande.

Le déclencheur est une **PAR supérieure à 5 W**, et non 10 W PIRE. Le destinataire est l'**ANFR**, non le régulateur. Le délai est de **deux mois après l'installation**, et non avant la mise en service. Et le contenu tient en trois informations : les coordonnées géographiques WGS 84 de l'installation et la PAR maximale utilisée en HF, VHF, UHF et SHF. La déclaration se fait en ligne sur le téléservice de l'ANFR. C'est l'objet des articles 4 et 5 de l'arrêté du 17 décembre 2007 modifié.

Ce qui n'est **pas** demandé mérite d'être souligné, parce que c'est tout le contenu de la procédure allemande : aucun calcul de distance de sécurité, aucune représentation graphique de la zone contrôlable, aucun diagramme d'antenne, aucun plan de masse, aucun dossier technique à tenir à disposition. La déclaration française sert à cartographier les émetteurs, pas à démontrer le respect des valeurs limites. Un changement de matériel n'appelle une nouvelle déclaration que s'il modifie l'une des données déclarées.

Elle n'est pas pour autant une formalité sans portée : un radioamateur qui veut déposer une demande d'instruction de brouillage auprès de l'ANFR doit avoir préalablement déclaré sa station fixe.

L'obligation de fond, elle, demeure : respecter le décret n° 2002-775. Elle repose entièrement sur l'exploitant.
</france>
