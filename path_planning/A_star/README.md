# A* Path Planning Algorithm

The A* (A-star) algorithm is a popular pathfinding and graph traversal algorithm used in many fields of computer science due to its performance and accuracy.

## How It Works

A* uses a heuristic to estimate the cost to reach the goal from the current node. The algorithm maintains a priority queue of nodes to be explored, where the priority is determined by the estimated total cost (the sum of the cost to reach the node and the estimated cost to reach the goal from the node).

## Example Code

The example code in this directory demonstrates the A* algorithm on a simple grid. The grid is represented as a 2D array, and the algorithm finds the shortest path from the start position to the goal position.

### Usage

To compile and run the example code, use the following commands:

```bash
gcc -o a_star a_star.c -lm
./a_star
```

### Overview

The A* algorithm is a popular pathfinding and graph traversal algorithm. It is widely used in robotics and AI for its efficiency and accuracy in finding the shortest path.

### How A* Algorithm Works

The A* algorithm combines the strengths of Dijkstra's algorithm and Greedy Best-First-Search. It uses a heuristic to guide the search, aiming to find the shortest path from a start node to a goal node.

#### Initialization

- Initialize two lists: `open_list` (nodes to be evaluated) and `closed_list` (nodes already evaluated).
- Add the start node to the `open_list`.

#### Select Node

- Select the node with the lowest `f` value from the `open_list`. The `f` value is calculated as:
  - `f(n) = g(n) + h(n)`
  - `g(n)` is the cost from the start node to the current node.
  - `h(n)` is the heuristic estimate of the cost from the current node to the goal node.

#### Goal Check

- If the selected node is the goal node, reconstruct the path and terminate.

#### Generate Successors

- Generate all possible successors of the selected node (neighboring nodes).
- For each successor, calculate the `g`, `h`, and `f` values.

#### Evaluate Successors

- If a successor is in the `closed_list` and has a higher `f` value, skip it.
- If a successor is not in the `open_list` or has a lower `f` value than a previously considered path, update its `f` value and set its parent to the current node. Add it to the `open_list` if not already present.

#### Repeat

- Move the current node to the `closed_list`.
- Repeat steps 2-5 until the `open_list` is empty or the goal is reached.

### Key Features

- **Heuristic Function**: Uses a heuristic to estimate the cost to the goal, which helps to optimize the pathfinding process.
- **Combines Algorithms**: Merges the benefits of Dijkstra's algorithm (guarantees the shortest path) and Greedy Best-First-Search (fast exploration).

### Example

An example of the A* algorithm is provided in `a_star.c`. The code demonstrates how to set up a grid, define start and goal points, and execute the algorithm to find the shortest path.

### Visualization of Steps

#### Grid Initialization

- Represent the environment as a grid where 0s represent walkable cells and 1s represent obstacles.

#### Open and Closed Lists

- Use lists to manage nodes to be evaluated and nodes already evaluated.

#### Cost Calculation

- Compute the cost to move to each neighboring node and update paths based on the lowest cost estimate.

#### Path Reconstruction

- Once the goal node is reached, backtrack to reconstruct the path from the start node to the goal node.
