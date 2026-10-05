---
layout: page
research_connection: >-
  Understanding calibration, latency, and movement-dependent sensing errors informs my work on reliable signal decoding in closed-loop BCIs.
title: EyeTTS
description: Evaluating and calibrating eye tracking during mixed-reality locomotion.
img: assets/img/publication_preview/eyetts.webp
importance: 5
category: "Neural Interfaces & Biosignals"
completed_on: "Sep 2021–Jun 2023"
demo_video: https://www.youtube.com/playlist?list=PLQbqwztmTvAVAUClXj-sOkpQ9sBJbT5pG
github: https://github.com/EyeTTS
project_pdf: /assets/pdf/IEEEPosterEyeTracking2024.pdf
_styles: |
  .eyetts-context { color: var(--global-text-color-light); font-size: 0.9rem; line-height: 1.7; }
  .post article hr { margin: 2rem 0; border-top: 1px solid var(--global-divider-color); }
  .post article h2 { margin-top: 2rem; color: var(--global-theme-color); }
  .post article h3 { margin-top: 1.75rem; font-size: 1.15rem; }
  .eyetts-task-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; margin: 1.5rem 0; }
  .eyetts-task-grid figure { margin: 0; }
  .eyetts-task-grid img { width: 100%; aspect-ratio: 4 / 3; object-fit: contain; background: var(--global-card-bg-color); border-radius: 6px; }
  .eyetts-task-grid .caption { margin-top: 0.65rem; text-align: left; line-height: 1.5; }
  .eyetts-figure { max-width: 800px; margin: 1.5rem auto 2rem; }
  .eyetts-figure-compact { max-width: 640px; }
  .eyetts-figure figure { margin: 0; }
  .eyetts-figure img { display: block; width: 100%; height: auto; border-radius: 6px; }
  .eyetts-figure .caption { margin-top: 0.65rem; text-align: left; line-height: 1.5; }
  .eyetts-table { overflow-x: auto; margin: 1.25rem 0 1.75rem; }
  .eyetts-table table { width: 100%; font-size: 0.9rem; line-height: 1.5; border-collapse: collapse; }
  .eyetts-table th, .eyetts-table td { padding: 0.7rem 0.8rem; vertical-align: top; border-bottom: 1px solid var(--global-divider-color); }
  .eyetts-table th { background: var(--global-card-bg-color); }
  .eyetts-pipeline { padding: 1rem 1.25rem; background: var(--global-card-bg-color); border-left: 3px solid var(--global-theme-color); line-height: 1.7; }
  @media (max-width: 575.98px) { .eyetts-task-grid { grid-template-columns: minmax(0, 1fr); } }
---

**EyeTTS (Eye Tracking Test Suite)** studies how reliably mixed-reality headsets measure gaze when people move, follow targets, and switch between spatial reference frames. It combines a Unity-based experimental platform with a Python calibration and analysis pipeline.

<div class="eyetts-context"><strong>Graduate Researcher · Four Eyes Laboratory, UC Santa Barbara</strong><br>Advisor: Prof. Tobias Höllerer · Co-advisor: Prof. Michael Beyeler<br>First-author poster papers: IEEE ISMAR Adjunct 2023 and IEEE VR Workshops 2024.</div>

---

## Research question

How do target motion, head and body movement, and the choice of reference frame affect gaze-tracking error—and how much can post-hoc calibration and temporal alignment improve the measurements?

A single aggregate error can hide differences between tasks and eye movements. EyeTTS evaluates these conditions separately, connecting the experimental protocol to the analysis of recorded gaze trajectories.

## Experimental design

