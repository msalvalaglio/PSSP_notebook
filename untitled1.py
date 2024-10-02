import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-bit Style Platform Game with Animation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

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
turtle_speed = 1

# Game objects
platforms = []
coins = []
diamonds = []
turtles = []

player_velocity_y = 0
score = 0
coins_collected = 0
start_time = time.time()
last_speed_increase = time.time()
game_over = False
level = 1
high_score = 0
paused = False  # Initialize paused here
lives = 3

clock = pygame.time.Clock()

# Animation variables
animation_frames = []
current_frame = 0
animation_speed = 5  # Lower is faster
animation_counter = 0
facing_right = True


def create_player_sprite(frame):
    sprite = pygame.Surface((player_width, player_height), pygame.SRCALPHA)
    sprite.fill((0, 0, 0, 0))  # Transparent
    
    # Body (adjust y position based on frame for "bobbing" effect)
    y_offset = 2 if frame % 2 == 0 else 0
    pygame.draw.rect(sprite, (0, 0, 255), (0, 20 + y_offset, player_width, player_height - 20 - y_offset))
    
    # Shirt
    pygame.draw.rect(sprite, (255, 0, 0), (0, 20 + y_offset, player_width, 20))
    
    # Face
    pygame.draw.rect(sprite, (255, 200, 150), (0, 5, player_width, 15))
    
    # Eyes (blink every 4th frame)
    if frame % 4 != 0:
        pygame.draw.rect(sprite, (0, 0, 255), (10, 10, 5, 5))
        pygame.draw.rect(sprite, (0, 0, 255), (25, 10, 5, 5))
    
    # Mustache
    pygame.draw.rect(sprite, BLACK, (5, 20, 30, 5))
    
    # Baseball cap
    pygame.draw.rect(sprite, RED, (0, 0, player_width, 5))
    pygame.draw.rect(sprite, RED, (0, 0, 5, 10))
    
    # Letter G
    font = pygame.font.Font(None, 20)
    letter_g = font.render("G", True, WHITE)
    sprite.blit(letter_g, (15, 22 + y_offset))
    
    return sprite

# Create animation frames
for i in range(4):  # 4 frames of animation
    animation_frames.append(create_player_sprite(i))

def create_turtle_sprite():
    sprite = pygame.Surface((turtle_width, turtle_height), pygame.SRCALPHA)
    sprite.fill((0, 255, 0, 0))  # Transparent green
    
    # Shell
    pygame.draw.rect(sprite, (0, 100, 0), (5, 5, 30, 30))
    pygame.draw.rect(sprite, (0, 200, 0), (10, 10, 20, 20))
    
    # Head
    pygame.draw.rect(sprite, (0, 255, 0), (0, 15, 5, 10))
    
    # Eyes
    pygame.draw.rect(sprite, (255, 255, 255), (0, 15, 2, 2))
    
    return sprite

def create_coin_sprite():
    sprite = pygame.Surface((20, 20), pygame.SRCALPHA)
    sprite.fill((0, 0, 0, 0))  # Transparent
    
    pygame.draw.rect(sprite, (255, 215, 0), (0, 0, 20, 20))
    pygame.draw.rect(sprite, (255, 255, 0), (2, 2, 16, 16))
    pygame.draw.rect(sprite, (255, 215, 0), (6, 6, 8, 8))
    
    return sprite

def create_diamond_sprite():
    sprite = pygame.Surface((30, 30), pygame.SRCALPHA)
    sprite.fill((0, 0, 0, 0))  # Transparent
    
    pygame.draw.polygon(sprite, (0, 191, 255), [(15, 0), (30, 15), (15, 30), (0, 15)])
    pygame.draw.polygon(sprite, (135, 206, 250), [(15, 5), (25, 15), (15, 25), (5, 15)])
    
    return sprite

player_sprite = create_player_sprite()
turtle_sprite = create_turtle_sprite()
coin_sprite = create_coin_sprite()
diamond_sprite = create_diamond_sprite()

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

