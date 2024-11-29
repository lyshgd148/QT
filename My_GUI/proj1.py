from tkinter import *


class Application(Frame):
    def __init__(self, master, width, height):
        super().__init__(master)
        self.width = width
        self.height = height
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas = Canvas(self, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.rect = None
        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        Button(text="RestoreGraphic", command=self.restore).pack()

    def restore(self):
        self.draw(self.x, self.y)

    def draw(self, x, y, color="black", width=1):
        self.x = x[:]
        self.y = y[:]
        self.canvas.delete("all")  # 清除画布！
        block = 80
        self.canvas.create_line((block, 0, block, self.height), fill="black")
        self.canvas.create_line((0, self.height - block, self.width, self.height - block), fill="black")

        original = (block, self.height - block)
        Max_x = max(x)
        Min_x = min(x)
        Max_y = max(y)
        Min_y = min(y)
        stepx = Max_x - Min_x
        stepy = Max_y - Min_y
        ls = []
        for i in range(len(x)):
            yy = original[1] - int((y[i]) / stepy * (self.height - block) * 0.9)
            xx = original[0] + int((x[i]) / stepx * (self.width - block) * 0.9)
            ls.append(xx)
            ls.append(yy)
        self.canvas.create_line(ls, fill=color, width=width)

    def on_press(self, event):
        self.start_x = event.x
        self.strat_y = event.y

    def on_drag(self, event):
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.start_x, self.strat_y, event.x, event.y)

    def on_release(self, event):
        if self.rect:
            self.canvas.delete(self.rect)
            self.rect = None
            print(self.start_x, self.strat_y, event.x, event.y)


if __name__ == "__main__":
    import math

    width = 370
    height = 370
    x = [0.01 * i - 1 for i in range(1000)]
    y = list()
    for i in range(1, 1000):
        y.append(math.sin(x[i]) + 0.5 * math.cos(2 * x[i]))

    root = Tk()
    root.title("login")
    root.geometry(f"{width}x{height}+400+200")
    app = Application(root, width * 0.8, height * 0.8)
    app.draw(x[1:], y, width=1)

    root.mainloop()
