---
layout: page
title: projects
seo_title: "Research Projects | Satyam Awasthi"
permalink: /projects/
description: Research spanning physiological signal acquisition, intent decoding, and estimation and control for reliable closed-loop brain–computer interfaces.
nav: true
nav_order: 3
display_categories: ["Neural Interfaces & Biosignals", "Safe & Intelligent Control", "Human Sensing & Interaction", "Selected Engineering Projects"]
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="carousel-wrapper" data-project-carousel data-category="{{ category | escape }}">
    <button type="button" aria-label="Previous projects" class="carousel-btn prev-btn" data-direction="-1">
      <i class="fa-solid fa-chevron-left"></i>
    </button>
    <div id="carousel-{{ category | slugify }}" class="project-carousel carousel-container" tabindex="0" aria-label="{{ category | escape }} projects" data-count="{{ sorted_projects.size }}">
      {% for project in sorted_projects %}
        <div class="carousel-card-item" data-pinned="{% if project.pinned %}true{% else %}false{% endif %}">
          {% include projects.liquid %}
        </div>
      {% endfor %}
    </div>
    <button type="button" aria-label="Next projects" class="carousel-btn next-btn" data-direction="1">
      <i class="fa-solid fa-chevron-right"></i>
    </button>
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3 g-4">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>

<script defer src="{{ '/assets/js/project-carousel.js' | relative_url | bust_file_cache }}"></script>
