from tkinter import *

root = Tk()
root.geometry("530x300")


def test1():
    print("test1!")


def test2(event):
    print("test2!")


def test3(event):
    print("test3!")


b1 = Button(root, text="1", command=test1)
b1.pack()

b2 = Button(root,width=10,height=2, text="2")
b2.pack()

b2.bind("<Button-1>", test2)
b1.bind_class("Button", "<Button-2>", test3)

mainloop()
