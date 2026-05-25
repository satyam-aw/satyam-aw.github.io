---
layout: page
title: Spell Training in VR
description: A Unity-based VR experience that offers users an innovative interaction system: sketching in midair to summon and manipulate in-game characters.
img: assets/img/2.PNG
importance: 2
category: HCI and Computer Graphics
project_pdf: assets/pdf/2_CS291A.pdf
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

The spells cast (or sketches drawn) by the user are recognized via a OpenCV based [Gesture Recognition Module](https://github.com/shubhamtalbar96/virtual_board/tree/main). The engagement process is assisted via a webcam and hence there is no additional equipment baggage for the user. The [Unity-based VR game](https://github.com/satyam-aw/Spell-Training-in-VR) communicates with the [Gesture Recognition Module](https://github.com/shubhamtalbar96/virtual_board/tree/main) via a web-sockets to receive commands and the visual canvas feed for a seamless UI. 



<div class="d-flex justify-content-center">
  <iframe width="600" height="375" src="https://www.youtube.com/embed/xMe-xDbng2Y?si=fS7G9IriuC_PMUBD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

<br>
The entire project is composed of two backend systems working side-by side - first the Unity Game Engine, and second the Image Recognition module developed using OpenCV, MediaPipe Hands and Tesseract OCR libraries. To establish communication between the two components a server-client protocol was used to send commands/messages. Two servers were set up in total, each in one of the backends. Each backend also had a client connected to the server of the other.

<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/2_archi.PNG" title="example image" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 1: Architecture of the Spell Training VR game</figcaption>
</figure>

We utilize heuristics in [Mediapipe Handlandmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker) to identify 4 specific postures: 

1. Selection 
2. Painting 
3. Clear Canvas 
4. Recognize gesture 

These postures enable real-time midair sketching and canvas management. Once a sketch is complete, Google Tesseract optical character recognition (OCR) Engine processes the visual data. The recognized text is then converted into final code and then transmitted to the Unity Game, which executes the corresponding commands.


<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/2_canvas.PNG" title="example image" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 2: Image pre-processing and contour extraction for OCR</figcaption>
</figure>

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/2_raycast1.PNG" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/2_raycast2.PNG" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Figure 3: A raycast is fired to- summon a new creature or select an existing creature
</div>

Everytime a Raycast is instantiated, we check internally if the hit point of the Raycast is close to one of the spawned monsters already in the game. If the new Raycast is close enough then we destroy the corresponding monster!
