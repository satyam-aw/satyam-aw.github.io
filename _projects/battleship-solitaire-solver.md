---
layout: page
title: Battleship Solitaire Solver
description: Solver-aided constraint synthesis for Battleship Solitaire using Rosette/Racket, symbolic variables, and angelic execution.
img: assets/img/projects/battleship-solitaire/battleship-solver-overview.jpg
importance: 6
category: Systems Engineering
related_publications: false
project_pdf: /assets/pdf/battleship-solitaire-rosette-report.pdf
selected: true
github: https://github.com/satyam-aw/Battleship-Solitaire-Solver
giscus_comments: true
giscus_repo: satyam-aw/Battleship-Solitaire-Solver
giscus_repo_id: R_kgDOHZcSaA
giscus_category: General
giscus_category_id: DIC_kwDOHZcSaM4C9r7Q
giscus_mapping: pathname
# optional
giscus_dark_theme: dark
giscus_light_theme: light
giscus_input_position: bottom
giscus_reactions_enabled: 1
giscus_emit_metadata: 0
giscus_lang: en
---

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid loading="eager" path="assets/img/projects/battleship-solitaire/battleship-solver-overview.jpg" title="Battleship Solitaire solver pipeline" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Solver-aided pipeline: parse puzzle clues, initialize symbolic board variables, assert Battleship constraints, and synthesize a satisfying board assignment with Rosette/Z3.
</div>

**Code:** [GitHub](https://github.com/SatyamA007/CS292C-Battleship) &nbsp;|&nbsp;
**Report:** [PDF]({{ '/assets/pdf/battleship-solitaire-rosette-report.pdf' | relative_url }}) &nbsp;|&nbsp;
**Stack:** Rosette, Racket, Z3, symbolic execution, constraint solving

## Overview

Battleship Solitaire is a logic puzzle in which a hidden fleet must be reconstructed from row and column tallies, fleet-composition rules, and a small set of initially revealed cells. I formulated the puzzle as a **constraint-satisfaction problem (CSP)** and implemented a solver-aided synthesis pipeline in **Rosette/Racket**. The solver represents board cells and ship placements symbolically, encodes puzzle rules as assertions, and uses Rosette's angelic execution to search for a concrete assignment that satisfies all constraints.

The project also includes a puzzle generator and an evaluation of how solving time changes with grid size, fleet area, and packing fraction.

## Problem Formulation

A valid Battleship Solitaire solution must satisfy four core constraints:

- **Fleet composition:** all ships in the requested fleet must be placed on the board.
- **Initial clues:** any revealed water or ship cells must be preserved in the final solution.
- **Non-adjacency:** ships cannot overlap or touch each other, including diagonally.
- **Row/column tallies:** the number of occupied cells in each row and column must match the puzzle clues.

Each grid cell is represented as a symbolic variable `s_ij`, where `1` denotes a ship segment and `0` denotes water. A valid solution is a satisfying assignment over these symbolic variables and the symbolic ship placements.

## Approach

The system is organized around two modules: a **generator** and a **solution synthesizer**.

1. **Generate or load a puzzle.**  
   The generator randomly places ships on an `m x n` board while enforcing boundary and non-overlap constraints. The solver can also read human-readable puzzle files.

2. **Parse puzzle constraints.**  
   The parser extracts row sums, column sums, initial clues, grid dimensions, and fleet specification from a puzzle file.

3. **Initialize symbolic state.**  
   The solver constructs a symbolic puzzle object containing symbolic board cells and symbolic ship placements. Initially revealed cells are concretized through assertions.

4. **Assert global constraints.**  
   The solver encodes isolated-neighborhood constraints, row-sum constraints, column-sum constraints, ship-size constraints, and revealed-cell constraints as Rosette assertions.

5. **Synthesize a solution.**  
   Rosette's `solve` query searches for a model that satisfies all accumulated assumptions and assertions. If the query is satisfiable, the symbolic puzzle is evaluated under the returned model to produce a concrete board solution.

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/battleship-solitaire/battleship-synthesis-workflow.jpg" title="Course of action for the synthesis algorithm" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  The synthesis workflow parses puzzle inputs, applies clue and tally constraints, invokes Rosette/Z3, and prints a concrete solution. Different valid solutions may exist for the same puzzle instance.
</div>

## Results

I evaluated the solver across easy, medium, and hard puzzle instances. Average solving time increased sharply with puzzle difficulty:

| Difficulty | Grid Size Range | Average Time |
| --- | ---: | ---: |
| Easy | `N < 10` | 8.04 s |
| Medium | `10 <= N <= 13` | 44.41 s |
| Hard | `N > 13` | 517.59 s |

The evaluation suggests that puzzle difficulty is influenced by both the number of symbolic constants, which grows with grid size, and the fleet's packing fraction. Larger grids increase the symbolic search space, while packing fraction affects how constrained the board is and how many feasible placements remain.

<div class="row justify-content-sm-center">
  <div class="col-sm-6 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/battleship-solitaire/difficulty-vs-grid-size.png" title="Solving time versus grid size" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-6 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/battleship-solitaire/difficulty-vs-packing-fraction.png" title="Solving time versus packing fraction" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Runtime trends from the project report: solving time generally increases with symbolic problem size, while packing fraction helps explain local variations in perceived difficulty.
</div>

## Technical Highlights

- Modeled a structured logic puzzle as a symbolic constraint-satisfaction problem.
- Encoded row/column tallies, fleet composition, adjacency, and initial-clue constraints as formal assertions.
- Used Rosette's solver-aided execution to synthesize concrete board assignments from symbolic variables.
- Built a parser and puzzle generator to support multiple puzzle sizes and difficulty levels.
- Evaluated solver runtime across grid sizes, fleet configurations, and packing fractions.

## Reflection

Although Battleship Solitaire is a puzzle domain rather than a robotics domain, the project strengthened my foundation in **constraint formulation**, **symbolic reasoning**, and **optimization-style problem solving**. These ideas are closely related to how autonomy systems formulate feasibility constraints, search over structured decision spaces, and use solvers inside planning or control pipelines.
