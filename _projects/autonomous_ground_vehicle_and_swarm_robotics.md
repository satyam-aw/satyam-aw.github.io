---
layout: page
title: Autonomous Navigation & Robotics
description: Undergraduate robotics work with the AGV group and Technology Robotix Society at IIT Kharagpur, spanning autonomous navigation, robot coordination, and drones.
img: assets/img/9_agv.webp
images:
  - assets/img/9_agv.webp
completed_on: "IIT-KGP, 2016–2018"
demo_video: https://www.youtube.com/@agvkgp
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
project_resources:
  - label: AGV research group
    url: http://www.agv.iitkgp.ac.in/
  - label: Technology Robotix Society
    url: https://www.robotix.in/
project_toc: true
project_toc_level: "2"
---

During my undergraduate years at IIT Kharagpur, I worked with the [**Autonomous Ground Vehicle (AGV) group**](http://www.agv.iitkgp.ac.in/) and the [**Technology Robotix Society**](https://www.robotix.in/). My AGV work contributed to the perception, estimation, and navigation architecture of the **Eklavya autonomous ground vehicle platform**. Through Technology Robotix Society, I also worked on robotics projects involving robot coordination and drones.

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

## 1. Autonomous Navigation Pipeline for AGV

My AGV work involved a ROS-based autonomous navigation stack for the Eklavya platform, addressing perception, planning, and control in outdoor environments.

<figure class="mt-3 mt-md-0 text-center">
  {% include figure.liquid path="assets/img/9_agv.webp" title="Eklavya autonomous ground vehicle platform" class="img-fluid rounded" %}
  <figcaption class="caption">
    Figure 1: The Eklavya AGV platform used to develop and test perception, planning, and navigation algorithms.
  </figcaption>
</figure>

- **Perception & Vision**: Contributed to visual obstacle-detection pipelines using OpenCV-based image processing and learning-based segmentation approaches, including U-Net-style architectures for scene understanding.
- **Motion Planning**: Worked on hierarchical planning methods combining global path-search algorithms such as $A^*$ and Dijkstra with local obstacle-avoidance strategies for real-time navigation.
- **Local Control & Collision Avoidance**: Integrated local planning concepts such as the Dynamic Window Approach to support feasible trajectory generation for a non-holonomic ground vehicle.
- **State Estimation**: Used Extended Kalman Filter-based sensor fusion to combine noisy wheel encoder, IMU, GPS, and LiDAR/camera-derived measurements for more reliable localization.
- **ROS-Based Integration & Visualization**: Developed modular C++ and Python software components within the ROS ecosystem, using Gazebo for simulation and RViz for debugging, visualization, sensor-stream inspection, trajectory validation, and end-to-end system integration before deployment on physical hardware.

---

## 2. Technology Robotix Society Projects

Through Technology Robotix Society, I worked on mobile robotics and drone projects. The mobile-robot work included decentralized coordination, peer-to-peer communication, and relative pose estimation.

- **Decentralized Multi-Agent Path Planning**: Implemented coordination strategies where each robot planned locally while treating neighboring robots as dynamic obstacles. Agents exchanged local intent and state information to reduce spatial conflicts without relying on a centralized controller.
- **Relative Pose Estimation**: Developed neighbor-based relative pose estimation workflows using fiducial markers such as AprilTags, allowing robots to estimate nearby agents’ positions and maintain a local representation of neighboring robots.
- **Peer-to-Peer Communication**: Configured ad-hoc communication using XBee modules to support low-latency state sharing between nearby robots.
- **Embedded Control & Hardware Integration**: Worked with ATmega-based custom PCB designs for low-level motor control, power distribution, and IR sensor integration.
- **System-Level Testing**: Validated coordination behavior across perception, communication, and control loops on physical robot platforms.

---

## Research Relevance

This project shaped my current research interests in safe and reliable autonomy, particularly at the intersection of perception, planning, control, and multi-agent coordination. The AGV work exposed me to the challenges of deploying autonomy stacks on real robots under noisy sensing, imperfect state estimation, non-holonomic motion constraints, and real-time execution limits.

The Technology Robotix Society projects further motivated my interest in decentralized decision-making, relative localization, and coordination under communication and sensing limitations. Together, these experiences now inform my broader interest in learning-enhanced model predictive control, safe multi-agent autonomy, and robot decision-making under uncertainty.
