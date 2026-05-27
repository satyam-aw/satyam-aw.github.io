---
layout: page
title: 3D Maze Exploration via Fixed-Function OpenGL
description: First-person 3D maze game built with C++ and legacy fixed-function OpenGL via FreeGLUT
img: assets/img/3.webp
completed_on: UCSB, S22
importance: 3
download_link: https://github.com/satyam-aw/3d_Maze_openGL/blob/main/resources/Play_Game.zip
category: HCI and Computer Graphics
github: https://github.com/satyam-aw/3d_Maze_openGL
giscus_comments: true
giscus_repo: satyam-aw/3d_Maze_openGL
giscus_repo_id: R_kgDOHJjNmg
giscus_category: General
giscus_category_id: DIC_kwDOHJjNms4C99Sg
giscus_mapping: pathname
# optional
giscus_dark_theme: dark
giscus_light_theme: light
giscus_input_position: bottom
giscus_reactions_enabled: 1
giscus_emit_metadata: 0
giscus_lang: en
---
<div style="display: flex; gap: 15px; width: 120%; margin-left: -10%; margin-right: -10%; box-sizing: border-box; flex-wrap: wrap;">
  <!-- Left Video and Caption Container -->
  <div style="flex: 1; min-width: 300px;">
    <div style="aspect-ratio: 16/9; width: 100%;">
      <iframe width="100%" height="100%" src="https://www.youtube.com/embed/WjW-mPkbtok?si=O4Bf62oOqxIZnWbB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    <p style="text-align: center; font-style: italic; font-size: 0.9em; color: #666; margin-top: 8px; margin-bottom: 0;">
      Level 2 Gameplay Playthrough
    </p>
  </div>

  <!-- Right Video and Caption Container -->
  <div style="flex: 1; min-width: 300px;">
    <div style="aspect-ratio: 16/9; width: 100%;">
      <iframe width="100%" height="100%" src="https://www.youtube.com/embed/O8dUZq9Oty0?si=2UhlAstBdnHgZY7p" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
    <p style="text-align: center; font-style: italic; font-size: 0.9em; color: #666; margin-top: 8px; margin-bottom: 0;">
      Course Assignment Explanation
    </p>
  </div>
</div>

<br>

This project showcases an interactive, first-person 3D maze game built with C++ and legacy fixed-function OpenGL via FreeGLUT. It highlights methods to bypass default desktop input lag, implementing frame-rate-independent navigation (strafing/jumping), smooth infinite mouse look, collision structures, and dynamic text-file map parsing.

##### 📥 Important Links

* **Source Code:** [GitHub Repository](https://github.com/satyam-aw/3d_Maze_openGL)
* **Download Game (Portable Windows x86):** [Play_Game.zip](https://github.com/satyam-aw/3d_Maze_openGL/blob/main/resources/Play_Game.zip) _(launch using Play_Game.bat)_

---
<br>

#### 1. Introduction & System Architecture
Developing real-time 3D environments requires tight syncing between logic threads and hardware rendering pipelines. This project builds a reliable first-person viewport framework using legacy state-driven APIs. 

* **Environment:** Microsoft Visual Studio 2022
* **Libraries:** FreeGLUT & GLEW linked seamlessly via the `nupengl.core` NuGet toolchain.
* **Assets:** Parses plain ASCII text maps (e.g., `maze1.txt`) into 3D structural boundaries at runtime.

---
<br>

#### 2. Core System Implementations

##### 2.2. Stutter-Free Input & Delta Time
Standard operating system keyboard repeat timers introduce micro-stutters when keys are held down. To achieve smooth movement:
* **Asynchronous Keys:** A custom boolean status array (`keys[...]`) tracks exact press/release states globally.
* **Delta Time Scaling ($dt$):** To prevent frame-rate fluctuations from speeding up or slowing down the game physics, the system checks system ticks using `glutGet(GLUT_ELAPSED_TIME)` to normalize actions across varying system refresh rates:

$$dt = \frac{T_{\text{current}} - T_{\text{previous}}}{1000}$$

##### 2.3. Smooth First-Person Infinite Mouse Look
To replicate standard first-person desktop game controls, the engine uses a continuous mouse resetting script via `glutWarpPointer`. The app calculates raw positional mouse deltas ($\Delta x, \Delta y$) relative to the viewport center, updates rotation variables, and snaps the system cursor back to coordinates $(cx, cy)$. This establishes an endless, boundary-free viewing axis.

##### 2.4. Kinematic Jumps & Collision Handling
Vertical player flight (jumping) incorporates basic gravitational acceleration equations:

$$v_y = v_{y0} + g \cdot dt$$

$$\text{camera}_y = \text{camera}_{y0} + v_y \cdot dt$$

If structural spatial data matches solid map bounds, a reactive bounding offset (`BOUNCEBACK`) immediately offsets player positioning vectors to prevent clipping through the maze layout.

---
<br>

#### 3. Performance Results & Conclusion
Real-world testing shows that decoupling input tracking into state arrays combined with Delta Time scaling completely clears up operational stuttering. Memory usage sits comfortably under 50MB during active runtime execution. 

This project successfully proves that combining legacy fixed-function OpenGL configurations with modern algorithmic input handling yields a high-utility, performant first-person game engine framework.
