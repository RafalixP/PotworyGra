import sys
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pygame Test")
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30, 30, 30))
        # Rysujemy prostokąt w środku ekranu
        pygame.draw.rect(screen, (200, 40, 40), pygame.Rect(270, 190, 100, 100))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()