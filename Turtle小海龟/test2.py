import turtle as t

t.setup(500, 500, 0, 0)
t.tracer(False)  # 禁用画笔的动画效果

for i in range(360):
    t.forward(2)
    t.right(1)

t.tracer(True)  # 启用动画效果，显示完成的图形
t.done()
