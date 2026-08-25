---
layout: page

title: SmartWatch for Wall Writing
description: Real-time transcription of free-form wall writing from smartwatch inertial sensing
img: assets/img/publication_preview/smart_watch.png
category: "Human Sensing & Interaction"
importance: 5
---

## SmartWatch for Wall Writing

This project investigates **wearable inertial sensing for recognizing human writing gestures**. Using motion signals recorded from a smartwatch worn on the writing hand, the system aims to infer characters written freely on a vertical surface and convert them into digital text.

The work combines **human-motion sensing, temporal signal processing, and sequence recognition**, using the smartwatch's inertial measurements as a compact sensing interface.

### System Overview

The recognition pipeline follows:

**Watch IMU → motion segmentation → signal preprocessing → learned gesture representation → character recognition → transcription**

Rather than requiring an instrumented pen or external camera, the system observes the natural movement of the user's wrist through the smartwatch.

### Research Focus

The project explores several challenges inherent to wearable gesture recognition:

- variations in writing speed and scale,
- differences in motion trajectories across users,
- temporal segmentation of continuous movements,
- extracting discriminative patterns from noisy inertial signals,
- translating physical human motion into symbolic output.

This work contributed to:

**“SmartWatch for Wall Writing: Real-time Transcription of Wall Writing from Inertial Sensing”**  
*COMSNETS 2022*

The project represents an early exploration of **wearable biosensing-adjacent interfaces and computational modeling of human movement**, themes that continue in my work on physiological sensing and neural interfaces.
