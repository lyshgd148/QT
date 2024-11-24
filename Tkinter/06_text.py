import webbrowser
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        Button(self, text="重复插入文本", command=self.insertText).pack(side="left")
        Button(self, text="返回文本", command=self.returnText).pack(side="left")
        Button(self, text="添加图片", command=self.addImage).pack(side="left")
        Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        Button(self, text="tag精确控制文本", command=self.testTag).pack(side="left")

        self.w1 = Text(self.master, width=50, height=12, bg="gray")
        self.w1.pack()

        self.w1.pack()
        self.w1.insert(1.0, "dasdasdasdas\n")
        self.w1.insert(2.0, "234234242342343dasdas")

    def insertText(self):
        self.w1.insert(INSERT, "lys")
        self.w1.insert(END, "[end]")

    def returnText(self):
        print(self.w1.get(1.2, 1.5))
        print("all:---------\n")
        print(self.w1.get(1.0, END))

    def addImage(self):
        self.photo = PhotoImage(file="./image/1.gif")
        self.photo = self.photo.subsample(4, 4)
        self.w1.image_create(END, image=self.photo)

    def addWidget(self):
        b1 = Button(self.w1, text="test")
        self.w1.window_create(INSERT, window=b1)

    def testTag(self):
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, "lysdasdad\n13124234233\nfasfasf64654\nfsfasfafafa")
        self.w1.tag_add("123", 1.0, 1.4)
        self.w1.tag_config("123", background="blue", foreground="yellow")

        self.w1.tag_add("search", 2.0, 2.7)
        self.w1.tag_config("search", underline=True)
        self.w1.tag_bind("search", "<Button-1>", self.search)

    def search(self, event):
        webbrowser.open("https://lysnjit.cn")


if __name__ == "__main__":
    root = Tk()
    root.title("login")
    root.geometry("370x370+400+200")
    app = Application(root)
    root.mainloop()
