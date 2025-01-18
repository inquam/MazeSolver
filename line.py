from point import Point
from tkinter import Tk, Canvas

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.__start_point  = start_point
        self.__end_point    = end_point

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.__start_point.x, self.__start_point.y,
            self.__end_point.x, self.__end_point.y,
            fill=fill_color,
            width=2
        )