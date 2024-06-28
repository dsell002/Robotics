import math
import heapq

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return False

class Node:
    def __init__(self, point, cost, parent=None):
        self.point = point
        self.cost = cost
        self.parent = parent

def heuristic(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def points_equal(a, b):
    return a.x == b.x and a.y == b.y

def a_star(start, goal, grid, rows, cols):
    open_list = []
    heapq.heappush(open_list, (0, Node(start, 0)))
    closed_list = set()

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if points_equal(current.point, goal):
            print("Path found:")
            path = []
            while current:
                path.append((current.point.x, current.point.y))
                current = current.parent
            for p in reversed(path):
                print(p)
            return

        closed_list.add((current.point.x, current.point.y))

        neighbors = [
            Point(current.point.x + 1, current.point.y),
            Point(current.point.x - 1, current.point.y),
            Point(current.point.x, current.point.y + 1),
            Point(current.point.x, current.point.y - 1)
        ]

        for neighbor in neighbors:
            if (0 <= neighbor.x < cols and
                0 <= neighbor.y < rows and
                grid[neighbor.y][neighbor.x] == 0 and
                (neighbor.x, neighbor.y) not in closed_list):
                
                cost = current.cost + 1 + heuristic(neighbor, goal)
                heapq.heappush(open_list, (cost, Node(neighbor, cost, current)))

    print("No path found.")

def main():
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    start = Point(0, 0)
    goal = Point(4, 4)

    a_star(start, goal, grid, 5, 5)

if __name__ == "__main__":
    main()
