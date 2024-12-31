import turtle

turtle.setup(500, 500)
# 禁用动画
turtle.tracer(0)

for i in range(150):
    turtle.forward(3*i)
    turtle.left(90)

turtle.update()
turtle.done()
