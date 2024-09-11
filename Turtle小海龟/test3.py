import turtle

turtle.setup(500, 500)
turtle.tracer(False)  # 禁用画笔的动画效果
# turtle.speed(10)
for k in range(0, 180, 30):
    for i in range(30, 80, 5):
        turtle.circle(i)
        turtle.circle(-i)

    turtle.right(k)
    for i in range(30, 80, 5):
        turtle.circle(i)
        turtle.circle(-i)
turtle.tracer(True)  # 禁用画笔的动画效果
turtle.done()
