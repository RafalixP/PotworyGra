import pygame
import sys
from pygame.locals import *
from settings import WIDTH, HEIGHT, FPS, DELAY_RESPAWN
from objects import Player, Bullet, Enemy, FastShootingBonus, BoostBonus #Bonus deleted
from ui import draw_text, show_menu, confirm_exit, game_over_screen
import random

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kosmiczny Atak Potworów")
clock = pygame.time.Clock()

shoot_sound = None
enemy_hit_sound = None
player_hit_sound = None

def spawn_bonus():
    bonus_classes = [FastShootingBonus, BoostBonus]
    bonus_class = random.choice(bonus_classes)
    return bonus_class()

def main():
    while True:
        difficulty = show_menu(screen)

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
                        if confirm_exit(screen):
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
                player.update_boost()

            for bullet in bullets[:]:
                bullet.update()
                if bullet.rect.bottom < 0:
                    bullets.remove(bullet)

            if pygame.time.get_ticks() - enemy_timer > 1500:
                if len(enemies) < difficulty:
                    enemies.append(Enemy())
                    enemy_timer = pygame.time.get_ticks()

            if pygame.time.get_ticks() - bonus_timer > 10000 and bonus is None:
                bonus = spawn_bonus()
                bonus_timer = pygame.time.get_ticks()

            for enemy in enemies[:]:
                enemy.update()
                if enemy.rect.top > HEIGHT:
                    player.lives = 0
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
                    if getattr(bonus, "bonus_type", None) == "fast_shooting":
                        player.shoot_delay = 250  # Faster shooting
                    elif getattr(bonus, "bonus_type", None) == "quick_move":
                        if player.speed >= 0.9 * 12:
                            player.speed = 12
                        else:
                            player.speed = min(12, 1.4 * player.speed)         # Faster movement (default is 6)
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

            if player.respawning and pygame.time.get_ticks() - player.last_hit_time > DELAY_RESPAWN:
                player.respawning = False
                player.rect.midbottom = (WIDTH // 2, HEIGHT - 10)

            player.draw(screen)
            for bullet in bullets:
                bullet.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            if bonus:
                bonus.draw(screen)

            draw_text(screen, f"Życia: {player.lives}", 10, 10)
            draw_text(screen, f"Wynik: {player.score}", 10, 40)
            draw_text(screen, f"Boost: {player.boost_gauge}%", 10, 70)

            pygame.display.flip()

            if player.lives <= 0:
                game_over_screen(screen)
                break

if __name__ == "__main__":
    main()