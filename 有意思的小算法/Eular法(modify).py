import matplotlib.pyplot as plt


class Eular():
    def __init__(self, x, y, end, dx):
        self.x = x
        self.y = y
        self.end = end
        self.dx = dx

    def K(self):
        return self.x * (1 - self.y)

    def f(self):
        return self.y + self.K() * self.dx

    def eular(self):
        temp_y = []
        temp_x = []
        for i in range(int(self.end // self.dx)):
            temp_x.append(self.x)
            k = ((self.x + self.dx) * (1 - self.f()) + self.K()) / 2
            self.y = self.y + k * self.dx
            self.x = self.x + self.dx
            temp_y.append(self.y)
        return temp_x, temp_y


la = Eular(0, 2, 10, 0.01)
x, y = la.eular()

plt.figure()
plt.plot(x, y)
plt.show()
