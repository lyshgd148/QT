from tkinter import *

root = Tk()
root.geometry("530x300")


def test(v):
    print("value:" + v)
    Font = ("宋体", v)
    a.config(font=Font)


a = Label(root, text="lys", width=10, height=1, bg="pink", fg="yellow")
a.pack()
s1 = Scale(root, from_=0, to=100, length=100, orient=HORIZONTAL, command=test)
s1.pack()

mainloop()
