---
layout: page
pinned: true
title: Error-Related EEG During Mouse Movements
description: Investigating responses to unexpected target displacement through participant-wise EEG analysis and matched preprocessing comparisons.
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
  - FORCe comparison
project_resources:
  - label: Original Graz BCI study (2024)
    url: https://repository.essex.ac.uk/38379/1/tDCS_ErrP_9th_Graz_BCI_Conference_2024.pdf
project_toc: true
project_toc_level: "2"
_styles: |
  .post article h2 { color: var(--global-theme-color); }
  .errp-note { border-left: 3px solid var(--global-theme-color); background: var(--global-card-bg-color); padding: 1rem 1.25rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
---

**Ongoing remote research collaboration under the guidance of Dr. Serafeim Perdikis at the University of Essex, working with Mushfika Sultana.**

Can EEG reveal the response to an unexpected change in a movement's intended outcome? I am analysing recordings from a fast computer-mouse reaching task to investigate **error-related potentials (ErrPs)** and their variability across participants and sessions.

The work extends analysis of an existing dataset used in the [2024 Graz BCI study by Amaunam and colleagues](https://repository.essex.ac.uk/38379/1/tDCS_ErrP_9th_Graz_BCI_Conference_2024.pdf). My contribution is the analysis pipeline and methodological evaluation; the original experiment and recordings were produced by the study team.

<div class="errp-note"><strong>Current status</strong><br>The analysis is ongoing. Differences between displaced and non-displaced trials are being investigated; a consistent ErrP, its timing and polarity, and reliable single-trial classification have not yet been established by this work.</div>

## 1. Research question and task

Participants move a mouse rapidly from a starting point toward a visual target. On some trials, the target unexpectedly shifts sideways after movement begins, requiring an adjustment of the reach. On other trials, it stays fixed.

{% include figure.liquid path="assets/img/projects/mouse-displacement-eeg/task-overview.png" alt="Conceptual comparison of a fixed target and an unexpected lateral target shift during an upward mouse movement" class="img-fluid rounded" %}

<p class="small text-muted">Original conceptual illustration; not a screenshot, recorded trajectory or EEG result.</p>

The central question is whether the **displaced-minus-non-displaced EEG response** provides evidence of error processing, and how consistently it appears across people and sessions. Target displacement is an experimental condition, not proof that every trial contains the same perceived error or neural response.

The available analysis dataset includes 25 participants, with pre, post and retest sessions. EEG was recorded at 500 Hz from eight channels: P3, PO3, PO7, CP5, CP1, Cz, FCz and FC1. The present emphasis is participant- and session-wise characterisation before group-level conclusions or stimulation-effect claims.

## 2. My contributions

- Developed a four-stage MATLAB workflow for event parsing, epoch preprocessing, participant-level plots and participant-weighted group summaries.
- Matched EEG markers with mouse-task logs, preserving recording and trial identities and explicit reasons for invalid events or rejected epochs.
- Integrated the supplied FORCe implementation and documented coding corrections and comparisons with a no-FORCe reference.
- Investigated discontinuities introduced when independently cleaned windows are joined, separating adjacent-sample jumps from broader waveform changes.
- Prepared an input-only quality assessment and research notes to support review of concerning recordings before interpreting condition differences.

## 3. From event validation to condition comparisons

The workflow separates four questions: which events are valid, which trials meet the quality criteria, how each participant's condition averages differ, and whether a group summary is justified.

EEG and mouse logs are aligned before movement-locked epochs are extracted. Trial identities and rejection reasons remain available throughout processing, so changes in a waveform can be distinguished from changes in which trials contribute to it.

For matched cleaning comparisons, recordings and trial IDs are held constant, along with filtering, baseline correction and event alignment. The planned outputs include all eight channels, both condition averages and their difference, together with descriptive amplitude and peak-timing comparisons. Peaks are not automatically assigned to validated ERP components.

## 4. What the methodological pilot established

**Cleaning can introduce structure at the event of interest.** Joining separately FORCe-cleaned one-second windows can create discontinuities. A subsequent low-pass attenuates the sharp steps, but reduced step size does not establish recovery of the underlying EEG or absence of broader transitions.

**Recording quality varies across participants and sessions.** The two-participant input assessment found large disturbances concentrated in some recordings, alongside smaller spectral and morphological features requiring review. These measurements preceded final filtering and rejection; they do not establish that contaminated trials survive into the analysis.

**Quality handling and the value of a particular cleaner are separate questions.** The no-FORCe pipeline is the primary working analysis, retaining event validation, data-loss handling and quality-control and rejection rules. FORCe remains a secondary sensitivity comparison, using one-second cleaning windows without further algorithm adaptations for now.

These findings guide the analysis rather than establish that FORCe is necessary or that a visually smoother trace is a better neural measurement.

## 5. Current analysis and next steps

The next quality check links input-screen flags to final accepted and rejected trials, summarised by participant, session, run and displaced/non-displaced condition. Concerning examples that remain accepted will be inspected before deciding whether rejection needs adjustment.

Matched FORCe/no-FORCe waveforms will then be compared across participants and sessions. The main questions remain the response's timing, polarity and consistency, including possible overlap with visual and movement-related activity.

Simple displaced/non-displaced classifiers are planned after these checks, using held-out recordings and consistent trial selection. Condition discrimination alone would not establish that a classifier uses an ErrP rather than another task-related signal.
