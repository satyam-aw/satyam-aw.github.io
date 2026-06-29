---
layout: page
title: EyeTTS
description: Evaluating and Calibrating Eye Tracking for Mobile Mixed Reality
img: assets/img/publication_preview/eyetts.webp
importance: 1
category: Spatial Perception
demo_video: https://www.youtube.com/playlist?list=PLQbqwztmTvAVAUClXj-sOkpQ9sBJbT5pG
github: https://github.com/CohesiveAR/.github
project_pdf: assets/pdf/IEEEVR-2024-Poster-A0.pdf

---

> ### Project at a Glance
>
> | | |
> |:---|:---|
> | **Research Area** | Spatial Perception · Mixed Reality · Human-Computer Interaction |
> | **Institution** | Four Eyes Laboratory, University of California, Santa Barbara |
> | **Duration** | September 2021 – June 2024 |
> | **Advisor** | Prof. Tobias Höllerer |
> | **Co-Advisor** | Prof. Michael Beyeler |
> | **Role** | Graduate Researcher (Lead Developer & First Author) |
> | **Research Outputs** | IEEE ISMAR Adjunct 2023 · IEEE VR Workshops 2024 |
> | **Open-Source Artifacts** | User Study Framework · Calibration Framework · Dataset |
> | **Technologies** | Unity, C#, Python, Jupyter, NumPy, Pandas, OpenCV |


EyeTTS (Eye Tracking Test Suite) is an end-to-end framework for evaluating eye-tracking performance during natural mixed-reality locomotion. The project combines controlled experimental environments with automated calibration and statistical analysis pipelines to study gaze accuracy across heterogeneous AR devices.

EyeTTS consists of two complementary research artifacts: **a Unity-based user study framework** and a **post-hoc calibration and analysis backend**.

---

### Research Motivation

Eye tracking is becoming a primary interaction modality for AR and mixed reality.

While modern headsets perform well in static laboratory settings, accuracy degrades considerably during natural locomotion due to

- calibration drift
- head motion
- hardware latency
- changing spatial reference frames

EyeTTS was developed to systematically quantify these effects using reproducible experimental protocols.

---

### User Study Framework

The front-end system was developed in Unity for Magic Leap 1 and standardized across multiple AR headsets.

The framework implements seven experimental paradigms spanning static calibration, world-stabilized tracking, screen-stabilized tracking, body-stabilized tracking, and ambulatory locomotion.

<div class="row mt-3">
    <div class="col-sm-6">
        {% include figure.liquid
            path="assets/img/projects/eyetts/wsw.png"
            title="Walking World Stabilized"
            class="img-fluid rounded"
            caption="World-stabilized locomotion task."
        %}
    </div>

    <div class="col-sm-6">
        {% include figure.liquid
            path="assets/img/projects/eyetts/ssw.png"
            title="Screen Stabilized"
            class="img-fluid rounded"
            caption="Screen-stabilized tracking paradigm."
        %}
    </div>
</div>

<div class="row mt-3">
    <div class="col-sm-6">
        {% include figure.liquid
            path="assets/img/projects/eyetts/bsw.png"
            title="Body Stabilized"
            class="img-fluid rounded"
            caption="Body-stabilized eye-tracking task."
        %}
    </div>

    <div class="col-sm-6">
        {% include figure.liquid
            path="assets/img/projects/eyetts/h.png"
            title="Hallway Task"
            class="img-fluid rounded"
            caption="Linear hallway locomotion experiment."
        %}
    </div>
</div>

---

### Calibration Framework

The backend automatically processes experimental logs and performs

- temporal synchronization
- drift estimation
- coordinate recalibration
- behavioral segmentation
- statistical analysis

The framework generates publication-quality plots directly from raw participant logs.

---

### Key Results

#### Tracking Accuracy

Eye tracking remains highly accurate during smooth pursuit but deteriorates significantly during rapid saccadic motion.

<div class="row mt-3">
    <div class="col-sm-12">
        {% include figure.liquid
            path="assets/img/projects/eyetts/pre-post-calibration.png"
            title="Calibration Results"
            class="img-fluid rounded"
            caption="Tracking error before and after post-hoc calibration."
        %}
    </div>
</div>

---

#### Static vs Moving Targets

Eye-tracking precision decreases consistently when users follow moving stimuli compared to static fixation targets.

<div class="row mt-3">
    <div class="col-sm-10 mx-auto">
        {% include figure.liquid
            path="assets/img/projects/eyetts/comparing_s_m.png"
            title="Static vs Moving"
            class="img-fluid rounded"
            caption="Error comparison across locomotion conditions."
        %}
    </div>
</div>

---

#### Hardware Latency

