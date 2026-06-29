---
layout: page
title: CohesiveAR
description: Augmented Reality Pipeline for Texture Extraction and Homography Mapping
img: assets/img/1.png
images: 
  - assets/img/1.png
  - assets/img/1_holo.png
  - assets/img/1_ladder.png
download_link: https://drive.google.com/file/d/1JFnizZqqHfdgrDATeiZgwWax0WHh_LOp/view?usp=sharing
completed_on: UCSB, Fall 22
demo_video: https://www.youtube.com/watch?v=eUzmJmamqFk
importance: 6
selected: true
category: Spatial Perception
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
Interactive spatial AI applications in Augmented Reality (AR) require highly accurate real-world geometric modeling to achieve realistic contextual blending. We present **"CohesiveAR"**, a spatial computing framework designed for real-time, viewpoint-invariant texture extraction and dynamic mapping onto target virtual surfaces using the Google ARCore SDK and OpenCV. 

The architecture coordinates three core geometric modules:
1. **Surface Localization & Extraction**: Detects and captures real-world surface textures from variable viewpoints utilizing a bounded tracking widget.
2. **Geometric Homography & Processing**: Normalizes perspective warp via OpenCV to generate standardized, orthogonal texture maps stored in a centralized asset database.
3. **Dynamic Coordinate Mapping**: Retrieves processed textures, projects them onto target virtual meshes, and computes dynamic UV coordinate adjustments.

The virtual assets produced by this pipeline appear visually cohesive and seamless, blending naturally with the surrounding physical environment's illumination and structure.

Check out the demo video [here](https://youtu.be/eUzmJmamqFk?si=eJcXW2aYxK9W3143).

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT_lzRCA515SO4wR5ZAKa5cK2QtyCsiNDw8BvPrHqZ7xuwdv3e7UmxN8cuuGBgcg1I9oZvzWjSYXX-G/pubembed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

### Top-Level Architecture

<figure class="mt-3 mt-md-0 text-center w-50 mx-auto">
    {% include figure.liquid path="assets/img/1-top-level.png" title="Architecture Diagram" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 1: Top-level architecture highlighting the Spatial Ingestion and Mesh Manipulation Pipelines</figcaption>
</figure>

At the highest level, the framework initializes via a unified tracking portal. From this point, a decision engine branches system execution into one of two decoupled subsystems based on the required operation:
* **The Spatial Ingestion Pipeline (`Scan Textures`)**: Responsible for real-time visual tracking, geometric normalization, and matrix transformations.
* **The Mesh Manipulation Pipeline (`Manipulate Scene Object`)**: Responsible for virtual coordinate alignment, spatial grounding, and real-time interactive mapping.


### Spatial Ingestion & Rectification Pipeline (`Scan Textures`)

<figure class="mt-3 mt-md-0 text-center mx-auto" style="width: 70%;">
    {% include figure.liquid path="assets/img/1-scan.png" title="Architecture Diagram" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 2: The Spatial Ingestion and Geometric Rectification Pipeline</figcaption>
</figure>

The spatial ingestion subsystem isolates, extracts, and normalizes physical surface textures for virtual deployment through three primary stages:

#### 1. Coordinate Mapping & Image Capture
* **Marker Localization**: The user places a digital bounding anchor over the target physical surface.
* **Spatial Translation**: The system tracks 3D world coordinates (`marker vertices in AR Scene`) and projects them into 2D image coordinates using pinhole camera model principles.
* **Frame Ingestion**: Raw pixel arrays are ingested directly from the live camera frame buffer.

#### 2. Geometric Normalization
* **Perspective Rectification**: A homography transformation matrix maps the skewed image coordinates back to a canonical reference plane.
* **Homography Transformation**: The system executes a linear perspective warp operator to completely remove camera tilt skew, flattening the targeted surface region into a standardized orthogonal texture square.

#### 3. Feedback & Refinement
* **Audio-Visual Notification**: An Earcon + UI animation loop confirms successful texture extraction and bounding validation.
* **Interface Transition**: The application initializes the editing workspace, loading the unedited texture asset as a static reference object matrix.
* **Asset Optimization**: The user adjust surface properties (e.g., contrast, brightness) using localized image correction matrices.
* **Storage Commit**: The finalized, normalized asset matrix is pushed directly to the central database for immediate projection.


### Object Instantiation & Mesh Manipulation Pipeline (`Manipulate Scene Object`)

<figure class="mt-3 mt-md-0 text-center w-50 mx-auto">
    {% include figure.liquid path="assets/img/1-mani.png" title="Architecture Diagram" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 3: The Mesh Manipulation and Coordinate Binding Pipeline</figcaption>
</figure>

This subsystem handles virtual asset instantiation, spatial transformations, and dynamic material tracking within the AR workspace:

#### 1. Object Placement & Spatial Validation
* **Scene Presence Verification**: The system evaluates whether a target virtual asset is active within the current spatial scene.
* **Instantiation Loop**: If no object exists, the user selects from a structural geometry library to initialize an arbitrary 3D geometric mesh into the tracking environment.
* **Spatial Feedback**: Asset placement triggers a closed-loop audio-visual confirmation to verify robust spatial grounding.

#### 2. Asset Query & User Interface Routing
* **Object Selection**: Selecting an active virtual asset mesh initializes the runtime texture mapping pipeline.
* **Dynamic Asset Fetching**: The application queries the centralized database to compile and index user-generated textures.
* **Interactive Selector**: The system loads the asset navigation interface, enabling seamless iteration through saved surface texture matrices.

#### 3. Dynamic Texture Binding & Transformation
* **Material Mapping Application**: Selecting an asset applies the chosen texture matrix directly onto the active 3D geometric mesh layout.
* **Transform Manipulation**: Post-application, the user can execute rotation and scaling gesture mechanics to interactively adjust transformation parameters, modifying texture orientation and spatial alignment in real time.
