from window import Window
from line import Line
from point import Point

class Cell:
    __win: Window  = None
    __wall_length: int = 20

    def __init__(self, x, y):
        self.has_left_wall      = True
        self.has_right_wall     = True
        self.has_top_wall       = True
        self.has_bottom_wall    = True

        self.__x1 = x
        self.__y1 = y
        self.__x2 = x + self.__wall_length
        self.__y2 = y + self.__wall_length

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

    @classmethod
    def set_wall_length(cls, length) -> None:
        cls.__wall_length = length

    @classmethod
    def get_wall_length(self) -> int:
        return self.__wall_length

    def draw(self) -> None:
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), 'black' if self.has_left_wall else 'white')
        self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), 'black' if self.has_right_wall else 'white')
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), 'black' if self.has_top_wall else 'white')
        self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), 'black' if self.has_bottom_wall else 'white')

    def draw_move(self, to_cell, undo:bool = False) -> None:
        fill_color = 'red' if not undo else 'grey'
        self.__win.draw_line(
            Line(
                Point(self.__x1 + self.__wall_length / 2, self.__y1 + self.__wall_length / 2),
                Point(to_cell.__x1 + self.__wall_length / 2, to_cell.__y1 + self.__wall_length / 2)
            ),
            fill_color
        )