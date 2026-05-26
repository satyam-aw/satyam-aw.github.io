---
layout: page
title: Tweeter 
description: A Twitter-like micro blogging social media app for load testing and bottleneck analysis
completed_on: UCSB, F21
img: assets/img/8.webp
importance: 2
category: Software Engineering
project_pdf: https://docs.google.com/document/d/1oxVZuh_Wj5Tc_Jv-8qsjNRmkKm0Kov0G5AQeYhBpz3M/edit?usp=sharing
github: https://github.com/satyam-aw/Tweeters
giscus_comments: true
giscus_repo: satyam-aw/Tweeters
giscus_repo_id: R_kgDOGwhrMQ
giscus_category: General
giscus_category_id: DIC_kwDOGwhrMc4C9r7c
giscus_mapping: pathname
# optional
giscus_dark_theme: dark
giscus_light_theme: light
giscus_input_position: bottom
giscus_reactions_enabled: 1
giscus_emit_metadata: 0
giscus_lang: en
---

The Tweeters App is a social media app which allows users to create profiles, follow other users, create posts, comment, and like on posts as well as to message other users. We built the frontend using the Ruby-on-Rails built-in templating engine to keep the focus on creating a scalable application capable of handling high-traffic conditions. While unregistered guests can view all posts and comments, the creation of posts, comments, likes, and messages is restricted to registered users.

You may view the source code at the [GitHub repository (archived)](https://github.com/scalableinternetservicesarchive/Tweeters) or my [fork](https://github.com/satyam-aw/Tweeters).

<div class="d-flex justify-content-center">
  <iframe width="600" height="375" src="https://www.youtube.com/embed/7h5pKCCxcLs?si=Hc8tH9fNg6p7OCwm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

<br><br>
<h3>User Flows Implemented</h3>
The initial task for the first-time user is to register his profile details into the application. If the user does not register the functionality will be limited for that session. 
<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/8_workflows.PNG" title="example image" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 1: All the possible user flows for the Tweeters App</figcaption>
</figure>

<h3>Data Model</h3>
We have created an entity-relationship based data model to facilitate the business logic of the application. 
<figure class="mt-3 mt-md-0 text-center">
    {% include figure.liquid path="assets/img/8_data_model.jpg" title="example image" class="img-fluid rounded" %}
  <figcaption class="caption">Figure 2: Entity relationship Model for Tweeters</figcaption>
</figure>

### Load Testing Using Tsung

[Tsung](https://erlang-projects.org) is an open-source load-testing tool designed to help developers identify bottleneck workflows within web applications. It simulates user actions at precisely defined rates.

We performed a bottleneck analysis to test optimizations aimed at improving performance. Performance was measured using two primary metrics:
* **Requests served per minute**
* **Mean duration between requests**

The testing environment consisted of servers deployed on Amazon EC2 instances.

##### Test Workflow: Browsing the Homepage
We first tested the workflow of an authenticated user viewing tweets on the homepage. This scenario involves three sequential steps:
1. **Log in:** The authenticated user visits the "view all tweets" page.
2. **Think time:** The user waits one second to simulate browsing content.
3. **Log out:** The user logs out of the application.

##### Tsung Load Configuration
The load testing strategy exponentially increments the number of users added each second across consecutive phases:

* **Phase 1:** 1 user/sec
* **Phase 2:** 2 users/sec
* **Phase 3:** 4 users/sec
* *...and so on...*
* **Phase 9:** 256 users/sec
* **Phase 10:** 512 users/sec


Please refer the [project report](https://docs.google.com/document/d/1oxVZuh_Wj5Tc_Jv-8qsjNRmkKm0Kov0G5AQeYhBpz3M/edit?usp=sharing) to see our complete findings for a comprehensive suite of workflows and optimizations. Below are the results associated with only the above workflow and pagination optimization.

<div class="row justify-content-sm-center">
    <div class="mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/8_results.PNG" title="example image" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Figure 3: Pagination optimization results for the `tweet-viewing` workflow
</div>

