---
layout: page
title: Dual-Stage Agent Pipelines for Generative UI
description: Designing robust dual-stage agent architectures and generative UI layouts for large-scale data systems.
img: assets/img/gen_ui2.jpg
importance: 1
category: "Sequential Decision Models, Generative AI, and Applied ML"
---


## Overview

User interface (UI) development is moving rapidly toward **highly personalized interfaces customized for each individual user**. Instead of showing everyone the same static screens, modern apps use AI to build custom layouts on the fly based on what a user needs at that exact moment. 

    {% include figure.liquid path="assets/img/gen_ui.jpg" title="Architecture Diagram" class="img-fluid rounded" %}

However, letting AI automatically build interfaces introduces two major technical problems:
1. **AI Hallucinations**: The model often invents fake UI buttons or broken components that do not exist.
2. **Context Loss**: The AI frequently forgets what the user was doing earlier in the conversation.

If the AI makes a single text error or forgets the user's current situation, it sends broken code to the app, causing the mobile screen to crash. 


At Intuit, I researched and engineered a reliable **dual-stage agent pipeline** to completely solve these issues. This system separates the step of finding the user's true intent from the step of building the actual UI layout. By splitting these tasks, the framework forces unpredictable AI models to follow strict software design rules, ensuring that every dynamically generated screen is completely error-free and stable.

## Project Architecture & Tooling

<div class="row mt-3 backend-pipeline">
    <!-- Item 1 -->
    <div class="col-12 mb-3 pipeline-block">
        <div class="pl-3 border-left-theme">
            <h6 class="font-weight-bold tracking-wide mb-1">
                <i class="fa-solid fa-code-branch mr-2 theme-color-text"></i>OpenAI API (Structured Outputs)
            </h6>
            <div class="mb-2">
                <small class="text-uppercase text-muted font-weight-semi-bold tracking-wider">
                    Core System Function: Constraint Enforcement & Syntactic Compilation
                </small>
            </div>
            <p class="card-text text-justify text-muted small-body">In a generative UI environment, standard text generations are highly prone to formatting anomalies that crash frontend codebases. I utilized the OpenAI Structured Outputs API as a rigid grammatical compiler. This tool intercepts the raw capabilities of the language model and forces its generation into absolute compliance with our schema parameters, acting as a structural guarantee that no malformed data reaches the client device.</p>
        </div>
    </div>
    
    <!-- Item 2 -->
    <div class="col-12 mb-3 pipeline-block">
        <div class="pl-3 border-left-theme">
            <h6 class="font-weight-bold tracking-wide mb-1">
                <i class="fa-solid fa-shapes mr-2 theme-color-text"></i>Pydantic / JSON Schema Calibration
            </h6>
            <div class="mb-2">
                <small class="text-uppercase text-muted font-weight-semi-bold tracking-wider">
                    Core System Function: Finite State Canvas Definition & Parameter Validation
                </small>
            </div>
            <p class="card-text text-justify text-muted small-body">To map user desires to an actual interface, the application space must be treated as a strict geometric canvas with clear operational rules. I implemented Pydantic and JSON Schema to explicitly outline our system's valid state profiles and allowed layout parameters. This validation layer defines the exact attributes each layout requires, providing a mathematically sound frame for slot-filling algorithms to complete without risking context degradation.</p>
        </div>
    </div>

    <!-- Item 3 -->
    <div class="col-12 mb-3 pipeline-block">
        <div class="pl-3 border-left-theme">
            <h6 class="font-weight-bold tracking-wide mb-1">
                <i class="fa-solid fa-route mr-2 theme-color-text"></i>LangChain
            </h6>
            <div class="mb-2">
                <small class="text-uppercase text-muted font-weight-semi-bold tracking-wider">
                    Core System Function: Goal-Directed Tool Routing & Intent Classification
                </small>
            </div>
            <p class="card-text text-justify text-muted small-body">Autonomous agents must be able to make logical decisions based on fluctuating, unstructured environmental signals. I configured LangChain to manage the system's core decision policy. This orchestration layer parses incoming streaming requests and matches them dynamically against our strict tool definitions. It functions as the brain of Stage 1, accurately determining what the user intends to achieve and updating the internal state vectors accordingly.</p>
        </div>
    </div>

    <!-- Item 4 -->
    <div class="col-12 mb-3 pipeline-block">
        <div class="pl-3 border-left-theme">
            <h6 class="font-weight-bold tracking-wide mb-1">
                <i class="fa-solid fa-database mr-2 theme-color-text"></i>Milvus Vector Database
            </h6>
            <div class="mb-2">
                <small class="text-uppercase text-muted font-weight-semi-bold tracking-wider">
                    Core System Function: State-Conditioned Fragment Retrieval (RAG)
                </small>
            </div>
            <p class="card-text text-justify text-muted small-body">Because an LLM cannot memorize an entire enterprise design library within its standard context window, a retrieval mechanism is necessary. I built a Retrieval-Augmented Generation (RAG) pipeline powered by a Milvus Vector Database. This infrastructure stores the high-dimensional vector embeddings of code templates, visual primitives, and token designs, allowing the system to rapidly look up and fetch the exact structural pieces needed for any verified user state.</p>
        </div>
    </div>
</div>

## Pipeline Architecture

