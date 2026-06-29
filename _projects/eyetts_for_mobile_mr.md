---
layout: page
title: EyeTTS
description: Evaluating and Calibrating Eye Tracking for Mobile Mixed Reality
img: assets/img/projects/eyetts/cover.webp
importance: 1
category: Spatial Perception & XR
---

# EyeTTS

EyeTTS (Eye Tracking Test Suite) is an end-to-end framework for evaluating eye-tracking performance during natural mixed-reality locomotion. The project combines controlled experimental environments with automated calibration and statistical analysis pipelines to study gaze accuracy across heterogeneous AR devices.

<div class="row mt-3">
    <div class="col-sm-12">
        {% include figure.liquid
            path="assets/img/projects/eyetts/system_overview.png"
            title="EyeTTS Pipeline"
            class="img-fluid rounded z-depth-1"
            caption="EyeTTS consists of two complementary research artifacts: a Unity-based user study framework and a post-hoc calibration and analysis backend."
        %}
    </div>
</div>

---

# Research Motivation

Eye tracking is becoming a primary interaction modality for AR and mixed reality.

While modern headsets perform well in static laboratory settings, accuracy degrades considerably during natural locomotion due to

- calibration drift
- head motion
- hardware latency
- changing spatial reference frames

EyeTTS was developed to systematically quantify these effects using reproducible experimental protocols.

---

# User Study Framework

The front-end system was developed in Unity for Magic Leap 1 and standardized across multiple AR headsets.

The framework implements seven experimental paradigms spanning static calibration, world-stabilized tracking, screen-stabilized tracking, body-stabilized tracking, and ambulatory locomotion.

<div class="row mt-3">
    <div class="col-sm-6">
        {% include figure.liquid
            path="assets/img/projects/eyetts/wsw.png"
            title="Walking World Stabilized"
            class="img-fluid rounded z-depth-1"
            caption="World-stabilized locomotion task."
        %}
    </div>

    <div class="col-sm-6">
        {% include figure.liquid
            path="assets/img/projects/eyetts/ssw.png"
            title="Screen Stabilized"
            class="img-fluid rounded z-depth-1"
            caption="Screen-stabilized tracking paradigm."
        %}
    </div>
</div>

<div class="row mt-3">
    <div class="col-sm-6">
        {% include figure.liquid
            path="assets/img/projects/eyetts/bsw.png"
            title="Body Stabilized"
            class="img-fluid rounded z-depth-1"
            caption="Body-stabilized eye-tracking task."
        %}
    </div>

    <div class="col-sm-6">
        {% include figure.liquid
            path="assets/img/projects/eyetts/hallway.png"
            title="Hallway Task"
            class="img-fluid rounded z-depth-1"
            caption="Linear hallway locomotion experiment."
        %}
    </div>
</div>

---

# Calibration Framework

The backend automatically processes experimental logs and performs

- temporal synchronization
- drift estimation
- coordinate recalibration
- behavioral segmentation
- statistical analysis

The framework generates publication-quality plots directly from raw participant logs.

---

# Key Results

## Tracking Accuracy

Eye tracking remains highly accurate during smooth pursuit but deteriorates significantly during rapid saccadic motion.

<div class="row mt-3">
    <div class="col-sm-12">
        {% include figure.liquid
            path="assets/img/projects/eyetts/pre-post-calibration.png"
            title="Calibration Results"
            class="img-fluid rounded z-depth-1"
            caption="Tracking error before and after post-hoc calibration."
        %}
    </div>
</div>

---

## Static vs Moving Targets

Eye-tracking precision decreases consistently when users follow moving stimuli compared to static fixation targets.

<div class="row mt-3">
    <div class="col-sm-10 mx-auto">
        {% include figure.liquid
            path="assets/img/projects/eyetts/comparing_s_m.png"
            title="Static vs Moving"
            class="img-fluid rounded z-depth-1"
            caption="Error comparison across locomotion conditions."
        %}
    </div>
</div>

---

## Hardware Latency

Cross-correlation analysis revealed an average delay of approximately **9 frames (~150 ms)** between gaze and target trajectories.

<div class="row mt-3">
    <div class="col-sm-10 mx-auto">
        {% include figure.liquid
            path="assets/img/projects/eyetts/time_shift.png"
            title="Latency Analysis"
            class="img-fluid rounded z-depth-1"
            caption="Signal synchronization using cross-correlation."
        %}
    </div>
</div>

---

## Behavioral Segmentation

EyeTTS separates gaze into fixation, smooth pursuit, and saccadic behaviors to evaluate tracking precision under different physiological conditions.

<div class="row mt-3">
    <div class="col-sm-12">
        {% include figure.liquid
            path="assets/img/projects/eyetts/gaze_data_playback.webp"
            title="Playback"
            class="img-fluid rounded z-depth-1"
            caption="Playback of reconstructed gaze trajectories from experimental logs."
        %}
    </div>
</div>

---

# Contributions

### Experimental Design

- Designed seven mixed-reality locomotion experiments.
- Developed randomized trial scheduling using Latin-square balancing.
- Standardized protocols across Magic Leap, HoloLens 2, and Quest Pro.

### Software Infrastructure

- Unity-based user study platform.
- High-frequency synchronized gaze logging.
- Cross-device data collection pipeline.

### Analysis Pipeline

- Drift-aware recalibration.
- Signal synchronization.
- Statistical evaluation.
- Publication-quality visualization.

---

# Publications

**Eye Tracking Performance in Mobile Mixed Reality**

IEEE VR Workshops 2024

---

**EyeTTS: Evaluating and Calibrating Eye Tracking for Mixed-Reality Locomotion**

IEEE ISMAR Adjunct 2023

---

# Open Source

### User Study Framework

GitHub:
https://github.com/satyam-aw/EyeTTS_User-Study-Framework_Magic-Leap-1

### Calibration Framework

GitHub:
https://github.com/satyam-aw/EyeTTS_Calibration-Framework

### Dataset

Participant datasets and user study recordings are publicly available.