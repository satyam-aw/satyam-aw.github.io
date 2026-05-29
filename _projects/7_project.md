---
layout: page
title: "Simplified Solar Tracker for PV Panels"
description: "A low-cost, dual-axis solar tracking system designed as a mechanical Maximum Power Point Tracker (MPPT) using an Arduino Uno and LDR sensors."
img: /assets/img/7.png
project_pdf: /assets/pdf/7_solar_tracker.pdf
importance: 1
category: Embedded Systems and IoT
demo_video: https://www.youtube.com/watch?v=yR4f5ZiOPAA
completed_on: IIT-KGP Apr'19
github: https://github.com/satyam-aw/Simplified-Solar-Tracker-for-PV-Panels
giscus_comments: true
giscus_repo: satyam-aw/Simplified-Solar-Tracker-for-PV-Panels
giscus_repo_id: R_kgDOSrZSFw
giscus_category: General
giscus_category_id: DIC_kwDOSrZSF84C-Fn-
giscus_mapping: pathname
# optional
giscus_dark_theme: dark
giscus_light_theme: light
giscus_input_position: bottom
giscus_reactions_enabled: 1
giscus_emit_metadata: 0
giscus_lang: en
---



<div class="d-flex flex-column align-items-center justify-content-center">
  <iframe width="600" height="375" src="https://www.youtube.com/embed/yR4f5ZiOPAA?si=0fF9zqePIs3vyO7Z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  <p class="text-center mt-2">
    <em>Figure 1: Dual-Axis Solar Tracker Prototype. If the embed does not load, <a href="https://www.youtube.com/watch?v=yR4f5ZiOPAA" target="_blank">click here to watch the live demonstration video directly on YouTube</a>.</em>
  </p>
</div>

<br>

Solar trackers automatically position objects at an optimal angle relative to the sun. While traditionally used to keep photovoltaic (PV) panels perpendicular to the sun’s rays for maximum energy absorption, they are also used to position space telescopes and heliostat mirrors.

This project implements a **Dual-Axis Solar Tracker** using an Arduino microcontroller and Light Dependent Resistors (LDRs). It acts as a mechanical Maximum Power Point Tracker (MPPT) to boost the efficiency of solar PV systems.

---
<br>

#### The Problem & Our Solution
* **The Problem:** Standard solar tracking systems rely on complex mathematical algorithms to maximize power output, making them expensive and difficult to maintain.
* **Our Solution:** We engineered a simplified tracking system that uses real-time light differentials captured by LDR sensors to adjust two perpendicular servo motors. 

---
<br>

#### Materials & Equipment


| Component | Quantity | Purpose |
| :--- | :---: | :--- |
| **Arduino Uno** | 1 | System microcontroller |
| **LDR Sensors** | 4 | Light intensity detection |
| **Servo Motors** | 2 | Horizontal and vertical movement |
| **10kΩ Resistors** | 4 | Voltage dividers for LDR data |
| **Breadboard & Jumpers** | 1 Set | Circuit prototyping |
| **Custom Mounts** | 2 | Cost-effective structural support |

---
<br>

#### Methodology & System Logic

```text
          [ Top LDR ]

               |
[ Left LDR ] --+-- [ Right LDR ]
               |
         [ Bottom LDR ]
```
<br>

The system operates on a continuous feedback loop based on the difference in light energy received by four sensors (Top, Bottom, Left, and Right). Two servo motors are mounted perpendicularly to provide two degrees of freedom.

##### Horizontal Tracking (Left / Right)
1. The Arduino reads the light intensity from the **Left** and **Right** LDRs.
2. If the Right LDR detects higher light intensity (lower resistance), the horizontal servo rotates right by a small increment.
3. The loop repeats until the light difference falls below a set threshold.

##### Vertical Tracking (Top / Bottom)
1. The Arduino reads the light intensity from the **Top** and **Bottom** LDRs.
2. The vertical servo adjusts up or down based on which sensor receives more light.
3. The panel stops moving once both sensors achieve equilibrium.

 **[View the Complete Source Code on GitHub](https://github.com/satyam-aw/Simplified-Solar-Tracker-for-PV-Panels)**

---
<br>

#### Experimental Results


##### Testing Observations
* **Light Source:** A smartphone torch was used to simulate the movement of the sun.
* **Tracking:** The system accurately tracked the light source across both axes within the servo motor's operational limit of 0 to 180 degrees.

---
<br>

#### Challenges & Engineering Insights

* **Servo Over-Rotation:** Servo motors are limited to a 0–179° range. We initialized the position variable at 90° and implemented software constraints to prevent the code from requesting negative angles or angles exceeding 180°.
* **Wire Strain:** Rapid panel movements initially caused jumper wires to disconnect from the breadboard. For a permanent deployment, the connections must be soldered.
* **Budget Optimization:** Instead of purchasing expensive commercial brackets, we custom-crafted the servo mounts to minimize total project costs.

---
<br>

#### Conclusion & Future Scope

This project successfully proves that a low-cost, mechanical solar tracker can effectively complement or back up electrical MPPT systems. By maintaining a perpendicular angle to the sun, the system maximizes solar energy absorption. 

##### Future Applications
The core logic of this tracking system can be adapted for:
* **Wind & Hydro Turbines:** Blade pitch angle control.
* **Telecommunications:** Satellite and dish antenna positioning for optimized signal reception.
