---
layout: page
# TODO (next portfolio update): document temporal evidence acquisition (requested 2026-10-29).
research_connection: >-
  Acquiring EEG signals and decoding intended commands connects this project to my work on closed-loop BCIs, particularly the trade-off between decoding reliability and command latency.
title: SSVEP-Based EEG Navigation
description: Toward reliable EEG-based navigation through SSVEP decoding and feedback control.
img: /assets/img/projects/bci_maze/ssvep_thumbnail.png
completed_on: "Remote collaboration · Inria, 2026–Present"
selected: true
pinned: true
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
  .bci-cap-photos { display: grid; grid-template-columns: repeat(2, minmax(0, 17rem)); justify-content: center; gap: 1rem; margin: 1.5rem 0; }
  .bci-cap-photos figure, .bci-photo-strip figure { margin-bottom: 0; }
  @media (max-width: 600px) { .bci-cap-photos { grid-template-columns: min(17rem, 78%); } }
  .bci-photo-strip { display: flex; gap: 1rem; overflow-x: auto; margin: 0.5rem 0 1.5rem; padding: 0.25rem 0.125rem 0.75rem; scroll-snap-type: x proximity; }
  .bci-photo-strip > div { flex: 0 0 min(var(--bci-photo-width, 17rem), 78%); min-width: 0; scroll-snap-align: start; }
  .bci-cap-photos img, .bci-photo-strip img { width: 100%; aspect-ratio: 4 / 3; object-fit: contain; }
  .bci-photo-strip:focus-visible { outline: 2px solid var(--global-theme-color); outline-offset: 3px; }
  .bci-launcher-strip { --bci-photo-width: 30rem; }
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
  - label: "🌐︎ Navigation interface"
    url: https://github.com/neurocontrol-lab/ssvep-navigation-ui
  - label: "🌐︎ Acquisition & optical tools"
    url: https://github.com/neurocontrol-lab/ssvep-acquisition
  - label: October single-target report
    url: https://github.com/neurocontrol-lab/ssvep-decoding/blob/main/docs/results/2026-10-16-round-01.md
  - label: Development and diagnostic sessions
    url: https://github.com/neurocontrol-lab/ssvep-decoding/blob/main/docs/results/session-catalog.md
  - label: "[ ▶︎ ] Original manual-navigation demo"
    url: https://youtu.be/9cJ7eTtbbqo
  - label: "⤓ Original Windows game"
    url: https://github.com/neurocontrol-lab/ssvep-navigation-ui/raw/refs/heads/opengl-game/resources/Play_Game.zip
project_toc: true
project_toc_level: "2"
---

**Ongoing remote research project under the guidance of Dr. Camille Gontier at Inria.**

I am investigating how a **four-channel EEG brain–computer interface (BCI)** can balance command reliability and response time in a 3D navigation task. I built a custom EEG acquisition setup and fitted cap, then linked a canonical correlation analysis (CCA) decoder to a maze with four flickering targets. The live link has been exercised end to end. Reliable EEG steering remains the research objective.

---

## 1. Research question and system overview

**How can an EEG interface balance command reliability and response time when physiological signals are noisy or ambiguous?**

The maze provides a concrete task for studying this trade-off. A wrong movement can be more disruptive than waiting for additional evidence, so decoding scores must be considered alongside false activations, decision latency, and eventual navigation outcomes.

