import matplotlib.pyplot as plt


class SimulationAccleaction():
    def __init__(self):
        self.vx = [10.2 * 10 ** 3]
        self.vy = [0]
        self.R = 6357
        self.G = 6.6743 * 10 ** (-11)
        self.M = 5.972 * 10 ** 24
        self.h = 500
        self.x = [0]
        self.y = [(self.R + self.h) * 10 ** 3]
        self.delat_t = 0.01
        self.main()

    def calculate(self):
        for i in range(1, int((3600*24) / self.delat_t)):
            self.vx.append(self.vx[i - 1] - (self.x[i - 1] * self.G * self.M * self.delat_t) / (
                    self.x[i - 1] ** 2 + self.y[i - 1] ** 2) ** (3 / 2))
            self.vy.append(self.vy[i - 1] + (self.y[i - 1] * self.G * self.M * self.delat_t) / (
                    self.x[i - 1] ** 2 + self.y[i - 1] ** 2) ** (3 / 2))
            self.x.append(self.x[i - 1] + self.vx[i - 1] * self.delat_t)
            self.y.append(self.y[i - 1] - self.vy[i - 1] * self.delat_t)

    def main(self):
        self.calculate()
        plt.figure()
        plt.plot(self.x, self.y)
        plt.axis('equal')
        plt.show()


trajectory = SimulationAccleaction()
