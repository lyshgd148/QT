import random
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas = Canvas(self, width=300, height=200, bg="pink")
        self.canvas.pack()

        ls = [10, 10, 30, 30, 50, 45]
        line = self.canvas.create_line(ls)

        rect = self.canvas.create_rectangle(50, 50, 100, 100)

        oval = self.canvas.create_oval(50, 50, 100, 80)

        global photo
        photo = PhotoImage(file="./image/1.gif")
        photo = photo.subsample(5, 5)
        self.canvas.create_image(150, 150, image=photo)

        Button(self, text="绘制多矩形", command=self.draw).pack()

    def draw(self):
        self.canvas.delete("all")
        for i in range(10):
            x1 = random.randrange(int(self.canvas["width"]) // 2)
            y1 = random.randrange(int(self.canvas["height"]) // 2)
            x2 = x1 + random.randrange(int(self.canvas["width"]) // 2)
            y2 = y1 + random.randrange(int(self.canvas["height"]) // 2)
            self.canvas.create_rectangle(x1, y1, x2, y2)


if __name__ == "__main__":
    root = Tk()
    root.title("login")
    root.geometry("370x370+400+200")
    app = Application(root)
    root.mainloop()
