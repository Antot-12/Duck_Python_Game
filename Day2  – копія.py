import random
import pygame
from pygame.constants import QUIT

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()

player_speed = [0, 0]

bonus_size = 20
bonus_speed = [0, 2]

enemy_size = 20
enemy_speed = [1, 0]

playing = True

bonuses = []
enemies = []

def create_bonus():
    x = random.randint(0, WIDTH - bonus_size)
    y = 0
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return pygame.Rect(x, y, bonus_size, bonus_size), color

def create_enemy():
    x = random.randint(0, WIDTH - enemy_size)
    y = HEIGHT // 2
    return pygame.Rect(x, y, enemy_size, enemy_size)

while playing:
    FPS.tick(120)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_speed[0] = -2
    elif keys[pygame.K_RIGHT]:
        player_speed[0] = 2
    else:
        player_speed[0] = 0
    
    if keys[pygame.K_UP]:
        player_speed[1] = -2
    elif keys[pygame.K_DOWN]:
        player_speed[1] = 2
    else:
        player_speed[1] = 0

    # Перевірка обмежень для гравця
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WIDTH:
        player_rect.right = WIDTH
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

    main_display.fill(COLOR_BLACK)

    for bonus_rect, bonus_color in bonuses:
        pygame.draw.rect(main_display, bonus_color, bonus_rect)
        bonus_rect.move_ip(bonus_speed)
    
    for enemy_rect in enemies:
        pygame.draw.rect(main_display, COLOR_RED, enemy_rect)
        enemy_rect.move_ip(enemy_speed)
    
    if random.random() < 0.02:
        bonuses.append(create_bonus())
    if random.random() < 0.01:
        enemies.append(create_enemy())

    player_rect.move_ip(player_speed)

    pygame.draw.rect(main_display, COLOR_WHITE, player_rect)
    
    bonuses = [bonus for bonus in bonuses if bonus[0].bottom <= HEIGHT]
    enemies = [enemy for enemy in enemies if enemy.right <= WIDTH]

    pygame.display.flip()

pygame.quit()
