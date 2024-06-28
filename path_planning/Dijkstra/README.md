# Dijkstra's Path Planning Algorithm

This directory contains an implementation of Dijkstra's path planning algorithm.

## Files

1. **dijkstra.c**
   - Implementation of Dijkstra's algorithm in C.

## Usage

To compile and run the Dijkstra example, use the following commands:

```bash
gcc -o dijkstra dijkstra.c
./dijkstra
```

## Overview

Dijkstra's algorithm is used to find the shortest paths between nodes in a graph. It is commonly used in networking and other fields for routing and pathfinding.

## How Dijkstra's Algorithm Works

Dijkstra's algorithm works by iteratively selecting the node with the smallest known distance from the source and updating the distance values of its adjacent nodes. Here are the key steps:

1. **Initialization:**
   - Set the distance to the source node to 0 and the distance to all other nodes to infinity.
   - Mark all nodes as unvisited. The unvisited nodes are used to keep track of the shortest path tree (SPT).

2. **Set the Current Node:**
   - Initially, set the current node to the source node.

3. **Update Distances:**
   - For the current node, consider all of its unvisited neighbors. 
   - Calculate their tentative distances through the current node.
   - If the calculated distance of a node is less than the known distance, update the shortest distance.

4. **Mark as Visited:**
   - After considering all neighbors of the current node, mark the current node as visited. 
   - A visited node will not be checked again.

5. **Select the Next Node:**
   - Select the unvisited node with the smallest tentative distance and set it as the new current node. 
   - Repeat steps 3-5 until all nodes are visited or the smallest tentative distance among the unvisited nodes is infinity.

6. **Termination:**
   - The algorithm terminates when all nodes have been visited. 
   - At this point, the shortest path to each node has been determined.

## Example
An example of Dijkstra's algorithm is provided in dijkstra.c. The code demonstrates how to set up a graph using an adjacency matrix, define a source node, and execute the algorithm to find the shortest paths to all other nodes.

## Key Features
   - Single Source Shortest Path: Finds the shortest path from a single source node to all other nodes in the graph.
   - Greedy Algorithm: Uses a priority queue to greedily select the minimum distance node at each step.
   - Efficient: Suitable for graphs with non-negative weights.

## Visualization of Steps

1. **Graph Initialization:**
   - Represent the graph using an adjacency matrix where the value at graph[i][j] represents the weight of the edge between nodes i and j.

2. **Distance Array:**
   - Maintain an array dist[] where dist[i] represents the shortest distance from the source to node i.

3. **Set Operations:**
   - Use a boolean array spt_set[] to track nodes included in the shortest path tree. 
   - Initially, all values in spt_set[] are false.

4. **Priority Queue Operations:**
   - Extract the node with the minimum distance that has not been processed yet.
   - Update the distance values of the adjacent nodes of the extracted node.

5. **Final Path:**
   - Once the algorithm finishes, dist[] contains the shortest distances from the source to all other nodes.