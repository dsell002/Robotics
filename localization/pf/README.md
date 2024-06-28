# Particle Filter (PF) for Localization

## Overview

The Particle Filter (PF) is a non-parametric filter that uses a set of particles to represent the probability distribution of the state of a system. Each particle represents a possible state, and the filter approximates the state distribution by updating the particles based on the motion model and measurements. PF is particularly useful in robotics for localization and tracking applications where the system's dynamics are nonlinear and non-Gaussian.

This directory contains example implementations of the PF in both C and Python for the purpose of localization.

## How PF Works

The PF operates in four main steps: **Initialization**, **Prediction**, **Update**, and **Resample**.

### 1. Initialization Step

In the initialization step, particles are randomly initialized within the state space. Each particle represents a possible state of the system.

### 2. Prediction Step

In the prediction step, the PF uses the motion model to predict the next state for each particle. This involves:
- **State Prediction**: Using the motion model, each particle's state is projected forward in time.

### 3. Update Step

In the update step, the PF uses the measurement to update the weight of each particle. This involves:
- **Measurement Prediction**: The expected measurement is calculated for each particle.
- **Weight Update**: The weight of each particle is updated based on the difference between the actual measurement and the predicted measurement.

### 4. Resample Step

In the resample step, particles are resampled according to their weights. This step helps to focus the particles on the more likely states of the system. Particles with higher weights are more likely to be selected, while particles with lower weights may be discarded.
