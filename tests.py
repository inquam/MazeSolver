import unittest
from window import Window
from maze import Maze
from cell import Cell

class TestMaze(unittest.TestCase):
    def setUp(self):
        win = Window("Maze Solver - Tests", 800, 600)
        # Pass win to Maze and Cell class so they can use it to draw themselves
        Maze.set_win(win)
        Cell.set_win(win)

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(2, 2, num_rows, num_cols)
        self.assertEqual(
            len(m1.get_cells()),
            num_cols,
        )
        self.assertEqual(
            len(m1.get_cells()[0]),
            num_rows,
        )

        visited = False

        for cols in m1.get_cells():
            for cell in cols:
                visited = cell.is_visited() or visited

        self.assertEqual(
            visited,
            False
        )

if __name__ == "__main__":
    unittest.main()