---
layout: page

title: EEG-Based BCI for 3D Navigation
description: Developing a 4-channel SSVEP-based EEG brain-computer interface for real-time intent decoding and navigation in an interactive 3D environment.
img: assets/img/projects/bci_maze/bioamp-hardware.jpg

completed_on: "(BCI Extension) 2026–Present"
selected: true

importance: 1

download_link: https://github.com/satyam-aw/3d_Maze_openGL/raw/refs/heads/main/resources/Play_Game.zip
demo_video: https://youtu.be/9cJ7eTtbbqo

category: "Neural Interfaces & Biosignals"
---

<div style="
  padding: 20px 24px;
  margin-bottom: 28px;
  border-left: 4px solid var(--global-theme-color);
  background: var(--global-card-bg-color);
  border-radius: 6px;
" markdown="1">

### 🧠 Ongoing Brain–Computer Interface Project

I am extending a previously developed interactive 3D navigation environment into a **4-channel EEG-based brain-computer interface (BCI)**.

The project focuses on building an end-to-end neural control pipeline:

**EEG acquisition → signal preprocessing → neural feature extraction → intent decoding → confidence-aware control → interactive navigation**

The initial objective is to decode a small set of discrete movement intentions from EEG and use them to navigate a virtual maze in real time.

</div>


---

<br>

## 1. Project Goal

Brain-computer interfaces provide a direct pathway from neural activity to external control, but practical systems must deal with several challenges:

- EEG signals have low signal-to-noise ratio,
- neural responses vary across time and recording sessions,
- classification decisions arrive at relatively low bandwidth,
- erroneous commands can significantly disrupt interactive control.

This project investigates a compact BCI pipeline in which neural signals are decoded into discrete navigation commands inside a controlled virtual environment.

The 3D maze provides a repeatable testbed where both **neural decoding performance** and **task-level control performance** can be measured quantitatively.

---

<br>

## 2. EEG Acquisition Hardware

The current hardware design uses **BioAmp EXG Pill** analog front ends for EEG acquisition.

<div class="row mt-3">

  <div class="col-sm-6 mt-3 mt-md-0">
    {% include figure.liquid
      loading="eager"
      path="assets/img/projects/bci_maze/bioamp-hero.avif"
      title="BioAmp EXG Pill"
      caption="BioAmp EXG Pill analog front end selected for EEG acquisition."
      class="img-fluid rounded z-depth-1"
      zoomable=true
    %}
  </div>

  <div class="col-sm-6 mt-3 mt-md-0">
    {% include figure.liquid
      loading="eager"
      path="assets/img/projects/bci_maze/bioamp-pinout.jpg"
      title="BioAmp EXG hardware interface"
      caption="Analog EEG front end used as the basis of the planned multi-channel acquisition system."
      class="img-fluid rounded z-depth-1"
      zoomable=true
    %}
  </div>

</div>

<p style="
  text-align: center;
  font-style: italic;
  font-size: 0.85em;
  color: #777;
  margin-top: 8px;
">
Hardware reference images: BioAmp EXG Pill / Robu.in.
</p>

The planned four-channel acquisition architecture is:

$$
\text{EEG Electrodes}
\rightarrow
\text{Analog Front Ends}
\rightarrow
\text{Multi-channel ADC}
\rightarrow
\text{Microcontroller}
\rightarrow
\text{Real-time Decoder}
$$

The modular electrode setup allows the recording locations to be selected according to the BCI paradigm rather than being constrained by a fixed consumer headset.

---

<br>

## 3. Initial BCI Paradigm: SSVEP

The first experimental direction is **Steady-State Visual Evoked Potential (SSVEP)** decoding.

Several visual targets flicker at distinct frequencies, with each stimulus associated with a navigation command.

For example:

| Stimulus | Intended Action |
|---|---|
| $f_1$ | Turn Left |
| $f_2$ | Move Forward |
| $f_3$ | Turn Right |

