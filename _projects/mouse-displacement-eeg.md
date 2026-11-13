---
layout: page
pinned: true
title: Error-Related EEG During Mouse Movements
description: Event-aligned EEG and held-out-run decoding of unexpected target displacement across 25 participants.
img: /assets/img/projects/mouse-displacement-eeg/task-overview.png
category: "Neural Interfaces & Biosignals"
importance: 4
completed_on: "Remote research collaboration · University of Essex, 2026–Present"
research_connection: >-
  Error-related EEG could provide feedback about unintended outcomes in a closed-loop BCI. This project studies whether a reliable response can be identified before using it for decoding or adaptation.
project_keywords:
  - Error-related potentials
  - EEG preprocessing
  - Visuomotor control
  - Participant and session variability
project_tools:
  - MATLAB
  - EEG and mouse-event logs
  - Python
  - Interactive reports
github: https://github.com/neurocontrol-lab/mouse-displacement-eeg
project_resources:
  - label: Original Graz BCI study (2024)
    url: /assets/pdf/GBCIC2024_paper_97.pdf
project_toc: true
project_toc_level: "2"
_styles: |
  .post article h2 { color: var(--global-theme-color); }
---

What happens in the EEG when a target moves unexpectedly during a reach? I’m working with Mushfika Sultana and Dr. Serafeim Perdikis at the University of Essex to find out. The study asks two related questions: when the EEG changes after a target jump, and whether those changes can distinguish displaced from non-displaced trials on new recording runs.

## The mouse-reaching task

Participants moved a cursor rapidly toward a visual target that either shifted laterally after movement began (D) or remained stationary (ND). The dataset used in this analysis includes pre, post and retest recordings from 25 participants, with eight EEG channels sampled at 500 Hz. The analysis extends the two-case [Graz BCI conference study by Amaunam et al. (2024)]({{ '/assets/pdf/GBCIC2024_paper_97.pdf' | relative_url }}). Two participants served as pilots; cohort inference and the primary decoding summary use the remaining participants.

{% include figure.liquid path="assets/img/projects/mouse-displacement-eeg/task-overview.png" alt="Schematic of a mouse reach to a stationary target or a target that moves sideways after movement begins" class="img-fluid rounded" %}

<p class="small text-muted"><strong>Figure 1.</strong> Schematic of the two task conditions.</p>

## How we compared trials

EEG markers were linked to mouse logs to check event timing and preserve trial identities and rejection reasons. The primary analysis uses continuous 1–20 Hz filtering without FORCe and a −200 to 0 ms movement-aligned baseline. FORCe comparisons were retained as a preprocessing sensitivity analysis: independently cleaned windows could introduce steps at the joins, and post-cleaning low-pass filtering reduced the sharp steps without establishing waveform preservation.

Within each recording, D and ND trials were paired by the time from initial target appearance to movement onset. Waveforms were aligned to movement onset or to the logged jump. In the latter analysis, the D trial's movement-to-jump delay was applied to its ND control, which had no actual jump.

The timing follow-up deliberately restricted the comparison to pairs in which both cursors entered the provisional 40 px circle around the final target. This provided a common observed reach outcome and reduced ambiguity about whether the cursor reached the target area. Entry was inferred from trajectories and was not a measure of perceived success or verified task feedback.

### How we tested the differences

Fixed-window analyses tested participant-level D − ND amplitudes with Holm correction within each planned set of comparisons. The matched-hit timing analysis searched 0–500 ms after the jump or matched pseudo-jump using one difference waveform per non-pilot participant. The temporal cluster test used 19,999 participant-level sign flips and the maximum cluster mass across time, both electrode groups and both polarities. An 80–150 ms posterior window was examined separately as an exploratory morphology check.

Decoding used shrinkage linear discriminant analysis (LDA) on 100 ms voltage averages from 200 to 900 ms after movement onset. Whole recording runs were held out within each participant and session. Participant scores averaged eligible sessions equally. The primary eight-channel model was compared with a null formed by 1,999 within-run label permutations, with Holm correction across the 23 non-pilot participants.

## What changed after the target jump

Across 9,269 matched pairs from 23 non-pilot participants, mean D − ND voltage at Cz/FCz was **+2.06 µV from 200 to 280 ms after the logged jump** (Holm-adjusted _p_ = .0044). This was opposite the expected interaction negativity. The conventional ERN/Pe and later Graz windows did not pass correction in this analysis.

