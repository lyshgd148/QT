import turtle


def Graphic_Init(width, height):
    turtle.setup(width, height)
    turtle.hideturtle()
    turtle.tracer(0)


def Graphic_draw_Dot(color="black"):
    turtle.pensize(1)
    turtle.penup()
    turtle.dot(5, color)
    pass


def Graphic_finish_Draw():
    turtle.done()


if __name__ == "__main_":
    pass
