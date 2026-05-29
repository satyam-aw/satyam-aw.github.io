---
layout: page
title: 3D Maze Exploration via Fixed-Function OpenGL
description: First-person 3D maze game built with C++ and legacy fixed-function OpenGL via FreeGLUT
img: assets/img/3.png
completed_on: UCSB, S22
importance: 2
download_link: https://github.com/satyam-aw/3d_Maze_openGL/raw/refs/heads/main/resources/Play_Game.zip
demo_video: https://youtu.be/9cJ7eTtbbqo
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
      <iframe width="100%" height="100%" src="https://www.youtube.com/embed/9cJ7eTtbbqo?si=cM0pXmQeOFvQLpKT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
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
* **Download Game (Portable Windows x86):** [Play_Game.zip](https://github.com/satyam-aw/3d_Maze_openGL/raw/refs/heads/main/resources/Play_Game.zip) _(launch using Play_Game.bat)_

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

##### 2.1. Stutter-Free Input & Delta Time
Standard operating system keyboard repeat timers introduce micro-stutters when keys are held down. To achieve smooth movement:
* **Asynchronous Keys:** A custom boolean status array (`keys[...]`) tracks exact press/release states globally.
* **Delta Time Scaling ($dt$):** To prevent frame-rate fluctuations from speeding up or slowing down the game physics, the system checks system ticks using `glutGet(GLUT_ELAPSED_TIME)` to normalize actions across varying system refresh rates:

$$dt = \frac{T_{\text{current}} - T_{\text{previous}}}{1000}$$

##### 2.2. Smooth First-Person Infinite Mouse Look
To replicate standard first-person desktop game controls, the engine uses a continuous mouse resetting script via `glutWarpPointer`. The app calculates raw positional mouse deltas ($\Delta x, \Delta y$) relative to the viewport center, updates rotation variables, and snaps the system cursor back to coordinates $(cx, cy)$. This establishes an endless, boundary-free viewing axis.

##### 2.3. Kinematic Jumps & Collision Handling
Vertical player flight (jumping) incorporates basic gravitational acceleration equations:

$$v_y = v_{y0} + g \cdot dt$$

$$\text{camera}_y = \text{camera}_{y0} + v_y \cdot dt$$

If structural spatial data matches solid map bounds, a reactive bounding offset (`BOUNCEBACK`) immediately offsets player positioning vectors to prevent clipping through the maze layout.

##### 2.4. Pipeline-Isolated 2D Orthographic Compass
To provide clear navigation guidance through the labyrinth, a dynamic HUD compass was implemented. The software architecture leverages a state-driven isolation pattern to draw 2D flat primitives over an active 3D context without corrupting the rendering pipeline from frame to frame:

* **State Snapshotting:** `glPushAttrib(GL_ALL_ATTRIB_BITS)` takes an immediate memory snapshot of all current 3D attributes (lighting, texturing flags, and depth-testing masks) before temporarily disabling features that cause color mixing or layer clipping errors.
* **Matrix Stack Preservation:** Calling `glPushMatrix()` on both the `GL_PROJECTION` and `GL_MODELVIEW` matrices safely caches your active 3D perspective and camera look matrices onto the system stack.
* **4x4 Identity Reset:** Calling `glLoadIdentity()` overwrites both active matrix tracks, clearing them back to neutral 4x4 Identity Matrices:

$$\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

* **Orthographic Projection Mapping:** A flat pixel-for-pixel coordinate system is established directly inside the 4x4 Projection Matrix via `gluOrtho2D`, mapping input pixel bounds to normalized device tracking spaces:

$$\text{Screen Viewport} \xrightarrow{\text{gluOrtho2D}} [0, \text{width}] \times [0, \text{height}]$$

* **Local View Transformations:** The drawing pipeline switches focus to `GL_MODELVIEW` mode, shifts to the upper-right viewport corner via `glTranslatef`, and rotates the local coordinate space using `glRotatef`:

$$\text{Rotation Angle (Degrees)} = \text{rot}_x \times 57.2957795$$

* **Flattened Primitive Projection:** Fixed quadrilateral vectors are plotted using flat pixels relative to the local origin space. Because the orthographic configurations remain isolated inside the projection slot, any movements processed in the modelview stage are flattened automatically on the UI layer.
* **Frame-to-Frame Context Restoration:** Calling `glPopMatrix()` and `glPopAttrib()` immediately pops the cached 3D matrices and spatial attributes back into active registers. This fully unwinds the temporary UI state changes, ensuring zero pipeline contamination carries over into the next frame's 3D rendering pass.

---
<br>

#### 3. Performance Results & Conclusion
Real-world testing shows that decoupling input tracking into state arrays combined with Delta Time scaling completely clears up operational stuttering. Memory usage sits comfortably under 50MB during active runtime execution. 

This project successfully proves that combining legacy fixed-function OpenGL configurations with modern algorithmic input handling yields a high-utility, performant first-person game engine framework.
