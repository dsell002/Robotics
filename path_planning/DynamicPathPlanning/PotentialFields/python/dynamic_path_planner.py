import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
NUM_FLOCK = 50
FPS = 60
MAIN_OBJECT_SPEED = 3
FLOCK_OBJECT_SPEED = 2
REPULSION_RADIUS = 100
ATTRACTION_FACTOR = 0.1
REPULSION_FACTOR = 1.5
COLLISION_RADIUS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Planning Through Dynamic Environment")
clock = pygame.time.Clock()

# Font for collision counter
font = pygame.font.SysFont(None, 36)

# Helper Functions
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
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)

class MainObject(MovingObject):
    def __init__(self, x, y, color, speed):
        super().__init__(x, y, color, speed)
        self.target = (WIDTH // 2, HEIGHT // 2)
        self.velocity_x = 0
        self.velocity_y = 0
        self.collisions = 0
        self.last_collision = None
    
    def update(self, flock):
        force_x, force_y = 0, 0
        collision_detected = False
        
        for obj in flock:
            dist = distance(self.x, self.y, obj.x, obj.y)
            if dist < REPULSION_RADIUS:
                repulsion = REPULSION_FACTOR / (dist**2) if dist > 0 else 0
                force_x += (self.x - obj.x) * repulsion
                force_y += (self.y - obj.y) * repulsion
            if dist < COLLISION_RADIUS:
                if self.last_collision != obj:
                    self.collisions += 1
                    self.color = GREEN  # Change color to indicate collision
                    self.last_collision = obj
                collision_detected = True
            else:
                if not collision_detected:
                    self.color = RED  # Reset color if no collision
        
        if not collision_detected:
            self.last_collision = None
        
        # Move towards the target
        target_dist = distance(self.x, self.y, self.target[0], self.target[1])
        if target_dist > 0:
            force_x += (self.target[0] - self.x) * ATTRACTION_FACTOR
            force_y += (self.target[1] - self.y) * ATTRACTION_FACTOR
        
        # Normalize force vector
        force_magnitude = math.sqrt(force_x**2 + force_y**2)
        if force_magnitude > 0:
            force_x /= force_magnitude
            force_y /= force_magnitude
        
        self.velocity_x += force_x
        self.velocity_y += force_y
        
        # Cap velocity to maximum speed
        velocity_magnitude = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
        if velocity_magnitude > self.speed:
            self.velocity_x = (self.velocity_x / velocity_magnitude) * self.speed
            self.velocity_y = (self.velocity_y / velocity_magnitude) * self.speed
        
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Boundary conditions
        if self.x < 0:
            self.x = 0
            self.velocity_x = -self.velocity_x
        if self.x > WIDTH:
            self.x = WIDTH
            self.velocity_x = -self.velocity_x
        if self.y < 0:
            self.y = 0
            self.velocity_y = -self.velocity_y
        if self.y > HEIGHT:
            self.y = HEIGHT
            self.velocity_y = -self.velocity_y
    
    def set_target(self, x, y):
        self.target = (x, y)

def main():
    running = True
    main_object = MainObject(WIDTH // 2, HEIGHT // 2, RED, MAIN_OBJECT_SPEED)
    flock = [MovingObject(random.randint(0, WIDTH), random.randint(0, HEIGHT), BLUE, FLOCK_OBJECT_SPEED) for _ in range(NUM_FLOCK)]
    
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_object.set_target(*event.pos)
        
        main_object.update(flock)
        main_object.draw()
        
        for obj in flock:
            obj.move()
            obj.draw()
        
        # Display collision counter
        collision_text = font.render(f"Collisions: {main_object.collisions}", True, BLACK)
        screen.blit(collision_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
