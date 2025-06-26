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

        player = Player(diff_settings['life_threshold_multiplier'])
        player.lives = diff_settings['player_lives']  # Set lives based on difficulty
        bullets = []
        enemies = []
        bonus = None
        enemy_timer = 0
        bonus_timer = 0
        game_start_time = pygame.time.get_ticks()  # Track game start time
        
        # Progressive difficulty variables
        current_max_enemies = diff_settings['max_enemies']
        current_spawn_delay = diff_settings['enemy_spawn_delay']
        current_speed_multiplier = diff_settings['enemy_speed_multiplier']

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
                            # Save score when player exits
                            if player.score > 0:
                                game_over_screen(screen, player.score, difficulty_level)
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

            # Update bullets and remove off-screen ones efficiently
            for bullet in bullets:
                bullet.update()
            bullets = [bullet for bullet in bullets if bullet.rect.bottom >= 0]
            
            # Limit bullet count to prevent memory issues
            if len(bullets) > 50:
                bullets = bullets[-50:]

            # Progressive difficulty increase (except for easy mode)
            if difficulty_level > 1:
                game_time = (pygame.time.get_ticks() - game_start_time) / 1000  # Time in seconds
                progression = game_time * diff_settings['progression_rate']
                
                # Gradually increase max enemies (cap at +2 from base)
                current_max_enemies = min(diff_settings['max_enemies'] + 2, 
                                        diff_settings['max_enemies'] + int(progression * 2))
                
                # Gradually decrease spawn delay (minimum 300ms)
                current_spawn_delay = max(300, 
                                        diff_settings['enemy_spawn_delay'] - int(progression * 200))
                
                # Gradually increase speed (cap at 2x base speed)
                current_speed_multiplier = min(diff_settings['enemy_speed_multiplier'] * 2,
                                             diff_settings['enemy_speed_multiplier'] + progression)
            
            if pygame.time.get_ticks() - enemy_timer > current_spawn_delay:
                if len(enemies) < current_max_enemies:
                    enemy = Enemy()
                    enemy.speed *= current_speed_multiplier  # Apply progressive speed multiplier
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
                    # Award 1 point for collecting bonus
                    player.score += 1
                    # Check for life threshold after bonus collection
                    if player.score >= player.next_life_threshold:
                        player.lives += 1
                        player.next_life_threshold *= 2
                    
                    if getattr(bonus, "bonus_type", None) == "fast_shooting":
                        player.shoot_delay = max(150, 0.75 * player.shoot_delay)  # 150 ms minimum delay
                    elif getattr(bonus, "bonus_type", None) == "boost":
                        if player.speed >= 0.9 * 12:
                            player.speed = 12
                        else:
                            player.speed = min(12, 1.15 * player.speed)         # Faster movement (default is 6)
                    player.bonus_active = True
                    bonus = None

            # Optimized collision detection
            bullets_to_remove = set()
            enemies_to_remove = set()
            
            for i, bullet in enumerate(bullets):
                if i in bullets_to_remove:
                    continue
                    
                bullet_hit = False
                
                # Check bullet-enemy collisions
                for j, enemy in enumerate(enemies):
                    if j in enemies_to_remove:
                        continue
                    if bullet.rect.colliderect(enemy.rect):
                        bullets_to_remove.add(i)
                        enemies_to_remove.add(j)
                        if enemy_hit_sound:
                            enemy_hit_sound.play()
                        player.score += diff_settings['score_multiplier']
                        # Progressive life system
                        if player.score >= player.next_life_threshold:
                            player.lives += 1
                            player.next_life_threshold *= 2
                        bullet_hit = True
                        break
                
                # Check bullet-bonus collision
                if not bullet_hit and bonus and bullet.rect.colliderect(bonus.rect):
                    bullets_to_remove.add(i)
                    bonus = None
            
            # Remove bullets and enemies efficiently
            bullets = [bullet for i, bullet in enumerate(bullets) if i not in bullets_to_remove]
            enemies = [enemy for i, enemy in enumerate(enemies) if i not in enemies_to_remove]

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

            # Game timer at top center
            elapsed_time = (pygame.time.get_ticks() - game_start_time) // 1000
            hours = elapsed_time // 3600
            minutes = (elapsed_time % 3600) // 60
            seconds = elapsed_time % 60
            timer_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            draw_text(screen, timer_text, WIDTH // 2 - 50, 10)
            
            draw_text(screen, f"Życia: {player.lives}", 10, 10)
            draw_text(screen, f"Wynik: {player.score}", 10, 40)
            draw_text(screen, f"Boost: {player.boost_gauge}%", WIDTH - 150, 10)
            
            # Fast shooting indicator
            if player.shoot_delay < 500:  # Default is 500, so anything less means fast shooting is active
                draw_text(screen, "Fast Shooting", WIDTH - 150, 40)

            pygame.display.flip()

            if player.lives <= 0:
                game_over_screen(screen, player.score, difficulty_level)
                break

if __name__ == "__main__":
    main()