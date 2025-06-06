import pygame
import random
from settings import WIDTH, HEIGHT
from assets import player_img, bullet_img, enemy_img, bonus_img

class GameObject:
    def __init__(self, image, rect):
        """
        Initialize a GameObject instance.

        Args:
            image (pygame.Surface): The image representing the object.
            rect (pygame.Rect): The rectangle defining the object's position and size.
        """
        self.image = image
        self.rect = rect

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player(GameObject):
    def __init__(self):
        super().__init__(player_img, player_img.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10)))
        self.speed = 5
        self.lives = 3
        self.score = 0
        self.respawning = False
        self.last_hit_time = 0
        self.shoot_delay = 500
        self.last_shot_time = 0
        self.bonus_active = False

    def move(self, keys):
        from pygame.locals import K_LEFT, K_RIGHT
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        if not self.respawning:
            super().draw(screen)

class Bullet(GameObject):
    def __init__(self, x, y):
        super().__init__(bullet_img, bullet_img.get_rect(center=(x, y)))
        self.speed = -8

    def update(self):
        self.rect.y += self.speed

class Enemy(GameObject):
    def __init__(self):
        super().__init__(enemy_img, enemy_img.get_rect(midtop=(random.randint(20, WIDTH - 20), 0)))
        self.speed = 3

    def update(self):
        self.rect.y += self.speed

class Bonus(GameObject):
    def __init__(self):
        super().__init__(bonus_img, bonus_img.get_rect(midtop=(random.randint(20, WIDTH - 20), 0)))
        self.speed = 2

    def update(self):
        self.rect.y += self.speed