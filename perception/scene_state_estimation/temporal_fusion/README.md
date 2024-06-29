# Scene State Estimation with Temporal Fusion

This project implements a deep learning model using LSTM for scene state estimation, incorporating temporal information from a sequence of frames.

## How to Run

1. Install the required dependencies:
    ```sh
    pip install torch
    ```

2. Train the model:
    ```sh
    python train.py
    ```

3. Run the inference script:
    ```sh
    python main.py
    ```

## Description

The `LSTMSceneEstimator` class defines an LSTM-based neural network for scene state estimation. The `train.py` script trains the model on synthetic data, and the `main.py` script demonstrates how to load the trained model and perform inference on a new sample.
