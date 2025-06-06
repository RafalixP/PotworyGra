import sys
import random
import pygame

# ----------------------------
# Konfiguracja gry
# ----------------------------

# Rozmiary siatki (wiersze, kolumny)
ROWS = 10
COLS = 20

# Rozmiar jednego bloku w pikselach
BLOCK_SIZE = 30

# Wymiary okna
SCREEN_WIDTH = COLS * BLOCK_SIZE
SCREEN_HEIGHT = ROWS * BLOCK_SIZE

# Kolory
BLACK = (0, 0, 0)
GRID_COLOR = (40, 40, 40)
COLORS = {
    'I': (0, 240, 240),
    'O': (240, 240, 0),
    'T': (160, 0, 240),
    'L': (240, 160, 0),
    'S': (0, 240, 0),
}

# Definicja klocków (5 różnych)
SHAPES = {
    'I': [
        [(0,1), (1,1), (2,1), (3,1)],
        [(2,0), (2,1), (2,2), (2,3)],
    ],
    'O': [
        [(0,0), (1,0), (0,1), (1,1)],
    ],
    'T': [
        [(1,0), (0,1), (1,1), (2,1)],
        [(1,0), (1,1), (2,1), (1,2)],
        [(0,1), (1,1), (2,1), (1,2)],
        [(1,0), (0,1), (1,1), (1,2)],
    ],
    'L': [
        [(0,0), (0,1), (0,2), (1,2)],
        [(0,1), (1,1), (2,1), (0,2)],
        [(0,0), (1,0), (1,1), (1,2)],
        [(2,0), (0,1), (1,1), (2,1)],
    ],
    'S': [
        [(1,0), (2,0), (0,1), (1,1)],
        [(1,0), (1,1), (2,1), (2,2)],
        [(1,1), (2,1), (0,2), (1,2)],
        [(0,0), (0,1), (1,1), (1,2)],
    ],
}

# Częstotliwość ruchu w lewo (ms)
MOVE_INTERVAL = 500

# ----------------------------
# Klasa reprezentująca klocek
# ----------------------------
class Piece:
    def __init__(self, shape_key):
        self.shape_key = shape_key
        self.rotations = SHAPES[shape_key]
        self.rotation = 0  # indeks bieżącej rotacji
        self.color = COLORS[shape_key]
        # Obliczenie początkowej pozycji tak, aby cały klocek znajdował się przy prawej krawędzi
        coords = self.current_shape()
        max_x = max(x for x, y in coords)
        max_y = max(y for x, y in coords)
        # Pozycja X: najbardziej na prawo minus szerokość klocka
        self.x = COLS - 1 - max_x
        # Pozycja Y: wyśrodkowanie w pionie
        self.y = (ROWS // 2) - (max_y // 2)
    
    def current_shape(self):
        """Zwraca listę współrzędnych (x, y) bieżącej rotacji."""
        return self.rotations[self.rotation]
    
    def cells(self):
        """Zwraca zbiór współrzędnych w siatce (kolumna, wiersz)."""
        return [(self.x + x, self.y + y) for x, y in self.current_shape()]
    
    def rotate(self, grid):
        """Próba obrócenia klocka (zmiana rotacji o +1)."""
        next_rot = (self.rotation + 1) % len(self.rotations)
        coords = self.rotations[next_rot]
        # Sprawdzenie kolizji i granic
        for x_off, y_off in coords:
            new_x = self.x + x_off
            new_y = self.y + y_off
            if not (0 <= new_x < COLS and 0 <= new_y < ROWS):
                return  # poza polem
            if grid[new_y][new_x] is not None:
                return  # zderzenie z istniejącym blokiem
        # Jeśli ok, zmień rotację
        self.rotation = next_rot
    
    def can_move(self, dx, dy, grid):
        """Sprawdza, czy można przesunąć klocek o (dx, dy)."""
        for x_off, y_off in self.current_shape():
            new_x = self.x + x_off + dx
            new_y = self.y + y_off + dy
            if not (0 <= new_x < COLS and 0 <= new_y < ROWS):
                return False
            if grid[new_y][new_x] is not None:
                return False
        return True
    
    def move(self, dx, dy):
        """Przesunięcie bez sprawdzania kolizji."""
        self.x += dx
        self.y += dy

# ----------------------------
# Funkcje pomocnicze
# ----------------------------
def create_grid():
    """Tworzy pustą siatkę."""
    return [[None for _ in range(COLS)] for _ in range(ROWS)]

def lock_piece(piece, grid):
    """Zamraża bieżący klocek w siatce."""
    for x_cell, y_cell in piece.cells():
        grid[y_cell][x_cell] = piece.color

def spawn_new_piece():
    """Losuje i zwraca nowy klocek."""
    key = random.choice(list(SHAPES.keys()))
    return Piece(key)

def is_game_over(piece, grid):
    """Sprawdza, czy nowy klocek koliduje od razu (koniec gry)."""
    return not piece.can_move(0, 0, grid)

# ----------------------------
# Inicjalizacja Pygame
# ----------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Side Tetris")
clock = pygame.time.Clock()

# Timer ruchu w lewo
MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, MOVE_INTERVAL)

# ----------------------------
# Główna pętla gry
# ----------------------------
def main():
    grid = create_grid()
    current_piece = spawn_new_piece()
    if is_game_over(current_piece, grid):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Ruch automatyczny w lewo co MOVE_INTERVAL ms
            elif event.type == MOVE_EVENT:
                if current_piece.can_move(-1, 0, grid):
                    current_piece.move(-1, 0)
                else:
                    # Zamrożenie klocka i nowy klocek
                    lock_piece(current_piece, grid)
                    current_piece = spawn_new_piece()
                    if is_game_over(current_piece, grid):
                        print("Game Over!")
                        running = False

            # Obsługa klawiszy
            elif event.type == pygame.KEYDOWN:
                # Obrót (klawisz SPACJA)
                if event.key == pygame.K_SPACE:
                    current_piece.rotate(grid)

                # Ruch w górę (strzałka GÓRA)
                elif event.key == pygame.K_UP:
                    if current_piece.can_move(0, -1, grid):
                        current_piece.move(0, -1)

                # Ruch w dół (strzałka DÓŁ)
                elif event.key == pygame.K_DOWN:
                    if current_piece.can_move(0, 1, grid):
                        current_piece.move(0, 1)

                # Natychmiastowe umieszczenie po lewej (strzałka LEWO)
                elif event.key == pygame.K_LEFT:
                    # Przesuwaj aż do kolizji
                    while current_piece.can_move(-1, 0, grid):
                        current_piece.move(-1, 0)
                    # Zamroź i nowy klocek
                    lock_piece(current_piece, grid)
                    current_piece = spawn_new_piece()
                    if is_game_over(current_piece, grid):
                        print("Game Over!")
                        running = False

        # Czyszczenie ekranu
        screen.fill(BLACK)

        # Rysowanie siatki
        for row in range(ROWS):
            for col in range(COLS):
                rect = pygame.Rect(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, GRID_COLOR, rect, 1)
                if grid[row][col] is not None:
                    pygame.draw.rect(screen, grid[row][col], rect)

        # Rysowanie bieżącego klocka
        for x_cell, y_cell in current_piece.cells():
            rect = pygame.Rect(x_cell * BLOCK_SIZE, y_cell * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, current_piece.color, rect)

        # Odświeżanie ekranu
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()