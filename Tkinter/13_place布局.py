from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("布局管理place")
root["bg"] = "pink"

f1 = Frame(root, width=200, height=200, bg="yellow")
f1.place(x=30, y=30)

Button(root, text="刘雨生1").place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.1)
Button(f1, text="刘雨生2").place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.1)
Button(root, text="刘雨生3").place(x=250, y=150, width=200, height=100)

mainloop()