def generate_turtle():
    x = random.choice([0, WIDTH - turtle_width])
    y = HEIGHT - turtle_height
    direction = 1 if x == 0 else -1
    return {'rect': pygame.Rect(x, y, turtle_width, turtle_height), 'direction': direction}

def update_game():
    global player_x, player_y, player_velocity_y, score, coins_collected, platforms, start_time, game_over, last_speed_increase, level, high_score, lives, turtle_speed, paused, current_frame, animation_counter, facing_right

    if game_over or paused:
        return

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    
    keys = pygame.key.get_pressed()
    moving = False
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        moving = True
        facing_right = False
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        moving = True
        facing_right = True

    # Update animation
    if moving:
        animation_counter += 1
        if animation_counter >= animation_speed:
            current_frame = (current_frame + 1) % len(animation_frames)
            animation_counter = 0
    else:
        current_frame = 0  # Reset to standing frame when not moving

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

    # Update turtle positions
    for turtle in turtles:
        turtle['rect'].x += turtle['direction'] * turtle_speed
        if turtle['rect'].left <= 0 or turtle['rect'].right >= WIDTH:
            turtle['direction'] *= -1

    # Check for collision with turtles
    for turtle in turtles:
        if player_rect.colliderect(turtle['rect']):
            lives -= 1
            if lives > 0:
                player_x = 50
                player_y = HEIGHT - player_height
                player_velocity_y = 0
                print("Lost one life")
            else:
                game_over = True

    # Increase turtle speed every 20 seconds
    if time.time() - last_speed_increase >= 20:
        turtle_speed *= 1.02  # Increase speed by 2%
        last_speed_increase = time.time()

    # Level up every 50 points
    new_level = score // 50 + 1
    if new_level > level:
        level = new_level
        turtles.append(generate_turtle())

    # Update high score
    high_score = max(high_score, score)


def draw_game():
    global paused
    
    screen.fill(WHITE)
    
    # Draw the player with animation
    player_sprite = animation_frames[current_frame]
    if not facing_right:
        player_sprite = pygame.transform.flip(player_sprite, True, False)
    screen.blit(player_sprite, (player_x, player_y))
    
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)
    
    for coin in coins:
        screen.blit(coin_sprite, coin)
    
    for diamond in diamonds:
        screen.blit(diamond_sprite, diamond)
    
    # Draw turtles
    for turtle in turtles:
        screen.blit(turtle_sprite, turtle['rect'])
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(level_text, (10, 50))

    high_score_text = font.render(f"High Score: {high_score}", True, BLACK)
    screen.blit(high_score_text, (10, 90))

    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(lives_text, (10, 130))

    if game_over:
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
        screen.blit(game_over_text, text_rect)

        font = pygame.font.Font(None, 36)
        play_again_text = font.render("Press R to play again or Q to quit", True, BLACK)
        text_rect = play_again_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
        screen.blit(play_again_text, text_rect)

    if paused:
        font = pygame.font.Font(None, 72)
        pause_text = font.render("PAUSED", True, BLACK)
        text_rect = pause_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(pause_text, text_rect)

def main():
    global platforms, coins, game_over, turtle_sprite, turtles, paused, lives, turtle_speed
    
    platforms = generate_platforms()
    coins = [generate_coin() for _ in range(5)]
    turtles = [generate_turtle()]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if game_over:
                    if event.key == pygame.K_r:
                        # Reset the game
                        global player_x, player_y, player_velocity_y, score, coins_collected, start_time, last_speed_increase, level, high_score
                        player_x = 50
                        player_y = HEIGHT - player_height
                        player_velocity_y = 0
                        score = 0
                        coins_collected = 0
                        start_time = time.time()
                        last_speed_increase = time.time()
                        turtle_speed = 1
                        turtle_sprite = create_turtle_sprite()
                        platforms = generate_platforms()
                        coins = [generate_coin() for _ in range(5)]
                        turtles = [generate_turtle()]
                        game_over = False
                        level = 1
                        lives = 3
                    elif event.key == pygame.K_q:
                        running = False

        update_game()
        draw_game()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()