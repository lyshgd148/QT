from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.geometry("530x300")


def test():
    s = askcolor(color='green', title="SelectBG")
    print(s)
    root.config(bg=s[1])


Button(root, text="ChangeBG", command=test).pack()
mainloop()
