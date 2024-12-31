import turtle

turtle.setup(500, 500)
turtle.hideturtle()  # 隐藏海龟

# 禁用动画
turtle.tracer(0)

for i in range(150):
    turtle.forward(3*i)
    turtle.left(90)

turtle.clear()
for i in range(150):
    turtle.forward(3*i)
    turtle.right(90)

# turtle.update()
turtle.done()
