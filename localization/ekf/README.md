# Extended Kalman Filter (EKF) for Localization

## Overview

The Extended Kalman Filter (EKF) is a powerful algorithm used for estimating the state of a dynamic system from a series of incomplete and noisy measurements. It is an extension of the Kalman Filter that linearizes the nonlinear models around the current estimate. This makes it particularly useful in robotics for localization and tracking applications.

This directory contains example implementations of the EKF in both C and Python for the purpose of localization.

## How EKF Works

The EKF operates in two main steps: **Prediction** and **Update**.

### 1. Prediction Step

In the prediction step, the EKF uses the current state estimate and a motion model to predict the next state. This involves:

- **State Prediction**: Using the motion model, the state is projected forward in time.
- **Jacobian Calculation**: The Jacobian matrix of the motion model is calculated to linearize the nonlinear model.
- **Covariance Prediction**: The state covariance matrix is updated using the Jacobian and process noise covariance.

Mathematically, the prediction step can be represented as:
\[ \mathbf{x}_{k|k-1} = f(\mathbf{x}_{k-1|k-1}, \mathbf{u}_k) \]
\[ \mathbf{P}_{k|k-1} = \mathbf{F}_k \mathbf{P}_{k-1|k-1} \mathbf{F}_k^T + \mathbf{Q}_k \]

Where:
- \(\mathbf{x}_{k|k-1}\) is the predicted state.
- \(f\) is the nonlinear motion model.
- \(\mathbf{u}_k\) is the control input.
- \(\mathbf{P}_{k|k-1}\) is the predicted covariance.
- \(\mathbf{F}_k\) is the Jacobian of the motion model.
- \(\mathbf{Q}_k\) is the process noise covariance.

### 2. Update Step

In the update step, the EKF uses the measurement to correct the predicted state. This involves:

- **Measurement Prediction**: The expected measurement is calculated from the predicted state.
- **Innovation Calculation**: The difference between the actual measurement and the predicted measurement (innovation) is computed.
- **Kalman Gain Calculation**: The Kalman gain is computed to determine the weight given to the innovation.
- **State Update**: The predicted state is updated using the innovation and Kalman gain.
- **Covariance Update**: The state covariance matrix is updated to reflect the improved estimate.

Mathematically, the update step can be represented as:
\[ \mathbf{y}_k = \mathbf{z}_k - h(\mathbf{x}_{k|k-1}) \]
\[ \mathbf{S}_k = \mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^T + \mathbf{R}_k \]
\[ \mathbf{K}_k = \mathbf{P}_{k|k-1} \mathbf{H}_k^T \mathbf{S}_k^{-1} \]
\[ \mathbf{x}_{k|k} = \mathbf{x}_{k|k-1} + \mathbf{K}_k \mathbf{y}_k \]
\[ \mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k) \mathbf{P}_{k|k-1} \]

Where:
- \(\mathbf{y}_k\) is the innovation.
- \(\mathbf{z}_k\) is the actual measurement.
- \(h\) is the nonlinear measurement model.
- \(\mathbf{S}_k\) is the innovation covariance.
- \(\mathbf{H}_k\) is the Jacobian of the measurement model.
- \(\mathbf{R}_k\) is the measurement noise covariance.
- \(\mathbf{K}_k\) is the Kalman gain.
- \(\mathbf{x}_{k|k}\) is the updated state.
- \(\mathbf{P}_{k|k}\) is the updated covariance.
- \(\mathbf{I}\) is the identity matrix.