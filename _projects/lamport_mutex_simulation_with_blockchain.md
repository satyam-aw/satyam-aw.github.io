---
layout: page
title: Distributed Mutual Exclusion under Adversarial Networks
description: An investigation into distributed mutual exclusion within an adversarial network topology.
img: /assets/img/lamport_cover.jpg # Replace with a preview image if you have one
importance: 7
completed_on: UCSB, Winter 22 
category: Systems Engineering
related_publications: false
github: https://github.com/satyam-aw/lamport-blockchain-mutex
demo_video: https://www.youtube.com/watch?v=K6w52aim0ig
giscus_comments: true
giscus_repo: satyam-aw/lamport-blockchain-mutex
giscus_repo_id: R_kgDOGp_lRA
giscus_category: General
giscus_category_id: DIC_kwDOGp_lRM4C_hmd
giscus_mapping: pathname
# optional
giscus_dark_theme: dark
giscus_light_theme: light
giscus_input_position: bottom
giscus_reactions_enabled: 1
giscus_emit_metadata: 0
giscus_lang: en
---

## Abstract & Problem Statement

In distributed architectures lacking shared memory or a global physical clock, coordinating exclusive access to a non-replicated shared resource introduces fundamental concurrency challenges. This project provides an empirical validation of **Lamport's Distributed Mutual Exclusion Algorithm** within an adversarial network topology. 

### The Problem
The system models an untrusted, centralized ledger server hosting a non-replicated blockchain. Multiple independent client nodes concurrently attempt to compute balances or append state modifications to this centralized matrix. Without synchronous concurrency controls, simultaneous read/write actions precipitate race conditions, ledger corruption, and erratic financial data states.

### The Solution
While real-world public blockchains rely on probabilistic consensus models (e.g., Proof of Work) to resolve conflicts *post-facto*, this implementation applies a pessimistic locking strategy. By executing Lamport’s permission-based distributed framework, nodes establish a total ordering of events via logical timestamps. This guarantees that only a single verified client interacts with the blockchain master at any absolute interval, preserving absolute data consistency across all participants.

---

## Video Walkthrough

<div class="row justify-content-sm-center">
    <iframe width="600" height="375" src="https://www.youtube.com/embed/K6w52aim0ig?si=wo5vgtSwfF--F3cF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
<div class="caption">
    A live walk-through of the distributed synchronization execution space and telemetry dashboard..
</div>

---

## Architectural Protocol & Operational Flow

The execution cycle operates across three primary phases, governed entirely by peer-to-peer messaging and decoupled telemetry tracking.

<div class="row justify-content-center">
    <div class="col-md-10 mt-3 text-center">
        {% include figure.liquid path="assets/img/lamport_block_diagram.svg" title="Lamport Mutex Secured Banking Ledger" class="img-fluid rounded" %}
        <div class="caption mt-2">Figure 1: Distributed Banking Ledger via Lamport Mutual Exclusion.</div>
    </div>
</div>


### 1. The Distributed Locking Mechanism
When a client node initiates an action (either a balance query or a fund remittance), it cannot directly communicate with the blockchain master. Instead, it must successfully claim the system-wide distributed lock using a three-phase synchronization protocol:

* **The Request Phase:** The initiating node increments its local logical clock, appends its unique identifier, inserts this tuple `⟨Lamportclock, Processid⟩` into its sorted local request queue, and broadcasts a `REQUEST` packet to all registered peers.
* **The Reply Phase:** Peer nodes receive the incoming payload, process the logical timestamp to update their local clocks via $\max(L_{\text{local}}, L_{\text{incoming}}) + 1$, insert the request into their local queues, and immediately send back a timestamped `REPLY` confirmation.
* **The Critical Section Entry:** The initiating node safely establishes exclusive access to the blockchain master if and only if its own request sits at the **absolute top** of its local sorted queue, and it has collected a valid `REPLY` from every active peer in the network matrix.
* **The Release Phase:** Upon completing the ledger operations, the client clears its own item from its local queue and broadcasts a `RELEASE` packet. Peers extract this request from their queues, allowing the next sequential operation to advance to the top.

### 2. Stochastic Network Latency Simulation
To evaluate the protocol's resilience under realistic network conditions, the implementation introduces a randomized network transmission delay uniformly bounded between **0.1 and 1.0 seconds**. This stochastic injection accurately simulates the variable latencies, packet jitter, and out-of-order delivery characteristics inherent to a real physical network environment. 

By continuously shifting the arrival windows of competing messages, this variance deliberately stresses the local request queues and forces frequent clock-synchronization updates. It demonstrates that the system achieves absolute consensus and maintains ledger linearizability despite unpredictable network conditions.

---

## Hybrid Networking & Web Interface Architecture

To ensure precise runtime monitoring without degrading the underlying synchronous execution loop, the framework enforces a strict decoupling between the web layer and the core consensus layer.

### Asynchronous Telemetry Layer (`app.py`)
The system isolates the presentation tier by implementing an event-driven gateway driven by **Flask-SocketIO** running over non-blocking HTTP and WebSocket pipelines. This gateway acts as a proxy:
* It intercepts transactional events from the HTML5 front-end dashboard and serializes them as JSON payloads before passing them to the target compute nodes over native TCP sockets.
* It handles inbound logging strings, state mutations, and current node balances, rendering them in real time to the browser log without triggering blocking page reloads or interrupting the background networking loops.

### Synchronous Core Layers
* **The Blockchain Master Layer:** A standalone TCP daemon managing the centralized blockchain ledger. Each block structurally locks a single transaction `<Sender, Receiver, Amount>` utilizing linear cryptographic chaining through `SHA-256` hashing pointers. Balance calculations are performed on-demand via an $O(N)$ linear traversal of the chain to ensure absolute traceability.
* **The Edge Compute Nodes:** Independent local processes executing the core algorithmic logic. Every node initializes with a baseline virtual asset distribution of **\$10** and manages its individual network socket pipeline to process concurrent validation tasks.
