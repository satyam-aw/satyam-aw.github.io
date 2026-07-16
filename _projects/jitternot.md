---
layout: page
title: JitterNot 
description: LSTM-based Model Predictive Controller for Adaptive Video Streaming
completed_on: UCSB, Spring 22 
img: /assets/img/6_jitternot_block_diag.jpg
importance: 4
selected: true
category: "Autonomous Systems"
project_pdf: https://satyam-aw.github.io/Jitternot_CS293N_Final_Report/main.pdf
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

Video conferencing quality can vary significantly under changing network conditions. For a video-conferencing application (VCA), the way the system adapts video quality directly affects the user-perceived Quality of Experience (QoE).

Adaptive bitrate (ABR) algorithms are commonly used to regulate video quality during a call. Many practical ABR mechanisms rely on fixed rules or reactive heuristics, which may not fully exploit short-term predictions of the deployment environment and network conditions.

**JitterNot** is a learning-assisted Model Predictive Control (MPC) framework evaluated using Jitsi Meet as an open-source WebRTC testbed. An LSTM throughput predictor is trained offline using WebRTC telemetry collected under emulated network conditions. During a live call, the trained model performs online inference, and its short-horizon throughput forecasts are supplied to an MPC controller that selects the next video-resolution action.

##### Our Contributions
* **Short-Horizon Throughput Prediction:** An offline-trained Long Short-Term Memory (LSTM) model predicts future network throughput from recent WebRTC telemetry.
* **Control-System Simplification:** Frame jitter and quantization-parameter models are expressed as functions of predicted throughput and video resolution, reducing the online optimization to a single manipulated variable: video resolution \(R\).
* **QoE Optimization:** An MPC controller applies the Receding Horizon Control (RHC) principle to optimize predicted QoE while respecting resolution, jitter, and quantization constraints.
* **Open-Source Testbed:** Jitsi Meet provides a reproducible WebRTC environment for collecting telemetry and comparing JitterNot against the platform's default adaptation behavior.

We demonstrate that JitterNot can improve or match the QoE achieved by Jitsi Meet's default video adaptation mechanism under a range of emulated network conditions.

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRP9nMBj6mPrwvRNVPJRPV7taaE1sXctl6v4om8tYfFuHap1kkN3ZWDXQYD0qssYok7xbkfz8CWJFnl/pubembed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

<br>
<br>

#### System Architecture and Problem Formulation

JitterNot models the video-conferencing delivery path as a closed-loop control system in discrete time. Jitsi Meet supplies the WebRTC telemetry used by the estimator and serves as the application testbed on which the controller is evaluated.

