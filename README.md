Simple maze solver implemented in Python. Created as part of speedrunning a one free month on boot.dev.

You can also set the window size and size of the maze in `main` along with the graphical size of cells by altering `WALL_LENGTH` in `cell.py`.

### Usage
```
usage: main.py [-h] [--columns COLUMNS] [--rows ROWS] [--algorithm ALGORITHM] [--width WIDTH] [--height HEIGHT] [--slow]

Maze Solver

options:
  -h, --help            show this help message and exit
  --columns COLUMNS     Number of columns in the maze
  --rows ROWS           Number of rows in the maze
  --algorithm ALGORITHM
                        Choose if the generation and solving should be performed recursively or iteratively: recursive, iterative
  --width WIDTH         Window width in pixels
  --height HEIGHT       Window height in pixels
  --slow                Run the program in slow mode so the programs work is easier to follow. For large mazes it can get a bit slow anyway :)
  ```

### Example run

![Screenshot](solved_maze.png)