<div class="bci-flow" tabindex="0" role="region" aria-label="Scrollable EEG decoding and navigation feedback diagram">
<svg viewBox="0 0 980 190" role="img" aria-labelledby="bci-flow-title bci-flow-desc" xmlns="http://www.w3.org/2000/svg">
  <title id="bci-flow-title">EEG acquisition, decoding, and maze feedback</title>
  <desc id="bci-flow-desc">Four-channel EEG flows through preprocessing, CCA scoring, and the decision layer. The decoder sends scores and eligible commands to the maze, which displays visual feedback.</desc>
  <defs><marker id="bci-flow-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="flow-arrow" d="M 0 0 L 10 5 L 0 10 z"/></marker></defs>
  <rect class="flow-node" x="12" y="55" width="150" height="66"/>
  <rect class="flow-node" x="207" y="18" width="164" height="66"/>
  <rect class="flow-node" x="416" y="18" width="142" height="66"/>
  <rect class="flow-node" x="603" y="18" width="170" height="66"/>
  <rect class="flow-node" x="818" y="55" width="150" height="66"/>
  <path class="flow-edge" d="M 162 69 Q 182 51 207 51" marker-end="url(#bci-flow-arrow)"/>
  <path class="flow-edge" d="M 371 51 H 416" marker-end="url(#bci-flow-arrow)"/>
  <path class="flow-edge" d="M 558 51 H 603" marker-end="url(#bci-flow-arrow)"/>
  <path class="flow-edge" d="M 773 51 Q 798 51 818 69" marker-end="url(#bci-flow-arrow)"/>
  <path class="flow-edge" d="M 893 121 Q 893 164 850 164 H 130 Q 87 164 87 121" stroke-dasharray="3 3" marker-end="url(#bci-flow-arrow)"/>
  <text text-anchor="middle"><tspan x="87" y="82">4-channel EEG</tspan><tspan x="87" dy="21">BioAmp + MG24</tspan></text>
  <text text-anchor="middle"><tspan x="289" y="44">Preprocessing</tspan><tspan x="289" dy="21">Windowed EEG</tspan></text>
  <text text-anchor="middle"><tspan x="487" y="44">SSVEP / CCA</tspan><tspan x="487" dy="21">Target scores</tspan></text>
  <text text-anchor="middle"><tspan x="688" y="44">Decision layer</tspan><tspan x="688" dy="21">Score + persistence</tspan></text>
  <text text-anchor="middle"><tspan x="893" y="82">3D maze</tspan><tspan x="893" dy="21">HUD + steering</tspan></text>
  <text x="490" y="152" text-anchor="middle">Visual feedback from the maze</text>
</svg>
</div>
<div class="caption">The implemented path from EEG acquisition to maze feedback. Scroll horizontally on narrower screens.</div>

The maze receives live scores and accepted actions over local UDP. It can display decisions during manual navigation or apply a short movement pulse when an eligible command arrives and steering is armed. Keeping acquisition, decisions, and maze behavior separate makes it possible to compare offline replay, cued tests, and live integration runs.

---

## 2. DIY EEG cap and montage

### First prototype

For the October recordings, I used a winter cap, duct tape, electrode gel, and adjustable headbands. Tape held the electrodes and leads against the inside of the cap, and the headbands pressed the assembly against my scalp.

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

The nominal sites were O1, O2, Oz, and POz, with shared BioAmp `IN-` at Cz and shared `REF` at the left mastoid. The original ADC-to-site order was unrecorded, which limits channel-by-channel interpretation of those results.

### Fitted cap with press-stud mounts

For the November tests, I fitted a cotton skull cap to my own head. With the cap on, I located the inion at the back of my skull, marked the posterior sites around the occipital region and the mastoids behind each ear, then placed the press-stud mounts at those marks. I used a wide headband over the cap to help maintain contact. The design gives the electrodes defined positions for repeated setups. Placement repeatability and contact impedance remain to be measured.

