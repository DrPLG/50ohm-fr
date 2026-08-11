
% du kennst die zeitdarstellung
% du kennst die frequenzdarstellung
% fourier hat sich damit beschaeftigt wie man vom einen zum anderen kommt
% das zeitliche signal wir analysiert dahingehend wie "stark" welche sinusfrequenz enhalten ist
% zusammenfassung: jedes signal laesst sich in eine menge von sinusförmigen schwingungen aufteilen
% phase nicht vergessen

Venons-en maintenant à un sujet passionnant, qui a l'air plus compliqué qu'il ne l'est en réalité. On peut représenter les signaux de différentes manières. La représentation d'un signal dans le domaine temporel est sans doute bien connue. On y porte le temps sur l'axe des X et une valeur de tension ou de puissance sur l'axe des Y.

Savais-tu que tout signal peut être décomposé en oscillations sinusoïdales élémentaires ? Cela paraît fou, mais c'est ainsi. Tout signal peut être décrit par la superposition d'oscillations sinusoïdales pures, possédant une amplitude et une phase déterminées.

La transformation de Fourier est une fonction mathématiquement complexe (que nous ne détaillerons pas ici), qui analyse un signal disponible dans le domaine temporel et présente ensuite les différentes oscillations sinusoïdales qui composent ce signal. Cette information peut alors être représentée dans un diagramme du domaine fréquentiel, ou spectre de fréquences. L'axe des X y décrit désormais la fréquence et l'axe des Y la valeur de tension, ou encore la valeur de puissance, de la fréquence contenue dans le signal de départ. Un signal sinusoïdal pur à fréquence fixe se présente donc, dans le spectre de fréquences, comme un trait à sa fréquence.

La transformation de Fourier (également appelée transformation de Fourier discrète, en abrégé DFT) est, sous sa forme d'origine, une fonction mathématiquement lourde et complexe. Elle ne peut être mise en œuvre en logiciel que de manière très peu efficace. Au fil du temps, on a trouvé une méthode nettement plus efficace pour réaliser cette fonction mathématiquement complexe de façon plus simple — la transformation de Fourier rapide, ou FFT (Fast Fourier Transform). Son calcul s'en trouve considérablement simplifié, en particulier en logiciel et en matériel.

<indepth>
Les formes de signal non sinusoïdales, et en particulier celles qui présentent des « angles et arêtes » vifs, se composent de nombreuses composantes sinusoïdales de fréquences différentes et contiennent de nombreuses composantes harmoniques. Cet applet permet toutefois d'expérimenter d'ores et déjà la chose.

[include:fourier]
</indepth>

[question:AF630]

Rappelons-nous que les signaux très anguleux contiennent des composantes de fréquences plus élevées (les harmoniques). Si l'on observe maintenant un tel signal, par exemple un signal rectangulaire, dans le domaine fréquentiel, on remarque qu'il se compose d'un fort signal sinusoïdal à sa fondamentale, ainsi que de plusieurs signaux sinusoïdaux, de plus en plus faibles, aux multiples impairs de la fréquence fondamentale. C'est d'ailleurs aussi la raison pour laquelle il ne faut en aucun cas appliquer des signaux rectangulaires à une antenne avant qu'ils n'aient traversé un filtre passe-bas. Le filtre passe-bas fait en sorte, dans ce cas, que les composantes de signal plus élevées soient supprimées et que seule la fondamentale, sous la forme d'un signal sinusoïdal, sorte à sa sortie. Si l'on appliquait le signal rectangulaire directement à l'antenne, on recevrait une émission sur tous les multiples impairs de la fréquence fondamentale, ce qui perturberait à coup sûr massivement d'autres services de radiocommunication.

[question:AB404]
[question:AB405]
[question:AB406]
[question:AB407]
