# Probabilistic Roadmap (PRM) Path Planning Algorithm

This directory contains an implementation of the Probabilistic Roadmap (PRM) path planning algorithm.

## Files

1. **prm.c**
   - Implementation of the PRM algorithm in C.

## Usage

To compile and run the PRM example, use the following commands:

```bash
gcc -o prm prm.c
./prm
```

### Overview

The Probabilistic Roadmap (PRM) algorithm is a popular path planning algorithm used in robotics. It is particularly useful for high-dimensional configuration spaces and can efficiently find paths through complex environments.

### How PRM Algorithm Works

The PRM algorithm works by randomly sampling points in the configuration space and connecting these points to form a roadmap. This roadmap can then be used to find a path from the start to the goal.

#### Initialization

- Randomly sample points in the configuration space.
- Check if each sampled point is valid (i.e., not in an obstacle).

#### Connect Nodes

- For each valid sampled point, find its nearest neighbors.
- Connect the point to its neighbors to form the roadmap.

#### Path Finding

- Use graph search algorithms (e.g., Dijkstra's or A*) on the roadmap to find a path from the start to the goal.

### Key Features

- **Random Sampling**: Uses random sampling to generate nodes in the configuration space.
- **Roadmap Construction**: Connects nodes to form a roadmap that represents the connectivity of the space.
- **Flexible**: Can be combined with different graph search algorithms to find paths.

### Example

An example of the PRM algorithm is provided in `prm.c`. The code demonstrates how to generate random points, connect them to form a roadmap, and print the roadmap.

### Visualization of Steps

#### Random Point Generation

- Generate random points within the configuration space and ensure they are valid.

#### Neighbor Finding

- For each node, find the nearest neighbors and connect them to form the roadmap.

#### Roadmap Printing

- Print the nodes and their neighbors to visualize the constructed roadmap.
