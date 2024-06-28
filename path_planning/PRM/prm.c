#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NUM_NODES 100  // Number of random nodes to generate
#define MAX_NEIGHBORS 10  // Maximum number of neighbors for each node
#define WIDTH 100  // Width of the grid
#define HEIGHT 100  // Height of the grid

// Define the structure for a point
typedef struct {
    int x;
    int y;
} Point;

// Define the structure for a node in the PRM
typedef struct Node {
    Point point;
    struct Node* neighbors[MAX_NEIGHBORS];
    int num_neighbors;
} Node;

// Function to calculate the Euclidean distance between two points
double distance(Point a, Point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

// Function to generate random points
Point generate_random_point() {
    Point p;
    p.x = rand() % WIDTH;
    p.y = rand() % HEIGHT;
    return p;
}

// Function to check if a point is valid (i.e., not an obstacle)
int is_valid_point(Point p, int grid[WIDTH][HEIGHT]) {
    return grid[p.x][p.y] == 0;
}

// Function to find the nearest neighbors for a given node
void find_neighbors(Node* nodes, int num_nodes, int max_neighbors) {
    for (int i = 0; i < num_nodes; i++) {
        for (int j = 0; j < num_nodes; j++) {
            if (i != j && nodes[i].num_neighbors < max_neighbors) {
                double d = distance(nodes[i].point, nodes[j].point);
                nodes[i].neighbors[nodes[i].num_neighbors++] = &nodes[j];
            }
        }
    }
}

// Function to print the PRM nodes and their neighbors
void print_prm(Node* nodes, int num_nodes) {
    for (int i = 0; i < num_nodes; i++) {
        printf("Node (%d, %d):\n", nodes[i].point.x, nodes[i].point.y);
        for (int j = 0; j < nodes[i].num_neighbors; j++) {
            printf("  Neighbor (%d, %d)\n", nodes[i].neighbors[j]->point.x, nodes[i].neighbors[j]->point.y);
        }
    }
}

int main() {
    // Define the grid (0 = walkable, 1 = obstacle)
    int grid[WIDTH][HEIGHT] = {0};

    // Generate random nodes
    Node nodes[NUM_NODES];
    int num_nodes = 0;
    while (num_nodes < NUM_NODES) {
        Point p = generate_random_point();
        if (is_valid_point(p, grid)) {
            nodes[num_nodes].point = p;
            nodes[num_nodes].num_neighbors = 0;
            num_nodes++;
        }
    }

    // Find neighbors for each node
    find_neighbors(nodes, num_nodes, MAX_NEIGHBORS);

    // Print the PRM
    print_prm(nodes, num_nodes);

    return 0;
}
