import pygame
import sys
from pygame.locals import *
from settings import WIDTH, HEIGHT, WHITE
from scoreboard import get_top_scores, DIFFICULTY_NAMES

def get_font():
    return pygame.font.SysFont("arial", 30)

def draw_text(screen, text, x, y):
    font = get_font()
    label = font.render(text, True, WHITE)
    screen.blit(label, (x, y))

def show_menu(screen):
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, "Kosmiczny Atak Potworów", 165, 200)
        draw_text(screen, "1 - Łatwy (1 potwór)", 225, 300)
        draw_text(screen, "2 - Średni (2 potwory)", 225, 350)
        draw_text(screen, "3 - Trudny (3 potwory)", 225, 400)
        draw_text(screen, "4 - Tablica wyników", 225, 450)
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
                    show_scoreboard_menu(screen)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def confirm_exit(screen):
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, "Czy na pewno chcesz zakończyć grę? (T/N)", 100, HEIGHT // 2)
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

def get_player_name(screen):
    """Get player name for scoreboard"""
    name = ""
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, "Wprowadź swoje imię:", WIDTH // 2 - 150, HEIGHT // 2 - 50)
        draw_text(screen, name + "_", WIDTH // 2 - 100, HEIGHT // 2)
        draw_text(screen, "Naciśnij ENTER aby zatwierdzić", WIDTH // 2 - 180, HEIGHT // 2 + 50)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN and name.strip():
                    return name.strip()
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.unicode.isprintable() and len(name) < 15:
                    name += event.unicode

def show_scoreboard_menu(screen):
    """Show difficulty selection for scoreboard"""
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, "WYBIERZ POZIOM TRUDNOŚCI", WIDTH // 2 - 180, 200)
        draw_text(screen, "1 - Łatwy", WIDTH // 2 - 50, 300)
        draw_text(screen, "2 - Średni", WIDTH // 2 - 50, 350)
        draw_text(screen, "3 - Trudny", WIDTH // 2 - 50, 400)
        draw_text(screen, "4 - Expert", WIDTH // 2 - 50, 450)
        draw_text(screen, "ESC - Powrót", WIDTH // 2 - 50, 500)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    show_scoreboard(screen, 1)
                elif event.key == K_2:
                    show_scoreboard(screen, 2)
                elif event.key == K_3:
                    show_scoreboard(screen, 3)
                elif event.key == K_4:
                    show_scoreboard(screen, 4)
                elif event.key == K_ESCAPE:
                    return

def show_scoreboard(screen, difficulty):
    """Display scoreboard for specific difficulty"""
    scores = get_top_scores(difficulty)
    difficulty_name = DIFFICULTY_NAMES[difficulty]
    
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, f"TABLICA - {difficulty_name.upper()}", WIDTH // 2 - 120, 50)
        
        if not scores:
            draw_text(screen, "Brak wyników", WIDTH // 2 - 80, HEIGHT // 2)
        else:
            y = 120
            for i, score in enumerate(scores[:20]):  # Show top 20
                place_text = f"{i+1:2d}. {score['name'][:12]:<12} {score['score']:>6}    {score['date']}"
                draw_text(screen, place_text, 50, y)
                y += 30
                if y > HEIGHT - 100:
                    break
        
        draw_text(screen, "Naciśnij ESC aby wrócić", WIDTH // 2 - 150, HEIGHT - 50)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

def game_over_screen(screen, player_score=0, difficulty=2):
    """Game over screen with optional score saving"""
    if player_score > 0:
        name = get_player_name(screen)
        from scoreboard import add_score
        add_score(name, player_score, difficulty)
    
    screen.fill((0, 0, 0))
    draw_text(screen, "GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 30)
    draw_text(screen, "Naciśnij dowolny klawisz, aby powrócić do menu", WIDTH // 2 - 265, HEIGHT // 2 + 20)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                waiting = False