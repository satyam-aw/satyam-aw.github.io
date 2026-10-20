---
layout: page
pinned: true
title: EEG-to-Kinematics Decoding
description: Evaluating EEG-based wrist decoding across recording runs, participants, movement stages, and object conditions on WAY-EEG-GAL.
research_connection: >-
  Reliable movement decoding is a component of closed-loop brain-computer interfaces. This project tests where EEG-based predictions generalize and where errors concentrate before introducing adaptation or feedback control.
img: /assets/img/projects/eeg-kinematics/eeg-kinematics-thumbnail.jpg
category: "Neural Interfaces & Biosignals"
importance: 2
selected: true
thumbnail_credit:
  authors: "Luciw, Jarocka & Edin"
  source: https://www.nature.com/articles/sdata201447
  license: https://creativecommons.org/licenses/by/4.0/
completed_on: "Remote collaboration · University of Reading, 2026–Present"
github: https://github.com/neurocontrol-lab/eeg-kinematics-decoding
_styles: |
  .evaluation-flow { margin: 1.5rem 0; }
  .evaluation-steps, .evaluation-branches { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.5rem; }
  .evaluation-card { position: relative; padding: 1rem; border: 1px solid var(--global-theme-color); border-radius: 6px; background: var(--global-card-bg-color); }
  .evaluation-card strong { display: block; margin-bottom: 0.4rem; color: var(--global-theme-color); }
  .evaluation-card span { display: block; font-size: 0.9rem; line-height: 1.5; }
  .evaluation-steps .evaluation-card:not(:last-child)::after { content: "→"; position: absolute; right: -1.3rem; top: 45%; color: var(--global-text-color); }
  .evaluation-connector { text-align: center; margin: 1rem 0; font-size: 0.9rem; }
  .evaluation-connector span { display: block; font-size: 1.4rem; }
  @media (max-width: 600px) {
    .evaluation-steps, .evaluation-branches { grid-template-columns: 1fr; }
    .evaluation-steps .evaluation-card:not(:last-child)::after { content: "↓"; right: 50%; top: auto; bottom: -1.5rem; }
  }
  .post article h2, .post article h3, .research-label { color: var(--global-theme-color); }
  .post article hr { margin: 2.25rem 0; border-top: 1px solid var(--global-divider-color); }
  .research-note { border-left: 3px solid var(--global-theme-color); background: var(--global-card-bg-color); padding: 1rem 1.25rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
  .research-figure { max-width: 720px; margin: 1.5rem auto; }
  .post article table { width: 100%; border-collapse: collapse; margin: 1.25rem 0 1.75rem; font-size: 0.95rem; line-height: 1.55; }
  .post article th, .post article td { padding: 0.8rem 1rem; vertical-align: top; border-bottom: 1px solid var(--global-table-border-color); }
  .post article .key-table thead { background: transparent; color: var(--global-text-color); }
  .post article .key-table tbody tr { background: transparent; color: var(--global-text-color); }
  .post article td:first-child { font-weight: 500; }
project_keywords:
  - EEG decoding
  - Movement kinematics
  - Run-separated evaluation
  - Cross-participant generalization
  - Movement-stage errors
project_resources:
  - label: Experiment status and code
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding
  - label: Six-model P1 results
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/six-model-comparison-p1-gpu-20260930T095506Z/RESULTS.md
  - label: Frozen participant transfer
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/frozen-p1-cross-participant-gpu-20260930T125956Z/RESULTS.md
  - label: Movement-stage analysis
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/saved-decoder-analysis-p1-20261013T172654Z/RESULTS.md
  - label: Condition classification
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/weight-classification-p1-gpu-20261014T115817Z/RESULTS.md
  - label: Target and coordinate provenance
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/documentation/dataset/COORDINATE_SYSTEM.md
  - label: Corrected baseline methods
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/documentation/methods/PIPELINE_V2_CORRECTED_BASELINE.md
  - label: WAY-EEG-GAL dataset paper
    url: https://doi.org/10.1038/sdata.2014.47
project_toc: true
project_toc_level: "2"
---

**Ongoing remote research collaboration under the guidance of Prof. Slawomir Nasuto at the University of Reading.**

How reliably can EEG reconstruct wrist movement across recording runs and participants, and which parts of a movement are hardest to predict?

I investigate these questions using 32-channel EEG from the WAY-EEG-GAL grasp-and-lift dataset. I extended a fork of [Thowfiq23/hand_motion_eeg](https://github.com/Thowfiq23/hand_motion_eeg), preserving the original pipeline as a reference and building an evaluation-corrected baseline. The work now includes six-model comparisons, frozen cross-participant transfer, event-aligned error analysis, and an initial condition-classification experiment.

<div class="research-note"><strong class="research-label">Current scope</strong><br>Six regressors trained on P1 with seed 42, followed by zero-adaptation evaluation on P2–P12. Movement-stage diagnostics and weight classification currently focus on P1. Results and interpretation updated October 20, 2026.</div>

---

## 1. Evaluation design

Each experiment defines its participant scope, prediction target, and analysis interval. EEG can be examined across continuous recordings, within full trials or movement stages, or under selected experimental conditions. Complete recording runs separate training, validation, and test data; cross-participant evaluation additionally holds out participants. Any fitted scaling uses training data only, and frozen transfer retains the P1-fitted processing.

<div class="evaluation-flow" role="group" aria-label="Shared evaluation design with three experiment-specific analysis paths">
  <div class="evaluation-steps">
    <div class="evaluation-card"><strong>Define the question</strong><span>32-channel EEG, movement events, wrist targets and trial conditions.</span></div>
    <div class="evaluation-card"><strong>Separate held-out groups</strong><span>Choose recording runs and participants for training, validation and testing.</span></div>
    <div class="evaluation-card"><strong>Fit on training data</strong><span>Fit scaling and models on training data; select settings using validation data.</span></div>
  </div>
  <div class="evaluation-connector"><span aria-hidden="true">↓</span>Experiment-specific inputs and evaluation</div>
  <div class="evaluation-branches">
    <div class="evaluation-card"><strong>Continuous decoding</strong><span>Run-contained EEG windows predict wrist X/Y/Z; compare within-P1 performance and frozen participant transfer.</span></div>
    <div class="evaluation-card"><strong>Movement-stage analysis</strong><span>Align saved predictions to events and compare error across stages. Stage-specific decoder training is planned.</span></div>
    <div class="evaluation-card"><strong>Condition decoding</strong><span>Select trials by experimental condition, then aggregate EEG-window predictions to classify object weight.</span></div>
  </div>
</div>

**Reference protocol: six-model P1 regression.** The earlier pipeline randomly split overlapping windows. The corrected comparison separates complete recording runs before scaling or windowing, then takes fixed-stride windows across continuous recordings. Neighboring windows from one run therefore cannot appear in both training and test sets. The settings below describe this reference experiment; stage and condition experiments define their own analysis intervals and selections.

| Design choice                | Protocol                                                              |
| ---------------------------- | --------------------------------------------------------------------- |
| Training / validation / test | Runs 1–6 / run 7 / runs 8–9                                           |
| Scaling                      | Separate EEG and wrist-target scalers fitted on training samples only |
| Input                        | 128 EEG samples at 500 Hz, advancing by 64 samples                    |
| Target                       | Wrist-position sample immediately after the input window              |
| Boundaries                   | Windows and targets remain inside recording runs                      |

Regression uses continuous recordings, including intertrial samples. Both held-out runs are **weight series at fixed sandpaper**. They test new recordings of conditions represented in training, rather than unseen experimental conditions.

---

## 2. Experiments and findings

### 2.1. Six-model P1 comparison

All six models use the same P1 split and seed. Ridge regularization is selected on validation data. The ELU variant adds nonlinear activations to the original CNN; EEGNet regression provides a separate architecture reference.

<div class="key-table" markdown="1">

| Model             | Wrist X R² | Wrist Y R² | Wrist Z R² |
| ----------------- | ---------: | ---------: | ---------: |
| Training mean     |     -0.204 |     -0.324 |     -0.185 |
| Ridge regression  |      0.558 |      0.420 |      0.462 |
| Original CNN      |      0.547 |      0.399 |      0.451 |
| CNN–BiLSTM        |  **0.809** |  **0.783** |  **0.748** |
| CNN + ELU         |      0.746 |      0.713 |      0.678 |
| EEGNet regression |      0.758 |      0.683 |      0.663 |

</div>

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/eeg-kinematics/eeg-kinematics-r2.png" alt="Held-out P1 wrist-position R-squared comparison across six models" class="img-fluid rounded" %}
<div class="caption">Six-model comparison on held-out runs from P1. These are single-seed results, not a population-level performance estimate.</div>
</div>

CNN–BiLSTM leads within P1, and adding ELU improves the original CNN on all three axes. These comparisons do not establish statistical significance or identify the source of the predictive information. [Full P1 results](https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/six-model-comparison-p1-gpu-20260930T095506Z/RESULTS.md).

### 2.2. Frozen cross-participant transfer

I evaluated all six saved P1 models on **P2–P12 without adaptation**, retaining the P1 training scalers and inference-time model statistics. The primary comparison uses runs 8–9, which are weight series at fixed sandpaper for every participant. P1 replay provides a source-participant control.

The positive within-P1 scores **did not transfer reliably**: every model/axis participant-macro R² was negative. The frozen P1 training-mean predictor outperformed the learned models on these macro averages, even though individual comparisons varied. CNN–BiLSTM, the strongest P1 model, had the poorest transfer averages among the six references.

This evaluates transfer from one source participant. It does not test a population-trained decoder or establish whether participant physiology, signal normalization, target coordinates, or other upstream processing dominates the failure. [Transfer protocol and results](https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/frozen-p1-cross-participant-gpu-20260930T125956Z/RESULTS.md).

### 2.3. Movement stages and error timing

I reconstructed the six models' saved predictions for all **68 held-out P1 trials** and aligned them with raw movement events. Exact EEG and wrist sample matches verified a two-second offset between the trial-metadata and continuous-recording clocks. The analysis adds no training or new predictions.

For CNN–BiLSTM, errors were larger during reaching and return than during preparation or the airborne interval. Trial-average plots show observed and predicted coordinates alongside error magnitude, with exploratory simultaneous trial-block bootstrap bands marking error elevated relative to each trial's preparation period.

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/eeg-kinematics/p1-run8-trial-average.png" alt="P1 run 8 trial-average wrist X, Y and Z trajectories with CNN–BiLSTM predictions, error magnitude, movement stages, and elevated-error intervals" class="img-fluid rounded" %}
<div class="caption">Run 8 averages across 34 LEDOn-aligned trials. Orange intervals indicate error elevated relative to preparation under the exploratory simultaneous-band analysis. Error units are normalized coordinates; later stages can blur because trial durations differ.</div>
</div>

The airborne interval combines lifting and holding. Short phases have few or no windows entirely contained within the phase. These diagnostics motivate stage-specific comparisons, but **no stage-specific decoders have been trained**, and prediction errors alone do not establish distinct neural control routines. [Stage analysis](https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/saved-decoder-analysis-p1-20261013T172654Z/RESULTS.md) and [trial-average methods](https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/saved-decoder-analysis-p1-20261013T172654Z/trial_averages/RESULTS.md).

### 2.4. Trial-Condition Audit and Weight Classification

An audit of **3,528 supplied trials across P1–P12** distinguishes recording-series type from each trial's current and previous weight/surface. All held-out current weight/surface combinations occur in v2 training, although the mix of series types differs between splits.

The first controlled classification task asks whether P1 EEG distinguishes **three object-weight classes: 165, 330 and 660 g**, with the surface held fixed as sandpaper. For this three-class task, the **balanced-accuracy chance reference is 1/3 = 33.33%**. Runs 1/4 train, run 7 validates, and runs 8/9 provide 68 test trials. EEG windows stay inside full LEDOn-to-hand-stop trials, and averaging window probabilities gives one prediction per trial.

| Classifier                  | Held-out trial balanced accuracy |
| --------------------------- | -------------------------------: |
| Training-majority reference |                           33.33% |
| Logistic regression         |                           32.48% |
| CNN + ELU                   |                           27.73% |

**Both learned classifiers scored below the 33.33% chance reference**: logistic regression reached 32.48% and CNN + ELU reached 27.73% held-out trial balanced accuracy. Neither classifier showed reliable held-out discrimination in this setup. A conditional circular-shift reference keeps predictions fixed and shifts whole-trial labels within each test run; it does not retrain under shuffled labels. The result does not establish that EEG lacks weight information. [Condition audit](https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/condition-audit-20261014T115618Z/RESULTS.md) and [classification results](https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/weight-classification-p1-gpu-20261014T115817Z/RESULTS.md).

---

## 3. Target provenance and practical limits

Sample-aligned raw/reduced comparisons identify the targets as wrist **X/Y/Z** across P1–P12. The authors' event code and an all-trial trajectory check confirm **position Z is vertical, positive upward**. Contact-plate forces use a different frame: force X is lifting/load force and force Z is grip. X/Y anatomical directions remain unresolved.

The reduced files' exact upstream filtering and scaling remain undocumented. Reduced positions and trajectory-error norms therefore do not represent physical distances; regression MSE and MAE use training-standardized targets. [Coordinate definitions](https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/documentation/dataset/COORDINATE_SYSTEM.md) and [axis audit](https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/vertical-axis-audit-20261020/REPORT.md).

A separate saved-model benchmark measures synchronized CPU/GPU calls for individual windows and batches. It excludes acquisition, preprocessing, and window accumulation, so it does not demonstrate end-to-end real-time control. [Inference benchmark](https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/inference-benchmark-p1-20261014/RESULTS.md).

---

## 4. My contributions and next steps

- Corrected split/scaling evaluation and established six comparable P1 references.
- Implemented frozen-model participant transfer with source replay and provenance checks.
- Reconstructed event-aligned predictions and examined stage errors, trial averages, density, bias, and low-speed sensitivity.
- Audited trial conditions, built the first fixed-surface classifier comparison, and verified target/axis identity.
- Organized reproducible reports, numeric evidence, and independent checks in the [public repository](https://github.com/neurocontrol-lab/eeg-kinematics-decoding).

Next experiments include fixed-condition versus pooled decoders and within-stage versus cross-stage comparisons, controlling sample availability and stage difficulty. Population training and participant-specific calibration/fine-tuning remain open. Settings must be selected using training/validation data rather than the existing test results.

---

<p class="small text-muted"><strong>Thumbnail credit:</strong> Matthew D. Luciw, Ewa Jarocka, and Benoni B. Edin, <a href="https://www.nature.com/articles/sdata201447">“Multi-channel EEG recordings during 3,936 grasp and lift trials with varying weight and friction”</a>, <em>Scientific Data</em> 1, 140047 (2014). Source image used as a resized project thumbnail under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. The photograph depicts the original dataset's experimental setup.</p>
