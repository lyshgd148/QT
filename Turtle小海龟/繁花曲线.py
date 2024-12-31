import turtle

# 设置画布
screen = turtle.Screen()
screen.bgcolor("white")  # 设置背景颜色

# 创建海龟
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)  # 设置速度为最快，瞬间完成绘制

# 隐藏海龟
t.hideturtle()

# 设置笔的大小为1，模拟像素点
t.pensize(1)
t.penup()  # 不开始绘制
t.goto(50, 50)  # 设置位置
t.dot(5, "black")  # 绘制一个大小为5的黑色点

# 完成后保持窗口直到手动关闭
turtle.done()
