import random
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label_01 = Label(self, text="用户名:")
        self.label_01.grid(row=0, column=0, sticky=E)
        self.entry_01 = Entry(self)
        self.entry_01.grid(row=0, column=1)

        self.label_02 = Label(self, text="密码:")
        self.label_02.grid(row=1, column=0, sticky=E)
        self.entry_02 = Entry(self, show="*")
        self.entry_02.grid(row=1, column=1)

        Button(self, text="登录").grid(row=2, column=0)
        Button(self, text="取消").grid(row=2, column=1)


if __name__ == "__main__":
    root = Tk()
    root.title("login")
    root.geometry("370x370+400+200")
    app = Application(root)
    root.mainloop()
