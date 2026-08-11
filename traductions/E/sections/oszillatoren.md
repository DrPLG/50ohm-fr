Les oscillateurs comptent parmi les éléments de circuit les plus importants du radioamateurisme. Ils sont pour ainsi dire le cœur de tout appareil radio. Les oscillateurs servent à produire des oscillations haute fréquence dans les émetteurs et les récepteurs. Il existe différentes façons de réaliser techniquement des oscillateurs.

---

<margin>
[include:applet_schwingkreis]
</margin>

La forme la plus simple d'oscillateur est ce qu'on appelle l'*oscillateur LC*, qui contient comme éléments déterminant la fréquence un circuit oscillant (composé d'une bobine et d'un condensateur), que nous avons découvert au chapitre précédent.

[question:ED501]

Les oscillateurs LC ont l'inconvénient que leurs composants déterminant la fréquence (L et C) peuvent varier fortement en fonction de la température, ce qui peut conduire à d'importants écarts de fréquence.

Selon le formulaire, la formule de la fréquence d'oscillation (formule de Thomson) est :

$ f_0 = \frac{1}{2\pi \sqrt{L\cdot C}} $

La fréquence d'un oscillateur LC change lorsque la valeur du condensateur ou de la bobine varie, par exemple sous l'effet de la température. La formule permet de voir comment cela agit sur la fréquence :
lorsque la capacité du condensateur *augmente* ou que l'inductance de la bobine augmente, *la fréquence du circuit oscillant diminue*. Inversement, *la fréquence augmente* lorsque la capacité ou l'inductance *diminue*.

[question:ED503]
[question:ED505]
[question:ED502]
[question:ED504]

La vitesse de variation de la température détermine aussi la vitesse de variation de la fréquence d'un oscillateur. La fréquence ne varie cependant pas par sauts, car les effets thermiques sont toujours soumis à une certaine inertie. C'est pourquoi la fréquence d'un oscillateur exposé à des températures fluctuantes varie la plupart du temps lentement dans un sens ou dans l'autre.

[question:EF304]

Un type d'oscillateur nettement plus stable en fréquence est l'*oscillateur à quartz*. On utilise ici comme composant déterminant la fréquence un quartz, dont la fréquence de résonance ne dépend que très faiblement de la température (en comparaison avec les oscillateurs LC).

[question:ED506]
[question:ED507]

Pour éviter les rayonnements indésirables, les oscillateurs ainsi que les étages tampons devraient toujours être aussi bien blindés que possible. On peut y parvenir, par exemple, en montant l'oscillateur dans un boîtier métallique mis à la terre.

[question:EF207]