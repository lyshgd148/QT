import matplotlib.pyplot as plt
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):  # 创建类时候的初始化函数，创建时自动调用
        super().__init__(master)  # 继承Frame 并初始化
        self.master = master
        self.pack()  # 设置布局并显示
        self.createWidget()  # 调用createWidget函数 创建主件

    def createWidget(self):
        # 创建四个StringVar变量用于存储输入框的参数值
        self.v1 = StringVar()
        self.v2 = StringVar()
        self.v3 = StringVar()
        self.v4 = StringVar()

        # 创建标签用于显示参数名称
        Label(self.master, text="Kp: ").place(relx=0.22, rely=0)
        Label(self.master, text="Kd: ").place(relx=0.22, rely=0.1)
        Label(self.master, text="T: ").place(relx=0.22, rely=0.2)
        Label(self.master, text="K: ").place(relx=0.22, rely=0.3)

        # 创建一个确定按钮  command=self.PID --->绑定回调函数（按一下确定按钮 就运行这个绑定的函数）
        Button(self.master, text="确定", command=self.PID).place(relx=0.44, rely=0.4)

        # 初始化 Kp、Kd、T、K
        self.Kp = 0.2
        self.Kd = 0.01
        self.T = 1
        self.K = 10

        # 将默认参数值设置到对应的StringVar变量中（初始化参数值）
        self.v1.set(str(self.Kp))
        self.v2.set(str(self.Kd))
        self.v3.set(str(self.T))
        self.v4.set(str(self.K))

        # 创建输入框，用于用户输入参数值  .place(relx,rely)设置输入框的位置
        Entry(self.master, textvariable=self.v1).place(relx=0.3, rely=0.0)
        Entry(self.master, textvariable=self.v2).place(relx=0.3, rely=0.1)
        Entry(self.master, textvariable=self.v3).place(relx=0.3, rely=0.2)
        Entry(self.master, textvariable=self.v4).place(relx=0.3, rely=0.3)

    def PID(self):
        # 从输入框中获取用户输入的参数值
        self.Kp = float(self.v1.get())
        self.Kd = float(self.v2.get())
        y_0 = 10
        y = [0]
        e_k = y_0 - 0
        e_last_k = 0

        t = [0]  # t时间列表
        for i in range(1, 100):  # 从1 循环到99
            x = self.Kp * e_k + self.Kd * (e_k - e_last_k)  # 离散化的PID公式 算x(T)=Kp*e_k+Kd*(e_k-e_k_last)
            y.append(((self.K * x) + self.T * y[i - 1]) / (self.T + 1))  # 根据算出来的x 计算y=(K*x+T*y_last)/(T+1)，添加到y列表
            e_last_k = e_k  # 将这一次的误差赋值给上一次
            e_k = y_0 - y[i]  # 算出新的误差 e_k
            t.append(i)  # 向t列表里添加时间

        # 绘制PID响应曲线
        plt.figure()
        plt.plot(t, y)
        plt.text(0.88, 0.9, f'Kp:{self.Kp}', fontsize=10, color='red', transform=plt.gca().transAxes)
        plt.text(0.88, 0.85, f'Kd:{self.Kd}', fontsize=10, color='red', transform=plt.gca().transAxes)
        plt.show()  # 显示画面


if __name__ == "__main__":  # 如果__name__=="__mian__"就执行，当你在其他的.py 程序里调用时PID.py时 下面的就不会执行
    root = Tk()  # 创建根窗口
    root.title("PID")  # 窗口标题
    root.geometry("300x300+400+200")  # 窗口大小300*300 距离电脑显示屏左边400像素 距离显示屏上边200像素
    app = Application(root)  # 调用Application类 创建实例对象
    root.mainloop()  # 不断循环 如果去掉后 画面显示一帧就消失