<figure class="mt-3 mt-md-0 text-center">
  {% include figure.liquid path="assets/img/6_jitternot_block_diag.jpg" title="JitterNot system architecture" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 1: JitterNot closed-loop architecture using Jitsi Meet as the WebRTC testbed.</figcaption>
</figure>

##### 1. Throughput Prediction with an LSTM

The throughput predictor is trained offline using WebRTC statistics collected from Jitsi Meet sessions under varied network conditions. At runtime, the trained LSTM processes a 10-second history window of WebRTC telemetry \((t-10 \rightarrow t-1)\) and forecasts network throughput \(C\) over the MPC prediction horizon.

The LSTM weights remain fixed during a call. Only inference is performed online, which keeps the real-time control loop lightweight and reproducible.

##### 2. QoE State-Mapping Models

The system observes several video-quality and network variables, but the online controller optimizes a single manipulated variable: video resolution \(R\). Frame jitter and quantization behavior are modeled as functions of resolution and predicted throughput.

* **Frame-Jitter Model \(F\):** Estimates frame-delay variation over a sliding five-second window:

  $$F(t) =
  \sum_{k=t-4}^{t}
  \left|
  \frac{R(k)}{C(k)}
  -
  \frac{R(k-1)}{C(k-1)}
  \right|$$

* **Quantization-Parameter Model \(P\):** Uses third-degree polynomial regression to model encoding compression as a function of available throughput relative to frame resolution:

  $$
  P(t) =
  \sum_{k=0}^{3}
  a_k
  \left(
  \frac{100\,C(t)}{R(t)}
  \right)^k
  $$

Because \(F\) and \(P\) are expressed in terms of \(R\) and the predicted throughput \(C\), the controller can optimize over a one-dimensional resolution sequence rather than independently optimizing several quality variables.

##### 3. QoE Objective and Receding-Horizon Control

At every control step, the MPC predicts QoE over the look-ahead horizon and minimizes the error relative to a normalized target QoE of \(r(k)=1\):

$$
\min_{\{R_k\}_{k=t}^{t+N}}
J =
\frac{1}{N}
\sum_{k=t}^{t+N}
\left(
\widehat{\mathrm{QoE}}(k)-r(k)
\right)^2
$$

subject to:

$$
\begin{aligned}
0 &\leq F(k) \leq 1.5F_{\max},\\
R_{\min}/2 &\leq R(k) \leq R_{\max},\\
0 &\leq P(k) \leq 1.5P_{\max}.
\end{aligned}
$$

The normalized QoE metric is:

$$
\widehat{\mathrm{QoE}}_k =
\frac{
\alpha \log(R_k/R_{\min})
-
\beta P_k
-
\gamma F_k
}{
\mathrm{QoE}_{\mathrm{avg}}
}
$$

The optimizer computes a sequence of candidate resolution actions for the full prediction horizon. Following the receding-horizon principle, JitterNot applies only the first resolution decision, collects fresh Jitsi/WebRTC telemetry, shifts the horizon forward, and solves the optimization problem again.

---

#### Evaluation Summary

JitterNot was evaluated using live **Jitsi Meet** sessions running in Google Chrome. Nested MahiMahi network-emulation shells were used to generate a broad range of network conditions:

* latency from 0 to 1500 ms,
* random packet loss from 0% to 35%, and
* link rates from 3 Mbps to 100 Mbps.

WebRTC statistics were collected through Chrome's `webrtc-internals` interface and used both to train the offline throughput predictor and to evaluate the closed-loop controller.

##### Core Findings vs. Jitsi Meet's Default Adaptation

* **Predictive Accuracy:** The LSTM throughput predictor achieved an average normalized RMSE of **0.4** on the held-out evaluation data.
* **Resolution Selection:** Across the evaluated windows, the MPC-selected resolution profile matched or exceeded the resolution selected by Jitsi Meet's default adaptation mechanism.
* **QoE Improvement:** Across 10 evaluation sessions, JitterNot improved the project-defined QoE metric and several associated video-quality terms.

| Performance Metric | Average Change vs. Jitsi Meet Baseline |
| :--- | :--- |
| **Overall QoE Metric** | **+18.78%** |
| **Perceived Video Quality \(q(R)\)** | **+68.50%** |
| **Frame Jitter** | **-18.97%** |
| **Quantization-Parameter Metric** | **+9.77%** |

<br>

##### Current Limitations

* **Solver Latency:** Each MPC decision required approximately 100–400 ms in the evaluated implementation. This is high for a client-side real-time controller and motivates a faster solver, an amortized policy, or server-side computation.
* **Interaction with Jitsi's Existing Adaptation Loop:** JitterNot was evaluated on top of Jitsi Meet's default codec and adaptation behavior. The two control loops can interact, which may affect latency, jitter, or stability. Because Jitsi Meet is open source, a stronger future implementation could integrate JitterNot directly into the sender-side adaptation path or disable the default controller for a cleaner comparison.
* **Generalization:** The LSTM was trained offline on data collected under the selected MahiMahi conditions and video workload. Prediction performance may degrade under substantially different network environments or source-video characteristics.
* **Discrete Resolution Actions:** Video resolutions are selected from a finite set. A production implementation should explicitly use candidate-sequence search, dynamic programming, mixed-integer optimization, or a continuous bitrate relaxation followed by quantization.

##### Conclusion

JitterNot demonstrates how learned short-horizon throughput prediction can be combined with model predictive control for adaptive real-time video conferencing. The LSTM captures recent network dynamics, while MPC converts those predictions into constraint-aware resolution decisions using a receding-horizon feedback loop.

The results indicate that prediction-based control can improve the project-defined QoE relative to Jitsi Meet's default adaptation behavior under the evaluated network conditions. Jitsi Meet also provides an open-source path toward tighter integration, lower control-loop interaction, and more reproducible future experimentation.

Please read our [full report](https://satyam-aw.github.io/Jitternot_CS293N_Final_Report/main.pdf) for complete implementation details and findings.