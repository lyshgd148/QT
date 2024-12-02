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
        Label(self.master, text="Kp: ").place(relx=0.22, rely=0.05)
        Label(self.master, text="Kd: ").place(relx=0.22, rely=0.25)

        Button(self.master, text="确定", command=self.Ok).place(relx=0.44, rely=0.4)

        self.Kp = 0.3
        self.Kd = 0
        self.v1.set(str(self.Kp))
        self.v2.set(str(self.Kd))
        Entry(self.master, textvariable=self.v1).place(relx=0.3, rely=0.05)
        Entry(self.master, textvariable=self.v2).place(relx=0.3, rely=0.25)

    def Ok(self):
        K = 10
        T = 1
        self.Kp = float(self.v1.get())
        self.Kd = float(self.v2.get())
        y_0 = 10
        y = [0]
        e_k = y_0 - 0
        e_last_k = 0

        t = [0]
        for i in range(1, 100):
            x = self.Kp * e_k + self.Kd * (e_k - e_last_k)
            y.append(((K * x) + T * y[i - 1]) / (T + 1))
            e_last_k = e_k
            e_k = y_0 - y[i]
            t.append(i)

        plt.figure()
        plt.plot(t, y)
        plt.show()


# K = 10
# T = 1
# Kp = 1.2
# Kd = 0.1
#
# y_0 = 10
# y = [0]
# e_k = y_0 - 0
# e_last_k = 0
#
# t = [0]
# for i in range(1, 100):
#     x = Kp * e_k + Kd * (e_k - e_last_k)
#     y.append(((K * x) + T * y[i - 1]) / (T + 1))
#     e_last_k = e_k
#     e_k = y_0 - y[i]
#     t.append(i)
#
# plt.figure()
# plt.plot(t, y)
# plt.show()

if __name__ == "__main__":
    root = Tk()
    root.title("PID")
    root.geometry("300x300+400+200")
    app = Application(root)
    root.mainloop()
