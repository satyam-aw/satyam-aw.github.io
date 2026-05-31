---
layout: page
title: Autonomous Ground Vehicle and Swarm Robotics
description: Developed perception, motion-planning, and decentralized coordination systems for the institute's AGV and swarm robotics research groups.
img: assets/img/9_agv.webp
images: 
- assets/img/9_agv.webp
- assets/img/9_swarm.jpg
- assets/img/9_agv_e6.PNG
completed_on: IIT-KGP, 2016-2018
selected: true
demo_video: https://www.youtube.com/@agvkgp
importance: 4
category: Embedded Systems and Robotics
---


During my undergraduate years at IIT Kharagpur, I served as a core technical member of the [**Autonomous Ground Vehicle (AGV)**](http://www.agv.iitkgp.ac.in/) and [**Swarm**](https://swarm-iitkgp.github.io/index.html) research groups. My work sat at the intersection of Artificial Intelligence, Computer Vision, and Embedded Systems. We focused on building fully autonomous systems capable of navigating complex, dynamic indoor and outdoor environments.

---

#### Core Domains & Areas of Expertise

* **Robot Perception**: Designing pipelines for real-time obstacle detection and environment mapping.
* **Motion Planning**: Developing path planning algorithms for non-holonomic ground vehicles.
* **Embedded Systems**: Integrating sensors, microcontrollers, and single-board computers (SBCs).
* **Sensor Fusion**: Combining data from LiDAR, IMU, GPS, and cameras for localization.

---

#### Key Projects & Technical Details

##### 1. Autonomous Navigation Pipeline for AGV
We engineered an end-to-end software and hardware stack for an outdoor autonomous rover designed to navigate unstructured campus environments.

<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/9_agv.webp" title="example image" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 1: AGV Dune buggy, a full-scale autonomous buggy testbed developed by the Autonomous Ground Vehicles group for field-testing real-world perception and navigation algorithms</figcaption>
</figure>

* **Vision & Perception**: Implemented lane detection and obstacle segmentation using traditional computer vision (OpenCV) combined with deep learning models (SegNet/U-Net) optimized for embedded deployment.
* **Path Planning**: Developed a hierarchical planning system. Used **A* / Dijkstra** for global path generation and **Dynamic Window Approach (DWA)** for local obstacle avoidance.
* **Localization**: Utilized an **Extended Kalman Filter (EKF)** to fuse odometry data from wheel encoders, IMU, and GPS, reducing drift during long-range traversal.
* **Software Stack**: Developed entirely within the **Robot Operating System (ROS)** ecosystem using C++ and Python.

##### 2. Swarm Robotics & Swarm Intelligence
As part of the [Swarm](https://swarm-iitkgp.github.io/index.html) research group, I researched decentralized coordination among low-cost mobile robots.

<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/9_swarm.jpg" title="Swarm Communication and Tracking Workflows" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 2: Modular, peer-to-peer swarm agents utilizing onboard Linux compute and vision sensors for decentralized relative pose estimation swarm coordination</figcaption>
</figure>

* **Algorithms**:
  1. **Multi-Agent Path Planning**: Implemented a **Decentralized A*** approach where each agent computes its own path independently. Agents treat neighboring robots as dynamic obstacles and broadcast intent vectors to resolve spatial conflicts locally without a central coordinator.
  2. **Relative Pose Estimation**: To overcome occlusion and bandwidth constraints as the swarm scales, individual robots track only their immediate neighbors rather than the entire fleet. Implemented an **observation-only** broadcasting strategy, allowing peer swarm agents to receive and update their local pose graphs to infer the global swarm map. Relative pose estimation was achieved using **AprilTags** as fiducial markers.

* **Communication**: Set up an ad-hoc mesh network using **XBee modules** to enable real-time state sharing and low-latency communication between adjacent robots.
* **Hardware**: Designed custom PCBs hosting **ATmega microcontrollers** to manage closed-loop motor control, localized power distribution, and IR sensor arrays.

---

#### Technical Stack

* **Languages**: C++, Python, MATLAB
* **Frameworks & Tools**: ROS (Robot Operating System), OpenCV 
* **Hardware**: Arduino, Raspberry Pi, BeagleBone Black, Hokuyo LiDAR, IMU (MPU6050)
