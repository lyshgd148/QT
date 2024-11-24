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
        self.s1 = IntVar()
        self.s2 = IntVar()
        self.s1.set(3)
        self.s2.set(3)

        self.ss1 = StringVar()
        self.ss2 = StringVar()
        self.ss1.set("0")
        self.ss2.set("0")

        self.c1 = Checkbutton(self, text="看片", variable=self.ss1, onvalue="1", offvalue="2")
        self.c2 = Checkbutton(self, text="打飞机", variable=self.ss2, onvalue="1", offvalue="2")
        self.c1.pack(side="left")
        self.c2.pack(side="left")

        Button(self, text="ojbk", command=self.confirm).pack(side="left")

    def confirm(self):
        print(self.s1.get(), self.s2.get(), self.ss1.get(), self.ss2.get())
        if self.s1.get() == 1 and self.s2.get():
            messagebox.showinfo("hah", "爽爽！！")
        elif self.s1.get() == 1 and self.s2.get() == 0:
            messagebox.showinfo("hah", "小爽！！")
        elif self.s1.get() == 0 and self.s2.get() == 1:
            messagebox.showinfo("hah", "小爽！！")
        elif self.s1.get() == 0 and self.s2.get() == 0:
            messagebox.showinfo("hah", "爽p！！")


if __name__ == "__main__":
    root = Tk()
    root.title("login")
    root.geometry("370x370+400+200")
    app = Application(root)
    root.mainloop()
