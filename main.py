from window import Window
from objects import Line, Point

win = Window(800, 600)
p1 = Point(100, 100)
p2 = Point(200, 200)
line1 = win.draw_line(Line(p1, p2), "black")
win.wait_for_close()
