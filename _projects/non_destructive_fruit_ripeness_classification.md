---
layout: page
title: Non-Destructive Fruit Ripeness Classification
description: Utilizing IR thermal signatures and supervised machine learning classifiers to determine berry ripeness states.
completed_on: IIT-KGP, May '18
img: /assets/img/4_ripeness_classifier.png
importance: 4
category: "Sequential Decision Models, Generative AI, and Applied ML"
project_pdf: /assets/pdf/4_fruits.pdf # you can also use external links here
---

#### Overview

This project presents non-destructive methodologies to determine the ripeness state of local berries by training and benchmarking five supervised machine learning models: **Decision Tree**, **Quadratic Discriminant Analysis (QDA)**, **Support Vector Machine (SVM)**, **Ensemble Learning**, and **$k$-Nearest Neighbors ($k$-NN)**. Infrared (IR) thermal profiles of freshly harvested specimens were captured across distinct maturity stages. Geometrical feature extraction routines were then executed to map the average temperature and relative surface area of the higher-temperature inner cores, serving as the primary predictor metrics for classifier training.

---

#### Methodology & Feature Extraction

The berries were freshly plucked from trees within the institute campus at the Indian Institute of Technology, Kharagpur. Infrared (IR) thermal images were captured using a commercial IR camera featuring a temperature resolution of $0.1\text{ K}$.

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_ir.png" title="Raw IR signature" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_processed.png" title="Segmented thermal core" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <strong>Figure 1:</strong> Pre-processing and core segmentation pipeline. <em>Left:</em> Corresponding IR spectrum thermal signature captured at a temperature resolution of $0.1\text{ K}$. <em>Right:</em> Segmented thermal mask revealing the internal core signature; unripe specimens display a thermally homogeneous makeup, whereas ripe fruits exhibit a distinctly defined, elevated core temperature profile.
</div>

The data extraction and sampling process for individual berry samples involved computing geometric ratios from the segmented inner cores:

1. **Relative Area:** $\text{Area of berry inner core} \div \text{Area of complete berry}$
2. **Relative Axis Length:** $\mathit{MajorAxisLength}\text{ of inner core} \div \mathit{MajorAxisLength}\text{ of complete berry}$
3. **Core Temperature:** Average inner core thermal footprint.

---

#### Classification Model Performance

The optimized classification models were trained and benchmarked across the primary algorithm families. For each family, the configuration yielding the highest cross-validation prediction accuracy was selected for formal performance comparison.

<div class="row justify-content-center align-items-center"> 
  <div class="col-md-7 mt-3 mt-md-0"> 
    {% include figure.liquid loading="eager" path="assets/img/4_scatter.png" title="SVM classification scatter plot" class="img-fluid rounded z-depth-1 w-100" %} 
  </div> 
  <div class="col-md-5 mt-3 mt-md-0"> 
    {% include figure.liquid loading="eager" path="assets/img/4_roc.png" title="SVM ROC Curve" class="img-fluid rounded z-depth-1 w-100" %} 
  </div> 
</div>
<div class="caption">
    <strong>Figure 2:</strong> Classification feature space (left) and corresponding ROC curve (right) for the optimized Quadratic SVM architecture. Demonstrating an AUC of $0.86$ and a validation accuracy of $91.7\%$, this framework emerged as the top-performing standalone supervised classifier.
</div>

##### Empirical Results Breakdown

Below is the consolidated performance layout tracking individual validation berry specimens against true versus predicted classes:



| Method | Ripe (Class 1) Samples | Unripe (Class 0) Samples | Overall Accuracy |
| :--- | :---: | :---: | :---: |
| **Complex DT** | 1, 1, 1, 1 | 0, 0, 0 | **100%** |
| **Quadratic Discriminant** | 0, 0, 1, 1 | 0, 0, 0 | **71.429%** |
| **Quadratic SVM** | 1, 1, 0, 1 | 0, 0, 0 | **85.714%** |
| **Fine $k$-NN** | 1, 1, 1, 1 | 0, 0, 0 | **100%** |
| **Ensemble (Bagged)** | 1, 1, 1, 1 | 0, 0, 0 | **100%** |

