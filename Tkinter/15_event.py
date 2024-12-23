from tkinter import *

root = Tk()
root.geometry("530x300")

c1 = Canvas(root, width=200, height=200, bg="green")
c1.pack()


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
c1.bind("<KeyPress>", keyboardTest)
c1.bind("<KeyPress-a>", press_a_test)
c1.bind("<KeyRelease-a>", relase_a_test)

mainloop()
