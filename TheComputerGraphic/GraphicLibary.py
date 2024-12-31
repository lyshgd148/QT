import turtle


def Graphic_Init(width, height):
    turtle.setup(width, height)
    turtle.hideturtle()
    turtle.tracer(0)


def Graphic_draw_Dot(x, y, size=2, color="black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(size, color)


def Graphic_draw_Line(x0, y0, x1, y1, color="black") -> None:
    """ :param x0: 起点x  :param y0: 起点y :param x1: 终点x :param y1: 终点y """
    if x0 != x1 and y0 != y1:
        k = (y1 - y0) / (x1 - x0)
        if 0 < k <= 1:

            pass
        elif k > 1:
            pass
        elif -1 <= k < 0:
            pass
        elif k < -1:
            pass
    elif x0 == x1 and y0 != y1:
        while y0 <= y1:
            Graphic_draw_Dot(x0, y0, color=color)
            y0 += 1

    elif x0 != x1 and y0 == y1:
        while x0 <= x1:
            Graphic_draw_Dot(x0, y0, color=color)
            x0 += 1


def Graphic_finish_Draw():
    turtle.done()


if __name__ == "__main__":
    Graphic_Init(500, 500)
    Graphic_draw_Line(2, 2, 2, 90)
    Graphic_draw_Line(2, 2, 100, 2)

    Graphic_finish_Draw()
