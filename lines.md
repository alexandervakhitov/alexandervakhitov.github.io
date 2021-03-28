---
layout: page
title: Visual SLAM with Lines and Points 
permalink: /lines/
---
![Line and point SLAM](/assets/lld/lld_small.png)

Line segments are especially helpful for feature-based camera pose estimation in man-made 
environments with repetitive visual appearance and lack of unique texture.

In this project, we created solvers for the [*absolute*]({{site.url}}/pnpl/) and [*relative*]({{site.url}}/sego/) camera 
pose as well as [*mono-*]((https://www.albertpumarola.com/research/pl-slam/)) and [*stereo*](({{site.url}}/lld/)) SLAM systems based on the fusion of points and lines.
We developed a deep SLAM-oriented [*descriptor*](({{site.url}}/lld/)) for line segment matching. 

#### Collaborators
[Albert Pumarola](https://www.albertpumarola.com/), 
[Jan Funke](http://funkey.science/), 
[Antonio Agudo](http://www.iri.upc.edu/people/aagudo/), 
[Victor Lempitsky](http://sites.skoltech.ru/compvision/members/vilem/),
[Yinqiang Zheng](https://sites.google.com/site/yinqiangzheng/),
[Francesc Moreno-Noguer](https://www.iri.upc.edu/people/fmoreno/) 

#### Papers

[Uncertainty-Aware Camera Pose Estimation from Points and Lines]({{site.url}}/uncertain-pnp/)
<!-- [pdf]({{site.url}}/) 
[bib]({{site.url}}/) 
[code](https://github.com/alexandervakhitov/uncertain-pnp) -->

[Learnable Line Descriptor for Visual SLAM]({{site.url}}/lld/)
<!-- [pdf]({{site.url}}/scripts/publications/files/vakhitov-lld-2019.pdf) 
[bib]({{site.url}}/scripts/publications/bib/vakhitov2019learnable.bib) 
[code](https://github.com/alexandervakhitov/lld-slam) -->            

[Stereo relative pose from line and point feature triplets]({{site.url}}/sego/)
<!-- [pdf]({{site.url}}/scripts/publications/files/vakhitov2018.pdf) 
[bib]({{site.url}}/scripts/publications/bib/vakhitov2018stereo.bib) 
[code](https://github.com/alexandervakhitov/sego) -->           

[PL-SLAM: Real-time Monocular Visual SLAM with Points and Lines](https://www.albertpumarola.com/research/pl-slam/)
<!-- [pdf]({{site.url}}/scripts/publications/files/pl-slam-2017.pdf)
[bib]({{site.url}}/scripts/publications/bib/pumarola2017pl.bib) --> 

[Accurate and Linear Time Pose Estimation from Points and Lines]({{site.url}}/pnpl/)
<!--[pdf]({{site.url}}/scripts/publications/files/pnpl2016.pdf)
[bib]({{site.url}}/scripts/publications/bib/vakhitov2016accurate.bib)
[code](https://github.com/alexandervakhitov/pnpl)-->

[Camera Pose and Focal Length Estimation Using Regularized Distance Constraints]({{site.url}}/pnpf/)