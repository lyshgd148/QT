class LowPassFilter:
    def __init__(self, w, t):
        self.w = w
        self.y_0 = 0
        self.y_last = self.y_0
        self.T = t

    def filter(self, u):
        y = 1 / (1 + self.w * self.T) * self.y_last + ((self.w * self.T) / (1 + self.w * self.T)) * u
        self.y_last = y
        return y


class HightPassFilter:
    def __init__(self):
        pass