The matched-hit subset contained **2,273 pairs from 22 non-pilot participants**. The Cz/FCz mean difference over the same 200–280 ms window was +2.76 µV (95% CI +1.19 to +4.33 µV; Holm-adjusted _p_ = .0060). In the temporal search, three clusters passed correction:

| Electrodes | Interval after jump | Mean D − ND | Corrected _p_ |
| ---------- | ------------------- | ----------: | ------------: |
| Cz/FCz     | 210–312 ms          |    +2.76 µV |         .0108 |
| P3/PO3/PO7 | 220–360 ms          |    +2.24 µV |        .00175 |
| Cz/FCz     | 366–500 ms          |    −2.63 µV |        .00720 |

{% include figure.liquid path="assets/img/projects/mouse-displacement-eeg/matched-hit-clusters.png" alt="Matched-hit EEG differences for central and posterior electrodes, pooled and by session, with three shaded corrected cluster intervals" class="img-fluid rounded" %}

<p class="small text-muted"><strong>Figure 2.</strong> Cohort difference waveforms for matched target entries. Shaded bands mark clusters from the pooled test; the session traces are descriptive.</p>

The separate **80–150 ms posterior window** showed a mean difference of −1.60 µV (95% CI −2.73 to −0.47 µV; nominal _p_ = .0078). This early negativity was a fixed-window finding rather than a fourth corrected cluster. The late central cluster reached the 500 ms search limit, so its duration beyond that point is unknown.

[Explore the waveform contrasts and timing results](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/mouse-displacement-eeg/blob/main/output/ERP_event_related_potentials/report/index.html#erp-hit-timing).

## How well could we decode displacement?

Mean participant balanced accuracy was **76.3% using all eight channels**, compared with **70.3% using Cz and FCz alone**. The primary model exceeded the within-run permutation null for 23 of 23 non-pilot participants after correction. These scores assess performance on new runs from the same participant and session.

{% include figure.liquid path="assets/img/projects/mouse-displacement-eeg/cohort-decoding.svg" alt="Mean balanced accuracy on held-out runs across 23 non-pilot participants: 76.3 percent for eight channels and 70.3 percent for Cz and FCz" class="img-fluid rounded" %}

<p class="small text-muted"><strong>Figure 3.</strong> Mean balanced accuracy for the two LDA channel sets. The dashed line marks the 50% reference.</p>

## What this tells us about ErrPs

The matched-hit contrast shows that displacement is associated with EEG differences among reaches with a common observed outcome. Contrasts by target entry within D trials alone were smaller and sensitive to the entry definition. The data therefore support a response associated with the perturbation and subsequent reach; visual processing, corrective movement and error monitoring may all contribute. The contrast and classifier results do not isolate an ErrP.

The jump marker timestamps the logged event rather than an independently measured display onset. Observed entry depends on provisional geometry and available trajectory coverage. Cluster intervals do not estimate component onset or offset, and held-out-run decoding does not establish transfer to unseen participants.

## Explore the results

The [trajectory explorer](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/mouse-displacement-eeg/blob/main/output/AUD_data_audit/report/index.html#trajectories) supports filtering by participant, session, displacement, steering and EEG acceptance. Observed-entry filters are available for EEG-accepted trials. The [analysis repository](https://github.com/neurocontrol-lab/mouse-displacement-eeg) contains the MATLAB and Python workflows, methods and saved results behind the reports.

| Report                                                                                                                                                                                  | What to explore                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [Event-related potentials](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/mouse-displacement-eeg/blob/main/output/ERP_event_related_potentials/report/index.html)   | Eight-channel waveforms, timing tests, steering and target-entry comparisons, and distance filters |
| [Decoding and classification](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/mouse-displacement-eeg/blob/main/output/DEC_decoding/report/index.html)                | Held-out-run accuracy, model and channel-set comparisons, and permutation inference                |
| [Data audit](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/mouse-displacement-eeg/blob/main/output/AUD_data_audit/report/index.html)                               | Event timing, mouse trajectories and checks on reach labels and outcomes                           |
| [Preprocessing and artifacts](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/mouse-displacement-eeg/blob/main/output/PRE_preprocessing_artifacts/report/index.html) | Participant/session waveforms, trial retention and matched cleaning comparisons                    |
| [Features and repeatability](https://htmlpreview.github.io/?https://github.com/neurocontrol-lab/mouse-displacement-eeg/blob/main/output/FEA_features_repeatability/report/index.html)   | Feature summaries and stability across recordings and preprocessing conditions                     |

**My role.** I developed the event alignment, quality checks, waveform and decoding analyses, and interactive reports. The original study team designed the experiment and collected the recordings.
