La fréquence d'un VFO dépend directement de sa tension de service (tension continue). Cela est provoqué avant tout par la dépendance du point de fonctionnement du transistor de son oscillateur.
Pour atteindre une stabilité de fréquence aussi élevée que possible d'un VFO vis-à-vis des fluctuations de la tension de service, celle-ci doit être *stabilisée en tension* aussi bien que possible par des mesures appropriées au niveau du montage. La tension de service d'un VFO devrait donc être indépendante des tensions de service des autres étages (stabilisée) et être *filtrée et découplée* aussi bien que possible. Cela peut être obtenu par exemple au moyen d'un régulateur de tension fixe (cf. figure [ref:a_osc_stab]).

[question:AD612]
[question:AD608]
[question:AD607]

<margin>
[picture:200:a_osc_stab:Régulateur de tension fixe]
</margin>

---

Lorsque la tension de service est mal stabilisée, les émetteurs CW très simples peuvent présenter une perturbation de la hauteur du son, appelée *chirp* : au début de chaque dit ou de chaque dah, la hauteur du son est d'abord un peu plus élevée ou un peu plus basse, puis se rapproche de la hauteur véritable. Le mot anglais « chirp » signifie littéralement « gazouillis ». Lorsque la hauteur du son se rapproche par le haut, l'effet acoustique évoque effectivement un gazouillis.

[question:AD609]

<margin>
Voici un exemple d'un tel signal chirpé :

[include:applet_chirp_1]

Un autre exemple, un QSO entre RA1OW et OM3YCY, dans lequel l'effet de chirp est nettement audible lors du deuxième passage :

[include:applet_chirp_2]

</margin>
