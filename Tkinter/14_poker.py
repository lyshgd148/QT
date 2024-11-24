import random
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.photos = [PhotoImage(file="image/1.gif").subsample(4, 4) for _ in range(10)]
        self.pokers = [Label(self.master, image=self.photos[i]) for i in range(10)]

        for i in range(10):
            self.pokers[i].place(x=10 + i * 50, y=50)
            # self.pokers[i].bind("<Button-1>", self.discard)
        self.pokers[0].bind_class("Label", "<Button-1>", self.discard)

    def discard(self, event):
        print(event.widget.winfo_y())
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)


if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    root.geometry("600x230+300+200")
    app = Application(root)
    root.mainloop()
