Les atténuateurs sont souvent nécessaires en technique HF pour affaiblir de façon définie le niveau des signaux. Un atténuateur de puissance permet par exemple de réduire la puissance de sortie d'un émetteur au point que son signal de sortie n'endommage ni ne sature les appareils de mesure raccordés. On utilise également des atténuateurs pour ramener les niveaux d'entrée des amplificateurs et des récepteurs à une valeur définie.

Un atténuateur doit ici toujours être conçu pour une impédance système définie en entrée comme en sortie. Dans les atténuateurs de structure symétrique, les impédances d'entrée et de sortie sont identiques. Il s'agit souvent des $\qty{50}{\ohm}$ usuels en technique HF. Pour qu'un atténuateur présente les impédances requises à son entrée et à sa sortie, une terminaison d'impédance correcte est nécessaire des deux côtés. Cela s'obtient par un réseau de résistances approprié. L'atténuation est ici indiquée en dB (décibels) et se rapporte à la puissance ; ainsi $\qty{20}{\dB}$ signifient par exemple une atténuation de la puissance d'entrée d'un facteur $\num{100}$. La puissance de sortie après cet atténuateur ne vaut donc plus que $\frac{1}{100}$ de la puissance d'entrée, ce qui, dans le cas d'une puissance d'entrée de $\qty{100}{\watt}$, correspond à une puissance de sortie de $\qty{1}{\watt}$.

Dans les atténuateurs ohmiques, l'atténuation se fait par transformation en chaleur de la puissance injectée. Si l'on atténue par exemple de $\qty{20}{\dB}$ un signal de $\qty{100}{\watt}$ comme décrit précédemment, $\qty{99}{\watt}$ sont transformés en chaleur dans l'atténuateur. La puissance restante de $\qty{1}{\watt}$ est alors encore disponible à la sortie de l'atténuateur.

[question:AD806]
[question:AD803]
[question:AD804]
[question:AD805]

Un atténuateur symétrique peut par exemple être réalisé en réseau en T ou en Pi à partir de résistances. La dénomination résulte ici de l'aspect de la disposition des résistances dans le montage.

<margin>
[picture:342:daempfungsglied_pi:Atténuateur en configuration PI avec source et résistance de charge]
</margin>

<margin>
[picture:341:daempfungsglied_t:Atténuateur en configuration T avec source et résistance de charge]
</margin>

%TODO: EVTL. PI ALS SONDERZEICHEN EINFÜGEN

[question:AD801]
[question:AD802]



