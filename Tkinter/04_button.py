from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn_01 = Button(self, text="登录", command=self.login)
        self.btn_01.pack()

        global gif
        gif = PhotoImage(file="./image/1.gif")
        gif = gif.subsample(10, 10)
        self.btn_02 = Button(self, image=gif, command=self.login)
        self.btn_02.pack()
        self.btn_02.config(state="disabled")

        self.btn_03 = Button(self, image=gif, command=self.login)
        self.btn_03.pack()

    def login(self):
        messagebox.showinfo("login", "Welcome to my world!")


if __name__ == "__main__":
    root = Tk()
    root.title("login")
    root.geometry("300x300+400+200")
    app = Application(root)
    root.mainloop()