The [Magic Leap 1 study framework](https://github.com/EyeTTS/User-Study-Framework_Magic-Leap-1) renders targets, manages trials, and records gaze, head pose, target position, confidence, and timing information. Companion implementations for [HoloLens 2](https://github.com/EyeTTS/User-Study-Framework_Hololens-2), developed by Vivian Ross, and [Meta Quest Pro](https://github.com/EyeTTS/User-Study-Framework_Meta_Quest_Pro), developed by Sydney Lim, support the broader cross-device study; each uses its own headset SDK.

Seven tasks vary the participant's movement and the target's reference frame:

<div class="eyetts-table" markdown="1">

| Task                                 | Experimental condition                                                     |
| :----------------------------------- | :------------------------------------------------------------------------- |
| Recalibration (R)                    | Head constrained; target jumps between discrete positions.                 |
| Head-constrained (HC / w1)           | Continuous world-stabilized tracking within the field of view.             |
| Body-constrained (BC / w2)           | Seated tracking with head rotation and a world-stabilized target.          |
| World-stabilized walking (WSW / w3)  | Walking around a table while following a target fixed to the world frame.  |
| Screen-stabilized walking (SSW / s4) | Walking while following a target defined in display coordinates.           |
| Body-stabilized walking (BSW / b5)   | Walking while following a target anchored to the participant's body frame. |
| Hallway (H)                          | Walking along a corridor while following a moving target.                  |

</div>

<div class="eyetts-task-grid">
  <div>{% include figure.liquid path="assets/img/projects/eyetts/wsw.png" alt="World-stabilized target above a table while a participant walks around it" sizes="(min-width: 576px) 450px, 95vw" caption="<strong>World-stabilized.</strong> The target remains tied to the room as the participant moves." %}</div>
  <div>{% include figure.liquid path="assets/img/projects/eyetts/ssw.png" alt="Screen-stabilized target shown relative to the headset display" sizes="(min-width: 576px) 450px, 95vw" caption="<strong>Screen-stabilized.</strong> The target is defined relative to the headset display." %}</div>
  <div>{% include figure.liquid path="assets/img/projects/eyetts/bsw.png" alt="Body-stabilized target anchored using a controller worn by the participant" sizes="(min-width: 576px) 450px, 95vw" caption="<strong>Body-stabilized.</strong> A worn controller anchors the target to the participant's body frame." %}</div>
  <div>{% include figure.liquid path="assets/img/projects/eyetts/h.png" alt="Participant tracking a target while walking through a hallway" sizes="(min-width: 576px) 450px, 95vw" caption="<strong>Hallway locomotion.</strong> The participant follows a target while moving along a corridor." %}</div>
</div>

## Calibration and analysis

The [calibration framework](https://github.com/EyeTTS/Calibration-Framework) processes participant logs into corrected gaze trajectories and task-level error measurements.

<div class="eyetts-pipeline">Recorded gaze and target logs → cleaning and temporal alignment → participant-specific recalibration → task and eye-movement analysis</div>

The [recalibration script](https://github.com/EyeTTS/Calibration-Framework/blob/main/python_scripts/recalibrate_data.py) fits participant-specific regression models and applies them across tasks. Its outputs include corrected CSV files and a consolidated error table. Separate notebooks examine target dynamics, sampling intervals, eye-movement behavior, and gaze–target lag.

<div class="eyetts-figure">
{% include figure.liquid path="assets/img/projects/eyetts/gaze_data_playback.webp" alt="Animated reconstruction of gaze and target trajectories from participant recordings" caption="Recorded trajectories can be replayed to inspect gaze, target motion, and their spatial relationship over time." %}
</div>

## Findings

### Target motion and spatial calibration

The static-versus-moving comparison shows higher tracking errors for moving targets across the five evaluated reference-frame conditions. Recalibration has a more limited, condition-dependent effect: spatial correction alone does not resolve every source of error.

<div class="eyetts-figure eyetts-figure-compact">
{% include figure.liquid path="assets/img/projects/eyetts/comparing_s_m.png" alt="Bar chart comparing static and moving target errors across w1, w2, w3, s4, and b5" caption="Static and moving targets across head-constrained, body-constrained, and walking conditions. These task-level comparisons are distinct from the eye-movement analysis below." %}
</div>

<div class="eyetts-figure">
{% include figure.liquid path="assets/img/projects/eyetts/pre-post-calibration.png" alt="Plots of moving-target errors before and after spatial recalibration" caption="Moving-target error before and after recalibration, alongside the corresponding angular-error measurements. Improvements vary across tasks." %}
</div>

### Eye-movement behavior

The [behavior-analysis notebook](https://github.com/EyeTTS/Calibration-Framework/blob/main/jupyter_notebooks/precision_saccade_smooth_fixation.ipynb) reports the following mean angular errors. The task context matters: fixation during continuous tracking and fixation during rapid recalibration are separate conditions.

<div class="eyetts-table" markdown="1">

| Eye movement and task                | Mean error | 95% confidence interval |
| :----------------------------------- | ---------: | ----------------------: |
| Smooth pursuit · continuous tracking |      0.46° |              0.40–0.52° |
| Fixation · continuous tracking       |      0.61° |              0.53–0.69° |
| Saccades · rapid recalibration       |      1.98° |              1.69–2.27° |
| Fixation · rapid recalibration       |      1.33° |              1.26–1.40° |

</div>

These are measurements from the recorded task conditions, rather than universal accuracy limits for eye tracking. They show why target dynamics and eye-movement context should be considered together.

### Temporal alignment

The [lag-analysis notebook](https://github.com/EyeTTS/Calibration-Framework/blob/main/jupyter_notebooks/time_shift.ipynb) examines the offset between target and gaze trajectories. The illustrated alignment uses a **9-frame shift**, approximately **150 ms** at 60 Hz. This observed offset combines the participant's gaze response and the tracking pipeline; it is not an isolated measurement of hardware latency.

<div class="eyetts-figure">
{% include figure.liquid path="assets/img/projects/eyetts/time_shift.png" alt="Target and gaze time series showing the effect of a nine-frame temporal shift" caption="Example gaze–target alignment over a selected recording window, before and after a nine-frame shift." %}
</div>

## My contributions

- Developed the Magic Leap 1 experimental platform and contributed to the shared study protocol.
- Built the post-hoc calibration and analysis workflow for participant recordings.
- Evaluated task-dependent gaze errors, temporal alignment, and eye-movement behavior, contributing to two first-author poster papers.

## Publications and open resources

**Eye Tracking Performance in Mobile Mixed Reality**<br>
Satyam Awasthi, Vivian Ross, Sydney Lim, Michael Beyeler, and Tobias Höllerer. IEEE VR Workshops, 2024.<br>
[Paper](https://doi.org/10.1109/VRW62533.2024.00321) · [Poster]({{ '/assets/img/projects/eyetts/IEEEVR-2024-Poster-A0.pdf' | relative_url }})

**EyeTTS: Evaluating and Calibrating Eye Tracking for Mixed-Reality Locomotion**<br>
Satyam Awasthi, Vivian Ross, Michael Beyeler, and Tobias Höllerer. IEEE ISMAR Adjunct, 2023.<br>
[Paper](https://doi.org/10.1109/ISMAR-Adjunct60411.2023.00104) · [Poster]({{ '/assets/img/projects/eyetts/ISMAR2023_poster.pdf' | relative_url }})

The [EyeTTS GitHub organization](https://github.com/EyeTTS) brings together the shared calibration and analysis framework and the three headset-specific user study implementations.

**User study frameworks**

- [Magic Leap 1](https://github.com/EyeTTS/User-Study-Framework_Magic-Leap-1) — Satyam Awasthi
- [HoloLens 2](https://github.com/EyeTTS/User-Study-Framework_Hololens-2) — Vivian Ross
- [Meta Quest Pro](https://github.com/EyeTTS/User-Study-Framework_Meta_Quest_Pro) — Sydney Lim

**Analysis and supplementary material**

- [Calibration framework and analysis notebooks](https://github.com/EyeTTS/Calibration-Framework)
- [Participant data](https://github.com/EyeTTS/Calibration-Framework/tree/main/participant-data)
- [Task demonstrations and participant recordings](https://www.youtube.com/playlist?list=PLQbqwztmTvAVAUClXj-sOkpQ9sBJbT5pG)
