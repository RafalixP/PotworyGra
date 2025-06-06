import pygame
import random
import sys
from pygame.locals import *

# Inicjalizacja
pygame.init()

# Dźwięki
shoot_sound = None  # pygame.mixer.Sound("shoot.wav")
enemy_hit_sound = None  # pygame.mixer.Sound("enemy_hit.wav")
player_hit_sound = None  # pygame.mixer.Sound("player_hit.wav")

# Parametry gry
delay_respawn = 2000
WIDTH, HEIGHT = 600, 800
FPS = 60
FONT = pygame.font.SysFont("arial", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kosmiczny Atak Potworów")
clock = pygame.time.Clock()

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Gracz - nowa grafika (trójkąt)
player_img = pygame.Surface((50, 30), pygame.SRCALPHA)
pygame.draw.polygon(player_img, GREEN, [(0, 30), (25, 0), (50, 30)])

# Pocisk
bullet_img = pygame.Surface((5, 10))
bullet_img.fill(WHITE)

# Potwór - nowa grafika (krzyżak)
enemy_img = pygame.Surface((40, 30), pygame.SRCALPHA)
pygame.draw.rect(enemy_img, RED, (0, 10, 40, 10))
pygame.draw.rect(enemy_img, RED, (15, 0, 10, 30))

# Bonus
bonus_img = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(bonus_img, BLUE, (10, 10), 10)

class Player:
    def __init__(self):
        self.image = player_img
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))
        self.speed = 5
        self.lives = 3
        self.score = 0
        self.respawning = False
        self.last_hit_time = 0
        self.shoot_delay = 500
        self.last_shot_time = 0
        self.bonus_active = False

    def move(self, keys):
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self):
        if not self.respawning:
            screen.blit(self.image, self.rect)

class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -8

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

class Enemy:
    def __init__(self):
        self.image = enemy_img
        self.rect = self.image.get_rect(midtop=(random.randint(20, WIDTH - 20), 0))
        self.speed = 3

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

class Bonus:
    def __init__(self):
        self.image = bonus_img
        self.rect = self.image.get_rect(midtop=(random.randint(20, WIDTH - 20), 0))
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

def draw_text(text, x, y):
    label = FONT.render(text, True, WHITE)
    screen.blit(label, (x, y))

def show_menu():
    while True:
        screen.fill((0, 0, 0))
        draw_text("Kosmiczny Atak Potworów", 120, 200)
        draw_text("1 - Łatwy (1 potwór)", 180, 300)
        draw_text("2 - Średni (2 potwory)", 180, 350)
        draw_text("3 - Trudny (3 potwory)", 180, 400)
        draw_text("ESC - Wyjście", 180, 450)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    return 1
                if event.key == K_2:
                    return 2
                if event.key == K_3:
                    return 3
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def confirm_exit():
    while True:
        screen.fill((0, 0, 0))
        draw_text("Czy na pewno chcesz zakończyć grę? (T/N)", 100, HEIGHT // 2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_t:
                    return True
                if event.key == K_n:
                    return False

def game_over_screen():
    screen.fill((0, 0, 0))
    draw_text("GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 30)
    draw_text("Naciśnij dowolny klawisz, aby powrócić do menu", WIDTH // 2 - 220, HEIGHT // 2 + 20)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                waiting = False

def main():
    while True:
        difficulty = show_menu()

        player = Player()
        bullets = []
        enemies = []
        bonus = None
        enemy_timer = 0
        bonus_timer = 0

        running = True
        while running:
            clock.tick(FPS)
            screen.fill((0, 0, 0))

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        if confirm_exit():
                            running = False

            # Strzał
            if keys[K_SPACE] and not player.respawning:
                now = pygame.time.get_ticks()
                if now - player.last_shot_time > player.shoot_delay:
                    bullets.append(Bullet(player.rect.centerx, player.rect.top))
                    if shoot_sound:
                        shoot_sound.play()
                    player.last_shot_time = now

            if not player.respawning:
                player.move(keys)

            for bullet in bullets[:]:
                bullet.update()
                if bullet.rect.bottom < 0:
                    bullets.remove(bullet)

            if pygame.time.get_ticks() - enemy_timer > 1500:
                if len(enemies) < difficulty:
                    enemies.append(Enemy())
                    enemy_timer = pygame.time.get_ticks()

            if pygame.time.get_ticks() - bonus_timer > 10000 and bonus is None:
                bonus = Bonus()
                bonus_timer = pygame.time.get_ticks()

            for enemy in enemies[:]:
                enemy.update()
                if enemy.rect.top > HEIGHT:
                    player.lives = 0  # Potwór dotarł do dołu — gra kończy się
                    break
                if enemy.rect.colliderect(player.rect) and not player.respawning:
                    player.lives -= 1
                    player.respawning = True
                    player.last_hit_time = pygame.time.get_ticks()
                    player.shoot_delay = 500
                    player.bonus_active = False
                    if player_hit_sound:
                        player_hit_sound.play()
                    enemies.remove(enemy)

            if bonus:
                bonus.update()
                if bonus.rect.top > HEIGHT:
                    bonus = None
                elif bonus.rect.colliderect(player.rect):
                    player.shoot_delay = 250
                    player.bonus_active = True
                    bonus = None

            for bullet in bullets[:]:
                for enemy in enemies[:]:
                    if bullet.rect.colliderect(enemy.rect):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        if enemy_hit_sound:
                            enemy_hit_sound.play()
                        player.score += 1
                        if player.score % 10 == 0:
                            player.lives += 1
                        break

            if player.respawning and pygame.time.get_ticks() - player.last_hit_time > delay_respawn:
                player.respawning = False
                player.rect.midbottom = (WIDTH // 2, HEIGHT - 10)

            player.draw()
            for bullet in bullets:
                bullet.draw()
            for enemy in enemies:
                enemy.draw()
            if bonus:
                bonus.draw()

            draw_text(f"Życia: {player.lives}", 10, 10)
            draw_text(f"Wynik: {player.score}", 10, 40)

            pygame.display.flip()

            if player.lives <= 0:
                game_over_screen()
                break

if __name__ == "__main__":
    main()
