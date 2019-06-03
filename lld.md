---
layout: page
title: Learnable line descriptor
permalink: /lld/
---
### Learnable line descriptor for visual SLAM

Traditionally, indirect visual motion estimation and simultaneous localization and mapping (SLAM) systems were based on 
point features. In recent years, several SLAM systems that use lines as primitives were suggested. Despite the extra 
robustness and accuracy brought by line segment matching, the line segment descriptors used in such systems were 
hand-crafted and therefore sub-optimal.

In this work, we suggest to apply descriptor learning to construct line segment descriptors optimized for matching tasks. 
We show how such descriptors can be constructed on top of a deep yet lightweight fully-convolutional neural network. 
The coefficients of this network are trained using an automatically collected dataset of matching and non-matching line 
segments. The use of the fully-convolutional network ensures that the bulk of the computations needed to compute descriptors 
is shared among multiple line segments in the same image, enabling efficient implementation. We show that learned line 
segment descriptors outperform previously suggested hand-crafted line segment descriptors both in isolation (i.e.
 for the subtask of distinguishing matching and non-matching line segments), but also when built into the SLAM system. 
 We construct a new line based SLAM pipeline built upon a state-of-the-art point-only system. We demonstrate generalization 
 of the learned parameters of the descriptor network between two well-known datasets for autonomous driving and indoor micro aerial vehicle navigation. 

![My helpful screenshot](/assets/lld/lld.png)
*Top*: EuRoC Track MH05, the trajectory ground truth projected on XZ plane, and the reconstructed trajectories by 
different methods (each trajectory is rigidly aligned with the ground truth). The trajectory reconstructed by 
the ORB-SLAM2+LLD (red) is closer to the ground truth trajectory (dashed black) demonstrating the advantage of the 
proposed descriptor. 
*Bottom-left*: feature tracking visualization in the ORB-SLAM2+LLD system for a single frame of the sequence. 
*Bottom-right*: the map constructed by ORB-SLAM2+LLD system. The green frustum corresponds to the frame shown in the bottom-left; the blue frustums represent other frames of the reconstructed trajectory. Black lines show segments of 3D lines inserted into the map. Red (black) points correspond to the map points used (not used) in the local bundle adjustment. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/ntFFiwXIhoA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### LINKS

#### Code
[LLD-based line matching in python](https://github.com/alexandervakhitov/lld-public.git)

[Line detection and description library](https://github.com/alexandervakhitov/lbdmod.git)

[LLD-SLAM system](https://github.com/alexandervakhitov/lld-slam.git)


 
#### Paper

Vakhitov, Alexander and Lempitsky, Victor *Learnable Line Segment Descriptor for Visual SLAM* (2019), IEEE Access  [pdf](https://yadi.sk/d/ugN8qGun3r2mpQ/vakhitov-lld-2019.pdf)  [bib](/scripts/publications/bib/vakhitov2019learnable.bib)