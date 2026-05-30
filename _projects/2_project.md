---
layout: page
title: Spell Training in VR
description: A Unity-based VR experience that offers users an innovative interaction system—sketching in midair to summon and manipulate in-game characters.
completed_on: UCSB, Winter 22
img: assets/img/2.PNG
importance: 30
category: HCI and Computer Graphics
project_pdf: assets/pdf/2_CS291A.pdf
github: https://github.com/satyam-aw/Spell-Training-in-VR
giscus_comments: true
giscus_repo: satyam-aw/Spell-Training-in-VR
giscus_repo_id: R_kgDOG3tAmA
giscus_category: General
giscus_category_id: DIC_kwDOG3tAmM4C9r7E
giscus_mapping: pathname
# optional
giscus_dark_theme: dark
giscus_light_theme: light
giscus_input_position: bottom
giscus_reactions_enabled: 1
giscus_emit_metadata: 0
giscus_lang: en
---

The ability to perceive the shape and motion of hands can be a vital component in improving the user experience across a variety of technological domains and platforms. In our project we explore utilization of hand gestures, and create an innovative interaction system based on midair sketching and build a VR game to demonstrate its usability. The project is focused on creating an immersive experience for a user placed in a Unity-based virtual world and can cast spells from their magic wand to summon and manipulate in-game characters. 

The spells cast (or sketches drawn) by the user are recognized via a OpenCV based [Gesture Recognition Module](https://github.com/shubhamtalbar96/virtual_board/tree/main). The engagement process is assisted via a webcam and hence there is no additional equipment baggage for the user. The [Unity-based VR game](https://github.com/satyam-aw/Spell-Training-in-VR) communicates with the [Gesture Recognition Module](https://github.com/shubhamtalbar96/virtual_board/tree/main) via WebSockets to receive commands and the visual canvas feed for a seamless UI. 



<div class="d-flex justify-content-center">
  <iframe width="600" height="375" src="https://www.youtube.com/embed/xMe-xDbng2Y?si=fS7G9IriuC_PMUBD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

<br>
### Architecture
The project comprises two main systems running side by side: the Unity Game Engine and an Image Recognition module developed using OpenCV, MediaPipe Hands, and Tesseract OCR. To establish communication between these components, a bidirectional server-client protocol transfers commands and messages. We set up two servers in total (one in each system), with each system also running a client that connects to the opposing server.

<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/2_archi.PNG" title="Architecture Diagram" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 1: Architecture of the Spell Training VR game</figcaption>
</figure>

### Gesture Recognition Module

We utilize heuristics within the [MediaPipe Hand Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker) API to identify four specific gestures: 

1. Selection 
2. Painting 
3. Clear Canvas 
4. Recognize Gesture 

These gestures enable real-time, mid-air sketching and canvas management. Once a sketch is complete, the Google Tesseract Optical Character Recognition (OCR) engine processes the visual data. The recognized text translates into a specific action command, which is then transmitted to the Unity game for execution.

<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/2_canvas.PNG" title="OCR Pre-processing" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 2: Image pre-processing and contour extraction for OCR</figcaption>
</figure>

### Unity Raycast System

When the Unity VR game receives a command, it evaluates the *Raycast hit point*. Depending on whether the Raycast hits an existing creature or empty space, the game executes the command to either **summon** or **manipulate** a creature along the spell's path.

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/2_raycast1.PNG" title="Raycast Summoning" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/2_raycast2.PNG" title="Raycast Selection" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Figure 3: A Raycast is cast to either summon a new creature or select an existing one.
</div>

Each time a Raycast is cast, the system checks if the hit point is within range of an active, spawned monster. If the hit point is close enough to a monster, that specific monster is targeted and destroyed.

This page provides a brief summary covering only the fundamental aspects of the project. Please refer to our full [project report](https://docs.google.com/document/d/1xfZlb3wNs5YU3gytwz8naTpyTMmHXUMzQ_JH7zJFFVs/edit?usp=sharing) for complete implementation details.
