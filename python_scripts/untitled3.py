import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 960
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PLAYER_SPEED = 5
ALIEN_SPEED = 2
BULLET_SPEED = 7
ALIEN_DROP = 10
FPS = 60
INITIAL_LIVES = 3
ALIEN_ROWS = 3
ALIEN_COLS = 10
ALIEN_WIDTH = 50
ALIEN_HEIGHT = 30
ALIEN_SPACING_X = 70
ALIEN_SPACING_Y = 50
NEW_ALIENS_PER_LEVEL = 2
ALIEN_DROP_INCREASE = 5
HIGH_SCORE_FILE = "high_score.txt"

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load high score
def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    return 0

# Save high score
def save_high_score(score):
    high_score = load_high_score()
    if score > high_score:
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))

# Draw X-Wing (Player Ship)
def draw_xwing(surface, x, y):
    pygame.draw.rect(surface, GREEN, (x, y, 50, 30))  # Body
    pygame.draw.rect(surface, BLACK, (x + 5, y + 10, 10, 10))  # Cockpit
    pygame.draw.rect(surface, GREEN, (x + 5, y, 10, 5))  # Front wing
    pygame.draw.rect(surface, GREEN, (x + 35, y, 10, 5))  # Back wing

# Draw TIE Fighter (Alien Ship)
def draw_tiefighter(surface, x, y):
    pygame.draw.rect(surface, RED, (x, y, 50, 30))  # Body
    pygame.draw.rect(surface, BLACK, (x + 5, y + 5, 10, 20))  # Cockpit
    pygame.draw.rect(surface, RED, (x + 15, y, 10, 30))  # Vertical wing
    pygame.draw.rect(surface, RED, (x + 25, y, 10, 30))  # Vertical wing

# Initialize player
player_rect = pygame.Rect(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 50, 50, 30)

# Initialize aliens
def create_aliens(level):
    aliens = []
    rows = ALIEN_ROWS + (level - 1)  # Increase rows of aliens with each level
    cols = ALIEN_COLS
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(50 + col * ALIEN_SPACING_X, 50 + row * ALIEN_SPACING_Y, ALIEN_WIDTH, ALIEN_HEIGHT)
            aliens.append(rect)
    return aliens

aliens = create_aliens(1)  # Start with level 1 aliens

# Initialize bullets
bullets = []

# Game variables
score = 0
lives = INITIAL_LIVES
level = 1
alien_speed = ALIEN_SPEED
alien_drop_rate = ALIEN_DROP

def move_aliens():
    global alien_speed, alien_drop_rate
    for alien in aliens:
        alien.x += alien_speed
    if any(alien.right > SCREEN_WIDTH or alien.left < 0 for alien in aliens):
        for alien in aliens:
            alien.x -= alien_speed
            alien.y += alien_drop_rate
        alien_speed = -alien_speed

def handle_bullets():
    global bullets
    new_bullets = []
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        if bullet.y > 0:
            new_bullets.append(bullet)
    bullets = new_bullets

def check_collisions():
    global aliens, bullets, score
    new_aliens = []
    new_bullets = []
    for alien in aliens:
        hit = False
        for bullet in bullets:
            if alien.colliderect(bullet):
                hit = True
                score += 100
                break
        if not hit:
            new_aliens.append(alien)
    for bullet in bullets:
        if not any(alien.colliderect(bullet) for alien in aliens):
            new_bullets.append(bullet)
    aliens = new_aliens
    bullets = new_bullets

def check_game_over():
    global lives
    for alien in aliens:
        if alien.bottom >= SCREEN_HEIGHT:
            lives -= 1
            if lives <= 0:
                return True
            else:
                return False
    return False

def increase_difficulty():
    global level, alien_speed, alien_drop_rate, aliens
    if not aliens:  # Check if all aliens are destroyed
        level += 1
        alien_speed += 1
        alien_drop_rate += ALIEN_DROP_INCREASE
        aliens = create_aliens(level)  # Reset aliens to the new total

def draw_game_info():
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, WHITE)
    lives_text = font.render(f'Lives: {lives}', True, WHITE)
    level_text = font.render(f'Level: {level}', True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    screen.blit(level_text, (10, 90))

def draw_intro_screen():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 72)
    title_text = font.render("SPACE INVADERS", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3))

    instructions_font = pygame.font.SysFont(None, 48)
    instructions_text = instructions_font.render("Press SPACE to start", True, WHITE)
    screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.flip()
    wait_for_space()

def draw_game_over_screen():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("GAME OVER", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))

    score_font = pygame.font.SysFont(None, 48)
    score_text = score_font.render(f'Final Score: {score}', True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

    high_score = load_high_score()
    high_score_text = score_font.render(f'High Score: {high_score}', True, WHITE)
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    save_high_score(score)

    restart_text = score_font.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 150))

    pygame.display.flip()
    wait_for_restart_or_quit()

def wait_for_space():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

def wait_for_restart_or_quit():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()  # Restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    global score, lives, level, alien_speed, alien_drop_rate, aliens, bullets

    # Game reset variables
    score = 0
    lives = INITIAL_LIVES
    level = 1
    alien_speed = ALIEN_SPEED
    alien_drop_rate = ALIEN_DROP
    aliens = create_aliens(level)
    bullets = []

    clock = pygame.time.Clock()
    
    draw_intro_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet_rect = pygame.Rect(player_rect.centerx - 2.5, player_rect.top - 10, 5, 10)
                    bullets.append(bullet_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:
            player_rect.x += PLAYER_SPEED

        move_aliens()
        handle_bullets()
        check_collisions()
        if check_game_over():
            draw_game_over_screen()
            break
        increase_difficulty()

        screen.fill(BLACK)
        draw_xwing(screen, player_rect.x, player_rect.y)
        for alien in aliens:
            draw_tiefighter(screen, alien.x, alien.y)
        for bullet in bullets:
            pygame.draw.rect(screen, BLUE, bullet)
        draw_game_info()

        pygame.display.flip()
        clock.tick(FPS)

    print("Game Over!")
    print(f'Final Score: {score}')
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