When a user visually attends to one of these stimuli, neural activity in posterior visual regions can exhibit a frequency-locked response related to the attended stimulus.

The EEG decoder therefore attempts to estimate

$$
\hat{c}
=
\arg\max_{c \in \mathcal{C}}
S_c(X),
$$

where:

- $X$ is a temporal window of multi-channel EEG,
- $\mathcal{C}$ is the set of candidate commands,
- $S_c$ is the decoder score associated with command $c$.

The initial experiments will determine suitable stimulus frequencies, electrode locations, window lengths, and decision thresholds empirically.

---

<br>

## 4. Neural Signal Processing Pipeline

The real-time decoding pipeline will operate on overlapping windows of continuously acquired EEG.

Planned preprocessing includes:

- removal of DC drift,
- band-pass filtering,
- power-line interference suppression,
- optional artifact rejection,
- normalization across channels,
- sliding-window segmentation.

For SSVEP decoding, the project will investigate:

- frequency-domain power,
- Power Spectral Density (PSD),
- signal-to-noise ratio around target frequencies,
- harmonic responses,
- Canonical Correlation Analysis (CCA),
- temporal aggregation across consecutive predictions.

The objective is not only to maximize offline classification accuracy, but to determine which decoding strategy remains sufficiently stable for **closed-loop interactive use**.

---

<br>

## 5. Real-Time BCI Architecture

The software pipeline separates acquisition, decoding, and interactive control.

```text
┌───────────────────────┐
│   4-Channel EEG       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Signal Acquisition    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Filtering / Artifact  │
│      Processing       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Sliding EEG Window    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ SSVEP Feature         │
│ Extraction / CCA      │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Intent Decoder        │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Confidence / Temporal │
│ Decision Logic        │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Navigation Command    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Interactive 3D Maze   │
└───────────────────────┘
````

A key design goal is to keep the **neural decoder independent from the environment**, allowing different classification and decision strategies to be compared without modifying the underlying navigation system.

---

<br>

## 6. Confidence-Aware Neural Control

A BCI classifier does not always produce an equally reliable prediction.

Instead of immediately executing every neural decision, the controller can use the decoder's confidence to determine whether sufficient evidence exists to act.

For a command probability vector

$$
p =
\begin{bmatrix}
p_{\text{left}} &
p_{\text{forward}} &
p_{\text{right}}
\end{bmatrix},
$$

the controller can execute

$$
u =
\arg\max_i p_i
$$

only when

$$
\max_i p_i \geq \tau,
$$

where $\tau$ is a confidence threshold.

Otherwise, the system can defer the command and collect another EEG window.

This introduces a natural trade-off between:

$$
\text{response latency}
\quad \leftrightarrow \quad
\text{command reliability}.
$$

The project will investigate this trade-off experimentally.

---

<br>

## 7. Temporal Evidence Accumulation

EEG decoding also allows decisions to be accumulated across time instead of treating each window independently.

For example, decoder evidence can be combined over successive windows:

$$
\bar{p}_t
=========

\alpha p_t
+
(1-\alpha)\bar{p}_{t-1},
$$

where:

* $p_t$ is the current decoder output,
* $\bar{p}_t$ is the temporally smoothed decision estimate,
* $\alpha$ controls responsiveness versus stability.

This provides another mechanism for reducing isolated false predictions while maintaining responsive BCI control.

---

<br>

## 8. Environment-Aware Shared Control

The virtual maze enables a later investigation into **shared control**, where neural intention is combined with basic knowledge about valid actions.

The EEG decoder remains responsible for estimating user intent.

The environment can then reject commands that are physically impossible or clearly inconsistent with the current state.

For example:

```text
EEG Prediction
      │
      ▼
"Turn Left"
      │
      ▼
Is Left Action Valid?
   /          \
 Yes           No
  │             │
