import pygame
import sys
from pygame.locals import *
from settings import WIDTH, HEIGHT, WHITE

def get_font():
    return pygame.font.SysFont("arial", 30)

def draw_text(screen, text, x, y):
    font = get_font()
    label = font.render(text, True, WHITE)
    screen.blit(label, (x, y))

def show_menu(screen):
    while True:
        screen.fill((0, 0, 0))
        draw_text(screen, "Kosmiczny Atak Potworów", 120, 200)
        draw_text(screen, "1 - Łatwy (1 potwór)", 180, 300)
        draw_text(screen, "2 - Średni (2 potwory)", 180, 350)
        draw_text(screen, "3 - Trudny (3 potwory)", 180, 400)
        draw_text(screen, "ESC - Wyjście", 180, 450)
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

def game_over_screen(screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 30)
    draw_text(screen, "Naciśnij dowolny klawisz, aby powrócić do menu", WIDTH // 2 - 220, HEIGHT // 2 + 20)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                waiting = False