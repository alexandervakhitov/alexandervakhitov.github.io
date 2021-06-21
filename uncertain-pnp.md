---
layout: page
title: Uncertainty-Aware Camera Pose Estimation from Points and Lines
permalink: /uncertain-pnp/
---
<style type="text/css">
.image-left {
  display: block;
  margin-left: auto;
  margin-right: auto;
  float: left;
}
</style>

### Computer Vision and Pattern Recognition (CVPR), 2021

Alexander Vakhitov, 
Luis Ferraz Colomina,
Antonio Agudo,
Francesc Moreno-Noguer

Perspective-n-Point-and-Line (PnPL) algorithms aim at fast, 
accurate, and robust camera localization with respect to a 3D model 
from 2D-3D feature correspondences, being a major part of modern 
robotic and AR/VR systems.
Current point-based pose estimation methods use only 2D feature 
detection uncertainties, and the line-based methods do not take 
uncertainties into account. In our setup, both 3D  coordinates 
and 2D projections of the features are considered uncertain. 
We propose PnP(L)  solvers based on EPnP and DLS for the uncertainty-aware pose estimation.
We also modify to the 
motion-only bundle adjustment to take 3D uncertainties into account. 
We perform exhaustive synthetic and real experiments on two different 
visual odometry datasets. The new PnP(L) methods outperform 
the state-of-the-art on real data in isolation, showing an increase
in mean translation accuracy by 18% on a representative subset of 
KITTI, while the new uncertain refinement improves pose accuracy 
for most of the solvers, e.g. decreasing mean translation error for
the EPnP by 16% compared to the standard pose refinement on the
same dataset. 

### Code
[Code in MATLAB](https://github.com/alexandervakhitov/uncertain-pnp.git)

### Paper
**Uncertainty-Aware Camera Pose Estimation From Points and Lines**  [pdf]({{site.url}}/scripts/publications/files/vakhitov2021uncertain.pdf)  [bib]({{site.url}}/scripts/publications/bib/vakhitov2021uncertainty.bib) 

 Vakhitov, Alexander and Ferraz, Luis and Agudo, Antonio and Moreno-Noguer, Francesc

  Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2021,  pp. 4659--4668
