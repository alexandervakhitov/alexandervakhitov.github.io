---
layout: page
title: CarpetVR
permalink: /carpetvr/
---

Alexander Vakhitov,
[Andrew Starostin](https://www.linkedin.com/in/andrew-starostin-0b561699/), 
[Victor Lempitsky](http://sites.skoltech.ru/compvision/members/vilem/)

![My helpful screenshot](/assets/carpetvr/demo.png)

CarpetVR is a system for realtime 6DoF virtual reality based on an arbitrary smartphone. 
A cheap case turns smartphone to a stereo VR helmet. We use a neural net-designed marker to enable
 fast and robust helmet pose estimation.  
A case has a slanted mirror to make the smartphone cam look down. See [carpetvr.com](http://www.carpetvr.com) for details.

In the image above, a user enjoys the VR experience (bottom-left: renderings) in our system. 

![Visual Inertial Pose](/assets/carpetvr/scheme.jpg)

My role was to create a visual-inertial pose estimation algorithm. It optimizes the camera poses in a temporal window
with inertial and visual constraints, while the previous poses are marginalized (see the schema).
 We start with estimating the visual pose from individual frames, and then use a MSCKF-like (Mourikis & Roumeliotis, 2007) nonlinear filter with inertial constraints.
 In the image above, we see the trajectory of a mirror-equipped camera. We marginalize the past observations (n-2 in the image)
  and use active observations (n-1, n) for visual-inertial pose estimation.  
 
### Main features
#### Tightly coupled visual-inertial pose estimation
#### *60 FPS*, System latency = IMU latency (2 ms)
#### Shaking-free motion trajectory generation


### Paper
Although it was a comercially-focused startup project, we have published an overview paper:  

Lempitsky, Victor and Vakhitov, Alexander and Starostin, Andrew **CarpetVR: The Magic Carpet Meets the Magic Mirror,**  2018 IEEE Conference on Virtual Reality and 3D User Interfaces (VR), 2018,  pp. 1--1   [bib]({{site.url}}/scripts/publications/bib/lempitsky2018carpetvr.bib)