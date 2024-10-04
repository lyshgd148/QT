import turtle as t

t.tracer(0)

nmax, width = 3 ** 5, 600
cell = width / nmax

t.speed(10)
def box(left, top, size, c):
    t.penup()
    t.goto(left*cell - width / 2, width / 2 - top*cell)
    t.pendown()
    t.color(c)
    t.begin_fill()
    for n in range(4):
        t.forward(cell * size)
        t.right(90)
    t.end_fill()


def spski(n, left, top):
    if n == 1:
        return
    for row in range(3):
        for col in range(3):
            if row == 1 and col == 1:
                box(left + n // 3, top + n // 3, n // 3, "white")
            else:
                spski(n // 3, left+n//3*col, top+n//3*row)


box(0, 0, nmax,"red")
spski(nmax, 0, 0)

t.update()
t.done()