<p id="bci-cap-scroll-hint" class="small text-muted mb-1">Scroll sideways to see all four views.</p>
<div class="bci-photo-strip" role="region" tabindex="0" aria-label="Fitted EEG cap photos" aria-describedby="bci-cap-scroll-hint">
<div>
{% include figure.liquid path="assets/img/projects/bci_maze/eeg_cap_20261108_011657.jpg" alt="Cotton EEG cap laid flat with marked press-stud positions on the back and sides" loading="lazy" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">Exterior of the fitted cap with the marked mounting positions and press studs.</div>
</div>
<div>
{% include figure.liquid path="assets/img/projects/bci_maze/eeg_cap_20261108_012211.jpg" alt="Inside the cotton EEG cap showing the press studs, with a wide headband beside it" loading="lazy" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">Interior of the cap and the separate headband used to hold it in place.</div>
</div>
<div>
{% include figure.liquid path="assets/img/projects/bci_maze/eeg_cap_20261108_014820.jpg" alt="Rear view of the fitted EEG cap with posterior mounts and leads running to the acquisition hardware" loading="lazy" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">Rear view of the fitted cap and lead routing during setup.</div>
</div>
<div>
{% include figure.liquid path="assets/img/projects/bci_maze/eeg_cap_20261108_020410.jpg" alt="Rear view of the fitted EEG cap held in place by the wide headband" loading="lazy" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">On-body fit with the headband in place for recording.</div>
</div>
</div>

| Connection          | Site          |
| ------------------- | ------------- |
| MG24 D1             | O1            |
| MG24 D2             | Oz            |
| MG24 D3             | O2            |
| MG24 D4             | POz           |
| Shared BioAmp `IN-` | Right mastoid |
| Shared BioAmp `REF` | Left mastoid  |

The decoder records this wiring as `occipital-mastoid-v1` when selected. `IN-` is the shared negative signal input, and `REF` is a separate BioAmp terminal. MG24 D0 is tied to MCU ground for diagnostics and excluded from decoding. [Montage record](https://github.com/neurocontrol-lab/ssvep-decoding/blob/main/docs/montages.md)

---

## 3. Acquisition and CCA pipeline

The hardware uses four **BioAmp EXG Pill** analog front ends connected to a **XIAO MG24**. The BioAmp boards are covered in Kapton tape to help prevent accidental shorts.

<div class="bci-photo">
{% include figure.liquid path="assets/img/projects/bci_maze/bioamp_4_channel_ensemble-common_gnd_ref.jpg" alt="Four BioAmp front ends covered in Kapton tape and connected to the acquisition assembly" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">Four-channel BioAmp assembly. The montage used for the first recordings is documented above; shared negative inputs and REF terminals have distinct roles.</div>
</div>

The tested decoder supports live MG24 input, recording replay, and synthetic input. It applies causal filtering, computes CCA scores, checks signal and timing quality, and logs candidate targets and command decisions.

| Component       | Tested configuration                                                                                                       |
| --------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Acquisition     | Four sequentially sampled inputs, D1–D4, at nominally 250 scans/s; raw 12-bit ADC counts                                   |
| Filtering       | Causal fourth-order Butterworth bandpass, 6–48 Hz; one-second warmup                                                       |
| CCA references  | Sine/cosine signals at each target's fundamental and first two higher harmonics                                            |
| Window / update | Two seconds in the October recordings and two- or four-second windows in November, updated every 63 samples (about 252 ms) |
| Output          | Saved scores and decision logs, with an optional live link to the maze                                                     |

For EEG window $X_t$ and sine/cosine reference matrix $Y_i$ for target $i$, CCA produces:

$$
s_i(t)=\max_{a,b}\operatorname{corr}(X_t a,Y_i b),
\qquad i_t^*=\arg\max_i s_i(t).
$$

The reference matrix includes the fundamental and its harmonics; the winning score ranks the candidate targets. The implementation uses a rank-aware SVD to handle redundant channels. **A CCA score is not a calibrated probability of intention.**

The seven October recordings had no sequence gaps in the received data and ran at approximately 250 scans/s by MCU timestamps. The last received missed-deadline and queue-overflow counters were zero. These checks describe acquisition continuity in those recordings.

The three repositories separate [decoding and decisions](https://github.com/neurocontrol-lab/ssvep-decoding), [acquisition and optical tools](https://github.com/neurocontrol-lab/ssvep-acquisition), and the [navigation interface](https://github.com/neurocontrol-lab/ssvep-navigation-ui).

---

## 4. Visual targets and test workflow

The maze provides four frame-sequenced targets for forward, backward, turn left, and turn right. Standalone PsychoPy sessions provide gaze cues and rest intervals for controlled comparisons. The maze adds a navigation task, moving visual content, and feedback about decoder scores and steering.

<div class="bci-screen">
{% include figure.liquid path="assets/img/projects/bci_maze/flickering_targets.png" alt="OpenGL maze with four bordered SSVEP targets, a central route hint, and a decoder HUD" loading="lazy" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">The current maze interface in keyboard-only mode, showing the four targets at one instant in their flicker cycles.</div>
</div>

For a frame sequence, nominal frequency is monitor refresh divided by the total bright and dark frames per cycle. At 60 Hz, the current 7/6/5/4-frame sequences correspond to approximately **8.571, 10, 12, and 15 Hz**. Changing the monitor or missing refreshes changes the delivered stimulus.

I built a **BPW34 photodiode circuit with a XIAO MG24** to measure optical output. Black foam and duct tape shield the detector from ambient light and neighboring targets; firmware and Python tools capture samples and report frequency and timing statistics.

<div class="bci-photo">
{% include figure.liquid path="assets/img/projects/bci_maze/optical_frequency_validation_circuit.jpg" alt="Shielded BPW34 photodiode wired to a XIAO MG24 for optical stimulus measurement" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">Optical measurement hardware. Each target still needs validation in its actual display configuration and under navigation load.</div>
</div>

PsychoPy frame logs exposed a long interruption in the first left recording, motivating a repeat. I use the photodiode to check the light output and software frame logs to diagnose display interruptions. Synchronizing optical onset to the EEG stream remains a separate timing task.

### Launchers for repeated tests

The **decoder test launcher** runs cued single-target, four-target, or rest-only sessions. It exposes the display profile and decision settings, saves the selected montage and resolved profiles with the recording, and produces a summary that can be compared with replays.

The **navigation launcher** selects fullscreen or windowed mode, route hints, the accepted-command overlay, and decoder mode. It can start a decoder from a chosen checkout, connect to a running decoder, or run with keyboard control. Managed runs can show live decisions in monitor mode or enable EEG steering. A separate stimulus tab previews the target frequencies. The maze checks those references against the active display before arming steering.

<details class="bci-launcher-details">
<summary>View the test and navigation launchers</summary>
<p id="bci-launcher-scroll-hint" class="small text-muted mt-2 mb-1">Scroll sideways to see both launchers.</p>
<div class="bci-photo-strip bci-launcher-strip" role="region" tabindex="0" aria-label="Launcher screenshots" aria-describedby="bci-launcher-scroll-hint">
<div>
{% include figure.liquid path="assets/img/projects/bci_maze/decoder_test_launcher.png" alt="PsychoPy and EEG test launcher showing the cued test, timing, and decoder settings" loading="lazy" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">The standalone test launcher configures cued and rest recordings.</div>
</div>
<div>
{% include figure.liquid path="assets/img/projects/bci_maze/navigation_launcher.png" alt="Navigation launcher showing decoder source, serial port, output mode, and profile settings" loading="lazy" class="img-fluid rounded z-depth-1" zoomable=true %}
<div class="caption">The navigation launcher's Decoder tab configures the live link to the maze.</div>
</div>
</div>
</details>

---

## 5. Evaluation and findings

### October single-target recordings

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

The recording report includes session IDs, timing diagnostics, selection rules, and threshold-replay results. Raw recordings are retained locally. [October recording report](https://github.com/neurocontrol-lab/ssvep-decoding/blob/main/docs/results/2026-10-16-round-01.md)

### November four-target and maze diagnostics

On 8 November 2026, I ran four-target PsychoPy sessions with the fitted cap and bilateral mastoid montage, then exercised the live decoder-to-maze link. In the cued PsychoPy tests, all four targets were visible during stimulation and the cue identified the target to attend. The maze runs exercised the online link without synchronized gaze cues.

| Run                                   | CCA window        | Peak live score | Commands emitted |
| ------------------------------------- | ----------------- | --------------: | ---------------: |
| Cued four-target run                  | 2 s / 3 harmonics |           0.549 |                0 |
| Cued four-target repeat               | 4 s / 3 harmonics |           0.384 |                0 |
| Latest maze run with EEG data         | 4 s / 3 harmonics |           0.450 |                0 |
| PsychoPy checks after low maze scores | 4 s / 3 harmonics | 0.336 and 0.489 |        0 in both |

The latest maze recording had **824 scored windows**. Its peak of **0.450** fell below the **0.55** score threshold. An earlier maze run logged three emitted commands, and whether the maze applied them is unverified. These are diagnostic runs with different tasks and conditions, so the peak scores describe each run. [November session catalog](https://github.com/neurocontrol-lab/ssvep-decoding/blob/main/docs/results/session-catalog.md)

Moving maze content may compete with the flickering targets for attention. Both follow-up PsychoPy checks also stayed below threshold, including the repeat after I adjusted electrode contacts, so the cause remains open. I widened the stationary target borders from **2 px to 12 px**. I plan to compare static and moving scenes at a fixed border width, then vary border width while keeping the scene, montage, and decoder settings fixed.

---

## 6. Command decisions and feedback

The implemented gate issues a command only when signal quality is valid, the winning CCA score exceeds a threshold, and its lead over the runner-up persists:

$$
u_t=\begin{cases}
\operatorname{action}(i_t^*), & q_t=1,\;s_{i_t^*}\geq\tau,\;s_{i_t^*}-s_{(2)}\geq\delta,\;T_{\mathrm{persist}}\geq T_p,\\
\mathrm{wait}, & \text{otherwise}.
\end{cases}
$$

Here $q_t$ marks valid signal quality and $s_{(2)}$ is the runner-up score. The current gate uses $\tau=0.55$, $\delta=0.10$, and $T_p=0.75$ s. Each new EEG window updates the candidate. The same target must keep winning and pass both thresholds for the full persistence interval. A change of winner, ambiguous scores, or an invalid window resets that interval. The decision logs and recording replays let me examine how often the gate waits, emits, or resets.

The original settings emitted no commands in the seven October recordings. Lowering the score threshold to 0.40 during replay recovered some intended commands and produced four emissions in the rest-only recording. This trade-off motivates calibrating the gate on development recordings and testing the fixed gate on fresh cued and rest data.

### Planned extension: error feedback

**Can the system detect that an action was wrong and use that evidence to correct subsequent control?** EEG error-related potentials motivate a separate error-monitoring path; continuous error-related activity may also support graded feedback {% cite ferrez2008errp yasemin2023errp pulferer2024feedback %}. Parallel error correction in intracortical BCIs, including Gontier et al.'s human error-damping preprint, provides complementary architectural motivation {% cite evenchen2017errors gontier2026errordamping %}.

This extension requires event-aligned error recordings, suitable electrode coverage, and evaluation of false corrections and added latency. After establishing reliable navigation, I plan to compare intention-only, confidence-gated, and error-feedback control.

---

## 7. Current status and next steps

<div class="key-table" markdown="1">

| Component               | Current status                                                                       | Next step                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| DIY cap and acquisition | Fitted press-stud cap and documented four-channel montage used in November tests     | Measure placement repeatability and contact quality across setups                                               |
| CCA and decision policy | Live scoring, persistence, and replay exercised in cued and rest recordings          | Fix settings on development data and evaluate target selection, idle rejection, and latency on fresh recordings |
| Stimulus timing         | Frame-sequenced displays and a BPW34 measurement setup are available                 | Check optical timing under navigation load and align optical onset with EEG                                     |
| End-to-end navigation   | The live link and HUD are working. The latest scored maze run emitted zero commands. | Compare static and moving scenes and test the wider borders before evaluating steering and task outcomes        |
| Neural error feedback   | Planned research extension                                                           | Record event-aligned error trials after establishing a navigation baseline                                      |

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