Cross-correlation analysis revealed an average delay of approximately **9 frames (~150 ms)** between gaze and target trajectories.

<div class="row mt-3">
    <div class="col-sm-10 mx-auto">
        {% include figure.liquid
            path="assets/img/projects/eyetts/time_shift.png"
            title="Latency Analysis"
            class="img-fluid rounded"
            caption="Signal synchronization using cross-correlation."
        %}
    </div>
</div>

---

#### Behavioral Segmentation

EyeTTS separates gaze into fixation, smooth pursuit, and saccadic behaviors to evaluate tracking precision under different physiological conditions.

<div class="row mt-3">
    <div class="col-sm-12">
        {% include figure.liquid
            path="assets/img/projects/eyetts/gaze_data_playback.webp"
            title="Playback"
            class="img-fluid rounded"
            caption="Playback of reconstructed gaze trajectories from experimental logs."
        %}
    </div>
</div>

---

### Contributions

##### Experimental Design

- Designed seven mixed-reality locomotion experiments.
- Developed randomized trial scheduling using Latin-square balancing.
- Standardized protocols across Magic Leap, HoloLens 2, and Quest Pro.

##### Software Infrastructure

- Unity-based user study platform.
- High-frequency synchronized gaze logging.
- Cross-device data collection pipeline.

##### Analysis Pipeline

- Drift-aware recalibration.
- Signal synchronization.
- Statistical evaluation.
- Publication-quality visualization.

---


### Research Outputs

The EyeTTS project produced a complete set of open research artifacts supporting reproducible mixed-reality eye-tracking research, including peer-reviewed publications, experimental software, analysis pipelines, and publicly available datasets.

#### Publications

##### Eye Tracking Performance in Mobile Mixed Reality

**Satyam Awasthi**, Vivian Ross, Sydney Lim, Michael Beyeler, Tobias Höllerer

*IEEE Conference on Virtual Reality and 3D User Interfaces Workshops (IEEE VRW), 2024*

This paper presents a large-scale empirical evaluation of eye-tracking accuracy during natural locomotion, quantifying the effects of calibration drift, behavioral eye movements, spatial reference frames, and hardware latency on tracking performance.

**Links**

- **IEEE Xplore:** https://doi.org/10.1109/VRW62533.2024.00321

---

##### EyeTTS: Evaluating and Calibrating Eye Tracking for Mixed-Reality Locomotion

**Satyam Awasthi**, Vivian Ross, Michael Beyeler, Tobias Höllerer

*IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR Adjunct), 2023*

Introduces EyeTTS as a reproducible framework for evaluating eye-tracking systems under realistic locomotion conditions. The work presents standardized experimental protocols, post-hoc calibration techniques, and quantitative metrics for benchmarking mixed-reality eye-tracking performance.

**Links**

- **IEEE Xplore:** https://doi.org/10.1109/ISMAR-Adjunct60411.2023.00104

---

### Research Artifacts

EyeTTS is released as two complementary software packages together with experimental datasets and recorded participant sessions.

#### ① User Study Framework

**Front-end experimental platform for mixed-reality eye-tracking studies**

Implements the complete experimental environment for Magic Leap 1, including randomized trial execution, synchronized gaze logging, locomotion tasks, and reproducible participant data collection.

**Repository**

**GitHub:** <https://github.com/satyam-aw/EyeTTS_User-Study-Framework_Magic-Leap-1>

---

#### ② Calibration Framework

**Backend pipeline for calibration, signal processing, and statistical analysis**

Processes raw participant logs through temporal synchronization, drift-aware calibration, behavioral segmentation, latency estimation, and publication-quality visualization.

**Repository**

**GitHub:** <https://github.com/satyam-aw/EyeTTS_Calibration-Framework>

---

#### ③ Dataset & Supplementary Material

To support reproducibility, the project publicly releases experimental resources used throughout the published studies.

##### Available Resources

- Mixed-reality participant datasets
- Raw gaze-tracking logs
- User study recordings
- Calibration notebooks
- Statistical analysis pipelines
- Experimental task demonstrations

**Resources**

**Participant Dataset**  
<https://github.com/satyam-aw/EyeTTS_Calibration-Framework/tree/main/participant-data>

**User Study Videos**  
<https://www.youtube.com/playlist?list=PLQbqwztmTvAVAUClXj-sOkpQ9sBJbT5pG>

---

### Impact

EyeTTS established a reproducible research infrastructure for evaluating eye-tracking performance under realistic mixed-reality locomotion. Beyond supporting two peer-reviewed IEEE publications, the project provides reusable software, datasets, and analysis pipelines that can serve as a foundation for future research in spatial perception, human-computer interaction, and eye-tracking evaluation across emerging AR platforms.