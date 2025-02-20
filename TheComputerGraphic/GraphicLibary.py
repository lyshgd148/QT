import turtle
import time


def Graphic_Init(width, height):
    turtle.setup(width, height)
    turtle.hideturtle()
    turtle.tracer(0)
    turtle.penup()


def Graphic_draw_Dot(x, y, size=2, color="black"):
    turtle.goto(x, y)
    turtle.dot(size, color)


# def Graphic_draw_MidLine(x0, y0, x1, y1, color="black") -> None:
#     """ 我写的中点画线算法 """
#     if x0 != x1 and y0 != y1:
#         A = -(y1 - y0)
#         B = (x1 - x0)
#         AA = int(2 * A)
#         BB = int(2 * B)
#         k = (-A) / B
#         # print(k)
#         if 0 < k <= 1:
#             d_old = int(AA + B)
#             Graphic_draw_Dot(x0, y0, color=color)
#             while x0 < x1:
#                 x0 += 1
#                 if d_old <= 0:
#                     y0 += 1
#                     Graphic_draw_Dot(x0, y0, color=color)
#                     d_old = d_old + AA + BB
#                 elif d_old > 0:
#                     Graphic_draw_Dot(x0, y0, color=color)
#                     d_old = d_old + AA
#             Graphic_draw_Dot(x1, y1, color=color)
#         elif k > 1:
#             d_old = int(A + BB)
#             Graphic_draw_Dot(x0, y0, color=color)
#             while y0 < y1:
#                 y0 += 1
#                 if d_old <= 0:
#                     Graphic_draw_Dot(x0, y0, color=color)
#                     d_old = d_old + BB
#                 elif d_old > 0:
#                     x0 += 1
#                     Graphic_draw_Dot(x0, y0, color=color)
#                     d_old = d_old + AA + BB
#             Graphic_draw_Dot(x1, y1, color=color)
#         elif -1 <= k < 0:
#             d_old = int(AA - B)
#             Graphic_draw_Dot(x0, y0, color=color)
#             while x0 < x1:
#                 x0 += 1
#                 if d_old <= 0:
#                     Graphic_draw_Dot(x0, y0, color=color)
#                     d_old = d_old + AA
#                 elif d_old > 0:
#                     y0 -= 1
#                     Graphic_draw_Dot(x0, y0, color=color)
#                     d_old = d_old + AA - BB
#             Graphic_draw_Dot(x1, y1, color=color)
#         elif k < -1:
#             pass
#
#     elif x0 == x1 and y0 != y1:
#         while y0 <= y1:
#             Graphic_draw_Dot(x0, y0, color=color)
#             y0 += 1
#     elif x0 != x1 and y0 == y1:
#         while x0 <= x1:
#             Graphic_draw_Dot(x0, y0, color=color)
#             x0 += 1


def Graphic_draw_MidLine(x0, y0, x1, y1, color="black") -> None:
    """我靠ChatGpt写的代码效率比我的高太多了，服气"""
    """ Enhanced Midpoint Line Algorithm """
    dx = x1 - x0
    dy = y1 - y0
    steep = abs(dy) > abs(dx)

    # Swap coordinates for steep slopes
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        dx, dy = dy, dx

    # Ensure left-to-right drawing
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    d = 2 * abs(dy) - abs(dx)
    y_step = 1 if y0 < y1 else -1

    y = y0
    for x in range(x0, x1 + 1):
        if steep:
            Graphic_draw_Dot(y, x, color=color)
        else:
            Graphic_draw_Dot(x, y, color=color)

        if d > 0:
            y += y_step
            d -= 2 * abs(dx)
        d += 2 * abs(dy)


def Graphic_finish_Draw():
    turtle.done()


if __name__ == "__main__":
    Graphic_Init(500, 500)

    # 中点线算法 画线测试
    Graphic_draw_MidLine(0, 0, 100, 0)
    Graphic_draw_MidLine(0, 0, 0, 100)
    Graphic_draw_MidLine(0, 0, 100, 100)
    Graphic_draw_MidLine(0, 0, 100, -100)
    Graphic_draw_MidLine(0, 0, 50, 100)
    # for j in range(1, 20):
    #     for i in range(100):
    #         Graphic_draw_MidLine(0, 0, j, i)

    Graphic_finish_Draw()