---

#### Discussion

Thermal signatures from two independent berry sets were captured across the IR spectrum. The baseline calibration batch served as the training matrix to optimize various supervised classifiers. The highest-performing model configuration from each core architectural family—Decision Tree, Discriminant, SVM, $k$-NN, and Ensemble Learning—was selected based on trends in cross-validation response accuracy. During the subsequent testing phase utilizing the independent validation set, three out of the five extracted models achieved a perfect $100\%$ classification tracking rate.

##### Confusion Matrices Breakdown

The comprehensive multi-model tracking performance of true versus predicted maturity states is compiled in Table 1:

<div class="table-responsive my-4">
<table class="table table-bordered table-striped text-center">
  <thead class="thead-dark">
    <tr>
      <th rowspan="3" class="align-middle">True Class</th>
      <th colspan="10">Predicted Class</th>
    </tr>
    <tr>
      <th colspan="5">Class 0 (Unripe)</th>
      <th colspan="5">Class 1 (Ripe)</th>
    </tr>
    <tr>
      <th>C.Tree</th>
      <th>QDA</th>
      <th>QSVM</th>
      <th>$k$-NN</th>
      <th>Ensemble</th>
      <th>C.Tree</th>
      <th>QDA</th>
      <th>QSVM</th>
      <th>$k$-NN</th>
      <th>Ensemble</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle"><strong>Class 0</strong></td>
      <td>4</td>
      <td>3</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td class="text-danger">2</td>
      <td class="text-danger">3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td class="align-middle"><strong>Class 1</strong></td>
      <td class="text-danger">3</td>
      <td class="text-danger">1</td>
      <td class="text-danger">1</td>
      <td class="text-danger">2</td>
      <td class="text-danger">1</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>4</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>
<div class="caption mt-n3 mb-4">
    <strong>Table 1:</strong> Matrix breakdown evaluating true versus predicted classification performance across the Complex Tree, Quadratic Discriminant, QSVM, Fine $k$-NN, and Bagged Ensemble frameworks. Red values denote misclassified sample counts.
</div>

While initial validation results are promising, further investigation is required to establish the long-term system resilience under shifting operational environments. Crucially, the transient temperature delta separating the inner core from the fruit surface remains highly sensitive to fluctuations in ambient environmental conditions, which can introduce instability into the predictive boundaries. 

For instance, post-harvest washing drastically altered the fruits' baseline thermal signatures—reducing both core and surface readings by up to $5^\circ\text{C}$ via evaporative cooling. Consequently, while several berry specimens resolved cleanly within the optical imagery reference (see Figure 3), they receded entirely and became indistinguishable inside the matching IR profiles due to this immediate temperature drop.

<div class="row justify-content-sm-center mt-4">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_ripeness_classifier.png" title="Optical spectrum samples" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <strong>Figure 3:</strong> Optical imagery of ripe and unripe wild berries harvested from the IIT Kharagpur campus showcasing sample indexing.
</div>

---

#### Conclusion

Despite these ambient design constraints, this study demonstrates that deploying supervised machine learning classifiers configured to analyze relative inner core area and localized core-to-surface thermal gradients provides a highly attractive, computationally efficient, and non-destructive framework for commercial agricultural sorting and quality grading.

---

#### Acknowledgments

The help provided by [Dr. P.K. Dutta](https://scholar.google.co.in/citations?hl=en&user=7elWBjEAAAAJ&view_op=list_works) with the experimental set-up, valuable guidance and the capturing of berries’ thermal images using his IR camera is gratefully acknowledged. I am deeply grateful to [Dr. P.K. Dutta](https://scholar.google.co.in/citations?hl=en&user=7elWBjEAAAAJ&view_op=list_works), for affording me the opportunity in working and exploring on the captivating subject.
