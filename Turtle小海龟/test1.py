import turtle as t

# t.screensize(100, 160)
t.setup(500, 500, 0, 0)
t.speed(1)
for i in range(4):
    t.forward(50)
    t.right(90)
print(t.pencolor(), t.speed())
t.done()
