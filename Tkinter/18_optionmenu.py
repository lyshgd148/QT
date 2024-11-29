from tkinter import *

root = Tk()
root.geometry("530x300")
v = StringVar()
v.set("ky")
om = OptionMenu(root, v, "lys", "wzy", "ky")
om["width"] = 10
om.pack()


def test(v):
    print("I love :" + v.get())


Button(root, text="OK!", command=lambda: test(v)).pack()

mainloop()
