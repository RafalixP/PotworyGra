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
        draw_text(screen, "1 - Łatwy (1 potwór)", 225, 280)
        draw_text(screen, "2 - Średni (2 potwory)", 225, 320)
        draw_text(screen, "3 - Trudny (3 potwory)", 225, 360)
        draw_text(screen, "4 - Expert (4 potwory)", 225, 400)
        draw_text(screen, "5 - Tablica wyników", 225, 450)
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
                if event.key == K_5:
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
        draw_text(screen, "ENTER - zapisz, ESC - pomiń", WIDTH // 2 - 150, HEIGHT // 2 + 50)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN and name.strip():
                    return name.strip()
                elif event.key == K_ESCAPE:
                    return None
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.unicode.isprintable() and len(name) < 15:
                    name += event.unicode

def show_scoreboard_menu(screen):
    """Show difficulty selection for scoreboard"""
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, "TABLICA WYNIKÓW", WIDTH // 2 - 180, 150)
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

def show_scoreboard(screen, difficulty, highlight_entry=None):
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
                # Highlight if this is the recent game entry (exact match)
                if (highlight_entry and 
                    score['score'] == highlight_entry['score'] and 
                    score['date'] == highlight_entry['date'] and 
                    score['name'] == highlight_entry['name']):
                    # Draw background highlight
                    pygame.draw.rect(screen, (50, 50, 100), (45, y+6, WIDTH-90, 25))
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

def countdown(screen):
    """Show 3-2-1 countdown before game starts"""
    font = pygame.font.SysFont("arial", 120)
    for count in [3, 2, 1]:
        screen.fill((0, 0, 0))
        text = font.render(str(count), True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)
    
    # Show "GO!" briefly
    screen.fill((0, 0, 0))
    go_text = font.render("GO!", True, (0, 255, 0))
    go_rect = go_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(go_text, go_rect)
    pygame.display.flip()
    pygame.time.wait(500)

def game_over_screen(screen, player_score=0, difficulty=2, game_time=0):
    """Game over screen with optional score saving"""
    # Format time display
    hours = game_time // 3600
    minutes = (game_time % 3600) // 60
    seconds = game_time % 60
    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    # Show final score and time
    screen.fill((0, 0, 0))
    draw_text(screen, "GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 100)
    draw_text(screen, f"Wynik: {player_score}", WIDTH // 2 - 80, HEIGHT // 2 - 50)
    draw_text(screen, f"Czas: {time_str}", WIDTH // 2 - 80, HEIGHT // 2 - 20)
    draw_text(screen, "Naciśnij ENTER aby kontynuować", WIDTH // 2 - 200, HEIGHT // 2 + 20)
    pygame.display.flip()
    
    # Wait for ENTER key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    waiting = False
    
    # Save score if > 0
    if player_score > 0:
        name = get_player_name(screen)
        if name:  # Only save if name was entered (not ESC)
            from scoreboard import add_score
            new_entry = add_score(name, player_score, difficulty)
            show_scoreboard(screen, difficulty, highlight_entry=new_entry)