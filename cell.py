from window import Window
from line import Line
from point import Point

WALL_LENGTH = 40

class Cell:
    __win: Window  = None

    def __init__(self, x, y):
        self.has_left_wall      = True
        self.has_right_wall     = True
        self.has_top_wall       = True
        self.has_bottom_wall    = True

        self.__x1 = x
        self.__y1 = y
        self.__x2 = x + WALL_LENGTH
        self.__y2 = y + WALL_LENGTH

        self.__visited = False

    def set_visited(self):
        self.__visited = True

    def is_visited(self):
        return self.__visited

    def reset_visited(self):
        self.__visited = False

    def __repr__(self):
        return f"Cell({self.__x1}, {self.__y1})"

    @classmethod
    def set_win(cls, win) -> None:
        cls.__win = win

    def draw(self) -> None:
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), 'black' if self.has_left_wall else 'white')
        self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), 'black' if self.has_right_wall else 'white')
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), 'black' if self.has_top_wall else 'white')
        self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), 'black' if self.has_bottom_wall else 'white')

    def draw_move(self, to_cell, undo:bool = False) -> None:
        fill_color = 'red' if not undo else 'grey'
        self.__win.draw_line(
            Line(
                Point(self.__x1 + WALL_LENGTH / 2, self.__y1 + WALL_LENGTH / 2),
                Point(to_cell.__x1 + WALL_LENGTH / 2, to_cell.__y1 + WALL_LENGTH / 2)
            ),
            fill_color
        )