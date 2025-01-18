import time
import random

from window import Window
from cell import Cell, WALL_LENGTH

class Maze:
    __win: Window = None

    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            seed = None
    ):
        self.__x: int                       = x
        self.__y: int                       = y
        self.__num_rows: int                = num_rows
        self.__num_cols: int                = num_cols
        self.__seed: int                    = seed if seed is not None else random.seed(seed)
        self.__cells: list[list[Cell]]|None = None
        self.__create_cells()

    def get_cells(self) -> list:
        return self.__cells

    @classmethod
    def set_win(cls, win) -> None:
        cls.__win = win

    def __create_cells(self) -> None:
        self.__cells = []

        for i in range(self.__num_cols):
            col = []
            for j in range(self.__num_rows):
                x = self.__x + (i * WALL_LENGTH)
                y = self.__y + (j * WALL_LENGTH)
                col.append(Cell(x, y))

            self.__cells.append(col)

        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[0])):
                self.__draw_cell(i, j)

        self.__break_entrance_and_exit()
        self.__break_walls_r()
        self.__reset_cells_visited()

    def __break_entrance_and_exit(self) -> None:
        """
        Creates entrance and exit.
        :return:
        """
        self.__cells[0][0].has_left_wall = False
        self.__draw_cell(0, 0)
        self.__cells[len(self.__cells) - 1][len(self.__cells[0]) - 1].has_right_wall = False
        self.__draw_cell(len(self.__cells) - 1, len(self.__cells[0]) - 1)

    def __break_walls_r(self, i=0, j=0, visited=None) -> None:
        """
        Breaks walls and creates a way through the maze
        :param i:
        :param j:
        :param visited:
        :return:
        """
        # Initialize visited set on first call
        if visited is None:
            visited = set()

        # Mark current cell as visited using tuple of coordinates
        visited.add((i, j))

        while True:
            # List to store possible directions as (i, j) coordinates
            possible_directions = []

            # Check all adjacent cells (up, right, down, left)
            # Up
            if j > 0 and (i, j - 1) not in visited:
                possible_directions.append((i, j - 1))
            # Right
            if i < self.__num_cols - 1 and (i + 1, j) not in visited:
                possible_directions.append((i + 1, j))
            # Down
            if j < self.__num_rows - 1 and (i, j + 1) not in visited:
                possible_directions.append((i, j + 1))
            # Left
            if i > 0 and (i - 1, j) not in visited:
                possible_directions.append((i - 1, j))

            # If no unvisited neighbors, we're done with this cell
            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return

            # Choose a random direction
            next_cell = random.choice(possible_directions)
            next_i, next_j = next_cell

            # Break down walls between current cell and chosen cell
            if next_i < i:  # Moving left
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_i][next_j].has_right_wall = False
            elif next_i > i:  # Moving right
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_i][next_j].has_left_wall = False
            elif next_j < j:  # Moving up
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False
            else:  # Moving down
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_i][next_j].has_top_wall = False

            # Draw current cell after breaking walls
            self.__draw_cell(i, j)

            # Recursively visit the next cell
            self.__break_walls_r(next_i, next_j, visited)

    def __reset_cells_visited(self) -> None:
        for coll in self.__cells:
            for cell in coll:
                cell.reset_visited()


    def __draw_cell(self, i:int, j:int) -> None:
        x = self.__x + (i * WALL_LENGTH)
        y = self.__y + (j * WALL_LENGTH)

        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self) -> None:
        self.__win.redraw()
        time.sleep(0.05)

    def solve(self) -> None:
        return self.__solve_r(0, 0)

    def __solve_r(self, i: int, j: int) -> bool:
        self.__animate()

        # Mark current cell as visited
        self.__cells[i][j].set_visited()

        # Did we reach the exit?
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        # Try each direction
        # Try moving right
        if (i < self.__num_cols - 1 and  # cell exists
                not self.__cells[i][j].has_right_wall and  # no wall blocking
                not self.__cells[i + 1][j].is_visited()):  # not visited
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self.__solve_r(i + 1, j):
                return True
            self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)  # undo

        # Try moving down
        if (j < self.__num_rows - 1 and
                not self.__cells[i][j].has_bottom_wall and
                not self.__cells[i][j + 1].is_visited()):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self.__solve_r(i, j + 1):
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)  # undo

        # Try moving left
        if (i > 0 and
                not self.__cells[i][j].has_left_wall and
                not self.__cells[i - 1][j].is_visited()):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self.__solve_r(i - 1, j):
                return True
            self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)  # undo

        # Try moving up
        if (j > 0 and
                not self.__cells[i][j].has_top_wall and
                not self.__cells[i][j - 1].is_visited()):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self.__solve_r(i, j - 1):
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)  # undo

        # If no direction worked, this path is a dead end
        return False