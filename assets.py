import pygame
from settings import GREEN, WHITE, RED, BLUE, ORANGE

# Additional colors for different boost types
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)
PURPLE = (128, 0, 128)

player_img = pygame.Surface((50, 30), pygame.SRCALPHA)
pygame.draw.polygon(player_img, GREEN, [(0, 30), (25, 0), (50, 30)])

bullet_img = pygame.Surface((5, 10))
bullet_img.fill(WHITE)

enemy_img = pygame.Surface((40, 30), pygame.SRCALPHA)
pygame.draw.rect(enemy_img, RED, (0, 10, 40, 10))
pygame.draw.rect(enemy_img, RED, (15, 0, 10, 30))

bonus_img = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(bonus_img, BLUE, (10, 10), 10)

fast_shooting_img = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(fast_shooting_img, ORANGE, (10, 10), 10)  # <-- draw on fast_shooting_img

# Different boost bonus images
small_boost_img = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(small_boost_img, LIGHT_BLUE, (10, 10), 10)  # Light blue for small boost

medium_boost_img = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(medium_boost_img, BLUE, (10, 10), 10)       # Blue for medium boost

large_boost_img = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(large_boost_img, DARK_BLUE, (10, 10), 10)   # Dark blue for large boost

# Keep the old quick_move_img for backward compatibility
quick_move_img = medium_boost_img