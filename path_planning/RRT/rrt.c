#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define WIDTH 100
#define HEIGHT 100
#define MAX_NODES 1000
#define STEP_SIZE 5

// Define the structure for a point
typedef struct {
    int x;
    int y;
} Point;

// Define the structure for a node in the RRT
typedef struct Node {
    Point point;
    struct Node* parent;
} Node;

// Function to calculate the Euclidean distance between two points
double distance(Point a, Point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

// Function to generate a random point
Point generate_random_point() {
    Point p;
    p.x = rand() % WIDTH;
    p.y = rand() % HEIGHT;
    return p;
}

// Function to find the nearest node in the tree to a given point
Node* nearest_node(Node* nodes[], int num_nodes, Point p) {
    Node* nearest = nodes[0];
    double min_dist = distance(nearest->point, p);
    for (int i = 1; i < num_nodes; i++) {
        double dist = distance(nodes[i]->point, p);
        if (dist < min_dist) {
            nearest = nodes[i];
            min_dist = dist;
        }
    }
    return nearest;
}

// Function to steer from one point towards another
Point steer(Point from, Point to, double step_size) {
    Point new_point;
    double theta = atan2(to.y - from.y, to.x - from.x);
    new_point.x = from.x + step_size * cos(theta);
    new_point.y = from.y + step_size * sin(theta);
    return new_point;
}

// Function to check if a point is valid (i.e., not an obstacle)
int is_valid_point(Point p, int grid[WIDTH][HEIGHT]) {
    return p.x >= 0 && p.x < WIDTH && p.y >= 0 && p.y < HEIGHT && grid[p.x][p.y] == 0;
}

// Function to check if the path from one point to another is valid
int is_valid_path(Point from, Point to, int grid[WIDTH][HEIGHT]) {
    int x0 = from.x, y0 = from.y;
    int x1 = to.x, y1 = to.y;
    int dx = abs(x1 - x0), dy = abs(y1 - y0);
    int sx = (x0 < x1) ? 1 : -1;
    int sy = (y0 < y1) ? 1 : -1;
    int err = dx - dy;

    while (x0 != x1 || y0 != y1) {
        if (grid[x0][y0] == 1) return 0;
        int e2 = 2 * err;
        if (e2 > -dy) { err -= dy; x0 += sx; }
        if (e2 < dx) { err += dx; y0 += sy; }
    }
    return 1;
}

// Function to print the path from the start to the goal
void print_path(Node* node) {
    if (node == NULL) return;
    print_path(node->parent);
    printf("(%d, %d)\n", node->point.x, node->point.y);
}

// RRT algorithm implementation
void rrt(Point start, Point goal, int grid[WIDTH][HEIGHT]) {
    Node* nodes[MAX_NODES];
    int num_nodes = 0;

    // Add the start node to the tree
    Node* start_node = (Node*)malloc(sizeof(Node));
    start_node->point = start;
    start_node->parent = NULL;
    nodes[num_nodes++] = start_node;

    // Main loop
    while (num_nodes < MAX_NODES) {
        // Generate a random point
        Point rand_point = generate_random_point();

        // Find the nearest node in the tree to the random point
        Node* nearest = nearest_node(nodes, num_nodes, rand_point);

        // Steer from the nearest node towards the random point
        Point new_point = steer(nearest->point, rand_point, STEP_SIZE);

        // Check if the new point is valid
        if (is_valid_point(new_point, grid) && is_valid_path(nearest->point, new_point, grid)) {
            // Add the new node to the tree
            Node* new_node = (Node*)malloc(sizeof(Node));
            new_node->point = new_point;
            new_node->parent = nearest;
            nodes[num_nodes++] = new_node;

            // Check if the goal has been reached
            if (distance(new_point, goal) < STEP_SIZE) {
                Node* goal_node = (Node*)malloc(sizeof(Node));
                goal_node->point = goal;
                goal_node->parent = new_node;
                nodes[num_nodes++] = goal_node;

                printf("Path found:\n");
                print_path(goal_node);
                return;
            }
        }
    }

    printf("No path found.\n");
}

int main() {
    // Define the grid (0 = walkable, 1 = obstacle)
    int grid[WIDTH][HEIGHT] = {0};

    // Define the start and goal points
    Point start = {0, 0};
    Point goal = {WIDTH - 1, HEIGHT - 1};

    // Run the RRT algorithm
    rrt(start, goal, grid);

    return 0;
}
