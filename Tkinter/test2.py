from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn_01 = Button(self)
        self.btn_01["text"] = "GIVE"
        self.btn_01["command"] = self.give
        self.btn_01.pack()

        self.btn_02 = Button(self, text="quit", command=self.master.destroy)
        self.btn_02.pack()

    def give(self):
        messagebox.showinfo("give", "Give you one flower!")


if __name__ == "__main__":
    root = Tk()
    root.title("Give one")
    root.geometry("300x300+400+200")
    app = Application(root)
    root.mainloop()
