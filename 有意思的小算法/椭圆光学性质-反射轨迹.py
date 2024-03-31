import matplotlib.pyplot as plt
import numpy as np


class Ellipse:
    def __init__(self, k, n):
        # 生成椭圆数据
        x = np.linspace(-5, 5, 5000)  # x 坐标范围
        y = np.linspace(-4, 4, 4000)  # y 坐标范围
        self.X, self.Y = np.meshgrid(x, y)  # 创建网格坐标矩阵
        self.Z = self.X ** 2 / 25 + self.Y ** 2 / 16  # 椭圆的方程
        self.x = [-3]
        self.y = [0]
        self.k = k
        self.n = n
        x1 = (-150 * self.k ** 2 + np.sqrt(25600 * (self.k ** 2 + 1))) / (50 * self.k ** 2 + 32)
        y1 = self.k * (x1 + 3)
        self.x.append(x1)
        self.y.append(y1)

    def data_ellipse(self):
        for i in range(self.n):
            if i % 2 == 0:
                k = self.y[i + 1] / (self.x[1 + i] - 3)
                x1 = (150 * k ** 2 + np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
                x2 = (150 * k ** 2 - np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
                if np.abs(x1 - self.x[i + 1]) > np.abs(x2 - self.x[i + 1]):
                    y_ = k * (x1 - 3)
                    self.x.append(x1)
                else:
                    y_ = k * (x2 - 3)
                    self.x.append(x2)
                self.y.append(y_)

            else:
                k = self.y[i + 1] / (self.x[i + 1] + 3)
                x1 = (-150 * k ** 2 + np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
                x2 = (-150 * k ** 2 - np.sqrt(25600 * (k ** 2 + 1))) / (50 * k ** 2 + 32)
                if np.abs(x1 - self.x[i + 1]) > np.abs(x2 - self.x[i + 1]):
                    y_ = k * (x1 + 3)
                    self.x.append(x1)
                else:
                    y_ = k * (x2 + 3)
                    self.x.append(x2)
                self.y.append(y_)

    def draw_ellipse(self):
        plt.contour(self.X, self.Y, self.Z, [1])
        plt.scatter([-3, 3], [0, 0], color='orangered', zorder=3)
        plt.axis('equal')
        plt.xlim(-7, 7)
        plt.ylim(-5, 5)
        for i in range(self.n):
            color = np.random.rand(3)
            plt.plot(self.x[i:i + 2], self.y[i:i + 2], color=color)
            plt.pause(0.25)
            # plt.cla()
        plt.plot(self.x, self.y)
        plt.show()

    def main(self):
        self.data_ellipse()
        self.draw_ellipse()


if __name__ == "__main__":
    Ellipse(1, 20).main()
