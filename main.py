from window import Window
from cell import Cell
from maze import Maze

def main():
    win = Window("Maze Solver", 800, 800)

    # Pass win to Maze and Cell class so they can use it to draw themselves
    Maze.set_win(win)
    Cell.set_win(win)

    maze = Maze(2, 2, 20, 20)
    maze.solve()

    win.wait_for_close()

if __name__ == '__main__':
    main()