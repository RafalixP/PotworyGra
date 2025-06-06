import pygame
from settings import GREEN, WHITE, RED, BLUE

player_img = pygame.Surface((50, 30), pygame.SRCALPHA)
pygame.draw.polygon(player_img, GREEN, [(0, 30), (25, 0), (50, 30)])

bullet_img = pygame.Surface((5, 10))
bullet_img.fill(WHITE)

enemy_img = pygame.Surface((40, 30), pygame.SRCALPHA)
pygame.draw.rect(enemy_img, RED, (0, 10, 40, 10))
pygame.draw.rect(enemy_img, RED, (15, 0, 10, 30))

bonus_img = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(bonus_img, BLUE, (10, 10), 10)