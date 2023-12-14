import random
import pygame
from pygame.constants import QUIT, KEYDOWN, K_RETURN
from pygame.locals import RLEACCEL
import os

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

# Завантаження зображень гравця, бонусів, ворогів та фону
player_frames = [pygame.image.load(f'1-{i}.png') for i in range(1, 6)]
player_frame_idx = 0
player_img = player_frames[player_frame_idx]
player_img = pygame.transform.scale(player_img, (144, 144))
player_img.set_colorkey((0, 0, 0), RLEACCEL)

ANIMATION_INTERVAL = 1000
last_frame_update = pygame.time.get_ticks()

bonus_img = pygame.image.load('bonus.png')
bonus_img = pygame.transform.scale(bonus_img, (180, 180))
bonus_img.set_colorkey((0, 0, 0), RLEACCEL)

enemy_img = pygame.image.load('enemy.png')
enemy_img = pygame.transform.scale(enemy_img, (180, 180))
enemy_img.set_colorkey((0, 0, 0), RLEACCEL)

background_img = pygame.image.load('background.png')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_rect = player_img.get_rect()
player_speed = [0, 0]

bonus_size = 180
bonus_speed = [0, 3]

enemy_size = 180
enemy_speed = [-3, 0]

playing = True
game_over = False
player_score = 0
player_health = 100

bonuses = []
enemies = []

player_rect.topleft = (0, random.randint(0, HEIGHT - player_rect.height))

score_font = pygame.font.Font(None, 36)

def create_bonus():
    x = random.randint(0, WIDTH - bonus_size)
    y = random.randint(0, HEIGHT - bonus_size)
    return pygame.Rect(x, y, bonus_size, bonus_size)

def create_enemy():
    x = WIDTH
    y = random.randint(0, HEIGHT - enemy_size)
    return pygame.Rect(x, y, enemy_size, enemy_size)

while playing:
    while game_over:
        main_display.fill(COLOR_BLACK)
        main_display.blit(background_img, (0, 0))
        game_over_text = score_font.render(f'Game Over. Score: {player_score}. Press Enter to play again.', True, COLOR_RED)
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.center = (WIDTH // 2, HEIGHT // 2)
        main_display.blit(game_over_text, game_over_text_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
                game_over = False
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    game_over = False
                    player_score = 0
                    bonuses.clear()
                    enemies.clear()
                    player_rect.topleft = (0, random.randint(0, HEIGHT - player_rect.height))
                    player_health = 100

    if player_health <= 0:
        game_over = True

    FPS.tick(120)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_speed[0] = -4
    elif keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_speed[0] = 4
    else:
        player_speed[0] = 0
    
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_speed[1] = -4
    elif keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
        player_speed[1] = 4
    else:
        player_speed[1] = 0

    main_display.blit(background_img, (0, 0))

    for bonus_rect in bonuses:
        main_display.blit(bonus_img, bonus_rect)
        bonus_rect.move_ip(bonus_speed)
    
    for enemy_rect in enemies:
        main_display.blit(enemy_img, enemy_rect)
        enemy_rect.move_ip(enemy_speed)
    
    if len(bonuses) < 6 and random.random() < 0.03:
        bonuses.append(create_bonus())
    if len(enemies) < 9 and random.random() < 0.02:
        enemies.append(create_enemy())

    player_rect.move_ip(player_speed)
    
    # Обробка зіткнень гравця з бонусами
    collected_bonuses = [bonus for bonus in bonuses if player_rect.colliderect(bonus)]
    for bonus in collected_bonuses:
        player_score += 1
        bonuses.remove(bonus)

    # Обробка зіткнень гравця з ворогами
    hit_enemies = [enemy for enemy in enemies if player_rect.colliderect(enemy)]
    if len(hit_enemies) >= 2:
        player_health = 0
        game_over = True
    for enemy in hit_enemies:
        enemies.remove(enemy)
        # Вороги наносять шкоду гравцю
        player_health -= 50  # Зменшено кількість життя гравця на половину

    current_time = pygame.time.get_ticks()
    if current_time - last_frame_update > ANIMATION_INTERVAL:
        last_frame_update = current_time
        player_frame_idx = (player_frame_idx + 1) % len(player_frames)
        player_img = player_frames[player_frame_idx]

    health_text = score_font.render(f'Health: {player_health}', True, COLOR_RED)
    main_display.blit(health_text, (10, 10))

    score_text = score_font.render(f'Score: {player_score}', True, COLOR_RED)
    main_display.blit(score_text, (10, 50))

    main_display.blit(player_img, player_rect)

    pygame.display.flip()

pygame.quit()
