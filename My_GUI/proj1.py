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
        self.canvas = Canvas(self.master, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.rect = None
        self.scale = 0.8
        self.canvas.bind(("<MouseWheel>"), self.on_mouse_wheel)

        Button(self.master, text="RestoreGraphic", command=self.restore).place(relx=0.25, rely=0.81)

        self.v = StringVar()
        self.v.set("9600")
        Label(self.master, text="波特率:", font=("Arial", 10)).place(relx=0.48, rely=0.82)
        OptionMenu(self.master, self.v, "4800", "9600", "14400", "19200", "38400", "57600", "115200",
                             "128000", "256000").place(relx=0.58, rely=0.81)


    def restore(self):
        self.scale = 0.8
        self.draw(self.x, self.y, color=self.ccolor, width=self.cwidth)

    def draw(self, x, y, color="black", width=1):
        self.x = x[:]
        self.y = y[:]
        self.cwidth = width
        self.ccolor = color

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
            yy = original[1] - int((y[i]) / stepy * (self.height - block) * self.scale)
            xx = original[0] + int((x[i]) / stepx * (self.width - block) * self.scale)
            ls.append(xx)
            ls.append(yy)
        self.canvas.create_line(ls, fill=color, width=width)

    def on_mouse_wheel(self, event):
        if event.delta > 0:
            self.scale += 0.05
        else:
            self.scale -= 0.05
        self.draw(self.x, self.y, color=self.ccolor, width=self.cwidth)


if __name__ == "__main__":
    import math

    width = 500
    height = 500
    x = [0.01 * i - 1 for i in range(1000)]
    y = list()
    for i in range(1, 1000):
        y.append(math.sin(x[i]) + 0.5 * math.cos(2 * x[i]))

    root = Tk()
    root.title("login")
    root.geometry(f"{width}x{height}+400+200")
    app = Application(root, width * 0.8, height * 0.8)
    app.draw(x[1:], y, color="pink", width=2)

    root.mainloop()
