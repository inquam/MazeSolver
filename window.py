from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, title: str, width: int, height: int):
        self.__width        = width
        self.__height       = height
        self.__is_running   = False
        self.__root         = Tk()

        self.__root.title(title)

        self.__canvas = Canvas(self.__root, width=self.__width, height=self.__height, background="white")
        self.__canvas.pack()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True

        while self.__is_running:
            self.redraw()

    def close(self) -> None:
        self.__is_running = False

    def draw_line(self, line: Line, fill_color: str = 'black') -> None:
        line.draw(self.__canvas, fill_color)