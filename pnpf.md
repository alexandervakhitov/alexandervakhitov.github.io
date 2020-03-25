---
layout: page
title: Camera Pose and Focal Length Estimation Using Regularized Distance Constraints
permalink: /pnpf/
---
### British Machine Vision Conference (BMVC), 2015

Ekaterina Kanaeva,
Lev Gurevich,
Alexander Vakhitov 

We propose a new method for camera pose estimation with unknown focal length 
(PnPf problem).  We combine projection equations and distance constraints in a single 
statistically meaningful cost function in the form of least squares. 
We fix the space of the search as a linear combination of several right singular vectors
 of the least squares system matrix. We use linear programming techniques to find 
 feasible solutions faster. Then we do nonlinear refinement with Levenberg-Marquardt. 
 Numerical experiments demonstrate that the method is faster than the state-of-the-art 
 methods for point numbers up to several hundreds, and real-life structure-from-motion experiments 
 demonstrate the applicability of the methods for models having hundreds of thousands of points. 
 It has the same accuracy of estimates as the the state-of-the-art methods. 
 We show that the method offers a tradeoff between speed and accuracy, 
 allowing the estimation to run several times faster while slightly 
 increasing the mean reprojection error.

### Code
[MATLAB implementation](https://github.com/alexandervakhitov/pnpf)
 
### Paper

Kanaeva, Ekaterina and Gurevich, Lev and Vakhitov, Alexander **Camera Pose and Focal Length Estimation Using Regularized Distance Constraints,**  BMVC, 2015,  pp. 162--1  [pdf]({{site.url}}/scripts/publications/files/kanaeva2015.pdf)  [bib]({{site.url}}/scripts/publications/bib/kanaeva2015camera.bib)