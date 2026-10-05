---
layout: page
permalink: /publications/
title: publications
seo_title: "Publications | Satyam Awasthi"
description: Research publications by Satyam Awasthi on physiological sensing, eye tracking in mixed reality, and human–computer interaction.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography --query @*[hidden!=true]* %}

</div>
