# Rapidly-exploring Random Tree (RRT) Path Planning Algorithm

This directory contains an implementation of the Rapidly-exploring Random Tree (RRT) path planning algorithm.

## Files

1. **rrt.c**
   - Implementation of the RRT algorithm in C.

## Usage

To compile and run the RRT example, use the following commands:

```bash
gcc -o rrt rrt.c -lm
./rrt
```

### Overview

The Rapidly-exploring Random Tree (RRT) algorithm is a popular path planning algorithm used in robotics. It is particularly useful for high-dimensional configuration spaces and can efficiently find paths through complex environments.

### How RRT Algorithm Works

The RRT algorithm works by incrementally building a tree that explores the space from a start node towards a goal node. It randomly samples points in the configuration space and attempts to connect these points to the existing tree, steering towards the goal.

#### Initialization

- Initialize the tree with the start node.
- Define the goal node and the configuration space.

#### Main Loop

- Randomly sample points in the configuration space.
- Find the nearest node in the tree to each sampled point.
- Steer from the nearest node towards the sampled point, creating a new node.
- Check if the new node is valid (i.e., not in an obstacle).
- Add the new node to the tree if it is valid.
- Check if the new node is close enough to the goal node to consider the goal reached.

### Key Features

- **Random Sampling**: Uses random sampling to explore the configuration space.
- **Tree Expansion**: Incrementally builds a tree that explores the space from the start node towards the goal node.
- **Flexible**: Can be combined with other path planning techniques to enhance performance and efficiency.

### Example

An example of the RRT algorithm is provided in `rrt.c`. The code demonstrates how to initialize the tree, randomly sample points, connect them to the tree, and print the resulting path if one is found.

### Visualization of Steps

#### Random Point Generation

- Generate random points within the configuration space.

#### Nearest Node Search

- For each random point, find the nearest node in the tree.

#### Steer Towards Random Point

- Create a new node by steering from the nearest node towards the random point.

#### Validity Check

- Ensure the new node is within the bounds of the configuration space and not in an obstacle.

#### Path Printing

- Print the path from the start node to the goal node if a path is found.
