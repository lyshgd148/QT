import turtle as t

t.setup(500, 500, 0, 0)
t.speed(10)
t.color('black', 'yellow')
t.begin_fill()
for i in range(36):
    t.forward(150)
    t.left(120)
    # print(i)
t.end_fill()
# t.goto(100, 50)
t.done()
