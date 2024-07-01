# Dynamic Path Planning with RRT* and Path Smoothing

This project implements a dynamic path planning algorithm using the RRT* (Rapidly-exploring Random Tree Star) algorithm. The application allows users to manually move obstacles around the screen and generate paths in real-time. Additionally, it features a path smoothing algorithm to improve the quality of the generated paths.

## Features

- **RRT* Algorithm**: Efficiently generates paths from a start point to a goal point while avoiding obstacles.
- **Path Smoothing**: Applies a shortcutting method to reduce sharp turns and discontinuities in the generated path.
- **Interactive Obstacles**: Users can manually move obstacles using the mouse.
- **Continuous Path Generation**: Option to enable continuous path generation every second while moving obstacles.

## Getting Started

### Prerequisites

- Python 3.x
- `pygame` library
- `pygame_gui` library

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dynamic-path-planning.git
    cd dynamic-path-planning
    ```

2. Install the required libraries:
    ```sh
    pip install pygame pygame_gui
    ```

### Running the Application

Run the `rrt.py` script:
```sh
python rrt.py
```

## Usage

- **Generate Path Button**: Click to generate a path from the start point (red circle) to the goal point (red circle) while avoiding obstacles (blue circles).
- **Smooth Path Toggle**: Click to toggle path smoothing on or off.
- **Continuous Gen Toggle**: Click to toggle continuous path generation on or off.
- **Move Obstacles**: Click and drag blue obstacles to new positions.

## Techniques Used

### RRT* Algorithm

The RRT* algorithm is an extension of the Rapidly-exploring Random Tree (RRT) algorithm. It is designed to efficiently explore high-dimensional spaces by randomly sampling points and incrementally building a tree. RRT* improves upon RRT by continuously optimizing the path, ensuring asymptotic optimality.

#### Key Steps:
1. **Sampling**: Randomly sample a point in the space.
2. **Nearest Neighbor**: Find the nearest node in the tree to the sampled point.
3. **New Node**: Create a new node towards the sampled point from the nearest node.
4. **Collision Check**: Ensure the path to the new node is free of obstacles.
5. **Rewire**: Rewire the tree to include the new node, optimizing the path by considering its neighbors.

### Path Smoothing

Path smoothing is applied to the generated path to reduce sharp turns and discontinuities. The method used here is the **shortcutting** technique, which attempts to directly connect non-consecutive waypoints if the path between them is collision-free.

#### Key Steps:
1. **Initialize**: Start with the original path.
2. **Check Collisions**: For each pair of non-consecutive waypoints, check if a direct path between them is free of obstacles.
3. **Update Path**: If a collision-free path exists between the waypoints, update the path to include this direct connection, skipping intermediate waypoints.

### Interactive Features

- **Mouse Interaction**: Users can click and drag obstacles to new positions. The system updates the path in real-time based on the new positions of the obstacles.
- **Continuous Path Generation**: When enabled, the path is regenerated every second, allowing for dynamic adjustments as obstacles are moved.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [pygame](https://www.pygame.org/) - Library for creating games and multimedia applications.
- [pygame_gui](https://pygame-gui.readthedocs.io/) - GUI library for pygame.
