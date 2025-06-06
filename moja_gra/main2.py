import sys
import os
import pygame

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Image Test")

# Kolory (RGB)
BLACK = (0, 0, 0)

# Ścieżka do obrazka (vista.png powinno być w tym samym folderze co main.py)
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "vista.png")

# Wczytanie obrazka
# Używamy convert_alpha(), aby zachować ewentualną przezroczystość w PNG
try:
    image = pygame.image.load(IMAGE_PATH).convert_alpha()
except pygame.error as e:


# --- dodajemy tutaj poniższy blok ---

# Zmienna określająca skalę (1.0 = oryginalny rozmiar)
    scale = 0.5  # ← tutaj możesz ustawić dowolną wartość

    # Skalowanie obrazka według wartości scale
    orig_width, orig_height = image.get_size()
    new_size = (int(orig_width * scale), int(orig_height * scale))
    image = pygame.transform.scale(image, new_size)


# Pobranie prostokąta obrazka
image_rect = image.get_rect()

# Ustawienie początkowej pozycji obrazka: wyśrodkowanie
image_rect.x = SCREEN_WIDTH // 2 - image_rect.width // 2
image_rect.y = SCREEN_HEIGHT // 2 - image_rect.height // 2

# Prędkości przesuwu obrazka (piksele na klatkę)
vx = 5
vy = 3

clock = pygame.time.Clock()

def main():
    global vx, vy

    running = True
    while running:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Przesunięcie obrazka
        image_rect.x += vx
        image_rect.y += vy

        # Sprawdzenie kolizji z krawędziami okna i odbicie
        if image_rect.x <= 0:
            image_rect.x = 0
            vx = -vx
        elif image_rect.x + image_rect.width >= SCREEN_WIDTH:
            image_rect.x = SCREEN_WIDTH - image_rect.width
            vx = -vx

        if image_rect.y <= 0:
            image_rect.y = 0
            vy = -vy
        elif image_rect.y + image_rect.height >= SCREEN_HEIGHT:
            image_rect.y = SCREEN_HEIGHT - image_rect.height
            vy = -vy

        # Rysowanie: najpierw czyścimy ekran, potem rysujemy obrazek
        screen.fill(BLACK)
        screen.blit(image, image_rect)

        # Odświeżenie wyświetlacza
        pygame.display.flip()

        # Utrzymanie stałego FPS (np. 60 klatek na sekundę)
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
