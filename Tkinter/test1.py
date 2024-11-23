from tkinter import *
from tkinter import messagebox


def give():
    messagebox.showinfo("Hello", "I give you a flower!")


root = Tk()
root.title("My First GUI")
root.geometry("100x100+600+300")
btn_01 = Button(root)
btn_01["text"] = "HAM"
btn_01.bind('<Button-1>', lambda event: give())  # 使用 lambda 函数包装 give()，不传递参数
btn_01.pack()

root.mainloop()
