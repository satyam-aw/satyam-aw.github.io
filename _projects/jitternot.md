---
layout: page
title: JitterNot 
description: LSTM-based Model Predictive Controller for Adaptive Video Streaming
completed_on: UCSB, Spring 22 
img: /assets/img/6_jitternot_block_diag.jpg
importance: 1
selected: true
category: "Sequential Decision Models, Generative AI, and Applied ML"
project_pdf: /assets/pdf/jitternot_293N_ml_ns.pdf
github: https://github.com/satyam-aw/Jitternot-LSTM-MPC-for-ABR
giscus_comments: true
giscus_repo: satyam-aw/Jitternot-LSTM-MPC-for-ABR
giscus_repo_id: R_kgDOHeRkiw
giscus_category: General
giscus_category_id: DIC_kwDOHeRki84C94HR
giscus_mapping: pathname
# optional
giscus_dark_theme: dark
giscus_light_theme: light
giscus_input_position: bottom
giscus_reactions_enabled: 1
giscus_emit_metadata: 0
giscus_lang: en
---

Video conferencing has become an essential part of everyday life worldwide. How a VCA varies video quality under different network conditions is pivotal in determining the user-perceived Quality of Experience (QoE). 

Adaptive Bitrate (ABR) algorithms are often used to optimize QoE during video conferencing. However, they use fixed control rules or heuristics and suffer from a key **limitation**: 
they do not take into account the deployment environment and network conditions. 

We use a Model Predictive Controller (MPC) in a closed loop and supply it with predicted throughput to effectively evaluate QoE parameters. 

##### Our Contributions
* **Throughput Prediction**: An Long Short-Term Memory (LSTM) model that simplifies the control system from Multi-Input Single-Output (MISO) to Single-Input Single-Output (SISO).
* **QoE Optimization**: An MPC controller that optimizes the perceived QoE by utilizing the Receding Horizon Control (RHC) principle to find the optimum value of video resolution ($R$).

We demonstrate that running the closed-loop control by JitterNot on top of the VCA can improve or match the default codec’s QoE during a video conference.



<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRP9nMBj6mPrwvRNVPJRPV7taaE1sXctl6v4om8tYfFuHap1kkN3ZWDXQYD0qssYok7xbkfz8CWJFnl/pubembed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>


<br>
<br>

#### System Architecture & Problem Formulation

The framework models the VCA delivery path as a Single-Input Single-Output (SISO) control loop operating in the discrete-time domain.
<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/6_jitternot_block_diag.jpg" title="example image" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 1: JitterNot Architecture for closed-loop MPC</figcaption>
</figure>


##### 1. Throughput Prediction (LSTM)
A Deep Long Short-Term Memory (LSTM) network acts as the system estimator. It processes a 10-second window of historical WebRTC engine telemetry ($t-10 \rightarrow t-1$) to output a multi-step forecast of network throughput or capacity ($C$) across a 5-second look-ahead prediction horizon ($N$).

##### 2. State Mapping Subsystems
To simplify the control system, contextual parameters namely Frame jitter and QP are mathematically mapped to the manipulated variable—Video Resolution ($R$):

* **Frame Jitter Model ($F$):** Estimates latency variation based on network download delays for each frame across a sliding 5-second window:
  $$F(t) = \sum_{k=t-4}^{t} \left| \frac{R(k)}{C(k)} - \frac{R(k-1)}{C(k-1)} \right|$$

* **Quantization Parameter Model ($P$):** A 3rd-degree polynomial regression pipeline modeling spatial detail compression vs. available capacity:
  $$P(t) = \sum_{k=0}^{3} a_k \left( \frac{100 \cdot C(t)}{R(t)} \right)^k$$

##### 3. Objective Function & Receding Horizon Control
The optimization engine utilizes the **Receding Horizon Control (RHC)** principle. At each step, it tracks a constant target baseline of normalized perfect QoE ($r(t) = 1$) by minimizing a Mean Squared Error (MSE) cost function:

$$\min_{R_k \in \mathcal{R}} J = \frac{1}{N} \sum_{k=t}^{t+N} \left( \widehat{\text{QoE}}(k) - r(k) \right)^2 \quad \text{s.t. } \begin{cases} 0 \leq F(t) \leq 1.5 F_{\max} \\ R_{\min}/2 \leq R(t) \leq R_{\max} \\ 0 \leq P(t) \leq 1.5 P_{\max} \end{cases}$$

Where the normalized target optimization variable is defined as:
$$\widehat{\text{QoE}}_k = \frac{\alpha \cdot \log(R_k/R_{\min}) - \beta P_k - \gamma F_k}{\text{QoE}_{\text{avg}}}$$

**Control Loop Execution:** The solver resolves the full sequence of actions for the entire look-ahead block ($t \rightarrow t+N$) but applies only the immediate optimal choice ($R_k$) at the current instance before rolling the horizon window forward by one step.

---

#### Evaluation Summary

The framework was benchmarked on live Google Meet sessions using nested MahiMahi network emulation containers to simulate high-stress network constraints (0–1500 ms latency, 0–35% random packet loss, 3–100 Mbps variable link speeds).

##### Core Findings vs. Google Meet Baseline
* **Predictive Accuracy:** The core LSTM look-ahead tracking model achieved a tight average Root Mean Square Error (RMSE) of **0.4** across test validation sets.
* **Resolution Maintenance:** Unlike rule-based heuristics, JitterNot's rolling horizon proactively anticipated traffic fluctuations, ensuring the calculated resolution profile matched or exceeded default WebRTC behaviors without degrading quality.
* **Metric Improvements:** Across 10 independent evaluation trials, JitterNot demonstrated substantial performance gains over standard Google Meet engine policies:


| Performance Metric | Average Gain vs. Default Google Meet Baseline |
| :--- | :--- |
| **Overall QoE Metric Score** | **+18.78%** |
| **Perceived Video Quality ($q(R)$)** | **+68.50%** |
| **Frame Jitter Suppression** | **-18.97%** (Lower Jitter) |
| **Quantization Parameter ($QP$)** | **+9.77%** (Slightly Higher Compression) |

<br>

##### Current Limitations
* **Computational Latency:** Solver execution overhead ranged between 100–400 ms per step. This delay is high for real-time edge devices, indicating a need for server-side offloading or lightweight heuristic approximations in production web implementations.
* **Loop Interaction:** Because JitterNot sits on top of Google Meet's internal codec loops, an unmodeled interactive feedback loop exists. Full architectural decoupling within open-source VCA engines is expected to unlock even higher performance ceilings.

##### Conclusion

The results suggest that significant improvements can be made to the current techniques
used by commercial VCAs by employing DL-based solutions since, unlike rule-based
approaches, they can inherently account for fluctuating network conditions across different
deployment environments and adapt to them dynamically.

Please read our [full report](/assets/pdf/jitternot_293N_ml_ns.pdf) for complete implementation details and findings.