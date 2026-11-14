---
layout: page
pinned: true
title: EEG-to-Kinematics Decoding
description: Studying how EEG timing, movement stage, and participant differences affect wrist decoding on WAY-EEG-GAL.
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
  - label: Interactive experiment reports
    url: https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/index.html
  - label: Code and experiment roadmap
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding#experiment-status
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

How reliably can EEG reconstruct wrist movement during grasping and lifting, and what limits that reliability? I study how predictions vary across participants and movement stages, how the timing and duration of the EEG input affect accuracy, and whether separate decoders could improve predictions for specific stages.

I investigate these questions using 32-channel EEG from the WAY-EEG-GAL grasp-and-lift dataset. I extended a fork of [Thowfiq23/hand_motion_eeg](https://github.com/Thowfiq23/hand_motion_eeg), preserving the original pipeline as a reference and building an evaluation-corrected baseline. The work spans model comparison, transfer across participants, movement-stage and condition analyses, and controlled comparisons of timing, EEG history and movement targets.

<div class="research-note"><strong class="research-label"><a href="https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/index.html">Explore the interactive experiment reports</a></strong><br>Browse charts and tables for ten experiment families. Filter by participant, model or movement stage where available, and follow the links to detailed results.</div>

<div class="research-note"><strong class="research-label">Current scope</strong><br>Timing, EEG history, movement targets, and stage-specific weight decoding were evaluated on held-out runs within each of the 12 participants. The six-model benchmark uses P1, and the transfer study tests those models on the other 11 participants. Updated November 14, 2026.</div>

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
    <div class="evaluation-card"><strong>Continuous decoding</strong><span>Run-contained EEG predicts wrist movement; vary timing, history and target within participants, and test frozen transfer separately.</span></div>
    <div class="evaluation-card"><strong>Movement-stage analysis</strong><span>Align saved predictions to events and compare error across stages. Stage-specific wrist regression is planned.</span></div>
    <div class="evaluation-card"><strong>Condition decoding</strong><span>Classify object weight at a fixed surface from EEG spanning individual movement stages.</span></div>
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

The reference decoder uses continuous recordings, including intertrial samples. Both test runs are weight series at fixed sandpaper, a condition also represented in training.

[Explore the interactive baseline report](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/continuous-decoding/index.html)

---

## 2. Experiments and findings

### 2.1. Six-model P1 comparison

The six-model benchmark uses the same training and test runs from P1 for each model. **CNN–BiLSTM had the highest held-out R² on all three wrist axes**, and adding ELU improved the original CNN on each axis. This comparison uses one participant and one training seed.

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

[Explore the interactive model comparison](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/model-comparison/index.html)

### 2.2. Frozen cross-participant transfer

I tested all six P1 models on **11 other participants without adaptation**, keeping the models and scaling fixed. The primary comparison used held-out runs with a fixed sandpaper surface in every participant.

**The P1 models did not transfer reliably.** Average R² across target participants was negative for every model and axis. The fixed P1 training mean outperformed the learned models on those averages. This tests transfer from a single source participant.

[Explore the interactive participant-transfer report](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/participant-transfer/index.html)

<h3 id="23-movement-stages-and-error-timing">2.3. Movement stages and prediction errors</h3>

Across 12 participants, I asked whether observed wrist velocity and acceleration helped explain prediction errors beyond wrist position and movement stage. **Adding these features did not improve average held-out error explanation** for ridge or CNN + ELU in the primary comparison. The analysis used observed movement after the fact.

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/eeg-kinematics/r6-dynamics-error-explanation.png" alt="Change in accuracy of error models after adding observed velocity and acceleration for ridge and CNN plus ELU at three smoothing durations" caption="Change in error-model performance after adding velocity and acceleration. Values below zero indicate worse error prediction." class="img-fluid rounded" zoomable=true %}
</div>

The trial-average example below shows how errors change within a trial. In this P1 example, the CNN–BiLSTM had larger errors during reaching and return than during preparation or lift and hold. The stage comparisons motivate testing whether separate wrist decoders improve on one model trained across stages.

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/eeg-kinematics/p1-run8-trial-average.png" alt="Observed and predicted wrist trajectories and aligned prediction errors for 34 held-out P1 trials" caption="Example from P1: 34 trials aligned to the start cue. Orange intervals mark error elevated relative to preparation under exploratory simultaneous bootstrap bands." class="img-fluid rounded" zoomable=true %}
</div>

[Explore the interactive movement-stage report](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/movement-stages/index.html)

<h3 id="24-trial-condition-audit-and-weight-classification">2.4. Object-weight decoding across movement stages</h3>

Can EEG distinguish **165, 330, and 660 g** during grasping and lifting? With the contact surface fixed to sandpaper, I trained separate classifiers for each participant and movement stage using EEG from the full stage. The evaluation covered **769 held-out trials across 12 participants**, including 275 trials where the weight changed from the previous trial.

**Loading showed the clearest evidence of weight discrimination.** On trials where the weight changed, shrinkage LDA reached **55.0% balanced accuracy during loading**, compared with **35.8% during reach** and a **33.3% chance reference**. Because the loading signal comes after contact, it may reflect movement, force, or sensory feedback. This result does not establish that participants anticipated the weight.

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/eeg-kinematics/c10-full-stage-weight-accuracy.png" alt="Full-stage EEG accuracy by movement stage for four classifiers. On switch trials, the two linear models peak at about 55 percent during loading." caption="Held-out balanced accuracy by movement stage for trials where the weight repeated or changed. The dashed line marks 33.3% chance; bars show exploratory 95% bootstrap intervals across participants." class="img-fluid rounded" zoomable=true %}
</div>

[Explore the interactive weight-decoding report](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/condition-decoding/index.html)

<h3 id="25-eeg-timing-history-and-movement-targets">2.5. EEG timing</h3>

Does the time between the last EEG sample and the wrist sample affect accuracy? I chose this gap using validation runs separately for each of the 12 participants and compared it with the 2 ms reference on the same test samples.

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/eeg-kinematics/t1-validation-selected-gaps.png" alt="Counts of participants at each validation-selected EEG end gap for Ridge, CNN plus ELU, CNN–BiLSTM, and EEGNet regression. Ridge selected 2 ms for nine participants; 100 ms was the most common choice for CNN plus ELU and CNN–BiLSTM." caption="Each bar counts participants whose lowest validation error occurred at that gap. CNN + ELU uses validation scores averaged across three training seeds; CNN–BiLSTM and EEGNet each use one seed." class="img-fluid rounded" zoomable=true %}
</div>

**CNN + ELU had 3.4% lower mean test error**, with improvement in 9 of 12 participants. Ridge showed no clear benefit. This measures predictive performance for the tested gaps, without identifying a physiological delay.

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/eeg-kinematics/t1-paired-test-scores.png" alt="Paired test errors per participant at the 2 ms reference and at the validation-selected gap" caption="Held-out error at the 2 ms reference and at the gap selected on validation. Each colored line pairs one participant’s scores; black shows the mean, with equal weight per participant." class="img-fluid rounded" zoomable=true %}
</div>

[Explore the interactive timing report](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/timing-alignment/index.html)

### 2.6. EEG history

Does giving the decoder more EEG history help? I compared 256, 512, and 1,024 ms of EEG with the same input dimensions and prediction targets for each of the 12 participants.

**Using 1,024 ms instead of 256 ms lowered CNN + ELU test error in all 12 participants**, by **17.3% on average**. The longer histories also used more averaging, and this comparison cannot separate those effects.

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/eeg-kinematics/t2-history-duration-effects.png" alt="Paired test error reductions for 512 and 1,024 ms of EEG compared with 256 ms across 12 participants" caption="Change in test error relative to 256 ms of EEG history. Positive values favor the longer history; bars show exploratory 95% participant bootstrap intervals." class="img-fluid rounded" zoomable=true %}
</div>

[Explore the interactive EEG history report](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/history-duration/index.html)

### 2.7. Position versus velocity

Using the same EEG windows and test times for all 12 participants, I compared prediction of wrist position and signed velocity. I evaluated each target against its own training-mean baseline.

**Both models beat the velocity baseline on average.** Position showed a larger improvement over its own baseline for both models.

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/eeg-kinematics/t7-position-velocity-skill.png" alt="Paired position and velocity test scores for ridge and CNN plus ELU across 12 participants" caption="Position and velocity on matched EEG windows. A score above zero beats that target’s training-mean baseline." class="img-fluid rounded" zoomable=true %}
</div>

[Explore the interactive movement-target report](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/movement-targets/index.html)

---

## 3. Target provenance and practical limits

Sample-aligned raw/reduced comparisons identify the targets as wrist **X/Y/Z** across P1–P12. The authors' event code and an all-trial trajectory check confirm **position Z is vertical, positive upward**. Contact-plate forces use a different frame: force X is lifting/load force and force Z is grip. X/Y anatomical directions remain unresolved.

The reduced files' upstream filtering and scaling remain undocumented. Positions and errors in those files are expressed in normalized units.

The inference benchmark measures model calls on CPU and GPU. It leaves out acquisition, preprocessing, and window accumulation, so it does not measure end-to-end latency.

[Explore the interactive dataset audits](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/dataset-audits/index.html) · [Explore the interactive inference benchmark](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/reports/inference-latency/index.html)

---

## 4. My contributions and next steps

- Corrected split/scaling evaluation and established six comparable P1 references.
- Implemented frozen-model participant transfer with source replay and provenance checks.
- Aligned predictions to movement events and tested how stage and movement dynamics relate to errors.
- Ran matched comparisons of EEG timing, history duration and wrist position versus velocity.
- Tested object-weight decoding by movement stage and verified the wrist targets and coordinate axes.
- Organized reproducible reports, numeric evidence, and independent checks in the [public repository](https://github.com/neurocontrol-lab/eeg-kinematics-decoding).

Next, I plan to test whether EEG distinguishes event-defined movement stages beyond what trial timing alone predicts. A separate comparison will ask whether stage-specific wrist decoders outperform a single model when training sample counts are matched. Condition-specific wrist regression and adaptation to new participants remain open. See the [experiment roadmap](https://github.com/neurocontrol-lab/eeg-kinematics-decoding#experiment-status) for the full plan.

---

<p class="small text-muted"><strong>Thumbnail credit:</strong> Matthew D. Luciw, Ewa Jarocka, and Benoni B. Edin, <a href="https://www.nature.com/articles/sdata201447">“Multi-channel EEG recordings during 3,936 grasp and lift trials with varying weight and friction”</a>, <em>Scientific Data</em> 1, 140047 (2014). Source image used as a resized project thumbnail under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. The photograph depicts the original dataset's experimental setup.</p>
