<margin>
[picture:542:n_digital_voice_repeaternetwork:Réseau de relais pour Digital Voice — station relais DB0FZ avec accès Internet, hotspot DN9YI et station relais DB0HOB reliée à DB0FZ par faisceau hertzien]
</margin>

La voix peut elle aussi être transmise en numérique, p. ex. avec les procédés DMR, D-Star, C4FM et M17. Selon le procédé, cela peut se faire avec un ordinateur ou avec un poste radio adapté. On peut ainsi, via des stations relais VHF ou UHF interconnectées, trafiquer avec des radioamateurs du monde entier. Lorsque deux stations relais ou plus sont interconnectées, les émissions reçues par l'une d'elles peuvent être retransmises via un réseau, p. ex. le HAMNET ou Internet, et réémises sur d'autres stations reliées. Pour accéder à un tel réseau de relais, on peut aussi exploiter chez soi un point d'accès appelé hotspot. Tant qu'aucune autorisation de station télécommandée n'a été obtenue, l'exploitation d'un hotspot ne peut se faire qu'en station occupée : il faut donc couper l'émetteur lorsqu'il n'est pas surveillé sur place. Sur ondes courtes, les liaisons vocales numériques s'établissent principalement en direct, par exemple avec FreeDV.

<webmargin>
| l: Abréviation | X: Procédé de transmission |
| D-STAR | Digital Smart Technologies for Amateur Radio |
| C4FM | Continuous 4-level frequency modulation |
| DMR | Digital Mobile Radio |
| M17 | Procédé de transmission libre (open source) |
[table:n_dv_uebertragungsverfahren:Procédés fréquemment utilisés pour la phonie numérique]
</webmargin>

[question:NE404]

---

En transmission numérique de la voix, les signaux vocaux sont convertis en un flux de données avant l'émission. Plusieurs de ces flux peuvent aussi être transmis en alternance rapide et périodique. C'est ce qu'on appelle le TDMA (Time Division Multiple Access) ou multiplexage temporel. Ainsi, deux liaisons vocales ou plus utilisent quasi simultanément la même fréquence. Pour un poste, cela signifie qu'avec la touche PTT enfoncée, il doit commuter en permanence et rapidement entre émission et réception pour ne pas perdre la cadence.

<margin>
[picture:474:n_digital_voice_tdma:TDMA avec trois liaisons sur une fréquence]
</margin>

<tip>
La plupart des amplificateurs de puissance externes ne peuvent pas commuter aussi vite entre émission et réception que le TDMA l'exigerait. C'est pourquoi, pour le DMR et les autres procédés à intervalles de temps, seuls des amplificateurs de puissance adaptés doivent être utilisés. Sinon, la fréquence se trouve occupée au-delà de son propre intervalle de temps, ce qui peut perturber les émissions d'autres stations sur la même fréquence.
</tip>

[question:NE403]

---

Contrairement aux émissions analogiques, où il suffit le plus souvent de connaître la fréquence et le type de modulation pour établir une liaison, la voix numérique demande souvent de tenir compte de davantage de réglages, par exemple le groupe de conversation (talkgroup), la salle ou le réflecteur servant à interconnecter les stations relais, ou encore l'intervalle de temps TDMA à utiliser.

<indepth>
Selon le procédé, il peut y avoir une multitude d'autres réglages, par exemple, en DMR, le color-code, qui permet à plusieurs groupes d'utilisateurs de partager une fréquence sans s'entendre mutuellement. De tels paramètres doivent être correctement réglés sur l'appareil avant le début d'une liaison pour que celle-ci s'établisse.
</indepth>

[question:NE402]

Sur les portatifs VHF/UHF et via les stations relais, on utilise souvent, à côté de la phonie FM, les procédés numériques DMR, D-Star ou C4FM.

[question:NE307]

% TODO: Auf die Tabelle wird nicht eingegangen und sie ist nicht komplett ... 
%<webmargin>
%| l: Verfahren | l: Eigene Kennung | l: Gruppenruf | l: Direktruf | X: Sonstige |
%| M17 | Rufzeichen | - | Rufzeichen | Channel Access Number (CAN), Übertragungsrate (1600 oder 3200 Bit/s) |
%| FreeDV | - | - | - | Mode (1600, 700C, 700D, 700E, 2020) |
%| DMR | DMR-ID | Talkgroup | DMR-ID | Color-Code (1 bis 4, im Amateurfunk meist 1), Zeitschlitz (TS 1 oder TS 2) |
%| C4FM | Rufzeichen | Reflektor | - | |
%| D-Star | Rufzeichen | ? | ? | |
%[table:n_digital_voice_verfahren:Verfahren für Digital Voice und mögliche Einstellungen]
%</webmargin>

<latexonly>
\newpage
</latexonly>

<france>
# Numérique et passerelles, côté français

La décision n° 2012-1241 a précisément été prise, en 2012, pour **permettre aux radioamateurs français d'utiliser les modes numériques** : c'est l'un des trois objectifs annoncés dans ses motifs, avec la mise en conformité au Règlement des radiocommunications. Aucune classe d'émission n'est donc interdite au titulaire du certificat actuel, sous réserve du plafond de largeur de bande.

Deux limites méritent d'être connues. Les titulaires de l'**ex-classe 3**, eux, restent enfermés dans une liste fermée de six classes d'émission : A1A, A2A, A3E, G3E, J3E et F3E. Un F0 ne peut donc pas légalement pratiquer les modes numériques modernes.

Et sur les **passerelles vers Internet**, la décision prend soin de préciser que la fixation des modalités de connexion d'une station d'amateur à un réseau ouvert au public ne relève pas de la compétence de l'ARCEP, mais du pouvoir réglementaire. La question n'est donc pas tranchée par ce texte — ce qui explique la prudence des exploitants de passerelles françaises.
</france>
