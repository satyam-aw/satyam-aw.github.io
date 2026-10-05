---
layout: page
title: State-Dependent Robust Output-Feedback MPC
description: Dynamic estimation and tracking-error bounds using a reproduced ROHMPC certificate and state-dependent disturbance envelopes.
img: /assets/img/projects/safe-output-fb-mpc.jpg
category: "Safe & Intelligent Control"
importance: 3
selected: true
completed_on: "2026–Present"
github: https://github.com/satyam-aw/ROHMPC-State-Dependent-Uncertainty
project_pdf: https://github.com/satyam-aw/ROHMPC-State-Dependent-Uncertainty/blob/master/research/state_dependent_bounds/manuscript/state_dependent_rohmpc.pdf
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
---

**Ongoing research with Dr. Johannes Köhler, Imperial College London.**

This project studies robust output-feedback model predictive control when uncertainty varies with the system state. An observer estimates the state from noisy measurements; estimation error and tracking error then jointly determine the robustness margins used by the controller.

The implementation builds on the upstream [ROHMPC design pipeline](https://github.com/dbenders1/rohmpc). My extension is documented under the fork's `research/state_dependent_bounds` directory. The upstream repository's navigation results describe the baseline, rather than completed closed-loop results for this extension.

---

## 1. Estimation and tracking architecture

<svg class="research-flow" viewBox="0 0 930 130" role="img" aria-labelledby="mpc-flow-title" xmlns="http://www.w3.org/2000/svg"><title id="mpc-flow-title">Noisy measurements → State observer → Estimation-error bound → Coupled tracking tube → Constraint tightening → Candidate robust MPC</title><defs><marker id="mpc-flow-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker></defs><rect x="10" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="77" y="59" text-anchor="middle" font-size="13" fill="currentColor">Noisy</text><text x="77" y="79" text-anchor="middle" font-size="13" fill="currentColor">measurements</text><path d="M 144 65 H 162" stroke="currentColor" fill="none" marker-end="url(#mpc-flow-arrow)"/><rect x="165" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="232" y="69" text-anchor="middle" font-size="13" fill="currentColor">State observer</text><path d="M 299 65 H 317" stroke="currentColor" fill="none" marker-end="url(#mpc-flow-arrow)"/><rect x="320" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="387" y="59" text-anchor="middle" font-size="13" fill="currentColor">Estimation-error</text><text x="387" y="79" text-anchor="middle" font-size="13" fill="currentColor">bound</text><path d="M 454 65 H 472" stroke="currentColor" fill="none" marker-end="url(#mpc-flow-arrow)"/><rect x="475" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="542" y="59" text-anchor="middle" font-size="13" fill="currentColor">Coupled</text><text x="542" y="79" text-anchor="middle" font-size="13" fill="currentColor">tracking tube</text><path d="M 609 65 H 627" stroke="currentColor" fill="none" marker-end="url(#mpc-flow-arrow)"/><rect x="630" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="697" y="59" text-anchor="middle" font-size="13" fill="currentColor">Constraint</text><text x="697" y="79" text-anchor="middle" font-size="13" fill="currentColor">tightening</text><path d="M 764 65 H 782" stroke="currentColor" fill="none" marker-end="url(#mpc-flow-arrow)"/><rect x="785" y="30" width="134" height="70" rx="6" fill="var(--global-card-bg-color)" stroke="var(--global-theme-color)"/><text x="852" y="59" text-anchor="middle" font-size="13" fill="currentColor">Candidate</text><text x="852" y="79" text-anchor="middle" font-size="13" fill="currentColor">robust MPC</text></svg>

<div class="research-note"><strong class="research-label">Research scope</strong><br>The current extension develops and illustrates dynamic error bounds. Closed-loop MPC integration and validation remain ongoing work.</div>

---

## 2. From a global certificate to dynamic bounds

The current derivation reuses the reproduced offline design's constant metric, observer gain, feedback gain, and LMI certificate. No new semidefinite program is solved.

In the global case, a scalar squared-radius propagation recovers the original observer bound. A local process-disturbance envelope then reduces its forcing term while retaining the same quadratic structure. The estimation bound couples to a tracking-error tube through an upper bound on the unknown true speed.

The current experiment scales acceleration-channel residual disturbance bounds with speed. These smaller uncertainty sets are prescribed synthetic subsets of the original bounds, not sets identified from new data. Measurement-noise bounds remain fixed.

---

The global squared-radius comparison has the form:

$$
\dot{R} = -\lambda R + q_0, \qquad q_0 = \lambda\epsilon^2, \qquad r = \sqrt{R}.
$$

Here, $R$ bounds the squared estimation-error norm, $r$ is its radius, and $\epsilon$ is the original observer bound. Initializing $R(0)=\epsilon^2$ recovers the constant global radius. The local construction reduces the forcing allowance according to the prescribed disturbance envelope.

| Ingredient                         | Treatment in the current prototype                                   |
| ---------------------------------- | -------------------------------------------------------------------- |
| Metric and observer/feedback gains | Reused from the offline design                                       |
| Global bound                       | Recovers the original observer radius                                |
| Local process uncertainty          | Synthetic speed-dependent subsets of the original disturbance bounds |
| Measurement noise                  | Fixed bounds                                                         |
| Tracking tube                      | Coupled to the estimation bound                                      |

---

## 3. Prototype result

The documented September 10 experiment uses a prescribed low/high/low nominal-speed schedule:

<div class="key-table" markdown="1">

| Measurement                      |     Value |
| -------------------------------- | --------: |
| Recovered global observer radius | 0.0744264 |
| Final local observer radius      | 0.0694546 |
| Final-time radius reduction      | **6.68%** |

</div>

<div class="research-note"><strong class="research-label">How to interpret the result</strong><br>This is a tube-propagation illustration, not a closed-loop quadrotor simulation, an average performance improvement, or a universal reduction. The repository includes MATLAB scripts, derivations, saved comparison data, and figures.</div>

---

## 4. Closed-loop formulation and remaining work

A subsequent analytical note develops a conditional formulation with tube-consistency initialization, tightened constraints, domain preservation, and terminal conditions. Its assumptions still need to be verified for an implemented controller; it does not certify the existing Falcon implementation or the complete planning/tracking hierarchy.

Remaining work includes rigorous Jacobian-domain coverage, numerical certificate validation, model/data validation, terminal-set compatibility, and closed-loop MPC integration and evaluation. Finite numerical audits alone do not establish nonlinear safety or recursive feasibility.

---

## 5. Code and research notes

- [Project repository](https://github.com/satyam-aw/ROHMPC-State-Dependent-Uncertainty)
- [Research implementation and scope](https://github.com/satyam-aw/ROHMPC-State-Dependent-Uncertainty/blob/master/research/state_dependent_bounds/README.md)
- [Baseline-equivalent LMI derivation and numerical comparison](https://github.com/satyam-aw/ROHMPC-State-Dependent-Uncertainty/blob/master/research/state_dependent_bounds/LMI_RADIUS_DERIVATION.md)
- [Conditional closed-loop proof framework](https://github.com/satyam-aw/ROHMPC-State-Dependent-Uncertainty/blob/master/research/state_dependent_bounds/CLOSED_LOOP_PROOF_FRAMEWORK.md)
- [Working manuscript](https://github.com/satyam-aw/ROHMPC-State-Dependent-Uncertainty/blob/master/research/state_dependent_bounds/manuscript/state_dependent_rohmpc.pdf)
