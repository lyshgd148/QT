import random
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        btnText = (("MC", "M+", "M-", "MR"),
                   ("C", "±", "/", "✖"),
                   (7, 8, 9, "-"),
                   (4, 5, 6, "+"),
                   (1, 2, 3, "="),
                   (0, "."))
        Entry(self).grid(row=0, column=0, columnspan=4, pady=10)
        for rindex, r in enumerate(btnText):
            for cindex, c in enumerate(r):
                if c == "=":
                    Button(self, text=c).grid(row=rindex + 1, column=cindex, rowspan=2, sticky=NSEW)
                elif c == 0:
                    Button(self, text=c).grid(row=rindex + 1, column=cindex, columnspan=2, sticky=NSEW)
                elif c == ".":
                    Button(self, text=c).grid(row=rindex + 1, column=cindex + 1, sticky=NSEW)
                else:
                    Button(self, text=c).grid(row=rindex + 1, column=cindex, sticky=NSEW)


if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    root.geometry("200x230+600+200")
    app = Application(root)
    root.mainloop()
