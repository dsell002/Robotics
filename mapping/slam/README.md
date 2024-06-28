# Simultaneous Localization and Mapping (SLAM)

## Overview

Simultaneous Localization and Mapping (SLAM) is a technique used in robotics to build a map of an unknown environment while simultaneously keeping track of the robot's location within that environment. This directory contains example implementations of a basic SLAM algorithm in both C and Python.

## How SLAM Works

The SLAM algorithm operates in two main steps: **Prediction** and **Update**.

### 1. Prediction Step

In the prediction step, the SLAM algorithm uses the robot's motion model to predict its new position and orientation. This involves:
- **State Prediction**: Using the motion model, the robot's state (position and orientation) is projected forward in time.
- **Covariance Prediction**: The state covariance matrix is updated to reflect the uncertainty in the prediction due to motion.

### 2. Update Step

In the update step, the SLAM algorithm uses sensor measurements to update the robot's position, orientation, and the positions of landmarks in the map. This involves:
- **Measurement Prediction**: The expected measurement is calculated from the predicted state and the known positions of landmarks. This involves predicting the position of landmarks relative to the robot's new estimated position.
- **Innovation Calculation**: The difference between the actual measurement and the predicted measurement (innovation) is calculated.
- **Kalman Gain Calculation**: The Kalman gain is computed, which determines the weight given to the innovation.
- **State and Covariance Update**: The predicted state and covariance are updated using the innovation and the Kalman gain. This step adjusts the robot's position and orientation as well as the positions of landmarks to better fit the actual measurements.
