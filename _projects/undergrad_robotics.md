---
layout: page
title: Autonomous Navigation & Robotics
description: Undergraduate robotics work at IIT Kharagpur on autonomous ground vehicle navigation, robot coordination, and aerial robotics.
img: assets/img/9_agv.webp
images:
  - assets/img/9_agv.webp
completed_on: "IIT-KGP, 2016–2018"
importance: 2
category: "Selected Engineering Projects"
github: https://github.com/satyam-aw/IGVC_Lane_Detector
project_keywords:
  - Autonomous navigation
  - Robot coordination
  - Drones
  - Perception
  - Motion planning
project_tools:
  - C++ / Python / MATLAB
  - ROS / OpenCV / PyTorch
  - Gazebo / RViz
  - LiDAR / IMU / GPS
  - Embedded boards / XBee
project_toc: true
project_toc_level: "2"
---

As an undergraduate at IIT Kharagpur, I contributed to perception, sensor fusion, and navigation for an autonomous ground vehicle. I also worked on mobile robot coordination and aerial robotics projects.

My work focused on building autonomous navigation and coordination systems for mobile robots operating in complex indoor and outdoor environments. Across these projects, I worked on perception, motion planning, state estimation, sensor fusion, inter-robot communication, ROS-based system integration, visualization/debugging workflows, and low-level embedded control.

---

## Core Technical Areas

- **Spatial Perception**: Developed vision-based pipelines for obstacle detection, segmentation, and structural environment understanding.
- **Motion Planning & Control**: Worked on global and local planning approaches for non-holonomic ground robots operating under real-time constraints.
- **Simulation-to-Hardware Deployment**: Built and tested ROS-based software modules in simulation before validating them on physical robot platforms.
- **State Estimation & Sensor Fusion**: Integrated telemetry from LiDAR, IMU, GPS, wheel encoders, and camera sensors to improve localization and navigation robustness.
- **ROS Tooling & Visualization**: Used Gazebo and RViz for simulation, debugging, sensor-stream inspection, trajectory visualization, and system-level validation.
- **Multi-Agent Coordination**: Implemented decentralized coordination strategies for low-cost mobile robots using local communication and relative pose estimation.

---

## 1. Autonomous Ground Vehicle Navigation

I contributed to a ROS-based navigation stack for an autonomous ground vehicle, focusing on perception, planning, and control in outdoor environments.

<figure class="mt-3 mt-md-0 text-center">
  {% include figure.liquid path="assets/img/9_agv.webp" title="Autonomous ground vehicle" class="img-fluid rounded" %}
  <figcaption class="caption">
    Figure 1: Ground vehicle used to develop and test perception, planning, and navigation algorithms.
  </figcaption>
</figure>

- **Perception & Vision**: Contributed to visual obstacle-detection pipelines using OpenCV-based image processing and learning-based segmentation approaches, including U-Net-style architectures for scene understanding.
- **Motion Planning**: Worked on hierarchical planning methods combining global path-search algorithms such as $A^*$ and Dijkstra with local obstacle-avoidance strategies for real-time navigation.
- **Local Control & Collision Avoidance**: Integrated local planning concepts such as the Dynamic Window Approach to support feasible trajectory generation for a non-holonomic ground vehicle.
- **State Estimation**: Used Extended Kalman Filter-based sensor fusion to combine noisy wheel encoder, IMU, GPS, and LiDAR/camera-derived measurements for more reliable localization.
- **ROS-Based Integration & Visualization**: Developed modular C++ and Python software components within the ROS ecosystem, using Gazebo for simulation and RViz for debugging, visualization, sensor-stream inspection, trajectory validation, and end-to-end system integration before deployment on physical hardware.

---

## 2. Robot Coordination and Aerial Robotics

Alongside drone projects, I worked on decentralized coordination for mobile robots. That work included peer-to-peer communication and relative pose estimation.

- **Decentralized Multi-Agent Path Planning**: Implemented coordination strategies where each robot planned locally while treating neighboring robots as dynamic obstacles. Agents exchanged local intent and state information to reduce spatial conflicts without relying on a centralized controller.
- **Relative Pose Estimation**: Developed neighbor-based relative pose estimation workflows using fiducial markers such as AprilTags, allowing robots to estimate nearby agents’ positions and maintain a local representation of neighboring robots.
- **Peer-to-Peer Communication**: Configured ad-hoc communication using XBee modules to support low-latency state sharing between nearby robots.
- **Embedded Control & Hardware Integration**: Worked with ATmega-based custom PCB designs for low-level motor control, power distribution, and IR sensor integration.
- **System-Level Testing**: Validated coordination behavior across perception, communication, and control loops on physical robot platforms.

---

## Research Relevance

Working on ground vehicle navigation showed me how noisy sensors, imperfect state estimates, vehicle motion constraints, and timing limits affect performance on real hardware.

Coordinating mobile robots raised a related question: how can robots make reliable decisions with limited sensing and communication? These experiences inform my interest in learning-enhanced model predictive control and reliable autonomy under uncertainty.
