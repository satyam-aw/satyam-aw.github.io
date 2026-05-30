---
layout: page
title: CohesiveAR for Interactive Design
description: Real-Time Texture Extraction and Mapping on Virtual Objects
img: assets/img/1.PNG
completed_on: UCSB, F22
demo_video: https://www.youtube.com/watch?v=eUzmJmamqFk
importance: 10
selected: true
category: HCI and Computer Graphics
github: https://github.com/CohesiveAR/.github
giscus_comments: true
giscus_repo: CohesiveAR/.github
giscus_repo_id: R_kgDORjZPmw
giscus_category: General
giscus_category_id: DIC_kwDORjZPm84C94zW
giscus_mapping: pathname
# optional
giscus_dark_theme: dark
giscus_light_theme: light
giscus_input_position: bottom
giscus_reactions_enabled: 1
giscus_emit_metadata: 0
giscus_lang: en
---
Interactive design and modeling applications in Augmented Reality (AR)—such as interior design and next-generation mobile AR games—supply real-world graphical information to their users. We present "CohesiveAR", an AR mobile application for real-time texture extraction and application to virtual objects using the Google ARCore SDK. The application architecture is designed around three core modules: 

1. **Texture Extraction**: Captures real-world textures in real time utilizing a dedicated marker widget.
2. **Texture Processing & Storage**: Edits the extracted textures via the OpenCV library and loads them into a centralized texture database (DB).
3. **Texture Mapping & Modification**: Retrieves textures from the database, applies them onto a target virtual scene object, and modifies their UV mapping coordinates.

The virtual objects produced by this application appear visually cohesive and seamless, blending naturally with the surrounding physical environment.

Check out the demo video [here](https://www.youtube.com/watch?v=eUzmJmamqFk).

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT_lzRCA515SO4wR5ZAKa5cK2QtyCsiNDw8BvPrHqZ7xuwdv3e7UmxN8cuuGBgcg1I9oZvzWjSYXX-G/pubembed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

### Top-Level Architecture

<figure class="mt-3 mt-md-0 text-center w-50 mx-auto">
    {% include figure.liquid path="assets/img/1-top-level.png" title="Architecture Diagram" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 1: Top-level architecture with the Ingestion and Manipulation Pipelines</figcaption>
</figure>

At the highest level, the application initializes via a **Welcome Screen**, which serves as the primary gateway for user routing. From this point, a decision engine (**Choose pipeline**) branches the system execution into one of two decoupled subsystems based on the required operation:
* **The Asset Ingestion Pipeline (`Scan Textures`)**: Responsible for real-time visual capture and data processing.
* **The Object Modification Pipeline (`Manipulate Scene Object`)**: Responsible for spatial mapping and real-time interactive rendering.


### Asset Ingestion Pipeline (`Scan Textures`)

<figure class="mt-3 mt-md-0 text-center mx-auto" style="width: 70%;">
    {% include figure.liquid path="assets/img/1-scan.png" title="Architecture Diagram" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 2: The Asset Ingestion Pipeline</figcaption>
</figure>

The asset ingestion subsystem isolates, extracts, and normalizes physical surface textures for virtual deployment through three primary stages:

#### 1. Coordinate Mapping & Image Capture
* **Marker Localization**: The user places a digital bounding marker over the target physical surface.
* **Spatial Translation**: The system captures 3D world coordinates (`marker vertices in AR Scene`) and uses OpenCV to project them into 2D display space (`Screen Coordinates`).
* **Frame Ingestion**: The system captures raw pixel data directly from the display layer via a device screenshot.

#### 2. Geometric Normalization
* **Perspective Rectification**: A matrix transformation operator merges the screen coordinates with the raw screenshot.
* **Homography Transformation**: The system executes a **Perspective Warp** to remove camera tilt skew, flattening the targeted surface region into a standardized orthogonal texture square.

#### 3. Feedback & Refinement
* **Audio-Visual Notification**: An **Earcon + UI Animation** loop confirms successful texture extraction to the user.
* **Interface Transition**: The application initializes the **`OpenCV_Edit` Scene**, loading the unedited texture asset as a static reference object.
* **Asset Optimization**: The user adjusts surface properties (e.g., contrast, brightness) via the **OpenCV Image Correction Menu**.
* **Storage Commit**: The finalized, normalized asset is pushed directly to the central **Texture DB** for immediate mapping.


### Object Manipulation Pipeline (`Manipulate Scene Object`)

<figure class="mt-3 mt-md-0 text-center w-50 mx-auto">
    {% include figure.liquid path="assets/img/1-mani.PNG" title="Architecture Diagram" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 3: The Object Manipulation Pipeline</figcaption>
</figure>


This subsystem handles virtual object instantiation, spatial transformations, and dynamic texture binding within the AR workspace:

#### 1. Object Placement & Spatial Validation
* **Scene Presence Verification**: The system evaluates if a virtual asset is active (`Object present in Scene`).
* **Instantiation Loop**: If no object exists, the user chooses from a structural asset library to initialize a **3D object of peculiar geometry** in the AR environment.
* **Spatial Feedback**: Placement triggers an **Earcon + Animate** feedback loop to confirm successful spatial grounding.

#### 2. Asset Query & User Interface Routing
* **Object Selection**: Tapping an active virtual asset (`Tap on scene object`) initializes the texture mapping pipeline.
* **Dynamic Asset Fetching**: The application queries the centralized **Texture DB** to compile a list of user-generated textures.
* **Interactive Selector**: The system loads the **`Page_Swiper` UI**, enabling the user to navigate saved texture profiles via lateral swipe gestures (`SWIPE TO LEFT`).

#### 3. Dynamic Texture Binding & Transformation
* **Material Mapping Application**: Selecting an asset applies the chosen texture from the user-curated list onto the active 3D geometric mesh.
* **Transform Manipulation**: Post-application, the user can execute **Rotate and Scale** gesture mechanics to interactively adjust texture mapping parameters and alignment in real time.
