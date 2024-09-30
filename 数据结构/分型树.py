import turtle

turtle.setup(750, 650)
turtle.speed(10)


def tree(length):
    if length > 5:
        turtle.forward(length)
        turtle.right(15)
        tree(length - 10)
        turtle.left(30)
        tree(length - 10)
        turtle.right(15)
        turtle.back(length)


turtle.left(90)
turtle.penup()
turtle.backward(325)
turtle.pendown()
turtle.pencolor('pink')
turtle.pensize(1)
tree(105)
turtle.hideturtle()

turtle.done()
