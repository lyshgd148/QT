import matplotlib.pyplot as plt
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.v1 = StringVar()
        self.v2 = StringVar()
        self.v3 = StringVar()
        self.v4 = StringVar()
        Label(self.master, text="Kp: ").place(relx=0.22, rely=0)
        Label(self.master, text="Kd: ").place(relx=0.22, rely=0.1)
        Label(self.master, text="T: ").place(relx=0.22, rely=0.2)
        Label(self.master, text="K: ").place(relx=0.22, rely=0.3)

        Button(self.master, text="确定", command=self.PID).place(relx=0.44, rely=0.4)

        self.Kp = 0.2
        self.Kd = 0.01
        self.T = 1
        self.K = 10

        self.v1.set(str(self.Kp))
        self.v2.set(str(self.Kd))
        self.v3.set(str(self.T))
        self.v4.set(str(self.K))
        Entry(self.master, textvariable=self.v1).place(relx=0.3, rely=0.0)
        Entry(self.master, textvariable=self.v2).place(relx=0.3, rely=0.1)
        Entry(self.master, textvariable=self.v3).place(relx=0.3, rely=0.2)
        Entry(self.master, textvariable=self.v4).place(relx=0.3, rely=0.3)

    def PID(self):
        self.Kp = float(self.v1.get())
        self.Kd = float(self.v2.get())
        y_0 = 10
        y = [0]
        e_k = y_0 - 0
        e_last_k = 0

        t = [0]
        for i in range(1, 100):
            x = self.Kp * e_k + self.Kd * (e_k - e_last_k)
            y.append(((self.K * x) + self.T * y[i - 1]) / (self.T + 1))
            e_last_k = e_k
            e_k = y_0 - y[i]
            t.append(i)

        plt.figure()
        plt.plot(t, y)
        plt.text(0.88, 0.9, f'Kp:{self.Kp}', fontsize=10, color='red', transform=plt.gca().transAxes)
        plt.text(0.88, 0.85, f'Kd:{self.Kd}', fontsize=10, color='red', transform=plt.gca().transAxes)
        plt.show()


if __name__ == "__main__":
    root = Tk()
    root.title("PID")
    root.geometry("300x300+400+200")
    app = Application(root)
    root.mainloop()
