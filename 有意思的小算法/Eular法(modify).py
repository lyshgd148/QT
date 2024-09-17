import matplotlib.pyplot as plt
import math


class Eular():
    def __init__(self, x, y, end, dx):
        self.x = x
        self.y = y
        self.end = end
        self.dx = dx

    def K(self):
        return ((self.x * self.y) / (self.x ** 2 + self.y ** 2)) * math.exp(self.x) - self.y

    def f(self):
        return self.y + self.K() * self.dx

    def K_(self):
        return (((self.x + self.dx) * self.f()) / (((self.x + self.dx)) ** 2 + self.f() ** 2)) * math.exp(
            self.x + self.dx) - self.f()

    def eular(self):
        temp_y = []
        temp_x = []
        for i in range(int(self.end // self.dx)):
            temp_x.append(self.x)
            k = (self.K_() + self.K()) / 2
            self.y = self.y + k * self.dx
            self.x = self.x + self.dx
            temp_y.append(self.y)
        return temp_x, temp_y


la = Eular(0, 350, 10, 0.0001)
x, y = la.eular()

plt.figure()
plt.plot(x, y)
plt.show()
