Techniquement, un multiplicateur de fréquence est réalisé de telle sorte que le signal d'entrée est d'abord appliqué à un étage distordeur non linéaire. Il peut s'agir par ex. d'un amplificateur de classe C. Ensuite, l'harmonique souhaité du signal est sélectionné dans le mélange de signaux au moyen de filtres et transmis à l'étage suivant. Comme la multiplication de fréquence repose sur les harmoniques, seuls des multiples entiers de la fréquence fondamentale sont possibles. En pratique, on n'utilise (à quelques exceptions près) que le 2e harmonique ou le 3e harmonique de la fréquence fondamentale (doublement, triplement).
Pour atteindre des multiplications de fréquence plus élevées, on met donc en cascade des étages de doublement ou de triplement, de sorte que leurs facteurs se multiplient ensuite.

[question:AF311]

La multiplication de fréquence et, le cas échéant, sa mise en cascade produisent des fréquences intermédiaires qui peuvent souvent conduire à des perturbations. C'est pourquoi les étages de multiplication de fréquence doivent être très bien blindés, afin de réduire au maximum les rayonnements indésirables.

[question:AF313]

Un montage typique de multiplicateur (voir figure [ref:a_frequenzvervielfacher_schaltung] ) contient un étage amplificateur qui est délibérément exploité sans tension de polarisation de base. Il en résulte un amplificateur en fonctionnement classe C, qui distord fortement le signal d'entrée et à la sortie duquel le signal est prélevé au moyen de filtres. Pour les filtres, on utilise ici des circuits oscillants appropriés, qui sont en résonance sur la fréquence souhaitée et sont le plus souvent accordables.

<margin>
[picture:489:a_frequenzvervielfacher_schaltung:Exemple de montage d'un multiplicateur de fréquence avec amplificateur de classe C sans tension de polarisation de base]
</margin>

[question:AF312]

Lorsque plusieurs étages multiplicateurs sont montés en cascade à l'intérieur d'un appareil, des perturbations peuvent apparaître sur des fréquences qui se forment entre les différents étages multiplicateurs. Pour déterminer ces fréquences, il faut calculer le cheminement du signal à travers les différents étages et les fréquences présentes à leur suite. C'est pourquoi l'ordre des étages multiplicateurs correspondants revêt une importance décisive dans la détermination des fréquences perturbatrices.

[question:AF314]
