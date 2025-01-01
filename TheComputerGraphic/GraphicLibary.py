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
    """ 中点画线算法 """
    if x0 != x1 and y0 != y1:
        A = -(y1 - y0)
        B = (x1 - x0)
        AA = int(2 * A)
        BB = int(2 * B)
        k = (-A) / B
        # print(k)
        if 0 < k <= 1:
            d_old = int(AA + B)
            Graphic_draw_Dot(x0, y0, color=color)
            while x0 < x1:
                x0 += 1
                if d_old <= 0:
                    y0 += 1
                    Graphic_draw_Dot(x0, y0, color=color)
                    d_old = d_old + AA + BB
                elif d_old > 0:
                    Graphic_draw_Dot(x0, y0, color=color)
                    d_old = d_old + AA
            Graphic_draw_Dot(x1, y1, color=color)
        elif k > 1:
            d_old = int(A + BB)
            Graphic_draw_Dot(x0, y0, color=color)
            while y0 < y1:
                y0 += 1
                if d_old <= 0:
                    Graphic_draw_Dot(x0, y0, color=color)
                    d_old = d_old+BB
                elif d_old > 0:
                    x0+=1
                    Graphic_draw_Dot(x0, y0, color=color)
                    d_old = d_old + AA+BB
            Graphic_draw_Dot(x1, y1, color=color)
        elif -1 <= k < 0:
            d_old = int(AA - B)
            Graphic_draw_Dot(x0, y0, color=color)
            while x0 < x1:
                x0 += 1
                if d_old <= 0:
                    Graphic_draw_Dot(x0, y0, color=color)
                    d_old = d_old + AA
                elif d_old > 0:
                    y0 -= 1
                    Graphic_draw_Dot(x0, y0, color=color)
                    d_old = d_old + AA - BB
            Graphic_draw_Dot(x1, y1, color=color)
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

    # 画线测试
    Graphic_draw_Line(0, 0, 100, 0)
    Graphic_draw_Line(0, 0, 0, 100)
    Graphic_draw_Line(0, 0, 100, 100)
    Graphic_draw_Line(0, 0, 100, -100)

    Graphic_finish_Draw()
