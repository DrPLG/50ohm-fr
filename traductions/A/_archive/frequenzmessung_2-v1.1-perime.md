Il n'existe guère d'appareils radio sur lesquels on puisse mesurer directement la fréquence de réception. Les montages de récepteur usuels ne présentent aucun point où elle soit disponible. C'est pourquoi, pour contrôler l'affichage de la fréquence, on raccorde à la prise d'antenne un oscillateur ou un générateur de fréquence aussi précis que possible. Sa fréquence est comparée à l'affichage du récepteur.

<attention>
Un générateur de fréquence raccordé directement peut facilement endommager une entrée de récepteur. Dans le doute, la mesure devrait être commencée avec la tension la plus basse du générateur et un atténuateur.
</attention>

Naturellement, ici aussi, les oscillateurs disciplinés par GPS et les OCXO sont en règle générale plus précis que des montages plus simples.

[question:AI511]
[question:AI504]

---

Sur les émetteurs, la mesure de fréquence est plus simple. Un fréquencemètre est raccordé à la prise d'antenne par l'intermédiaire d'un atténuateur. Cette mesure n'a naturellement de sens que sur une porteuse non modulée.

<indepth>
Les émetteurs SSB ne produisent aucun signal en l'absence de modulation. Pour mesurer leur fréquence d'émission, on peut injecter dans la prise micro un signal audio de fréquence connue. En USB, la fréquence audio est retranchée de la valeur mesurée par le fréquencemètre à la sortie de l'émetteur, afin d'obtenir la fréquence de la porteuse non émise. En LSB, elle est ajoutée.
</indepth>

% AI502
[question:AI502]


[question:AI501]


% TODO Der Text wird noch fertig geschrieben. - DB7YI 2024-04-22

La mesure de fréquence à l'oscilloscope n'est qu'un pis-aller, car ces appareils ont rarement une base de temps aussi précise que les fréquencemètres.
% AI503
[question:AI503]

Les fréquencemètres simples travaillent presque toujours avec ce qu'on appelle un *temps de porte*. L'appareil ouvre l'entrée pendant un temps déterminé, compte les périodes du signal d'entrée et en calcule la fréquence. C'est particulièrement simple avec un temps de porte d'une seconde, car il donne directement le nombre d'oscillations par seconde, et donc la fréquence en hertz.

Le temps de porte est réglable sur la plupart des fréquencemètres. Un temps de porte court fait que l'affichage est actualisé à intervalles rapprochés. Avec un temps de porte long, en revanche, la mesure devient plus précise.

% TODO Bild, das die Ungenauigkeit bei kurzer Torzeit veranschaulicht

%AI505
[question:AI505]

% Fünf Fragen zu Genauigkeit und Toleranz, die ursprünglich hier standen, habe ich in den Abschnitt "Frequenzgenauigkeit" verschoben. - DB7YI 2024-04-28