Execute      Reject /
Command      Re-sample
```

This creates three natural controller variants:

$$
\text{Direct EEG Control}
$$

$$
\text{Confidence-Gated EEG Control}
$$

$$
\text{EEG + Environment-Aware Shared Control}.
$$

The aim is to study whether lightweight assistance can improve usability without replacing the user's neural command.

---

<br>

## 9. Planned Experimental Evaluation

The project will be evaluated at both the **neural decoding level** and the **interactive control level**.

### Neural decoding metrics

* classification accuracy,
* confusion matrix,
* per-class precision and recall,
* false activation rate,
* command latency,
* cross-session consistency.

For BCI communication efficiency, the project will also measure **Information Transfer Rate (ITR)**.

### Navigation metrics

* maze completion time,
* incorrect movement commands,
* rejected commands,
* number of decoder decisions required,
* path efficiency,
* task completion rate.

These measurements will allow comparison between different signal-processing and control strategies.

---

<br>

## 10. Experimental Roadmap

<div style="
  padding: 18px 22px;
  margin: 15px 0 25px 0;
  background: var(--global-card-bg-color);
  border-radius: 6px;
" markdown="1">

**Stage 1 — EEG acquisition**  
Acquire clean multi-channel EEG and characterize signal quality.

↓

**Stage 2 — Offline SSVEP decoding**  
Collect labeled trials and evaluate spectral / CCA-based classification.

↓

**Stage 3 — Online intent decoding**  
Stream EEG and produce movement predictions in real time.

↓

**Stage 4 — Closed-loop maze control**  
Connect the neural decoder to the interactive navigation interface.

↓

**Stage 5 — Confidence-aware control**  
Evaluate decision thresholds and temporal evidence accumulation.

↓

**Stage 6 — Shared BCI navigation**  
Investigate environment-aware filtering of neural commands.

</div>

---

<br>

## 11. Existing Interactive Test Environment

The BCI controller is being integrated into a previously developed first-person 3D maze.

The environment already provides:

* discrete and continuous movement commands,
* collision-aware navigation,
* real-time state updates,
* multiple maze layouts,
* a repeatable environment for measuring navigation performance.

This makes it possible to focus the current project on **EEG acquisition, neural decoding, and human-machine control** rather than developing a new interactive environment from scratch.

---

<br>

## Original Environment Demo

<div style="
  aspect-ratio: 16/9;
  width: 110%;
  margin-left: -5%;
  margin-right: -5%;
">

  <iframe
    width="100%"
    height="100%"
    src="https://www.youtube.com/embed/9cJ7eTtbbqo"
    title="3D Maze Navigation Environment"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>

</div>

<p style="
  text-align: center;
  font-style: italic;
  font-size: 0.9em;
  color: #666;
  margin-top: 8px;
">
Original navigation environment now being used as the testbed for the EEG-based BCI.
</p>

The environment was originally developed as a UCSB graphics project in Spring 2022 using C++ and OpenGL. Its existing real-time navigation and collision system now provides the software interface for the ongoing neural-control work.

##### Links

* **Source Code:** [GitHub Repository](https://github.com/satyam-aw/3d_Maze_openGL)
* **Original Windows Demo:** [Play_Game.zip](https://github.com/satyam-aw/3d_Maze_openGL/raw/refs/heads/main/resources/Play_Game.zip)

---

<br>

## Current Status

| Component                          | Status                  |
| ---------------------------------- | ----------------------- |
| Interactive navigation environment | ✅ Complete              |
| EEG acquisition hardware           | 🔧 Hardware integration |
| 4-channel EEG recording            | 🔧 In development       |
| EEG preprocessing pipeline         | 🔧 In development       |
| Offline SSVEP decoding             | ⏳ Planned               |
| Real-time intent decoding          | ⏳ Planned               |
| EEG-controlled navigation          | ⏳ Planned               |
| Confidence-aware BCI controller    | ⏳ Planned               |
| Shared-control experiments         | ⏳ Planned               |

The long-term objective is to develop a compact experimental platform for studying **neural signal decoding, brain-computer interaction, and reliable closed-loop control from low-bandwidth EEG inputs**.

