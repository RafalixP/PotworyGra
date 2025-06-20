import pygame
import sys
from pygame.locals import *
from settings import WIDTH, HEIGHT, FPS, DELAY_RESPAWN, DIFFICULTY_SETTINGS
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
        difficulty_level = show_menu(screen)
        diff_settings = DIFFICULTY_SETTINGS.get(difficulty_level, DIFFICULTY_SETTINGS[2])  # Default to medium

        player = Player()
        player.lives = diff_settings['player_lives']  # Set lives based on difficulty
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

            if pygame.time.get_ticks() - enemy_timer > diff_settings['enemy_spawn_delay']:
                if len(enemies) < diff_settings['max_enemies']:
                    enemy = Enemy()
                    enemy.speed *= diff_settings['enemy_speed_multiplier']  # Apply speed multiplier
                    enemies.append(enemy)
                    enemy_timer = pygame.time.get_ticks()

            if pygame.time.get_ticks() - bonus_timer > diff_settings['bonus_spawn_delay'] and bonus is None:
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
                    # Usuń wrogów którzy są blisko dołu ekranu
                    enemies[:] = [e for e in enemies if e.rect.bottom < HEIGHT - 100]

            if bonus:
                bonus.update()
                if bonus.rect.top > HEIGHT:
                    bonus = None
                elif bonus.rect.colliderect(player.rect):
                    if getattr(bonus, "bonus_type", None) == "fast_shooting":
                        player.shoot_delay = max(150, 0.75 * player.shoot_delay)  # 150 ms minimum delay
                    elif getattr(bonus, "bonus_type", None) == "boost":
                        if player.speed >= 0.9 * 12:
                            player.speed = 12
                        else:
                            player.speed = min(12, 1.15 * player.speed)         # Faster movement (default is 6)
                    player.bonus_active = True
                    bonus = None

            for bullet in bullets[:]:
                for enemy in enemies[:]:
                    if bullet.rect.colliderect(enemy.rect):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        if enemy_hit_sound:
                            enemy_hit_sound.play()
                        player.score += diff_settings['score_multiplier']
                        if player.score % 10 == 0:
                            player.lives += 1
                        break
                
                if bonus and bullet.rect.colliderect(bonus.rect):
                    bullets.remove(bullet)
                    bonus = None

            if player.respawning and pygame.time.get_ticks() - player.last_hit_time > DELAY_RESPAWN:
                player.respawning = False
                player.rect.midbottom = (WIDTH // 2, HEIGHT - 10)
                player.velocity_x = 0  # Reset velocity to prevent drift

            player.draw(screen)
            for bullet in bullets:
                bullet.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            if bonus:
                bonus.draw(screen)

            draw_text(screen, f"Życia: {player.lives}", 10, 10)
            draw_text(screen, f"Wynik: {player.score}", 10, 40)
            draw_text(screen, f"Boost: {player.boost_gauge}%", WIDTH - 150, 10)
            
            # Fast shooting indicator
            if player.shoot_delay < 500:  # Default is 500, so anything less means fast shooting is active
                draw_text(screen, "Fast Shooting", WIDTH - 150, 40)

            pygame.display.flip()

            if player.lives <= 0:
                game_over_screen(screen)
                break

if __name__ == "__main__":
    main()