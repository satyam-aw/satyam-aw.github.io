---
layout: page
pinned: true
title: TENS Waveform Decoding from EEG
description: Auditing stimulus events and testing single-epoch EEG decoding of peripheral stimulation waveforms.
research_connection: >-
  Sensory feedback is the return path of a bidirectional neural interface. This project investigates whether EEG distinguishes peripheral stimulation conditions, while separating predictive information from timing, stimulation artifacts, and task context.
img: /assets/img/projects/tens-eeg/waveforms.png
importance: 4
category: "Neural Interfaces & Biosignals"
completed_on: "Remote collaboration · University of Central Florida, 2026–Present"
project_keywords:
  - Sensory feedback
  - Peripheral nerve stimulation
  - EEG decoding
  - Event auditing
project_resources:
  - label: Motivation · R. Collu et al. (2023)
    url: https://doi.org/10.1038/s41598-023-28594-0
  - label: Experimental foundation · Whitson (2026)
    url: https://stars.library.ucf.edu/hut2024/661/
project_toc: true
project_toc_level: "2"
_styles: |
  .post article h2 { color: var(--global-theme-color); }
  .tens-note { border-left: 3px solid var(--global-theme-color); background: var(--global-card-bg-color); padding: 1rem 1.25rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
  .post article table { width: 100%; margin: 1.25rem 0; font-size: 0.93rem; }
  .post article th, .post article td { padding: 0.7rem 0.8rem; vertical-align: top; border-bottom: 1px solid var(--global-divider-color); }
---

**Ongoing remote research collaboration with Prof. Mohsen Rakhshan at the University of Central Florida, with experimental guidance from Jason Whitson.**

I am investigating whether a single EEG epoch can distinguish which of five waveforms was delivered during transcutaneous electrical nerve stimulation (TENS) of the median nerve at the wrist. The wider motivation is sensory feedback for bidirectional interfaces: understanding how stimulation conditions relate to perceived sensation and measurable EEG responses.

My initial Task 4 baseline did **not demonstrate reliable decoding above the 20% chance reference**. The current work emphasizes an auditable event-to-label pipeline and diagnostic controls before introducing more complex models.

{% include figure.liquid path="assets/img/projects/tens-eeg/waveforms.png" alt="Illustrative profiles of sine, square, triangle, decreasing ramp, and increasing ramp stimulation waveforms" class="img-fluid rounded" %}

<div class="caption">Conceptual waveform profiles only. These are not recorded current traces or a representation of the experiment's pulse timing, polarity, amplitude, or charge.</div>

## Motivation and experimental context

R. Collu and colleagues' 2023 study, [_Non-rectangular neurostimulation waveforms elicit varied sensation quality and perceptive fields on the hand_](https://doi.org/10.1038/s41598-023-28594-0), motivates looking beyond square pulses for sensory stimulation. The present analysis uses recordings from the UCF experiment documented in [Jason Whitson's undergraduate thesis](https://stars.library.ucf.edu/hut2024/661/), together with subsequent protocol and label clarifications from the collaboration.

Task 4 presents pairs of waveforms and asks which feels **more natural**. A comparison ends when one member has been chosen five times. The behavioral choice is a subjective preference; it is separate from the delivered-waveform label that my classifier predicts.

The five classes are sine, square, centered triangle, decreasing ramp, and increasing ramp. The initial analysis includes ten participants, subjects 3–12; subject 2 used an incompatible earlier Task 4 protocol.

## Auditable event extraction

I built a separate baseline that reads continuous SAGA EEG/XDF recordings and aligns stimulation triggers with the master behavioral CSV. It accepts stable trigger runs, records rejected transitions, and requires an exact match to the complete expected sequence. Jason's corrected mapping resolves the increasing/decreasing ramp labels.

All **1,246 stimulation events** matched the CSV sequence. Comparison blocks passed the race-to-five consistency audit, and observed within-pair intervals were **1.408–1.448 seconds**. One pair exceeded the prespecified EEG peak-to-peak threshold of 500 µV, leaving **1,244 eligible epochs**.

<div class="tens-note"><strong>Timing scope.</strong> Epochs are trigger-aligned. Current-monitor signals were saved during acquisition, but their alignment with EEG and the physical trigger-to-current delay have not yet been established. A shorter epoch also cannot rule out carryover from the preceding stimulation.</div>

## First decoding experiment

**Given one post-trigger EEG epoch, can a fixed classifier identify one of five delivered waveforms above the 20% balanced-accuracy reference?**

The initial pipeline uses 50 ms mean-amplitude bins from **50–500 ms** across 14 fixed scalp channels, an average scalp reference, and a pre-trigger baseline. Standardization is fitted within training folds, followed by shrinkage linear discriminant analysis with no tuning. This deliberately minimal baseline applies no temporal filtering, ICA, or source localization.

Within-participant validation holds out complete waveform comparisons, keeping paired presentations together and purging shared sample support. Leave-one-subject-out evaluation tests transfer to an unseen participant. These splits assess generalization across comparison contexts and participants rather than randomly separating nearby trials.

## Initial findings

| Feature set                       | Mean within-participant balanced accuracy | Pooled leave-one-subject-out balanced accuracy |
| --------------------------------- | ----------------------------------------: | ---------------------------------------------: |
| Post-trigger, 50–500 ms · primary |                                 **19.1%** |                                      **18.5%** |
| Pre-trigger, −500 to −50 ms       |                                     16.8% |                                          19.3% |
| Late, 150–500 ms                  |                                     21.9% |                                          19.8% |
| Onset, 0–20 ms                    |                                     16.1% |                                          20.7% |
| Order/history only · no EEG       |                                     10.5% |                                          19.5% |

The descriptive participant-bootstrap 95% interval for the primary within-participant mean was **15.7–22.4%**, including the 20% reference. A diagnostic restricted-permutation test for the primary leave-one-subject-out score gave **p = 0.87**, using 99 permutations.

There is no evidence here of easy waveform separation using these fixed mean-amplitude features. This result does not establish that waveform information is absent from the recordings. The control analyses are diagnostic and exploratory; near-chance pre-trigger or order-only performance does not establish that contamination is absent.

## Interpretation and ongoing work

Predicting a waveform label would not by itself establish a cortical response specific to waveform shape. The conditions are not charge-matched, residual electrical or physiological artifacts may remain, and trigger-to-current timing is unresolved. This experiment also does not assess naturalness decoding or demonstrate a complete sensory-feedback interface.

Before changing the classifier, I am prioritizing signal-quality inspection, channel-level stimulus-aligned responses, first-versus-second presentation differences, and feature scaling and covariance stability. Task 3 offers a later extension, with explicit controls for its non-interleaved waveform order and possible anticipatory baseline activity.

## My contributions

- Reviewed the experimental documentation and supplied analysis code, and reconciled waveform labels using the collaboration's clarifications.
- Implemented debounced event extraction, strict CSV alignment, event manifests, and protocol consistency checks.
- Built the fixed sensor-space classifier, grouped validation, and pre-trigger, onset, late-window, and order/history controls.
- Documented the initial cohort results, interpretation limits, and priorities for the next analysis.

<p class="small text-muted">Initial analysis: 16 October 2026. Experimental acquisition and the supplied study materials are credited to Jason Whitson and Prof. Mohsen Rakhshan's research group. Participant recordings and individual-level outputs are not distributed through this portfolio.</p>
