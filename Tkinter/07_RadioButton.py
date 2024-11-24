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
        self.v = StringVar()
        self.v.set("M")

        self.r1 = Radiobutton(self, text="man", value="M", variable=self.v)
        self.r2 = Radiobutton(self, text="woman", value="F", variable=self.v)
        self.r1.pack(side="left")
        self.r2.pack(side="left")

        Button(self, text="ok", command=self.confirm).pack(side="left")

    def confirm(self):
        messagebox.showinfo("test", "性别为:" + self.v.get())


if __name__ == "__main__":
    root = Tk()
    root.title("login")
    root.geometry("370x370+400+200")
    app = Application(root)
    root.mainloop()
