---
layout: page
title: Fruit Ripeness Classifier
description: Nondestructive techniques for determining the ripeness state using ML methods.
completed_on: IIT-KGP, May '18
img: /assets/img/4_ripeness_classifier.png
importance: 3
category: Sequential Deep Learning and ML
project_pdf: /assets/pdf/4_fruits.pdf # you can also use external links here
---

We developed and compared nondestructive techniques to determine the ripeness of local berries using five machine learning algorithms: Decision Tree, Quadratic Discriminant Analysis (QDA), Support Vector Machine (SVM), Ensemble Learning, and \(k\)-Nearest Neighbors (\(k\)-NN). First, we captured infrared thermal images of freshly picked berries at various stages of ripeness. We then recorded the average temperature and relative size of the higher-temperature inner cores. Finally, we used these metrics as predictors for our models.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_ripeness_classifier.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_ir.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_processed.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Figure 1: On the left, images of ripe and unripe wild berries from the IIT-KGP campus. Middle, corresponding infrared spectrum thermal image with a temperature resolution of 0.1 K. Right, image processed to reveal the warmer fruit core. The unripen fruits have a thermally homogenous makeup whereas the core appears distinctly for ripe fruits. 
</div>
<div class="row align-items-center"> 
  <div class="col-md-7 mt-3 mt-md-0"> 
    {% include figure.liquid loading="eager" path="assets/img/4_scatter.png" title="example image" class="img-fluid rounded z-depth-1" %} 
  </div> 
  <div class="col-md-5 mt-3 mt-md-0"> 
    {% include figure.liquid loading="eager" path="assets/img/4_roc.png" title="example image" class="img-fluid rounded z-depth-1" %} 
  </div> 
</div>
<div class="caption">
    Figure 2: Scatter Plot (left) and the ROC curve (right) for the Quadratic SVM model. AUC of 0.86, with an accuracy of 91.7% was the highest amongst our supervised classifiers.  
</div>

<h3>Discussions</h3>
Thermal patterns from two distinct sets of berries were captured as infrared (IR) spectrum images. The first set was used to train various supervised classifier models. One model from each broad category—Tree, Discriminant, SVM, \(k\)-NN, and Ensemble—was selected based on the highest response vector prediction accuracy within that category. During the testing phase using the second set, three out of the five models achieved 100% accuracy.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/4_table.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Table 1: Confusion matrices of the berry-ripeness-classification problem with Complex Tree, Quadratic Discriminant, QSVM, KNN(fine) and Ensemble (Bagged) classifiers.
</div>

<p>
However, further work is needed to assess the long-term reliability of the system. In particular, the temperature difference between the core and the fruit surface depends heavily on the ambient environmental temperature, which can cause the method’s predictions to become unstable. For example, washing the berries drastically reduced their temperature—affecting both the surface and core by up to 5 °C. Although a few berries were visible in the optical spectrum image, they became indistinguishable in the corresponding IR image due to this 5 °C temperature drop post-washing.
</p>

<p>
Nevertheless, we believe that a supervised machine learning classifier based on core size and temperature relative to the fruit surface provides a promising approach for identifying the ripeness of commercial fruit.
</p>


<h3>
Acknowledgments
</h3>

The help provided by [Dr. P.K. Dutta](https://scholar.google.co.in/citations?hl=en&user=7elWBjEAAAAJ&view_op=list_works) with the experimental set-up, valuable guidance and the capturing of berries’ thermal images using his IR camera is gratefully acknowledged. I am deeply grateful to [Dr. P.K. Dutta](https://scholar.google.co.in/citations?hl=en&user=7elWBjEAAAAJ&view_op=list_works), for affording me the opportunity in working and exploring on the captivating subject.
