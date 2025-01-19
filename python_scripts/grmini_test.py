import pygame
import random

pygame.init()

# Game window dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Plumber's Adventure")

# Load images
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
coin_img = pygame.image.load("coin.png")

# Game objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 400
        self.speed = 5
        self.is_jumping = False
        self.jump_speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
        if self.is_jumping:
            self.rect.y -= self.jump_speed
            self.jump_speed -= 1
            if self.jump_speed <= -10:
                self.is_jumping = False
                self.jump_speed = 10

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width)
        self.rect.y = 400
        self.speed = 3

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width)
        self.rect.y = 400

# Game groups
all_sprites = pygame.sprite.Group()
player = Player()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites.add(player)

# Create enemies and coins
for i in range(5):
    enemies.add(Enemy())
    coins.add(Coin())

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    all_sprites.update()

    # Check collisions
    if pygame.sprite.spritecollide(player, enemies, False):
        # Handle collision with enemy
        print("Hit by enemy!")

    if pygame.sprite.spritecollide(player, coins, True):
        # Handle collision with coin
        print("Collected a coin!")

    # Draw on the screen
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()