import turtle as t

r = 100
t.setup(500, 500)
t.speed(10)
t.right(90)
t.penup()
t.forward(r)
t.pendown()
t.left(90)
t.circle(r, steps=720)
# t.right(60)

for k in range(0, 361, 25):
    t.penup()
    t.goto(0, 0)
    t.setheading(-90)
    t.left(k)
    t.forward(r)
    t.setheading(0)
    t.left(k - 60)
    t.pendown()
    for i in range(6):
        t.left(90)
        t.penup()
        t.forward(r)
        t.pendown()
        t.left(90)
        t.circle(r, 120)
t.done()
