import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platform Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Font for displaying text
font = pygame.font.Font(None, 36)

# Game variables
score = 0
level = 1
highscore = 0
lives = 3
obstacle_timer = 0
platform_timer = 0
game_state = "intro"

# Load character images for animation (use a set of 8-bit style images)
runner_images = [pygame.Surface((32, 32)) for _ in range(2)]  # Placeholder images
runner_images[0].fill((0, 128, 255))  # Image 1 (blue)
runner_images[1].fill((0, 100, 200))  # Image 2 (slightly different blue for animation)

# Runner class
class Runner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = runner_images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 70
        self.velocity_y = 0
        self.jump = False
        self.frame = 0

    def update(self):
        self.frame += 1
        self.image = self.images[self.frame // 10 % len(self.images)]  # Switch images to animate
        self.velocity_y += 1
        self.rect.y += self.velocity_y

        # Check if on the ground or on a platform
        if self.rect.y >= SCREEN_HEIGHT - 70:
            self.rect.y = SCREEN_HEIGHT - 70
            self.jump = False

        # Check platform collisions
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and self.velocity_y >= 0:
            self.rect.y = hits[0].rect.top - self.rect.height
            self.velocity_y = 0
            self.jump = False

    def jump_up(self):
        if not self.jump:
            self.jump = True
            self.velocity_y = -15

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 5 + level  # Speed increases with level
        if self.rect.x < -20:
            self.kill()
            global score
            score += 10  # Points awarded for dodging obstacle

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.image = pygame.Surface((width, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 3
        if self.rect.x < -self.rect.width:
            self.kill()

# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Create a player
player = Runner()
all_sprites.add(player)

def draw_text(text, font, color, x, y):
    screen.blit(font.render(text, True, color), (x, y))

# Function to handle the game over screen
def game_over_screen():
    screen.fill(WHITE)
    draw_text("Game Over", font, RED, SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 50)
    draw_text(f"Score: {score}", font, BLACK, SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2)
    draw_text("Press Enter to Restart", font, BLACK, SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()

# Function to handle the intro screen
def intro_screen():
    screen.fill(WHITE)
    draw_text("Platform Runner", font, BLACK, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
    draw_text("Press Space to Start", font, BLACK, SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2)
    pygame.display.flip()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == "intro" and event.key == pygame.K_SPACE:
                game_state = "playing"
                score = 0
                level = 1
                lives = 3
            elif game_state == "playing" and event.key == pygame.K_SPACE:
                player.jump_up()
            elif game_state == "gameover" and event.key == pygame.K_RETURN:
                game_state = "intro"

    # Game state management
    if game_state == "intro":
        intro_screen()
        continue

    elif game_state == "gameover":
        game_over_screen()
        continue

    # Spawn obstacles
    obstacle_timer += 1
    if obstacle_timer > 60 - level * 2:
        obstacle_timer = 0
        obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT - 70)
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # Spawn platforms
    platform_timer += 1
    if platform_timer > 120:
        platform_timer = 0
        platform = Platform(SCREEN_WIDTH, random.randint(200, SCREEN_HEIGHT - 100), random.randint(50, 150))
        all_sprites.add(platform)
        platforms.add(platform)

    # Update sprites
    all_sprites.update()

    # Check collisions
    if pygame.sprite.spritecollide(player, obstacles, True):
        lives -= 1
        if lives == 0:
            game_state = "gameover"

    # Level progression
    if score > level * 100:
        level += 1

    # Update highscore
    highscore = max(highscore, score)

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Draw score, level, and lives
    draw_text(f"Score: {score}", font, BLACK, 10, 10)
    draw_text(f"Level: {level}", font, BLACK, 10, 40)
    draw_text(f"Lives: {lives}", font, BLACK, 10, 70)
    draw_text(f"Highscore: {highscore}", font, BLACK, 10, 100)

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(FPS)

pygame.quit()
