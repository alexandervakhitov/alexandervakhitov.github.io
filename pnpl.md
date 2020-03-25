---
layout: page
title: Accurate and linear time pose estimation from points and lines
permalink: /pnpl/
---
### European Conference on Computer Vision (ECCV), 2016

Alexander Vakhitov, 
[Jan Funke](http://funkey.science/), 
[Francesc Moreno-Noguer](https://www.iri.upc.edu/people/fmoreno/) 

The Perspective-n-Point (PnP) problem seeks to estimate
the pose of a calibrated camera from n 3D-to-2D point correspondences.
There are situations, though, where PnP solutions are prone to fail be-
cause feature point correspondences cannot be reliably estimated (e.g.
scenes with repetitive patterns or with low texture). In such scenarios,
one can still exploit alternative geometric entities, such as lines, yielding
the so-called Perspective-n-Line (PnL) algorithms. Unfortunately, exist-
ing PnL solutions are not as accurate and efficient as their point-based
counterparts. In this paper we propose a novel approach to introduce
3D-to-2D line correspondences into a PnP formulation, allowing to si-
multaneously process points and lines. For this purpose we introduce
an algebraic line error that can be formulated as linear constraints on
the line endpoints, even when these are not directly observable. These
constraints can then be naturally integrated within the linear formula-
tions of two state-of-the-art point-based algorithms, the OPnP and
the EPnP, allowing them to indistinctly handle points, lines, or a
combination of them. Exhaustive experiments show that the proposed
formulation brings remarkable boost in performance compared to only
point or only line based solutions, with a negligible computational over-
head compared to the original OPnP and EPnP.

![Lines](/assets/pnpl/fig1_lines_v2.png)![Points](/assets/pnpl/fig1_pts_v2.png)

Comparison of pose estimation results with OPnPL (left) and OPnP 
(right) in a scenario with a lack of reliable feature points. Blue points and solid line segments  are detected in the image, and green dashed line segments are the model reference lines reprojected using the estimated pose.   

<iframe width="560" height="315" src="https://www.youtube.com/embed/ue73pcCfsYo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Code
[MATLAB implementation](https://github.com/alexandervakhitov/pnpl.git)
 
### Paper

Vakhitov, Alexander and Funke, Jan and Moreno-Noguer, Francesc **Accurate and linear time pose estimation from points and lines,**  European Conference on Computer Vision, 2016,  pp. 583--599  [pdf]({{site.url}}/scripts/publications/files/pnpl2016.pdf)  [bib]({{site.url}}/scripts/publications/bib/vakhitov2016accurate.bib)