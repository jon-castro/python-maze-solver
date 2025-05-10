from tkinter import Canvas


class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

        
class Line:
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2
        
    def draw(self, canvas, fill_color="black"):
       canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)


class Cell:
    def __init__(
            self,
            x1,
            y1,
            x2,
            y2,
            win,
            has_left_wall=True,
            has_right_wall=True,
            has_top_wall=True,
            has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        
    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(
                Point(self._x1, self._y1),
                Point(self._x1, self._y2),
                "black"
            )
        if self.has_right_wall:
            self._win.draw_line(
                Point(self._x2, self._y1),
                Point(self._x2, self._y2),
                "black"
            )
        if self.has_top_wall:
            self._win.draw_line(
                Point(self._x1, self._y1),
                Point(self._x2, self._y1),
                "black"
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Point(self._x1, self._y2),
                Point(self._x2, self._y2),
                "black"
            )