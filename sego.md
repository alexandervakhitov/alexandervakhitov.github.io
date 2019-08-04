---
layout: page
title: Stereo egomotion
permalink: /sego/
---
<style type="text/css">
.image-left {
  display: block;
  margin-left: auto;
  margin-right: auto;
  float: left;
}
</style>

### Stereo relative pose from line and point feature triplets

#### ECCV 2018

Alexander Vakhitov, 
[Victor Lempitsky](http://sites.skoltech.ru/compvision/members/vilem/),
[Yinqiang Zheng](https://sites.google.com/site/yinqiangzheng/)


![My helpful screenshot](/assets/sego.jpg){: .image-left }Stereo relative pose problem lies at the core of stereo visual odometry systems that are used in many applications. In this work
we present two minimal solvers for the stereo relative pose. We specifically consider the case when a minimal set consists of three point or
line features and each of them has three known projections on two stereo
cameras. We validate the importance of this formulation for practical
purposes in our experiments with motion estimation. We then present a
complete classification of minimal cases with three point or line correspondences each having three projections, and present two new solvers
that can handle all such cases. We demonstrate a considerable effect from
the integration of the new solvers into a visual SLAM system. 

This video shows how a proposed algorithm helps a SLAM system to recover from tracking failures due to fast motion on video sequences of a popular [KITTI](http://www.cvlibs.net/datasets/kitti/) dataset: 
{% include youtubePlayer.html id='SIMW1g2431w' %}

### LINKS

#### Code
[SEGO C++ library](https://github.com/alexandervakhitov/sego.git)

[Modified ORB-SLAM2 + SEGO system](https://github.com/alexandervakhitov/ORB_SLAM2_SEGO.git)
 
#### Paper

Vakhitov, Alexander and Lempitsky, Victor and Zheng, Yinqiang *Stereo relative pose from line and point feature triplets* (2018), Proceedings of the European Conference on Computer Vision (ECCV), 648--663  [pdf](https://yadi.sk/d/ugN8qGun3r2mpQ/vakhitov2018.pdf)  [bib](/scripts/publications/bib/vakhitov2018stereo.bib)