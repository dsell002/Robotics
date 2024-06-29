# Multi-Object Tracking with Kalman Filter

This project implements a basic multi-object tracking system using the Kalman Filter in Python.

## How to Run

1. Install the required dependencies:
    ```sh
    pip install numpy matplotlib filterpy
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

## Description

The `ObjectTracker` class uses the Kalman Filter to predict and update the state of a moving object based on noisy measurements. The `main.py` script demonstrates the tracking of a single object with 2D position measurements.
