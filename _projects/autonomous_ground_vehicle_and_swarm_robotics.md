---
layout: page
title: Autonomous Ground Vehicle Navigation & Swarm Robotics
description: Developed perception, motion-planning, and decentralized coordination systems for the institute's AGV and swarm robotics research groups.
img: assets/img/9_agv.webp
images: 
- assets/img/9_agv.webp
- assets/img/9_swarm.jpg
- assets/img/9_agv_e6.png
completed_on: IIT-KGP, 2016-2018
selected: true
demo_video: https://www.youtube.com/@agvkgp
importance: 2
category: Autonomous Systems
---


During my undergraduate years at IIT Kharagpur, I served as a core research and technical team member of the [**Autonomous Ground Vehicle (AGV)**](http://www.agv.iitkgp.ac.in/) and [**Swarm**](https://swarm-iitkgp.github.io/index.html) research groups. My work sat at the intersection of Robot Learning, Spatial Perception, and Control Theory, focusing on building fully autonomous, decentralized systems capable of navigating complex, unmodeled indoor and outdoor physical environments.

---

#### Core Domains & Areas of Expertise

* **Spatial Perception**: Designing pipelines for real-time dense semantic segmentation and structural environment mapping.
* **Motion Planning & Control**: Developing global/local trajectory planning frameworks for non-holonomic, constraint-bound ground vehicles.
* **Sim-to-Real (Sim2Real) Transfer**: Building hardware-agnostic ROS abstractions to validate software loops in high-fidelity simulation prior to physical deployment.
* **State Estimation & Multi-Modal Sensor Fusion**: Fusing asynchronous telemetry from LiDAR, IMU, GPS, and camera sensors to resolve state estimation under drift conditions.

---

#### Key Projects & Technical Details

##### 1. Autonomous Navigation Pipeline for AGV
We engineered an end-to-end, hardware-agnostic navigation stack for an outdoor autonomous rover designed to navigate unstructured campus environments under strict runtime limits.

<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/9_agv.webp" title="example image" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 1: AGV Dune buggy, a full-scale autonomous buggy testbed developed by the Autonomous Ground Vehicles group for field-testing real-world perception and navigation algorithms</figcaption>
</figure>

* **Perception & Vision**: Implemented robust visual obstacle segmentation using a custom U-Net architecture alongside traditional computer vision (OpenCV) filters optimized for real-time embedded deployment.
* **Hybrid Motion Planning**: Developed a hierarchical trajectory generation system, combining global path generation ($A^*$ / Dijkstra) with a **Dynamic Window Approach (DWA)** local planner for real-time, non-holonomic collision avoidance.
* **State Estimation**: Utilized an **Extended Kalman Filter (EKF)** to handle multi-modal sensor fusion by merging noisy wheel encoders, IMU, and GPS telemetry, drastically minimizing dead-reckoning tracking drift.
* **Sim2Real Optimization**: Developed the entire software stack within the **ROS** ecosystem using C++ and Python. By completely decoupling the core perception and planning algorithms from physical actuator configs, we achieved a zero-shot **Sim2Real transfer** from simulation to hardware.

##### 2. Swarm Robotics & Swarm Intelligence
As part of the [Swarm](https://swarm-iitkgp.github.io/index.html) research group, I formulated decentralized coordination protocols and peer-to-peer relative pose estimation mechanics for low-cost mobile robots.

<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/9_swarm.jpg" title="Swarm Communication and Tracking Workflows" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 2: Modular, peer-to-peer swarm agents utilizing onboard Linux compute and vision sensors for decentralized relative pose estimation swarm coordination</figcaption>
</figure>

* **Algorithms**:
  1. **Decentralized Multi-Agent Path Planning**: Implemented a decentralized routing framework where each agent computes its own path independently. Agents treat adjacent robots as dynamic physical obstacles and broadcast localized intent vectors to resolve spatial boundary conflicts without a centralized master node.
  2. **Relative Pose Estimation**: To overcome occlusion and bandwidth limits as the swarm scales, individual robots track only their immediate neighbors. Implemented an observation-only broadcasting strategy allowing peer agents to receive and update their local pose graphs to infer the global swarm map. Inter-agent relative pose was computed using **AprilTags** as fiducial markers.

* **Communication**: Configured an ad-hoc mesh network topology using **XBee modules** to enforce low-latency state sharing and deterministic message routing between adjacent robots.
* **Hardware & Low-Level Control**: Designed custom PCBs hosting **ATmega microcontrollers** to manage closed-loop motor control loops, localized power distribution, and IR sensor arrays.

---

#### Technical Stack

* **Languages**: C++, Python, MATLAB
* **Frameworks \& Tools**: ROS (Robot Operating System), OpenCV, PyTorch
* **Hardware \& Simulation**: Gazebo, Hokuyo LiDAR, Raspberry Pi, BeagleBone Black, Arduino
