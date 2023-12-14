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

while playing:
    FPS.tick(120)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
            
    main_display.fill(COLOR_BLACK)

    if player_rect.bottom >= HEIGHT:
        player_speed = [1, -1]	

    if player_rect.top <= 0:
        player_speed = [1, 1]

    if ball_rect.left <= 0 or ball_rect.top <= 0:
        ball_speed[0] *= -1
        ball_speed[1] *= -1

    main_display.blit(player, player_rect)
    main_display.blit(ball, ball_rect)

    player_rect = player_rect.move(player_speed)
    ball_rect = ball_rect.move(ball_speed)

    pygame.display.flip()

pygame.quit()
