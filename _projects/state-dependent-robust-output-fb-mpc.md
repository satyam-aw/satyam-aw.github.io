---
layout: page

title: State-Dependent Robust Output-Feedback MPC
description: State-dependent estimation and tracking-error bounds for safe output-feedback predictive control
img: assets/img/projects/safe-output-fb-mpc.jpg
category: "Safe & Intelligent Control"
importance: 2
selected: true
completed_on: "Summer 26-Present"
---

## State-Dependent Robust Output-Feedback MPC

**Ongoing research project with Dr. Johannes Köhler, Imperial College London**

This project investigates **robust output-feedback model predictive control (ROMPC)** when uncertainty depends on the operating state of the system.

In output-feedback control, the controller does not have direct access to the true system state. Instead, an observer estimates the state from noisy measurements, introducing an **estimation error** in addition to the usual disturbance-driven **tracking error**.

Conventional robust formulations often bound these uncertainties globally. This can be unnecessarily conservative when sensing quality or model uncertainty varies significantly across the state space.

### Research Direction

The project studies **state-dependent bounds for both estimation and tracking errors** within a robust MPC framework.

The resulting closed-loop architecture can be viewed as:

**Measurements → State Observer → Estimation-Error Bound → Robust MPC → Tracking-Error Bound → System**

The estimation and tracking tubes are coupled: uncertainty in the state estimate affects the controller's tracking error, while both contribute to robust constraint tightening.

The current direction uses available **incremental stability / contraction-based certificates** to propagate these bounds while allowing disturbance and measurement uncertainty to depend on the predicted state.

### Motivation

State-dependent uncertainty allows the controller to distinguish between regions where:

- measurements are reliable or unreliable,
- model mismatch is small or large,
- tighter or wider robustness margins are required.

Rather than applying the same worst-case uncertainty everywhere, the MPC can account for the uncertainty expected along a candidate trajectory.

This creates the possibility of **less conservative robust control** while maintaining safety guarantees and can naturally encourage trajectories through regions with better sensing or lower model uncertainty.

### Current Work

The project is currently focused on:

- reproducing the baseline robust output-feedback MPC formulation,
- implementing coupled estimation and tracking-error tubes,
- incorporating state-dependent process and measurement uncertainty,
- propagating the corresponding online error bounds,
- evaluating the effect on constraint tightening and closed-loop behavior.

The initial focus is on the state-dependent uncertainty formulation; observer and controller contraction certificates are treated as available rather than being jointly synthesized.
