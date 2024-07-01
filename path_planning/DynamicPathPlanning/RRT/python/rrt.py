import pygame
import pygame_gui
import random
import math
import time

# Pygame initialization
pygame.init()
width, height = 800, 600
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Pygame GUI initialization
manager = pygame_gui.UIManager((width, height))
generate_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 50), (100, 50)),
                                               text='Generate Path',
                                               manager=manager)
smooth_toggle = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 120), (150, 30)),
                                             text='Smooth Path: Off',
                                             manager=manager)
continuous_toggle = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 190), (200, 30)),
                                                 text='Continuous Gen: Off',
                                                 manager=manager)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

class RRTStar:
    def __init__(self, start, goal, obstacles, screen, step_size=20, goal_radius=10, max_iter=5000):
        self.start = Node(start[0], start[1])
        self.goal = Node(goal[0], goal[1])
        self.obstacles = obstacles
        self.screen = screen
        self.step_size = step_size
        self.goal_radius = goal_radius
        self.max_iter = max_iter
        self.nodes = [self.start]

    def get_random_node(self):
        return Node(random.randint(0, width), random.randint(0, height))

    def distance(self, node1, node2):
        return math.hypot(node1.x - node2.x, node1.y - node2.y)

    def get_nearest_node(self, random_node):
        return min(self.nodes, key=lambda node: self.distance(node, random_node))

    def is_collision(self, node1, node2):
        for obs in self.obstacles:
            if self.line_intersects_circle(node1, node2, obs):
                return True
        return False

    def line_intersects_circle(self, node1, node2, circle):
        ax, ay = node1.x, node1.y
        bx, by = node2.x, node2.y
        cx, cy, r = circle
        lab = math.hypot(bx - ax, by - ay)
        if lab == 0:
            return False  # If the distance is zero, they are the same point
        d = abs((bx - ax) * (ay - cy) - (ax - cx) * (by - ay)) / lab
        if d >= r:
            return False
        t = ((cx - ax) * (bx - ax) + (cy - ay) * (by - ay)) / (lab ** 2)
        ex, ey = ax + t * (bx - ax), ay + t * (by - ay)
        lec = math.hypot(ex - cx, ey - cy)
        return lec < r

    def get_new_node(self, nearest_node, random_node):
        theta = math.atan2(random_node.y - nearest_node.y, random_node.x - nearest_node.x)
        new_node = Node(nearest_node.x + self.step_size * math.cos(theta),
                        nearest_node.y + self.step_size * math.sin(theta))
        new_node.parent = nearest_node
        return new_node

    def rewire(self, new_node):
        for node in self.nodes:
            if node != new_node.parent and self.distance(node, new_node) < self.step_size:
                if not self.is_collision(node, new_node) and self.cost(new_node) + self.distance(node, new_node) < self.cost(node):
                    node.parent = new_node

    def cost(self, node):
        total_cost = 0
        while node.parent:
            total_cost += self.distance(node, node.parent)
            node = node.parent
        return total_cost

    def run(self):
        self.nodes = [self.start]  # Reset the tree
        for _ in range(self.max_iter):
            random_node = self.get_random_node()
            nearest_node = self.get_nearest_node(random_node)
            new_node = self.get_new_node(nearest_node, random_node)

            if not self.is_collision(nearest_node, new_node):
                self.nodes.append(new_node)
                self.rewire(new_node)

                if self.distance(new_node, self.goal) < self.goal_radius:
                    self.goal.parent = new_node
                    self.nodes.append(self.goal)
                    return self.get_path()

        return None

    def get_path(self):
        path = []
        node = self.goal
        while node.parent:
            path.append((node.x, node.y))
            node = node.parent
        path.append((self.start.x, self.start.y))
        path.reverse()
        return path

def smooth_path(path, obstacles):
    def is_collision_free(point1, point2):
        for obs in obstacles:
            if line_intersects_circle(point1, point2, obs):
                return False
        return True

    new_path = [path[0]]
    i = 0
    while i < len(path) - 1:
        for j in range(len(path) - 1, i, -1):
            if is_collision_free(path[i], path[j]):
                new_path.append(path[j])
                i = j
                break
    return new_path

def line_intersects_circle(point1, point2, circle):
    ax, ay = point1
    bx, by = point2
    cx, cy, r = circle
    lab = math.hypot(bx - ax, by - ay)
    if lab == 0:
        return False  # If the distance is zero, they are the same point
    d = abs((bx - ax) * (ay - cy) - (ax - cx) * (by - ay)) / lab
    if d >= r:
        return False
    t = ((cx - ax) * (bx - ax) + (cy - ay) * (by - ay)) / (lab ** 2)
    ex, ey = ax + t * (bx - ax), ay + t * (by - ay)
    lec = math.hypot(ex - cx, ey - cy)
    return lec < r

# Initialize start, goal, and obstacles
start = (50, 50)
goal = (750, 550)
obstacles = [(400, 300, 50), (200, 150, 30), (600, 400, 40), (150, 450, 20)]

selected_obstacle = None
continuous_generation = False
last_generation_time = time.time()

def main():
    global selected_obstacle, continuous_generation, last_generation_time

    rrt_star = RRTStar(start, goal, obstacles, win)
    path = []
    smooth_path_enabled = False

    run = True
    while run:
        time_delta = clock.tick(30) / 1000.0
        win.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, obs in enumerate(obstacles):
                    if math.hypot(event.pos[0] - obs[0], event.pos[1] - obs[1]) <= obs[2]:
                        selected_obstacle = i
            if event.type == pygame.MOUSEBUTTONUP:
                selected_obstacle = None
            if event.type == pygame.MOUSEMOTION:
                if selected_obstacle is not None:
                    obstacles[selected_obstacle] = (event.pos[0], event.pos[1], obstacles[selected_obstacle][2])
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == generate_button:
                        path = rrt_star.run()
                        if path and smooth_path_enabled:
                            path = smooth_path(path, obstacles)
                    elif event.ui_element == smooth_toggle:
                        smooth_path_enabled = not smooth_path_enabled
                        smooth_toggle.set_text(f'Smooth Path: {"On" if smooth_path_enabled else "Off"}')
                    elif event.ui_element == continuous_toggle:
                        continuous_generation = not continuous_generation
                        continuous_toggle.set_text(f'Continuous Gen: {"On" if continuous_generation else "Off"}')

            manager.process_events(event)

        manager.update(time_delta)

        if continuous_generation and time.time() - last_generation_time >= 1:
            path = rrt_star.run()
            if path and smooth_path_enabled:
                path = smooth_path(path, obstacles)
            last_generation_time = time.time()

        # Draw obstacles
        for obs in obstacles:
            pygame.draw.circle(win, blue, (obs[0], obs[1]), obs[2])

        # Draw path
        if path:
            for i in range(len(path) - 1):
                pygame.draw.line(win, green, path[i], path[i + 1], 2)

        # Draw start and goal
        pygame.draw.circle(win, red, start, 5)
        pygame.draw.circle(win, red, goal, 5)

        manager.draw_ui(win)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
