#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define the structure for a point
typedef struct {
    int x;
    int y;
} Point;

// Define the structure for a node in the priority queue
typedef struct Node {
    Point point;
    double cost;
    struct Node* parent;
} Node;

// Function to calculate the heuristic (Euclidean distance)
double heuristic(Point a, Point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

// Function to check if two points are equal
int points_equal(Point a, Point b) {
    return a.x == b.x && a.y == b.y;
}

// A* algorithm implementation
void a_star(Point start, Point goal, int grid[5][5], int rows, int cols) {
    // Initialize the priority queue (simple array for this example)
    Node* open_list[100];
    int open_list_size = 0;

    // Add the start node to the open list
    Node* start_node = (Node*)malloc(sizeof(Node));
    start_node->point = start;
    start_node->cost = 0;
    start_node->parent = NULL;
    open_list[open_list_size++] = start_node;

    // Main loop
    while (open_list_size > 0) {
        // Find the node with the lowest cost
        int lowest_cost_index = 0;
        for (int i = 1; i < open_list_size; i++) {
            if (open_list[i]->cost < open_list[lowest_cost_index]->cost) {
                lowest_cost_index = i;
            }
        }

        // Get the node with the lowest cost
        Node* current = open_list[lowest_cost_index];
        open_list[lowest_cost_index] = open_list[--open_list_size];

        // Check if the goal has been reached
        if (points_equal(current->point, goal)) {
            // Print the path
            printf("Path found:\n");
            while (current != NULL) {
                printf("(%d, %d)\n", current->point.x, current->point.y);
                current = current->parent;
            }
            return;
        }

        // Generate the neighbors (up, down, left, right)
        Point neighbors[4] = {
            {current->point.x + 1, current->point.y},
            {current->point.x - 1, current->point.y},
            {current->point.x, current->point.y + 1},
            {current->point.x, current->point.y - 1}
        };

        // Process each neighbor
        for (int i = 0; i < 4; i++) {
            Point neighbor = neighbors[i];

            // Check if the neighbor is within bounds and walkable
            if (neighbor.x >= 0 && neighbor.x < cols && neighbor.y >= 0 && neighbor.y < rows && grid[neighbor.y][neighbor.x] == 0) {
                // Calculate the cost
                double cost = current->cost + 1 + heuristic(neighbor, goal);

                // Create a new node for the neighbor
                Node* neighbor_node = (Node*)malloc(sizeof(Node));
                neighbor_node->point = neighbor;
                neighbor_node->cost = cost;
                neighbor_node->parent = current;

                // Add the neighbor to the open list
                open_list[open_list_size++] = neighbor_node;
            }
        }
    }

    // No path found
    printf("No path found.\n");
}

int main() {
    // Define the grid (0 = walkable, 1 = obstacle)
    int grid[5][5] = {
        {0, 1, 0, 0, 0},
        {0, 1, 0, 1, 0},
        {0, 0, 0, 1, 0},
        {0, 1, 0, 0, 0},
        {0, 0, 0, 1, 0}
    };

    // Define the start and goal points
    Point start = {0, 0};
    Point goal = {4, 4};

    // Run the A* algorithm
    a_star(start, goal, grid, 5, 5);

    return 0;
}