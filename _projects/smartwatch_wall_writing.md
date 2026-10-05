---
layout: page
title: SmartWatch for Wall Writing
description: WatchScribe reconstructs wall writing from smartwatch inertial signals using orientation correction and unsupervised stroke separation.
img: assets/img/projects/smart_watch_thumbnail.png
category: "Human Sensing & Interaction"
importance: 5
completed_on: "2019–2020"
project_pdf: /assets/pdf/2022_COMSNETS_WatchScribe.pdf
_styles: |
  .post article h2, .research-label { color: var(--global-theme-color); }
  .post article hr { margin: 2.25rem 0; border-top: 1px solid var(--global-divider-color); }
  .research-note { border-left: 3px solid var(--global-theme-color); background: var(--global-card-bg-color); padding: 1rem 1.25rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }
  .research-figure { max-width: 850px; margin: 1.5rem auto; }
  .post article table { width: 100%; border-collapse: collapse; margin: 1.25rem 0 1.75rem; font-size: 0.95rem; line-height: 1.55; }
  .post article th, .post article td { padding: 0.8rem 1rem; vertical-align: top; border-bottom: 1px solid #dfe3e8; }
  .post article .key-table thead { background: #e9edf2; color: #202b38; }
  .post article .key-table tbody tr:nth-child(odd) { background: #fff; color: #202b38; }
  .post article .key-table tbody tr:nth-child(even) { background: #f3f4f6; color: #202b38; }
---

**B.Tech. final-year project · IIT Kharagpur · 2019–2020**

**WatchScribe** explores how a wrist-worn smartwatch can reproduce writing on a vertical surface as digital boardwork. It uses accelerometer and gyroscope signals to estimate the pen's path, then removes the movements made while lifting and repositioning the pen between strokes.

The system uses **rotational kinematics and unsupervised clustering**, without a pretrained handwriting model or a user-specific training session. This collaborative work was presented at **COMSNETS 2022**.

<div class="research-note"><strong class="research-label">What “transcription” means here</strong><br>The output is reconstructed handwriting on a virtual board. The reported decipherability scores measure how well people can read that handwriting; they are not automated OCR or character-classification accuracy.</div>

---

## 1. Why wrist-based writing capture is difficult

A smartwatch does not follow exactly the same trajectory as a pen tip. Wrist flexion and extension continually change the sensor's orientation, mixing the writing motion across its axes. Directly integrating acceleration to recover small pen movements is also sensitive to measurement and reference-frame errors.

A second challenge is **pen-up/pen-down (PUPD) motion**. Moving the pen from the end of one stroke to the start of another produces a sensor trace, even though that movement should leave no ink. Reconstructing every measured movement would connect strokes that should remain separate.

WatchScribe addresses these problems in two stages: estimate the writing locus in a consistent frame, then separate writing strokes from repositioning gestures.

---

## 2. System architecture

<div class="research-figure">
{% include figure.liquid path="assets/img/projects/watchscribe/architecture.png" alt="WatchScribe architecture: inertial sensing, filtering, orientation correction, angular displacement and plane projection, followed by gesture clustering and transcription generation" class="img-fluid rounded" %}
<div class="caption">Original system architecture from Figure 2 of the submitted manuscript. Pen-locus estimation reconstructs the trajectory; transcription generation removes non-writing movements.</div>
</div>

| Stage                  | Purpose                                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Inertial sensing       | Collect three-axis accelerometer and gyroscope streams from a Moto360 smartwatch.                                              |
| Signal preprocessing   | Apply a low-pass filter with an empirically selected 2 Hz cutoff.                                                              |
| Orientation correction | Use accelerometer-derived roll and pitch with gyroscope readings to estimate Euler-angle rates in the Earth's reference frame. |
| Locus reconstruction   | Integrate angular rates and project the estimated trajectory onto the vertical writing plane.                                  |
| Stroke separation      | Identify and remove pen-up/pen-down intervals using gyro-signal deviations and two-stage clustering.                           |

---

## 3. Separating writing from repositioning

Pen lifts and repositioning often produce larger changes in gyroscope readings than ordinary writing strokes. WatchScribe extracts deviations between local peaks and subsequent dips, both within an axis and across different axes.

It first applies **k-means with two clusters** to these deviations. The smaller cluster is treated as a candidate for the less frequent PUPD events. Sharp turns within a genuine stroke can also produce large deviations, so a second clustering step separates these sparse points. A **silhouette score** helps select the PUPD cluster, and the corresponding intervals are removed from the reconstructed locus.

This approach adapts to the observed motion without requiring labelled examples of each character. It also preserves the handwritten shape instead of mapping every gesture to a fixed alphabet.

---

## 4. Experimental design

The study used **10 participants**, aged 20–35, including one left-handed writer. Participants wore a **Moto360 running Android Wear OS 2.0** on their writing wrist. A vertically mounted Wacom pen tablet or touchscreen monitor recorded the ground-truth handwriting.

| Study component              | Coverage                                                                                                                |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Individual symbols           | 133 characters: English and Bengali letters and digits, plus 10 mathematical symbols                                    |
| Words                        | 36 unique words per language, each 2–5 characters long; English words used two capitalization variants, giving 72 forms |
| Session boundaries           | Participants held the stylus still for 2 seconds before and after each writing session                                  |
| Human readability assessment | 24 independent validators, distinct from the writers, attempted to decipher reconstructed transcripts                   |
| Geometric comparison         | A multiscale grid-occupancy disparity score compared reconstructed and ground-truth images                              |
| Baseline                     | GyroPen, an existing inertial handwriting reconstruction approach                                                       |

Validators could make up to three guesses. The paper primarily reports performance within **two guesses**, because the third added little improvement. The disparity metric measures shape mismatch after cropping and resizing the images; a lower score indicates closer agreement with the original writing.

---

## 5. Results: how readable was the reconstruction?

The table below reports word decipherability from **Tables I and II of the submitted manuscript**. “First guess” and “within two guesses” describe the human validators' responses.

<div class="key-table" markdown="1">

| Measure                                          | First guess | Within two guesses |
| ------------------------------------------------ | ----------: | -----------------: |
| Exact word match, both languages                 |      69.37% |         **72.22%** |
| Exact word match, English                        |      69.79% |             73.61% |
| Exact word match, Bengali                        |      68.52% |             69.44% |
| English word match, ignoring case                |      86.11% |         **87.50%** |
| Longest common subsequence match, both languages |      83.93% |             85.02% |

</div>

Longest common subsequence (LCS) measures partial agreement between the intended word and the validator's answer. It should be read separately from exact word recognition.

For isolated characters, mean decipherability was **64.52% for English** and **56.28% for Bengali**, with a median of **66.67%** in both scripts. Words were easier to read than isolated symbols because linguistic context helped readers interpret imperfect strokes.

Against GyroPen, the manuscript reports lower geometric disparity and improved decipherability. The clearest qualitative benefit appears in characters with multiple strokes, where removing PUPD movements prevents unwanted connecting marks.

---

## 6. Limitations and lessons

- **Closed loops may not close completely.** Small gyroscope errors accumulate during trajectory estimation.
- **Straight strokes can become curved.** Distortion can make block letters appear cursive and confuse otherwise distinct symbols.
- **Stroke separation is imperfect.** Residual repositioning motion can leave small curves at the beginning or end of a stroke.
- **Writing style affects readability.** Similar uppercase/lowercase shapes and cursive characters remain ambiguous.
- **The study covers short writing tasks.** Its 10-participant evaluation and deliberate start/end pauses do not establish performance for unrestricted, continuous lecture-length boardwork.

The central result is that useful handwriting reconstruction is possible from a wrist-worn inertial sensor without character-specific training. Improving orientation and angular-displacement estimation is a natural next step toward more faithful strokes and more complex boardwork.

---

## 7. Paper and figure credit

**SmartWatch for Wall Writing: Real-time Transcription of Wall Writing from Inertial Sensing**<br>
Snigdha Das, Satyam Awasthi, Abdul Shamnar P, Pradipta De, Sandip Chakraborty, and Bivas Mitra. COMSNETS 2022.

[Read the submitted manuscript]({{ '/assets/pdf/2022_COMSNETS_WatchScribe.pdf' | relative_url }}).

<p class="small text-muted">The architecture figure is reproduced from Figure 2 of the submitted manuscript by Das et al. The methods and numerical results on this page refer to that manuscript version.</p>
