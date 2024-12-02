import matplotlib.pyplot as plt
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        pass


K = 1
T = 1
Kp = 1.2
Kd = 0.1

y_0 = 10
y = [0]
e_k = y_0 - 0
e_last_k = 0

t = [0]
for i in range(1, 100):
    x = Kp * e_k + Kd * (e_k - e_last_k)
    y.append(((K * x) + T * y[i - 1]) / (T + 1))
    e_last_k = e_k
    e_k = y_0 - y[i]
    t.append(i)

plt.figure()
plt.plot(t, y)
plt.show()

if __name__ == "__main__":
    root = Tk()
    root.title("PID")
    root.geometry("300x300+400+200")
    app = Application(root)
    root.mainloop()
