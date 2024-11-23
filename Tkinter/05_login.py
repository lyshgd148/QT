from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label_01 = Label(self, text="账户")
        self.label_01.pack()
        v1 = StringVar()
        v1.set("admin")
        self.entry_01 = Entry(self, textvariable=v1)
        self.entry_01.pack()

        self.label_02 = Label(self, text="密码")
        self.label_02.pack()
        v2 = StringVar()
        self.entry_02 = Entry(self, textvariable=v2, show="*")
        self.entry_02.pack()

        Button(self, text="登录", command=self.login).pack()
        Button(self, text="退出", command=self.master.destroy).pack()

    def login(self):
        user = self.entry_01.get()
        password = self.entry_02.get()
        if user == "lys" and password == "lyshgd":
            messagebox.showinfo("login", "Welcome to my world!")
            print("用户名：" + user)
            print("，密码：" + password)
        else:
            messagebox.showwarning(title="wrong", message="please go out!")


if __name__ == "__main__":
    root = Tk()
    root.title("login")
    root.geometry("300x300+400+200")
    app = Application(root)
    root.mainloop()
