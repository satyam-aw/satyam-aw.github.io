---
layout: page
title: EEG-to-Kinematics Decoding
description: Decoding wrist position from 32-channel EEG with run-separated evaluation and six regression baselines on WAY-EEG-GAL.
img: /assets/img/projects/eeg-kinematics/eeg-kinematics-thumbnail.jpg
category: "Neural Interfaces & Biosignals"
importance: 2
selected: true
thumbnail_credit:
  authors: "Luciw, Jarocka & Edin"
  source: https://www.nature.com/articles/sdata201447
  license: https://creativecommons.org/licenses/by/4.0/
completed_on: "University of Reading, 2026–Present"
github: https://github.com/neurocontrol-lab/eeg-kinematics-decoding
_styles: |
  .research-flow { display: block; width: 100%; height: auto; margin: 1.5rem 0; color: var(--global-text-color); }
  .post article h2, .research-label { color: var(--global-theme-color); }
  .post article hr { margin: 2.25rem 0; border-top: 1px solid var(--global-divider-color); }
  .research-note { border-left: 3px solid var(--global-theme-color); background: var(--global-card-bg-color); padding: 1rem 1.25rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
  .research-figure { max-width: 720px; margin: 1.5rem auto; }
  .post article table { width: 100%; border-collapse: collapse; margin: 1.25rem 0 1.75rem; font-size: 0.95rem; line-height: 1.55; }
  .post article th, .post article td { padding: 0.8rem 1rem; vertical-align: top; border-bottom: 1px solid #dfe3e8; }
  .post article .key-table thead { background: #e9edf2; color: #202b38; }
  .post article .key-table tbody tr:nth-child(odd) { background: #fff; color: #202b38; }
  .post article .key-table tbody tr:nth-child(even) { background: #f3f4f6; color: #202b38; }
  .post article td:first-child { font-weight: 500; }
project_keywords:
  - EEG decoding
  - Movement kinematics
  - Run-separated evaluation
project_resources:
  - label: Six-model results
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/outputs/six-model-comparison-p1-gpu-20260930T095506Z/RESULTS.md
  - label: Corrected baseline methods
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/documentation/PIPELINE_V2_CORRECTED_BASELINE.md
  - label: Target provenance
    url: https://github.com/neurocontrol-lab/eeg-kinematics-decoding/blob/main/documentation/KINEMATICS_PROVENANCE.md
  - label: WAY-EEG-GAL dataset paper
    url: https://doi.org/10.1038/sdata.2014.47
project_toc: true
project_toc_level: "2"
---

**Ongoing research under the guidance of Prof. Slawomir Nasuto at the University of Reading.**

This project investigates how well EEG can predict movement kinematics using the WAY-EEG-GAL grasp-and-lift dataset. The current target is the wrist tracker's **X, Y, and Z position**, predicted from 32 EEG channels.

I extended a fork of [Thowfiq23/hand_motion_eeg](https://github.com/Thowfiq23/hand_motion_eeg), preserving its original pipeline as a reproduction reference and adding a separate baseline with corrected evaluation. The emphasis is on generalization across recording runs, reproducible model comparisons, and clear target provenance.

---

## 1. Decoding pipeline

<svg class="research-flow" viewBox="0 0 930 130" role="img" aria-labelledby="eeg-flow-title" xmlns="http://www.w3.org/2000/svg"><title id="eeg-flow-title">32-channel EEG → Run-separated splits → Training-fitted scaling → 128-sample windows → Regression model → Wrist X, Y, Z</title><defs><marker id="eeg-flow-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs><rect x="10" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="77" y="69" text-anchor="middle" font-size="13" fill="currentColor">32-channel EEG</text><path d="M 144 65 H 162" stroke="currentColor" fill="none" marker-end="url(#eeg-flow-arrow)"/><rect x="165" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="232" y="59" text-anchor="middle" font-size="13" fill="currentColor">Run-separated</text><text x="232" y="79" text-anchor="middle" font-size="13" fill="currentColor">splits</text><path d="M 299 65 H 317" stroke="currentColor" fill="none" marker-end="url(#eeg-flow-arrow)"/><rect x="320" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="387" y="59" text-anchor="middle" font-size="13" fill="currentColor">Training-fitted</text><text x="387" y="79" text-anchor="middle" font-size="13" fill="currentColor">scaling</text><path d="M 454 65 H 472" stroke="currentColor" fill="none" marker-end="url(#eeg-flow-arrow)"/><rect x="475" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="542" y="59" text-anchor="middle" font-size="13" fill="currentColor">128-sample</text><text x="542" y="79" text-anchor="middle" font-size="13" fill="currentColor">windows</text><path d="M 609 65 H 627" stroke="currentColor" fill="none" marker-end="url(#eeg-flow-arrow)"/><rect x="630" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="697" y="59" text-anchor="middle" font-size="13" fill="currentColor">Regression</text><text x="697" y="79" text-anchor="middle" font-size="13" fill="currentColor">model</text><path d="M 764 65 H 782" stroke="currentColor" fill="none" marker-end="url(#eeg-flow-arrow)"/><rect x="785" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="852" y="69" text-anchor="middle" font-size="13" fill="currentColor">Wrist X, Y, Z</text></svg>

<div class="research-note"><strong class="research-label">Evaluation scope</strong><br>Published results cover held-out recording runs from participant P1 with seed 42. Cross-participant transfer has not yet been evaluated.</div>

---

## 2. Evaluation design

The original pipeline randomly splits overlapping windows. The corrected pipeline holds out complete recording runs so adjacent windows from one run cannot appear in both training and test sets.

| Design choice     | Protocol                                                        |
| ----------------- | --------------------------------------------------------------- |
| Training          | Runs 1–6                                                        |
| Validation        | Run 7; also used to select ridge regularization                 |
| Test              | Runs 8–9, evaluated after training                              |
| Scaling           | Separate EEG and target scalers fitted on training samples only |
| Input window      | 128 EEG samples, advancing by 64 samples                        |
| Prediction target | Wrist-position sample immediately after the input window        |
| Boundary rule     | Windows and targets never cross recording-run boundaries        |

---

## 3. Six-model comparison

The published comparison evaluates participant **P1**, using seed **42** and the same run split for all six models. Ridge regularization is selected on validation data.

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
<div class="caption">Published September 30, 2026 comparison: one participant, one seed, and held-out recording runs.</div>
</div>

<div class="research-note"><strong class="research-label">Result in context</strong><br>CNN–BiLSTM scores highest in this experiment. Adding ELU also improves the original CNN on all three axes. These observations motivate further experiments; they do not establish statistical significance or cross-participant decoding.</div>

---

## 4. Interpretation and next steps

Both test runs contain friction condition 3 only. Evaluation across other conditions, participants, and seeds remains necessary. P2 has passed preparation and model-build checks but has not been trained or evaluated.

The reduced kinematics columns were identified as wrist position through sample-aligned comparisons with original recordings. Their upstream filtering, scaling formula, and physical units are not documented. MSE and MAE therefore use standardized target units.

Next steps are to repeat run-level evaluation across conditions, establish a population model, and evaluate participant-specific fine-tuning with separate target-participant test data.

---

<p class="small text-muted"><strong>Thumbnail credit:</strong> Matthew D. Luciw, Ewa Jarocka, and Benoni B. Edin, <a href="https://www.nature.com/articles/sdata201447">“Multi-channel EEG recordings during 3,936 grasp and lift trials with varying weight and friction”</a>, <em>Scientific Data</em> 1, 140047 (2014). Source image used as a resized project thumbnail under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. The photograph depicts the original dataset's experimental setup.</p>