```text
[User Input] ──► [STAGE 1: LangChain Backend + Structured LLM]
                       │ (Intent Classification & State Tracking)
                       │
                       ├──► [Confidence < Threshold] ──► [Short-Circuit / Clarification]
                       │
                       └──► [Confidence ≥ Threshold]
                                  │ (State Vector + Intent Schema)
                                  ▼
                    [STAGE 2: Generative Spatial UI Engine]
                                  │
                                  ├──► [RAG Vector DB] ──► (Fetch UI Primitives)
                                  │                              │
                                  ▼                              ▼
                    [Structured LLM Parser] ◄────────────────────┘
                                  │
                                  └──► [Deterministic JSON Layout Schema] ──► [Web/Mobile UI Render]
```

## Detailed Architectural Breakdown

### Stage 1: Autonomous Intent Routing & State Tracking
The initial phase of the pipeline focuses on stabilizing the incoming data. The system ingests messy, heterogeneous inputs from various operational data streams and directs them to a structured LLM bounded by strict tool-schema limits.

* **Goal-Directed Policy Execution**: Instead of allowing the language model to chat freely, the system immediately binds raw user inputs to explicit functional pathways, classifying the goal of the prompt into a discrete state.
  * *Example*: A messy input like *"hey i just moved to california and need to figure out my state deductions"* is intercepted by the **LangChain framework** and mapped precisely to a discrete `tax_withholding_calculator` intent, rather than triggering a generic, conversational text response.
* **Dynamic Frame Slot-Filling**: Once a target intent is locked in by the routing engine, the backend initializes a matching template schema. The LLM is prompted to inspect the user's ongoing interaction history, isolate the required values, and fill in the open slots to build a reliable operational baseline.
  * *Example*: The backend loads a blank schema requiring `[state: string, user_tier: string, filing_status: string]`. The structured LLM extracts data points from the user's account history buffer and populates the slots:
    ```json
    {
      "intent": "tax_withholding_calculator",
      "slots": { "state": "CA", "user_tier": "Premium", "filing_status": "Single" }
    }
    ```
* **Conditional Early Exit Strategy**: To manage server overhead and eliminate downstream chaos, the system incorporates a conditional threshold gate. If Stage 1 cannot identify user intent with high confidence, it completely short-circuits the execution loop. The pipeline remains inside Stage 1 to trigger clarification dialogs, ensuring the system never runs costly downstream generation algorithms on unverified or garbage data.
  * *Example*: If a user submits an ambiguous query like *"make it look blue"*, the classifier yields a low confidence score of `0.23`. LangChain catches this score, flags it as below the operational `0.80` threshold, and skips Stage 2 entirely. It returns a structured clarification prompt asking: *"Would you like to change your app theme settings, or view your expense charts?"*

---

### Stage 2: Generative Spatial Interface Engine
Once the user's intent and parameters are successfully validated by Stage 1, the pipeline moves forward to resolve the spatial configuration. It must find the optimal way to display this information within a bounded screen.

* **State-Conditioned Retrieval (RAG)**: The pipeline takes the verified state vector from Stage 1—including user context variables like filing status and required parameters—and queries a **Milvus Vector Database**. It performs a semantic search to pull canonical blueprints, allowed component restrictions, and required parameter definitions matching that precise state profile.
  * *Example*: Using the state vector `[intent: tax_calculator, filing_status: Single]`, the RAG engine queries the design repository and returns raw text component documentation. It states that a `SingleFilerTaxCard` must be used, which strictly requires a `state_tax` attribute and allows a `PremiumGraph` component inside its visual block.
* **Constraint Satisfaction & Error Correction**: A structured LLM parser ingests the combined prompt payload, which includes both the dynamic state vectors from Stage 1 and the unconstrained, potentially noisy raw component documentation returned by the RAG search. This layer acts as a strict compiler, mapping runtime values into the structural parameters while filtering out layout anomalies.
  * *Example*: The LLM receives the state values `[state: CA, filing_status: Single]` alongside the retrieved primitive rule stating that a `SingleFilerTaxCard` requires a `state_tax` property. If the raw text returned by the RAG layer accidentally includes a legacy typo or an invalid attribute name like `"provincial_tax"`, the structured LLM intercepts and corrects it to match valid design standards.
* **Deterministic Layout Synthesis**: The structured LLM injects runtime parameters into the verified building blocks. Bound by a strict JSON layout schema, it outputs a clean, syntactically guaranteed configuration file that the web or mobile client can instantly render without experiencing layout errors or interface bugs.
  * *Example*: The final output compiled by the structured LLM maps the values directly into the corrected layout structural constraints, producing a production-ready payload parsed natively by the frontend framework:
    ```json
    {
      "ui_canvas": "split_pane",
      "components": [
        { 
          "type": "SingleFilerTaxCard", 
          "properties": { "state_tax": "CA", "filing_status": "Single" }
        },
        { "type": "PremiumGraph", "theme": "ca_tax_palette" }
      ]
    }
    ```

## Key Research Implications

1. **Fault-Tolerant Error Mitigation**: By anchoring conversational outputs to a strict JSON validation layout, this setup removes visual layout bugs and interface crashes caused by free-form text generations.
2. **Resource-Conscious Optimization**: The design of the conditional early-exit gate protects centralized server resources, ensuring that heavy embedding lookups and layout generation steps only occur for valid, confident states.
3. **Deterministic State Automation**: This framework serves as a practical blueprint for modern artificial intelligence, demonstrating how unpredictable, probabilistic neural network outputs can be successfully constrained using classical Finite State Machines (FSM) to build reliable software solutions.
