import turtle


def Graphic_Init(width, height):
    turtle.setup(width, height)
    turtle.hideturtle()
    turtle.tracer(0)


def Graphic_draw_Dot(x, y, size=2, color="black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(size, color)


def Graphic_draw_Line(x0, y0, x1, y1) -> None:
    """
    :param x0: 起点x
    :param y0: 起点y
    :param x1: 终点x
    :param y1: 终点y
    """


def Graphic_finish_Draw():
    turtle.done()


if __name__ == "__main__":
    Graphic_Init(500, 500)
    Graphic_draw_Dot(0, 0)
    Graphic_finish_Draw()
