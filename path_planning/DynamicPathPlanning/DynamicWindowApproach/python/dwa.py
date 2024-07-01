import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
FLOCK_OBJECT_SPEED = 1
NUM_FLOCK = 50
FPS = 60
ROBOT_RADIUS = 10
MAX_VEL = 3
MAX_ROT = math.pi / 4
VEL_RESOLUTION = 0.5
ROT_RESOLUTION = math.pi / 16
PREDICTION_TIME = 1.0
OBSTACLE_RADIUS = 5
DISTANCE_COST_WEIGHT = 5.0
COLLISION_THRESHOLD = ROBOT_RADIUS + OBSTACLE_RADIUS + 5  # Collision threshold with margin

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Planning with Dynamic Window Approach")
clock = pygame.time.Clock()

# Font for collision counter
font = pygame.font.SysFont(None, 36)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class MovingObject:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.angle = random.uniform(0, 2 * math.pi)
    
    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        
        # Boundary conditions
        if self.x < 0 or self.x > WIDTH:
            self.angle = math.pi - self.angle
        if self.y < 0 or self.y > HEIGHT:
            self.angle = -self.angle

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), OBSTACLE_RADIUS)

    def predict_position(self, prediction_time):
        pred_x = self.x + self.speed * math.cos(self.angle) * prediction_time
        pred_y = self.y + self.speed * math.sin(self.angle) * prediction_time
        return pred_x, pred_y

class Robot:
    def __init__(self, x, y, color, max_vel, max_rot):
        self.x = x
        self.y = y
        self.color = color
        self.vel = 0
        self.rot = 0
        self.angle = 0
        self.max_vel = max_vel
        self.max_rot = max_rot
        self.target = (WIDTH // 2, HEIGHT // 2)
        self.collisions = 0
        self.last_collision = None

    def set_target(self, x, y):
        self.target = (x, y)

    def move(self):
        self.x += self.vel * math.cos(self.angle)
        self.y += self.vel * math.sin(self.angle)
        self.angle += self.rot

        # Boundary conditions
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH:
            self.x = WIDTH
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT:
            self.y = HEIGHT

    def dwa(self, flock):
        best_cost = float('inf')
        best_vel = 0
        best_rot = 0
        
        for vel in [v * VEL_RESOLUTION for v in range(-int(self.max_vel/VEL_RESOLUTION), int(self.max_vel/VEL_RESOLUTION)+1)]:
            for rot in [r * ROT_RESOLUTION for r in range(-int(self.max_rot/ROT_RESOLUTION), int(self.max_rot/ROT_RESOLUTION)+1)]:
                if vel == 0 and rot == 0:
                    continue
                pred_x, pred_y, pred_angle = self.predict_position(vel, rot)
                heading_cost = self.calc_heading_cost(pred_x, pred_y)
                distance_cost = self.calc_distance_cost(pred_x, pred_y, flock)
                collision_free = self.check_collision_free(pred_x, pred_y, flock)
                
                if not collision_free:
                    continue
                
                total_cost = heading_cost + DISTANCE_COST_WEIGHT * distance_cost
                
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_vel = vel
                    best_rot = rot
        
        self.vel = best_vel
        self.rot = best_rot
    
    def predict_position(self, vel, rot):
        pred_x = self.x + vel * math.cos(self.angle) * PREDICTION_TIME
        pred_y = self.y + vel * math.sin(self.angle) * PREDICTION_TIME
        pred_angle = self.angle + rot * PREDICTION_TIME
        return pred_x, pred_y, pred_angle

    def calc_heading_cost(self, pred_x, pred_y):
        return distance(pred_x, pred_y, self.target[0], self.target[1])

    def calc_distance_cost(self, pred_x, pred_y, flock):
        min_dist = float('inf')
        for obj in flock:
            pred_obj_x, pred_obj_y = obj.predict_position(PREDICTION_TIME)
            dist = distance(pred_x, pred_y, pred_obj_x, pred_obj_y)
            if dist < min_dist:
                min_dist = dist
        return 1.0 / (min_dist + 1e-6)
    
    def check_collision_free(self, pred_x, pred_y, flock):
        for obj in flock:
            pred_obj_x, pred_obj_y = obj.predict_position(PREDICTION_TIME)
            if distance(pred_x, pred_y, pred_obj_x, pred_obj_y) < COLLISION_THRESHOLD:
                return False
        return True

    def update(self, flock):
        self.dwa(flock)
        self.move()
        
        for obj in flock:
            if distance(self.x, self.y, obj.x, obj.y) < ROBOT_RADIUS + OBSTACLE_RADIUS:
                if self.last_collision != obj:
                    self.collisions += 1
                    self.color = GREEN  # Change color to indicate collision
                    self.last_collision = obj
            else:
                if self.last_collision == obj:
                    self.color = RED  # Reset color if no collision
                    self.last_collision = None

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), ROBOT_RADIUS)

def main():
    running = True
    robot = Robot(WIDTH // 2, HEIGHT // 2, RED, MAX_VEL, MAX_ROT)
    flock = [MovingObject(random.randint(0, WIDTH), random.randint(0, HEIGHT), BLUE, FLOCK_OBJECT_SPEED) for _ in range(NUM_FLOCK)]
    
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                robot.set_target(*event.pos)
        
        robot.update(flock)
        robot.draw()
        
        for obj in flock:
            obj.move()
            obj.draw()
        
        # Display collision counter
        collision_text = font.render(f"Collisions: {robot.collisions}", True, BLACK)
        screen.blit(collision_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
