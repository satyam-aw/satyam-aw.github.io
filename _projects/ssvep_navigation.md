---
layout: page
research_connection: >-
  Acquiring EEG signals and decoding intended commands connects this project to my work on closed-loop BCIs, particularly the trade-off between decoding reliability and command latency.
title: SSVEP-Based EEG Navigation
description: Toward reliable EEG-based navigation through SSVEP decoding and feedback control.
img: /assets/img/projects/bci_maze/ssvep_thumbnail.png
completed_on: "Remote collaboration · Inria, 2026–Present"
selected: true
thumbnail_credit:
  authors: "Rejer & Cieszyński"
  source: https://link.springer.com/article/10.1007/s10044-018-0758-4
  license: https://creativecommons.org/licenses/by/4.0/
importance: 1
github: https://github.com/neurocontrol-lab/ssvep-decoding
category: "Neural Interfaces & Biosignals"
related_publications: true
_styles: |
  .bci-photo { max-width: 480px; margin: 1.5rem auto; }
  .bci-screen { max-width: 720px; margin: 1.5rem auto; }
  .bci-photo figure, .bci-screen figure { margin-bottom: 0; }
  .bci-cap-photos { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; margin: 1.5rem 0; }
  .bci-cap-photos figure { margin-bottom: 0; }
  @media (max-width: 600px) { .bci-cap-photos { grid-template-columns: 1fr; } }
  .post article h2 { color: var(--global-theme-color); }
  .bci-flow { overflow-x: auto; margin: 1.5rem 0; border-radius: 6px; background: #faf3fc; }
  .bci-flow svg { display: block; width: 100%; min-width: 760px; height: auto; }
  .bci-flow .flow-node { fill: #eeeaff; stroke: #a58bdd; stroke-width: 1.5; }
  .bci-flow .flow-edge { fill: none; stroke: #39343c; stroke-width: 1.8; }
  .bci-flow .flow-arrow { fill: #39343c; }
  .bci-flow text { fill: #211c26; font-family: inherit; font-size: 15px; }
  html[data-theme="dark"] .bci-flow { background: #25212d; }
  html[data-theme="dark"] .bci-flow .flow-node { fill: #352e49; stroke: #b39adb; }
  html[data-theme="dark"] .bci-flow .flow-edge { stroke: #e3dcea; }
  html[data-theme="dark"] .bci-flow .flow-arrow { fill: #e3dcea; }
  html[data-theme="dark"] .bci-flow text { fill: #eee7f5; }
  .post article hr { margin: 2.25rem 0; border-top: 1px solid var(--global-divider-color); }
  .post article table { width: 100%; border-collapse: collapse; margin: 1.25rem 0 1.75rem; font-size: 0.95rem; line-height: 1.55; }
  .post article th, .post article td { padding: 0.8rem 1rem; vertical-align: top; border-bottom: 1px solid var(--global-table-border-color); }
  .post article .key-table thead { background: var(--global-table-header-bg); color: var(--global-text-color); }
  .post article .key-table tbody tr:nth-child(odd) { background: var(--global-table-row-bg); color: var(--global-text-color); }
  .post article .key-table tbody tr:nth-child(even) { background: var(--global-table-stripe-bg); color: var(--global-text-color); }
  .post article td:first-child { font-weight: 500; }
project_keywords:
  - SSVEP
  - EEG acquisition
  - CCA decoding
  - Confidence-aware control
project_resources:
  - label: CCA evaluation report
    url: https://github.com/neurocontrol-lab/ssvep-decoding/blob/main/docs/results/2026-10-16-round-01.md
  - label: Navigation interface
    url: https://github.com/neurocontrol-lab/ssvep-navigation-ui
  - label: Acquisition & optical tools
    url: https://github.com/neurocontrol-lab/ssvep-acquisition
  - label: Original manual-navigation demo
    url: https://youtu.be/9cJ7eTtbbqo
  - label: Original Windows game
    url: https://github.com/neurocontrol-lab/ssvep-navigation-ui/raw/refs/heads/opengl-game/resources/Play_Game.zip
project_toc: true
project_toc_level: "2"
---

**Ongoing remote research project under the guidance of Dr. Camille Gontier at Inria.**

I am building a **four-channel EEG-based brain–computer interface (BCI)** that connects attention to flickering visual targets with navigation in a 3D maze. The project combines custom-built acquisition hardware and electrode mounting, canonical correlation analysis (CCA), and decision logic for acting on uncertain signals.

The goal is reliable closed-loop navigation: a system that can recognize an intended command, wait when the evidence is weak, and return useful visual feedback. The acquisition and decoding components have been tested in exploratory on-body recordings; integrating and evaluating the complete EEG-controlled maze remains ongoing work.

---

## 1. Research question and system overview

**How can an EEG interface balance command reliability and response time when physiological signals are noisy or ambiguous?**

The maze provides a concrete task for studying this trade-off. A wrong movement can be more disruptive than waiting for additional evidence, so decoding scores must be considered alongside false activations, decision latency, and eventual navigation outcomes.

<div class="bci-flow" tabindex="0" role="region" aria-label="Scrollable EEG decoding and planned feedback-control diagram">
<svg viewBox="0 0 980 190" role="img" aria-labelledby="bci-flow-title bci-flow-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="bci-flow-title">EEG acquisition, decoding, and planned closed-loop navigation</title>
  <desc id="bci-flow-desc">Four-channel EEG flows through preprocessing, CCA scoring, and the decision layer. The dashed connection to the maze and return visual-feedback path are planned integration.</desc>
  <defs><marker id="bci-flow-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="flow-arrow" d="M 0 0 L 10 5 L 0 10 z"/></marker></defs>
  <rect class="flow-node" x="12" y="55" width="150" height="66"/>
  <rect class="flow-node" x="207" y="18" width="164" height="66"/>
  <rect class="flow-node" x="416" y="18" width="142" height="66"/>
  <rect class="flow-node" x="603" y="18" width="170" height="66"/>
  <rect class="flow-node" x="818" y="55" width="150" height="66" stroke-dasharray="5 3"/>
  <path class="flow-edge" d="M 162 69 Q 182 51 207 51" marker-end="url(#bci-flow-arrow)"/>
  <path class="flow-edge" d="M 371 51 H 416" marker-end="url(#bci-flow-arrow)"/>
  <path class="flow-edge" d="M 558 51 H 603" marker-end="url(#bci-flow-arrow)"/>
  <path class="flow-edge" d="M 773 51 Q 798 51 818 69" stroke-dasharray="5 3" marker-end="url(#bci-flow-arrow)"/>
  <path class="flow-edge" d="M 893 121 Q 893 164 850 164 H 130 Q 87 164 87 121" stroke-dasharray="3 3" marker-end="url(#bci-flow-arrow)"/>
  <text text-anchor="middle"><tspan x="87" y="82">4-channel EEG</tspan><tspan x="87" dy="21">BioAmp + MG24</tspan></text>
  <text text-anchor="middle"><tspan x="289" y="44">Preprocessing</tspan><tspan x="289" dy="21">Windowed EEG</tspan></text>
  <text text-anchor="middle"><tspan x="487" y="44">SSVEP / CCA</tspan><tspan x="487" dy="21">Target scores</tspan></text>
  <text text-anchor="middle"><tspan x="688" y="44">Decision layer</tspan><tspan x="688" dy="21">Score + persistence</tspan></text>
  <text text-anchor="middle"><tspan x="893" y="82">3D maze</tspan><tspan x="893" dy="21">Planned execution</tspan></text>
  <text x="490" y="152" text-anchor="middle">Updated visual feedback — planned loop</text>
</svg>
</div>
<div class="caption">Acquisition → preprocessing → decoding → decisions → planned navigation and visual feedback. Scroll horizontally on narrower screens.</div>

The implemented path runs from the custom-built cap through acquisition, causal filtering, CCA, and temporal decision gates to logged decisions. The remaining connection to the maze will close the interaction loop. Signal processing, decision settings, and navigation behavior are kept separate so their contributions can be evaluated independently.

---

## 2. custom-built cap and electrode mounting

I used a **winter cap, duct tape, electrode gel, and adjustable headbands** for the exploratory recordings described below. The electrodes were attached to duct tape, then secured with additional tape inside the cap to restrict movement relative to the fabric. The headbands tightened the assembly to hold the electrodes firmly against my scalp.

<div class="bci-cap-photos">
<div>
{% include figure.liquid path="assets/img/projects/bci_maze/diy_cap_headband.jpg" alt="custom-built winter-cap EEG assembly with adjustable headbands and electrode leads" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">The cap and adjustable headbands used to hold the electrodes against the scalp during the first recordings.</div>
</div>
<div>
{% include figure.liquid path="assets/img/projects/bci_maze/diy_cap_connections.jpg" alt="Inside the custom-built EEG cap, showing electrodes and wires secured to the fabric with duct tape" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">Electrodes attached to duct tape and taped into the cap, restricting movement relative to the cap fabric.</div>
</div>
</div>

The nominal signal sites were **O1, O2, Oz, and POz**. All four BioAmp negative differential inputs (`IN-`) shared Cz; the separately named `REF` terminals shared the left mastoid. The intended channel differences were therefore approximately O1–Cz, O2–Cz, Oz–Cz, and POz–Cz. `REF` is distinct from both `IN-` and power ground.

This montage was documented retrospectively. The ADC-input-to-scalp-site mapping is no longer known, so individual channel results cannot be assigned to a specific scalp site. Electrode-position accuracy and contact impedance were not measured. The mounting approach was intended to improve contact and limit movement; its effect on signal quality has not been isolated experimentally.

A cotton skull cap with press-stud mounting is planned for the next setup. It was **not used for the reported results**; any change in mounting or montage will be recorded as a separate configuration.

---

## 3. Acquisition and CCA pipeline

The hardware uses four **BioAmp EXG Pill** analog front ends connected to a **XIAO MG24**. The BioAmp boards are covered in Kapton tape to help prevent accidental shorts.

<div class="bci-photo">
{% include figure.liquid path="assets/img/projects/bci_maze/bioamp_4_channel_ensemble-common_gnd_ref.jpg" alt="Four BioAmp front ends covered in Kapton tape and connected to the acquisition assembly" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">Four-channel BioAmp assembly. The montage used for the first recordings is documented above; shared negative inputs and REF terminals have distinct roles.</div>
</div>

The tested decoder supports live MG24 input, recording replay, and synthetic input. It applies causal filtering, computes CCA scores, checks signal and timing quality, and logs candidate targets and command decisions.

| Component       | Tested configuration                                                                     |
| --------------- | ---------------------------------------------------------------------------------------- |
| Acquisition     | Four sequentially sampled inputs, D1–D4, at nominally 250 scans/s; raw 12-bit ADC counts |
| Filtering       | Causal fourth-order Butterworth bandpass, 6–48 Hz; one-second warmup                     |
| CCA references  | Sine/cosine signals at each target's fundamental and first two higher harmonics          |
| Window / update | Two seconds / 63 samples, or 252 ms at 250 scans/s                                       |
| Output          | Recorded scores and decisions; keyboard output disabled                                  |

For EEG window $X_t$ and sine/cosine reference matrix $Y_i$ for target $i$, CCA produces:

$$
s_i(t)=\max_{a,b}\operatorname{corr}(X_t a,Y_i b),
\qquad i_t^*=\arg\max_i s_i(t).
$$

The reference matrix includes the fundamental and its harmonics; the winning score ranks the candidate targets. The implementation uses a rank-aware SVD to handle redundant channels. **A CCA score is not a calibrated probability of intention.**

All seven received streams had no sequence gaps and approximately 250 scans/s according to MCU timestamps; the last received missed-deadline and queue-overflow counters were zero. This supports decoder comparisons on the received data, but does not establish calibrated EEG amplitudes or completeness of samples still buffered when recording stopped.

The three repositories separate [decoding and decisions](https://github.com/neurocontrol-lab/ssvep-decoding), [acquisition and optical tools](https://github.com/neurocontrol-lab/ssvep-acquisition), and the [navigation interface](https://github.com/neurocontrol-lab/ssvep-navigation-ui).

---

## 4. Visual targets and optical timing

The maze already provides four frame-sequenced targets, mapped to forward, backward, turn left, and turn right. The first CCA recordings used the **separate PsychoPy single-target display**, rather than EEG control of this maze.

<div class="bci-screen">
{% include figure.liquid path="assets/img/projects/bci_maze/flickering_targets.png" alt="OpenGL maze with four directional SSVEP targets and a compass and timer" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">Four targets in the navigation interface. This screenshot shows their arrangement, not validated flicker timing or EEG-controlled navigation.</div>
</div>

For a frame sequence, nominal frequency is monitor refresh divided by the total bright and dark frames per cycle. At 60 Hz, the current 7/6/5/4-frame sequences correspond to approximately **8.571, 10, 12, and 15 Hz**. Changing the monitor or missing refreshes changes the delivered stimulus.

I built a **BPW34 photodiode circuit with a XIAO MG24** to measure optical output. Black foam and duct tape shield the detector from ambient light and neighboring targets; firmware and Python tools capture samples and report frequency and timing statistics.

<div class="bci-photo">
{% include figure.liquid path="assets/img/projects/bci_maze/optical_frequency_validation_circuit.jpg" alt="Shielded BPW34 photodiode wired to a XIAO MG24 for optical stimulus measurement" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">Optical measurement hardware. Each target still needs validation in its actual display configuration and under navigation load.</div>
</div>

PsychoPy frame logs exposed a long interruption in the first left recording, motivating a repeat. Software flip logs help diagnose display behavior, but synchronized optical onset and EEG timing remain future work.

---

## 5. Evaluation and findings

Initial evaluation comprises four single-target conditions, repeats for left and right, and a separate rest-only baseline, recorded on 16 October 2026. Each stimulus run presented **one black/white PsychoPy target at a time**, with four 12-second stimulation periods separated by 3-second gray rests. EEG recordings lasted approximately 75–77 seconds.

The decoder compared all four candidate frequencies even though only one target was displayed. The table summarizes interior stimulation windows, excluding transitions using approximate alignment between decoder and stimulus host timestamps.

<div class="key-table" markdown="1">

| Recording    | Nominal frequency | Attended target ranked highest | Mean CCA score: stimulation / short rest |
| ------------ | ----------------: | -----------------------------: | ---------------------------------------: |
| Forward      |          8.571 Hz |        85.5% (130/152 windows) |                            0.397 / 0.248 |
| Backward     |             10 Hz |        73.4% (113/154 windows) |                            0.325 / 0.272 |
| Left         |             12 Hz |         60.0% (93/155 windows) |                            0.329 / 0.237 |
| Right        |             15 Hz |         45.0% (68/151 windows) |                            0.305 / 0.200 |
| Left repeat  |             12 Hz |         60.7% (91/150 windows) |                            0.326 / 0.232 |
| Right repeat |             15 Hz |         52.7% (79/150 windows) |                            0.317 / 0.208 |

</div>

The attended-target mean score was higher during stimulation than during short rests in every recording. Forward showed the strongest ranking; right remained the least distinct. The left repeat produced a similar ranking after a long display interruption in the first run was absent.

These are **overlapping two-second windows**, not independent trials. The short rests provide few interior windows, timing alignment is approximate, and the frequencies are nominal rather than optically measured for these recordings. The findings support further testing with the custom-built setup; they do not yet establish neural specificity, held-out accuracy, or reliable command control.

[Read the full recording report](https://github.com/neurocontrol-lab/ssvep-decoding/blob/main/docs/results/2026-10-16-round-01.md) for session IDs, timing diagnostics, selection rules, and threshold-replay results. Raw recordings are retained locally rather than published in the repository.

---

## 6. Command decisions and feedback

The implemented gate issues a command only when signal quality is valid, the winning CCA score exceeds a threshold, and its lead over the runner-up persists:

$$
u_t=\begin{cases}
\operatorname{action}(i_t^*), & q_t=1,\;s_{i_t^*}\geq\tau,\;s_{i_t^*}-s_{(2)}\geq\delta,\;T_{\mathrm{persist}}\geq T_p,\\
\mathrm{wait}, & \text{otherwise}.
\end{cases}
$$

Here $q_t$ marks valid signal quality and $s_{(2)}$ is the runner-up score. Current settings are $\tau=0.55$, $\delta=0.10$, and $T_p=0.75$ s; invalid or ambiguous evidence resets persistence. These settings emitted no commands in the seven exploratory recordings. Lowering the score threshold to 0.40 recovered some intended commands but also four emissions in the rest-only recording, motivating calibration on development data and evaluation on fresh recordings.

### Planned extension: error feedback

**Can the system detect that an action was wrong and use that evidence to correct subsequent control?** EEG error-related potentials motivate a separate error-monitoring path; continuous error-related activity may also support graded feedback {% cite ferrez2008errp yasemin2023errp pulferer2024feedback %}. Parallel error correction in intracortical BCIs, including Gontier et al.'s human error-damping preprint, provides complementary architectural motivation {% cite evenchen2017errors gontier2026errordamping %}.

This is a future extension, distinct from CCA confidence gating. It requires event-aligned error recordings, suitable electrode coverage, and evaluation of false corrections and added latency. The current posterior montage has not been evaluated for error detection. After establishing navigation, I plan to compare intention-only, confidence-gated, and error-feedback control.

---

## 7. Current status and next steps

<div class="key-table" markdown="1">

| Component                                     | Current status                                      | Next step                                                                    |
| --------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------- |
| custom-built cap and four-channel acquisition | Used for the first on-body recordings               | Document channel mapping and evaluate the next mounting configuration        |
| Live CCA and recording replay                 | Implemented; seven exploratory recordings analyzed  | Compare windows and harmonics on development data                            |
| Decision gates and temporal persistence       | Implemented; default settings emitted no commands   | Calibrate target separation and idle rejection; evaluate on fresh recordings |
| PsychoPy stimuli and optical tools            | Used for stimulus presentation / hardware exercised | Synchronize optical onset with EEG and improve timing characterization       |
| OpenGL maze and four targets                  | Manual navigation implemented                       | Validate target timing under load and integrate command delivery             |
| Closed-loop EEG navigation                    | Not yet demonstrated                                | Evaluate simultaneous targets, command latency, and task outcomes            |
| Neural error feedback                         | Planned research extension                          | Establish event-aligned recordings and evaluate an error-monitoring path     |

</div>

---

## 8. Navigation environment and origins

The maze was originally developed for **UCSB CS280 in Spring 2022** using C++, OpenGL, and FreeGLUT. It includes collision-aware movement, mouse look, strafing and jumping, a compass and timer, and file-based maze layouts.

The original game is preserved on the navigation repository's `opengl-game` branch. Its demo shows manual control before EEG integration.

<div style="aspect-ratio: 16/9; width: 100%; max-width: 720px; margin: 1.5rem auto;">
  <iframe width="100%" height="100%" src="https://www.youtube.com/embed/9cJ7eTtbbqo" title="Original manually controlled OpenGL maze environment" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div class="caption">Original manually controlled maze demonstration.</div>

---

<p class="small text-muted"><strong>Thumbnail credit:</strong> Izabela Rejer and Łukasz Cieszyński, <a href="https://link.springer.com/article/10.1007/s10044-018-0758-4">“Independent component analysis for a low-channel SSVEP-BCI”</a>, <em>Pattern Analysis and Applications</em> 22, 47–62 (2019), Figure 1. Source diagram used as a resized project thumbnail under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. It illustrates the general SSVEP-BCI concept; the hardware photographs and navigation screenshot above document this project.</p>
