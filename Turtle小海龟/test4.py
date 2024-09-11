import turtle
 
turtle.setup(500, 500)
turtle.speed(10)
turtle.color('black', 'red')
turtle.begin_fill()
turtle.circle(30, 180, 180)
for i in range(3):
    turtle.forward(30)
    turtle.left(20)
turtle.end_fill()

turtle.done()
