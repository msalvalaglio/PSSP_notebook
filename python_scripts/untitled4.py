import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 1000, 700
BACKGROUND_COLOR = (30, 30, 30)
PARTICLE_COLOR = (200, 200, 200)
SLIDER_COLOR = (100, 100, 100)
SLIDER_KNOB_COLOR = (255, 50, 50)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Particle Simulation with Shooting Mechanics")

# Particle class
class Particle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = radius ** 2
        self.color = PARTICLE_COLOR
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, gravity):
        # Apply gravity
        self.vy += gravity

        # Update position
        self.x += self.vx
        self.y += self.vy

        # Boundary collision with screen
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vx *= -1
            self.x = max(self.radius, min(WIDTH - self.radius, self.x))

        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.vy *= -1
            self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

    # Check if particle is hit by a mouse click
    def is_hit(self, mouse_x, mouse_y):
        distance = math.sqrt((self.x - mouse_x) ** 2 + (self.y - mouse_y) ** 2)
        return distance < self.radius

# Slider class
class Slider:
    def __init__(self, x, y, min_value, max_value, width=200):
        self.x = x
        self.y = y
        self.width = width
        self.height = 10
        self.min_value = min_value
        self.max_value = max_value
        self.value = (min_value + max_value) / 2
        self.knob_x = x + width // 2
        self.knob_radius = 8
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, SLIDER_COLOR, (self.x, self.y, self.width, self.height))
        pygame.draw.circle(screen, SLIDER_KNOB_COLOR, (int(self.knob_x), self.y + self.height // 2), self.knob_radius)

    def update(self, events):
        # Handle dragging
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.dragging:
            self.knob_x = min(max(self.x, mouse_x), self.x + self.width)
            self.value = self.min_value + (self.knob_x - self.x) / self.width * (self.max_value - self.min_value)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if math.hypot(mouse_x - self.knob_x, mouse_y - (self.y + self.height // 2)) < self.knob_radius:
                    self.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False

# Function to handle particle collisions and Lennard-Jones potential
def handle_collisions(particles, lj_strength):
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            p1 = particles[i]
            p2 = particles[j]

            # Calculate distance between particles
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            min_distance = p1.radius + p2.radius

            # Lennard-Jones potential forces
            if distance < 100 and distance > 0:  # Only apply within a certain range
                force_magnitude = lj_strength * ((1 / distance) ** 12 - (1 / distance) ** 6)
                fx = force_magnitude * (dx / distance)
                fy = force_magnitude * (dy / distance)

                # Apply forces to particles
                p1.vx -= fx / p1.mass
                p1.vy -= fy / p1.mass
                p2.vx += fx / p2.mass
                p2.vy += fy / p2.mass

            # Check for collision
            if distance < min_distance:
                # Elastic collision response
                angle = math.atan2(dy, dx)
                total_mass = p1.mass + p2.mass

                # Velocities in the direction of collision
                vx1 = p1.vx * math.cos(angle) + p1.vy * math.sin(angle)
                vy1 = -p1.vx * math.sin(angle) + p1.vy * math.cos(angle)
                vx2 = p2.vx * math.cos(angle) + p2.vy * math.sin(angle)
                vy2 = -p2.vx * math.sin(angle) + p2.vy * math.cos(angle)

                # Update velocities after collision
                new_vx1 = ((p1.mass - p2.mass) * vx1 + 2 * p2.mass * vx2) / total_mass
                new_vx2 = ((p2.mass - p1.mass) * vx2 + 2 * p1.mass * vx1) / total_mass

                p1.vx = new_vx1 * math.cos(angle) - vy1 * math.sin(angle)
                p1.vy = new_vx1 * math.sin(angle) + vy1 * math.cos(angle)
                p2.vx = new_vx2 * math.cos(angle) - vy2 * math.sin(angle)
                p2.vy = new_vx2 * math.sin(angle) + vy2 * math.cos(angle)

                # Adjust positions to avoid overlap
                overlap = 0.5 * (min_distance - distance + 1)
                p1.x -= overlap * math.cos(angle)
                p1.y -= overlap * math.sin(angle)
                p2.x += overlap * math.cos(angle)
                p2.y += overlap * math.sin(angle)

# Main simulation loop
def main():
    particles = [Particle(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.randint(10, 20)) for _ in range(15)]
    gravity_slider = Slider(50, 50, 0, 1, 300)
    lj_slider = Slider(50, 100, -1000, 1000, 300)

    clock = pygame.time.Clock()
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a particle is clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for particle in particles:
                    if particle.is_hit(mouse_x, mouse_y):
                        particles.remove(particle)  # Remove particle when clicked

        # Update sliders
        gravity_slider.update(events)
        lj_slider.update(events)

        # Get slider values
        gravity = gravity_slider.value
        lj_strength = lj_slider.value

        screen.fill(BACKGROUND_COLOR)

        # Update particles
        for particle in particles:
            particle.update(gravity)

        # Handle collisions and Lennard-Jones potential
        handle_collisions(particles, lj_strength)

        # Draw sliders
        gravity_slider.draw(screen)
        lj_slider.draw(screen)

        # Draw particles
        for particle in particles:
            particle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
