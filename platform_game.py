import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enhanced Platform Game with Evil Turtle")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)

# Player properties
player_width = 40
player_height = 60
player_x = 50
player_y = HEIGHT - player_height
player_speed = 5
jump_speed = -15
gravity = 0.8

# Turtle properties
turtle_width = 40
turtle_height = 40
turtle_x = WIDTH - turtle_width
turtle_y = HEIGHT - turtle_height
turtle_speed = 0

# Game objects
platforms = []
coins = []
diamonds = []

player_velocity_y = 0
score = 0
coins_collected = 0
start_time = time.time()
game_over = False

clock = pygame.time.Clock()

def generate_platforms():
    platforms = []
    y = HEIGHT - 100
    while y > 0:
        x = random.randint(0, WIDTH - 200)
        platforms.append(pygame.Rect(x, y, 200, 20))
        y -= random.randint(player_height, player_height + 50)
    return platforms

def generate_coin():
    while True:
        x = random.randint(0, WIDTH - 20)
        y = random.randint(0, HEIGHT - 20)
        coin = pygame.Rect(x, y, 20, 20)
        if not any(coin.colliderect(platform) for platform in platforms):
            return coin

def generate_diamond():
    while True:
        x = random.randint(0, WIDTH - 30)
        y = random.randint(0, HEIGHT - 30)
        diamond = pygame.Rect(x, y, 30, 30)
        if not any(diamond.colliderect(platform) for platform in platforms):
            return diamond

def update_game():
    global player_x, player_y, player_velocity_y, score, coins_collected, platforms, start_time, turtle_x, turtle_speed, game_over

    if game_over:
        return

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_x = max(0, min(player_x, WIDTH - player_width))

    player_velocity_y += gravity
    player_y += player_velocity_y

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    for platform in platforms:
        if player_rect.colliderect(platform) and player_velocity_y > 0:
            player_y = platform.top - player_height
            player_velocity_y = 0

    if player_y >= HEIGHT - player_height:
        player_y = HEIGHT - player_height
        player_velocity_y = 0

    if keys[pygame.K_SPACE] and player_velocity_y == 0:
        player_velocity_y = jump_speed

    for coin in coins[:]:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            coins.append(generate_coin())
            score += 1
            coins_collected += 1

    for diamond in diamonds[:]:
        if player_rect.colliderect(diamond):
            diamonds.remove(diamond)
            score += 5

    if coins_collected >= 20:
        coins_collected = 0
        diamonds.append(generate_diamond())

    if time.time() - start_time >= 60:
        start_time = time.time()
        platforms = generate_platforms()

    # Update turtle position
    turtle_speed = min(3, (time.time() - start_time) / 20)  # Increase speed over time, max 3
    turtle_x += random.choice([-1, 1]) * turtle_speed
    turtle_x = max(0, min(turtle_x, WIDTH - turtle_width))

    # Check for collision with turtle
    turtle_rect = pygame.Rect(turtle_x, turtle_y, turtle_width, turtle_height)
    if player_rect.colliderect(turtle_rect):
        game_over = True

def draw_game():
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))
    
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)
    
    for coin in coins:
        pygame.draw.rect(screen, YELLOW, coin)
    
    for diamond in diamonds:
        pygame.draw.rect(screen, CYAN, diamond)
    
    # Draw turtle
    pygame.draw.rect(screen, GREEN, (turtle_x, turtle_y, turtle_width, turtle_height))
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if game_over:
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(game_over_text, text_rect)

def main():
    global platforms, coins, game_over
    
    platforms = generate_platforms()
    coins = [generate_coin() for _ in range(5)]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:
                    # Reset the game
                    global player_x, player_y, player_velocity_y, score, coins_collected, start_time, turtle_x, turtle_speed
                    player_x = 50
                    player_y = HEIGHT - player_height
                    player_velocity_y = 0
                    score = 0
                    coins_collected = 0
                    start_time = time.time()
                    turtle_x = WIDTH - turtle_width
                    turtle_speed = 0
                    platforms = generate_platforms()
                    coins = [generate_coin() for _ in range(5)]
                    game_over = False

        update_game()
        draw_game()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()