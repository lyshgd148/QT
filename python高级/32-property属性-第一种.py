class Goods1(object):
    def __init__(self):
        self.original_price = 100
        self.discount = 0.7

    @property
    def price(self):
        return self.original_price * self.discount

    @price.setter
    def price(self, val):
        self.original_price = val
        return self.original_price

    @price.deleter
    def price(self):
        del self.original_price


googs = Goods1()
print(googs.price)
val = googs.price = 200
print(val)
del googs.price
googs.price = 250
print(googs.price)
