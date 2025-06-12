import pygame
import random
from settings import WIDTH, HEIGHT
from assets import player_img, bullet_img, enemy_img, fast_shooting_img, quick_move_img, bonus_img

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
        self.base_speed = 6
        self.speed = self.base_speed
        self.lives = 3
        self.score = 0
        self.respawning = False
        self.last_hit_time = 0
        self.shoot_delay = 500
        self.last_shot_time = 0  # <-- Add this line
        self.boost_gauge = 0  # 0 to 100

    def move(self, keys):
        from pygame.locals import K_LEFT, K_RIGHT
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        if not self.respawning:
            super().draw(screen)

    def update_boost(self):
        # Decay speed if above base_speed
        if self.speed > self.base_speed:
            self.speed = max(self.base_speed, self.speed - 0.0005)  # or your chosen decay
        # Update boost gauge
        if self.speed >= 11.99:  # Use a tolerance instead of 12
            self.boost_gauge = 100
        else:
            self.boost_gauge = int(100 * (self.speed - self.base_speed) / (12 - self.base_speed))
        self.boost_gauge = max(0, min(100, self.boost_gauge))

class Bullet(GameObject):
    def __init__(self, x, y):
        super().__init__(bullet_img, bullet_img.get_rect(center=(x, y)))
        self.speed = -10

    def update(self):
        """
        Updates the position of the bullet by moving it upward.
        """
        self.rect.y += self.speed

class Enemy(GameObject):
    def __init__(self):
        super().__init__(enemy_img, enemy_img.get_rect(midtop=(random.randint(20, WIDTH - 20), 0)))
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

class Bonus(GameObject):
    def __init__(self, image):
        super().__init__(image, image.get_rect(midtop=(random.randint(20, WIDTH - 20), 0)))
        self.speed = 4
        print('Bonus')

    def update(self):
        self.rect.y += self.speed
        

class FastShootingBonus(Bonus):
    def __init__(self):
        super().__init__(fast_shooting_img)
        self.bonus_type = "fast_shooting"

class BoostBonus(Bonus):
    def __init__(self):
        super().__init__(quick_move_img)
        self.bonus_type = "quick_move"