import pygame
import sys
import gc
import asyncio
from pygame.locals import *
from settings import WIDTH, HEIGHT, FPS, DELAY_RESPAWN, DIFFICULTY_SETTINGS
from objects import Player, Bullet, Enemy, FastShootingBonus, BoostBonus
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

async def main():
    while True:
        difficulty_level = await show_menu_async(screen)
        diff_settings = DIFFICULTY_SETTINGS.get(difficulty_level, DIFFICULTY_SETTINGS[2])

        player = Player(diff_settings['life_threshold_multiplier'])
        player.lives = diff_settings['player_lives']
        bullets = []
        enemies = []
        bonus = None
        enemy_timer = 0
        bonus_timer = 0
        game_start_time = pygame.time.get_ticks()
        
        # Progressive difficulty variables
        current_max_enemies = diff_settings['max_enemies']
        current_spawn_delay = diff_settings['enemy_spawn_delay']
        current_speed_multiplier = diff_settings['enemy_speed_multiplier']
        
        # Text rendering cache
        last_lives = -1
        last_score = -1
        last_boost = -1
        last_timer = -1
        cached_texts = {}
        
        # Performance monitoring
        frame_count = 0
        last_fps_check = pygame.time.get_ticks()
        last_gc_time = pygame.time.get_ticks()
        
        # Disable automatic garbage collection
        gc.disable()

        running = True
        while running:
            # Dynamic FPS adjustment
            current_fps = FPS
            if frame_count > 60:
                avg_frame_time = (pygame.time.get_ticks() - last_fps_check) / 60
                if avg_frame_time > 20:
                    current_fps = 45
                if frame_count % 60 == 0:
                    last_fps_check = pygame.time.get_ticks()
            
            dt = clock.tick(current_fps)
            frame_count += 1
            
            skip_heavy_processing = (frame_count % 4 == 0) and (dt > 20)
            
            current_time = pygame.time.get_ticks()
            if current_time - last_gc_time > 5000 and dt < 18:
                gc.collect()
                last_gc_time = current_time
            
            screen.fill((0, 0, 0))

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            # Shooting
            if keys[K_SPACE] and not player.respawning:
                now = pygame.time.get_ticks()
                if now - player.last_shot_time > player.shoot_delay:
                    bullets.append(Bullet(player.rect.centerx, player.rect.top))
                    player.last_shot_time = now

            if not player.respawning:
                player.move(keys)
                player.update_boost()

            # Update bullets
            for bullet in bullets:
                bullet.update()
            bullets = [bullet for bullet in bullets if bullet.rect.bottom >= 0]
            
            if len(bullets) > 50:
                bullets = bullets[-50:]

            # Progressive difficulty
            if difficulty_level > 1 and not skip_heavy_processing:
                game_time = (pygame.time.get_ticks() - game_start_time) / 1000
                progression = game_time * diff_settings['progression_rate']
                
                current_max_enemies = min(diff_settings['max_enemies'] + 2, 
                                        diff_settings['max_enemies'] + int(progression * 2))
                
                current_spawn_delay = max(300, 
                                        diff_settings['enemy_spawn_delay'] - int(progression * 200))
                
                current_speed_multiplier = min(diff_settings['enemy_speed_multiplier'] * 2,
                                             diff_settings['enemy_speed_multiplier'] + progression)
            
            if pygame.time.get_ticks() - enemy_timer > current_spawn_delay:
                if len(enemies) < current_max_enemies:
                    enemy = Enemy()
                    enemy.speed *= current_speed_multiplier
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
                    enemies.remove(enemy)
                    enemies[:] = [e for e in enemies if e.rect.bottom < HEIGHT - 100]

            if bonus:
                bonus.update()
                if bonus.rect.top > HEIGHT:
                    bonus = None
                elif bonus.rect.colliderect(player.rect):
                    player.score += 1
                    if player.score >= player.next_life_threshold:
                        player.lives += 1
                        player.next_life_threshold *= 2
                    
                    if getattr(bonus, "bonus_type", None) == "fast_shooting":
                        player.shoot_delay = max(150, 0.75 * player.shoot_delay)
                    elif getattr(bonus, "bonus_type", None) == "boost":
                        if player.speed >= 0.9 * 12:
                            player.speed = 12
                        else:
                            player.speed = min(12, 1.15 * player.speed)
                    player.bonus_active = True
                    bonus = None

            # Collision detection
            bullets_to_remove = set()
            enemies_to_remove = set()
            
            for i, bullet in enumerate(bullets):
                if i in bullets_to_remove:
                    continue
                    
                bullet_hit = False
                
                for j, enemy in enumerate(enemies):
                    if j in enemies_to_remove:
                        continue
                    if bullet.rect.colliderect(enemy.rect):
                        bullets_to_remove.add(i)
                        enemies_to_remove.add(j)
                        player.score += diff_settings['score_multiplier']
                        if player.score >= player.next_life_threshold:
                            player.lives += 1
                            player.next_life_threshold *= 2
                        bullet_hit = True
                        break
                
                if not bullet_hit and bonus and bullet.rect.colliderect(bonus.rect):
                    bullets_to_remove.add(i)
                    bonus = None
            
            bullets = [bullet for i, bullet in enumerate(bullets) if i not in bullets_to_remove]
            enemies = [enemy for i, enemy in enumerate(enemies) if i not in enemies_to_remove]

            if player.respawning and pygame.time.get_ticks() - player.last_hit_time > DELAY_RESPAWN:
                player.respawning = False
                player.rect.midbottom = (WIDTH // 2, HEIGHT - 10)
                player.velocity_x = 0

            player.draw(screen)
            for bullet in bullets:
                bullet.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            if bonus:
                bonus.draw(screen)

            # Cached text rendering
            elapsed_time = (pygame.time.get_ticks() - game_start_time) // 1000
            if elapsed_time != last_timer:
                hours = elapsed_time // 3600
                minutes = (elapsed_time % 3600) // 60
                seconds = elapsed_time % 60
                cached_texts['timer'] = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                last_timer = elapsed_time
            
            if player.lives != last_lives:
                cached_texts['lives'] = f"Życia: {player.lives}"
                last_lives = player.lives
                
            if player.score != last_score:
                cached_texts['score'] = f"Wynik: {player.score}"
                last_score = player.score
                
            if player.boost_gauge != last_boost:
                cached_texts['boost'] = f"Boost: {player.boost_gauge}%"
                last_boost = player.boost_gauge
            
            draw_text(screen, cached_texts.get('timer', '00:00:00'), WIDTH // 2 - 50, 10)
            draw_text(screen, cached_texts.get('lives', 'Życia: 0'), 10, 10)
            draw_text(screen, cached_texts.get('score', 'Wynik: 0'), 10, 40)
            draw_text(screen, cached_texts.get('boost', 'Boost: 0%'), WIDTH - 150, 10)
            
            if player.shoot_delay < 500:
                draw_text(screen, "Fast Shooting", WIDTH - 150, 40)

            pygame.display.flip()
            await asyncio.sleep(0)  # Allow other tasks to run

            if player.lives <= 0:
                break

async def show_menu_async(screen):
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, "Kosmiczny Atak Potworów", 165, 200)
        draw_text(screen, "1 - Łatwy (1 potwór)", 225, 280)
        draw_text(screen, "2 - Średni (2 potwory)", 225, 320)
        draw_text(screen, "3 - Trudny (3 potwory)", 225, 360)
        draw_text(screen, "4 - Expert (4 potwory)", 225, 400)
        draw_text(screen, "ESC - Wyjście", 225, 500)
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
                if event.key == K_4:
                    return 4
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())