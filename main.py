import argparse

from window import Window
from cell import Cell
from maze import Maze

def main():
    parser = argparse.ArgumentParser(description='Maze Solver')

    parser.add_argument('--columns', type=int, default=20,
                        help='Number of columns in the maze')

    parser.add_argument('--rows', type=int, default=20,
                        help='Number of rows in the maze')

    parser.add_argument('--algorithm', type=str, default='iterative',
                        help='Choose if the generation and solving should be performed recursively or iteratively: recursive, iterative')

    parser.add_argument('--width', type=int, default=800,
                        help='Window width in pixels')

    parser.add_argument('--height', type=int, default=800,
                        help='Window height in pixels')

    parser.add_argument('--slow', action='store_true',
                        help='Run the program in slow mode so the programs work is easier to follow. For large mazes it can get a bit slow anyway :)')

    args = parser.parse_args()

    if args.algorithm not in ['recursive', 'iterative']:
        raise ValueError('Algorithm must be either "recursive" or "iterative"')

    win = Window(f"Maze Solver - Size: {args.columns}x{args.rows} Algorithm: {args.algorithm}", args.width, args.height)

    # Pass win to Maze and Cell class so they can use it to draw themselves
    Maze.set_win(win)
    Cell.set_win(win)

    # Calculate and set wall length to use based on maze and window size
    cell_wall_length = max(args.width / args.columns, args.height / args.rows)
    Cell.set_wall_length(cell_wall_length)

    maze = Maze(1, 1, args.rows, args.columns, args.algorithm, args.slow)
    maze.solve()

    win.wait_for_close()

if __name__ == '__main__':
    main()