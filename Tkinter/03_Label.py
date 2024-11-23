from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence


class Application(Frame):
    def __init__(self, master=None):
        self.index = 0

        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
        self.load("./image/1.gif")
        self.show_image()

    def createWidget(self):
        self.label_01 = Label(self, text="刘雨生", width=10, height=2, bg="blue", fg="white", font=("宋体", 30))
        self.label_01.pack()

        self.label_02 = Label(self)  # 创建一个Label用来展示图片
        self.label_02.pack()

        global photo
        photo = PhotoImage(file="./image/1.gif")
        photo = photo.subsample(2, 2)
        self.label_03 = Label(self, image=photo)
        self.label_03.pack()

        self.label_04 = Label(self, text="  lys\ndhasdjhkas\n刘雨生!", borderwidth=1, relief="solid", justify="left",
                              font=("黑体", 15))
        self.label_04.pack()

    def load(self, path):
        gif = Image.open(path)
        w, h = gif.size
        self.gifs = [ImageTk.PhotoImage(frame.resize((w // 2, h // 2))) for frame in ImageSequence.Iterator(gif)]

    def show_image(self):
        self.label_02.config(image=self.gifs[self.index])
        self.index = (self.index + 1) % len(self.gifs)
        self.after(50, self.show_image)


if __name__ == "__main__":
    root = Tk()
    root.title("Test")
    root.geometry("700x750+400+50")
    app = Application(root)
    root.mainloop()
