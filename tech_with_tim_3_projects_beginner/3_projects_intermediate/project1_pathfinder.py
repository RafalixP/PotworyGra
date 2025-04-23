import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdsc, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdsc.addstr(i, j*3, "X", RED)
            else:
                stdsc.addstr(i, j*3, value, BLUE)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None
def find_path(maze, stdsc):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start) 

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdsc.clear()
        print_maze(maze, stdsc, path)
        time.sleep(0.1)
        stdsc.refresh()

        if maze[row][col] == end:
            return path
        
        neighbours = find_neighbours(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue

            r, c = neighbour
            if maze[r][c] == "#":
                continue
            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)

def find_neighbours(maze, row, col):
    neighbours = []

    if row > 0: # UP
        neighbours.append((row -1, col))
    if row + 1 < len(maze): # DOWN
        neighbours.append((row +1, col))
    if col > 0: # LEFT
        neighbours.append((row, col - 1))
    if col + 1 < len(maze[0]): #right
        neighbours.append((row, col + 1))
    
    return neighbours

def main(stdsc):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    find_path(maze, stdsc)
    #blue_and_black = curses.color_pair(1)
    #stdsc.addstr(5, 0, "hello world!", blue_and_black)
    stdsc.getch()

wrapper(main)

