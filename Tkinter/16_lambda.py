from tkinter import *

root = Tk()
root.geometry("530x300")

c1 = Canvas(root, width=200, height=200, bg="green")
c1.pack()

Button(root, text="测试1", command=lambda: test(1, 2)).pack()


def test(a, b):
    print("a={0},b={1}".format(a, b))


def mouseTest(event):
    print("relate to father:({0},{1})".format(event.x, event.y))
    print("relate to screen:({0},{1})".format(event.x_root, event.y_root))
    print("widget:{0}".format(event.widget))


def testDrag(event):
    c1.create_oval(event.x, event.y, event.x + 1, event.y + 1)


def keyboardTest(event):
    print("keycose:{0}, char:{1}, keysym:{2} ".format(event.keycode, event.char, event.keysym))


def press_a_test(event):
    print("press 'a'")


def relase_a_test(event):
    print("relase 'a")


c1.bind("<Button-1>", mouseTest)
c1.bind("<B1-Motion>", testDrag)
root.bind("<KeyPress>", keyboardTest)
root.bind("<KeyPress-a>", press_a_test)
root.bind("<KeyRelease-a>", relase_a_test)

mainloop()
