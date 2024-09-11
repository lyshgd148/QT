import turtle as t

# t.screensize(100, 160)
t.setup(500, 500, 0, 0)
t.speed(0)
for i in range(360):
    t.forward(2)
    t.right(1)
print(t.pencolor(), t.speed())
t.done()
