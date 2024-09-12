import random
import pygame
from pygame.constants import QUIT

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
player_size = (20, 20)

player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_speed = [1, 1]

ball_size = 20
ball = pygame.Surface((ball_size, ball_size))
ball.fill(COLOR_WHITE)
ball_rect = ball.get_rect()
ball_speed = [2, 2]

playing = True

# Встановлюємо початкову позицію м'яча
ball_rect.topleft = (random.randint(0, WIDTH - ball_size), random.randint(0, HEIGHT - ball_size))

while playing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    # рух гравця (при цьому гравець просто рухається вгору/вниз)
    if player_rect.bottom >= HEIGHT:
        player_speed[1] = -1
    if player_rect.top <= 0:
        player_speed[1] = 1

    # зіткнення м'яча з лівою та верхньою межами
    if ball_rect.left <= 0:  # Відбивається від лівої межі
        ball_speed[0] *= -1
    if ball_rect.top <= 0:  # Відбивається від верхньої межі
        ball_speed[1] *= -1

    # Також можемо додати перевірки на зіткнення з правою і нижньою межами
    if ball_rect.right >= WIDTH:  # Відбивається від правої межі
        ball_speed[0] *= -1
    if ball_rect.bottom >= HEIGHT:  # Відбивається від нижньої межі
        ball_speed[1] *= -1

    main_display.blit(player, player_rect)
    main_display.blit(ball, ball_rect)

    player_rect = player_rect.move(player_speed)
    ball_rect = ball_rect.move(ball_speed)

    pygame.display.flip()

pygame.quit()
