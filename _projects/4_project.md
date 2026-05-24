---
layout: page
title: Fruit Ripeness Classifier
description: Nondestructive techniques for determining the ripeness state using ML methods. Completed May 2018
img: /assets/img/4_ripeness_classifier.PNG
importance: 3
category: fun
project_pdf: /assets/pdf/4_fruits.pdf # you can also use external links here
---

We developed and compared nondestructive techniques for the purpose of determining the ripeness state (classified as either reached ripeness or not – 2 states) of local berry fruit based on 5 machine learning methods: Decision Learning Tree, Quadratic discriminant, Support vector machine, Ensemble learning and kNN (k – Nearest Neighbors). Infrared thermal images of freshly plucked berries (ripen and unripen) were taken at two different instances. The relative size of higher temperature inner cores and its average temperature was recorded. These served as predictors or features used in each model.


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_ripeness_classifier.PNG" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_ir.PNG" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_processed.PNG" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    On the left, images of ripe and unripe wild berries from the IIT-KGP campus. Middle, corresponding infrared spectrum thermal image with a temperature resolution of 0.1 K. Right, image processed to reveal the warmer fruit core. The unripen fruits have a thermally homogenous makeup whereas the core appears distinctly for ripe fruits. 
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_scatter.PNG" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/4_roc.PNG" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Scatter Plot (left) and the ROC curve (right) for the Quadratic SVM model. AUC of 0.86, with an accuracy of 91.7% was the highest amongst our supervised classifiers.  
</div>

Thermal patterns of two different sets of berries was captured as images in IR spectrum. First set served as training set for different supervised classifier models. One model from each category: Tree, Discriminant, SVM, kNN and Ensemble – was chosen based on highest level of response vector
prediction accuracy amongst its category. During test phase (employing test batch), an accuracy of 100% was reached on 3 out of 5 of them.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/4_table.PNG" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Confusion matrices of the berry-ripeness-classification problem with Complex Tree, Quadratic Discriminant, QSVM, KNN(fine) and Ensemble (Bagged) classifiers.
</div>

However, further work to assess the long-term reliability of the system is needed. In particular, temperature difference between core and fruit surface depends on environmental temperature and so can make the method’s predictions unstable. For example, washing the berries drastically reduced
their temperature (both surface and core up to an extent of 5 oC) – as can be seen in Fig.1 & 4 that though few berries were present in visible spectrum image, receded from corresponding IR image as they were cooler by 5 oC after washing. 

Nevertheless, we believe that a supervised machine learning classifier-based on core size and temperature relative to fruits’ surface provides an attractive means of identifying the ripeness of
commercial fruit.

<h3 class="title">
Acknowledgments
</h3>

The help provided by Dr. P.K. Dutta with the experimental set-up, valuable guidance and the capturing of berries’ thermal images using his IR camera is gratefully acknowledged. I am deeply grateful to Dr. P.K. Dutta, for affording me the opportunity in working and exploring on the captivating subject.
