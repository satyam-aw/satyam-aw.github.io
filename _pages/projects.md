---
layout: page
title: projects
permalink: /projects/
description: A growing collection of cool projects.
nav: true
nav_order: 3
display_categories: ["Sequential Decision Models, Generative AI, and Applied ML", HCI and Computer Graphics, Embedded Systems and Robotics, Distributed Systems]
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
  <!-- Wrap the carousel with a container that holds the buttons -->
  <div class="carousel-wrapper">
    <button class="carousel-btn prev-btn" onclick="scrollCarousel('{{ category | slugify }}', -1)">
      <i class="fa-solid fa-chevron-left"></i>
    </button>
    <!-- Added data-count attribute to pass the number of items -->
    <div id="carousel-{{ category | slugify }}" class="project-carousel carousel-container" data-count="{{ sorted_projects.size }}">
      {% for project in sorted_projects %}
        <div class="carousel-card-item">
          {% include projects.liquid %}
        </div>
      {% endfor %}
    </div>
    <button class="carousel-btn next-btn" onclick="scrollCarousel('{{ category | slugify }}', 1)">
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

<script>
// Function to handle clicking the buttons
function scrollCarousel(categorySlug, direction) {
  const carousel = document.getElementById(`carousel-${categorySlug}`);
  if (!carousel) return;
  
  // One card width + gap (340px + 24px)
  const scrollAmount = 364; 
  
  carousel.scrollBy({
    left: direction * scrollAmount,
    behavior: 'smooth'
  });
}

// Function to hide navigation buttons if items are less than 3
document.addEventListener("DOMContentLoaded", function() {
  const carousels = document.querySelectorAll('.carousel-container');
  
  carousels.forEach(carousel => {
    const itemCount = parseInt(carousel.getAttribute('data-count'), 10) || 0;
    
    // If there are less than 3 items, hide the sibling buttons
    if (itemCount < 3) {
      const wrapper = carousel.closest('.carousel-wrapper');
      if (wrapper) {
        const buttons = wrapper.querySelectorAll('.carousel-btn');
        buttons.forEach(btn => btn.style.display = 'none');
      }
    }
  });
});
</script>
