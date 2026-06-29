---
layout: page
title: DeepConvLSTM for Wearable Human Activity Recognition
description: Human Activity Recognition using DeepConvLSTM and Smartphone Sensors. 
completed_on: IIT-KGP, Nov '19
img: assets/img/5.png
importance: 10
selected: true
category: "Machine Learning & Intelligent Systems"
related_publications: true
---

Human Activity Recognition transforms safety and healthcare by enabling automated monitoring for the elderly, individuals with disabilities, and security surveillance networks. Our goal was to build a data-driven mobile app that accurately classifies human activities to enhance independent living and situational awareness. Based on the DeepConvLSTM {% cite s16010115 %}. 


<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ-mk9EtbvaWmiLELGdl9n4iAQekwc6sR2RUb5lhpN8bbw7YDQLe7KNshwolmnddUJTQdnTbVk1ugPu/pubembed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>


<br><br>

<h3>Problems Faced and Workarounds</h3>

<section>
    <h4>1. Difficult to push a trained model on an Android phone</h4>
    <ul>
        <li><strong>Workaround:</strong> A remote server hosts the trained DeepConvLSTM model for cloud-based inference.</li>
        <li><strong>Data Pipeline:</strong> The smartphone collects 6-channel sensor data at 100 Hz and streams it to the server in 1-second packets.</li>
        <li><strong>Inference:</strong> The server maintains a rolling buffer, processes the full 5-second overlapping time window, and replies with the predicted user activity.</li>
    </ul>
</section>
<section>
    <h4>2. Feeding Raw Windows to an LSTM</h4>
    <p>An LSTM processes data step-by-step. If we feed all 500 raw time steps (representing 3,000 raw values across 6 channels) sequentially into an LSTM, it struggles to learn. It suffers from vanishing gradients over long sequences and causes severe processing slowdowns that drain smartphone batteries.</p>
    <ul>
        <li><strong>Workaround:</strong> A TimeDistributed CNN acts as an on-server data compressor.</li>
        <li><strong>Compression:</strong> It takes the 500 raw time steps and divides them into a sequence of 20 distinct sub-window blocks, each containing 25 readings.</li>
        <li><strong>Feature Extraction:</strong> The CNN condenses each 25-reading block into a single, clean "feature summary" vector.</li>
        <li><strong>Sequential Tracking:</strong> The LSTM then processes just these 20 high-level summary steps instead of 500 raw inputs, easily and accurately tracking how the activity changes over time.</li>
    </ul>
</section>
<br>
<h3>DeepConvLSTM Core Architecture</h3>
<ul>
    <li><strong>Input Layer:</strong> Receives a raw 4D data tensor (Activity Window, Sub-Window Block, Readings per Block, Sensor) split into sequential sub-windows.</li>
    <li><strong>TimeDistributed CNN:</strong> Extracts local features from each individual sub-window independently.</li>
    <li><strong>Flatten Layer:</strong> Compresses each sub-window's raw readings into a single feature summary vector.</li>
    <li><strong>LSTM Layer:</strong> Processes the chronological sequence of these summary vectors to track movement over time.</li>
    <li><strong>Dense MLP Output:</strong> Uses a Softmax activation layer to calculate the final activity probabilities.</li>
</ul>
<br><br>
{% raw %}

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import TimeDistributed, Conv1D, MaxPooling1D, Flatten, LSTM, Dense, Dropout

# --- Define Architecture Constants ---
BLOCKS = 20              # Number of sub-windows (LSTM time steps)
READINGS_PER_BLOCK = 25  # Number of sensor readings per sub-window
CHANNELS = 6             # Accel (X,Y,Z) + Gyro (X,Y,Z)
NUM_CLASSES = 4          # Number of target activities (walking, sitting, standing, falling)

# --- Build CNN-LSTM Model ---
model = Sequential(name="CNN_LSTM_Activity_Classifier")

# 1. CNN Feature Extraction (Wrapped in TimeDistributed)
model.add(TimeDistributed(
    Conv1D(filters=64, kernel_size=3, activation='relu'), 
    input_shape=(BLOCKS, READINGS_PER_BLOCK, CHANNELS)
))
model.add(TimeDistributed(Conv1D(filters=64, kernel_size=3, activation='relu')))
model.add(TimeDistributed(MaxPooling1D(pool_size=2)))
model.add(TimeDistributed(Dropout(0.5)))
model.add(TimeDistributed(Flatten()))  # Compresses 25 readings into a feature vector

# 2. Sequential Tracking (LSTM)
model.add(LSTM(units=100, return_sequences=False))
model.add(Dropout(0.5))

# 3. Final Classification (MLP Output Layer)
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=NUM_CLASSES, activation='softmax'))

# --- Compile Model ---
model.compile(
    optimizer='adam', 
    loss='categorical_crossentropy', 
    metrics=['accuracy']
)

# Print Summary to check tensor shapes
model.summary()

```

{% endraw %}
