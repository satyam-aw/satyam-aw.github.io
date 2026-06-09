---
layout: page
title: Tweeter
description: A Distributed Testbed for Stress-Testing and Bottleneck Optimization
completed_on: UCSB, Fall 21
img: assets/img/8.webp
importance: 2
category: Systems Research & Performance Engineering
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

## Project Overview

When engineering large-scale internet applications, high-concurrency traffic conditions inevitably expose hidden hardware and database limitations. This project introduces a containerized, distributed testbed modeled after a microblogging platform. It was engineered specifically to run high-throughput stress tests, monitor real-time system degradation, and systematically analyze infrastructure bottlenecks. 

Rather than focusing on frontend complexity, the application leverages a lightweight server layout to keep the computational focus entirely on optimizing backend database routing, horizontal scaling strategies, and memory performance under heavy concurrent workloads.

You may view the source code at the [GitHub repository (archived)](https://github.com/scalableinternetservicesarchive/Tweeters) or my [fork](https://github.com/satyam-aw/Tweeters).

<div class="d-flex justify-content-center my-4">
  <iframe width="600" height="375" src="https://www.youtube.com/embed/7h5pKCCxcLs?si=Hc8tH9fNg6p7OCwm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

## Experimental State Machine & Workflows

To accurately simulate complex production traffic, the testbed maps real-world user paths into structured, concurrent state machines. This design allows the framework to inject diverse reading and writing behaviors simultaneously, exposing lock contentions and query execution delays.

<div class="row justify-content-center">
    <div class="col-md-10 mt-3 text-center">
        {% include figure.liquid path="assets/img/8_workflows.jpg" title="Concurrent State Workflows" class="img-fluid rounded" %}
        <div class="caption mt-2">Figure 1: State transition paths utilized during distributed load testing.</div>
    </div>
</div>

---

## Relational Data Modeling

The system architecture utilizes an optimized entity-relationship schema designed to support relational business logic while undergoing rapid write cycles. This setup serves as the primary benchmark canvas to test how indexing, connection pooling, and nested data schemas behave when memory resources approach capacity.

<div class="row justify-content-center">
    <div class="col-md-10 mt-3 text-center">
        {% include figure.liquid path="assets/img/8_data_model.jpg" zoomable=true avoid_scaling=true title="Entity Relationship Model" class="img-fluid rounded" %}
        <div class="caption mt-2">Figure 2: Optimized data schema for relational stress-test analysis.</div>
    </div>
</div>

---

## Distributed Load Testing with Tsung

To stress-test the environment and identify system constraints, we deployed [Tsung](https://erlang-projects.org)—an open-source, XML-configured XML load-testing tool. Tsung allows developers to simulate mass user trajectories at precise, exponentially accelerating interaction intervals.

The experimental testing environment consisted of server clusters deployed across distributed **Amazon EC2 instances**. Optimization efficiency was evaluated using two core telemetry metrics:
* **Throughput Capacity**: Total requests successfully served per minute.
* **Response Latency**: The mean duration and distribution bounds between consecutive requests.

### Baseline Benchmark Scenario: Homepage Traversal
One of our primary benchmark evaluations focused on an intensive read/write workflow where authenticated sessions navigate active data feeds. The scenario enforces three sequential stages:
1. **State Ingestion (Log in)**: The session authenticates and immediately queries the global content feed.
2. **Simulated Delays (Think time)**: The session forces a one-second pause to simulate realistic content consumption patterns.
3. **State Termination (Log out)**: The session closes, clearing connection allocations.

### Multi-Phase Exponential Scale Configuration
The testing infrastructure increases concurrency systematically across consecutive execution phases to force the system past its operational thresholds:
* **Phase 1 to 3**: Baseline testing scaling from 1 to 4 users/second.
* **Phase 4 to 8**: Mid-tier stress scaling from 8 to 128 users/second.
* **Phase 9 & 10 (Peak Concurrency)**: Extreme stress scaling rapidly from 256 to **512 users/second**.

---

## Performance Telemetry & Optimization Results

Please refer to the comprehensive [project report](https://docs.google.com/document/d/1oxVZuh_Wj5Tc_Jv-8qsjNRmkKm0Kov0G5AQeYhBpz3M/edit?usp=sharing) to inspect the complete findings, including N+1 query optimization, caching, and indexing. Below are the specific results evaluating system throughput improvements after implementing pagination rules for the homepage workflow.

<div class="row justify-content-center">
    <div class="col-md-10 mt-3 text-center">
        {% include figure.liquid path="assets/img/8_results.png" zoomable=true avoid_scaling=true title="Pagination Optimization Telemetry" class="img-fluid rounded" %}
        <div class="caption mt-2">Figure 3: System throughput comparison between unoptimized query rendering and the pagination framework under peak concurrency.</div>
    </div>
</div>
