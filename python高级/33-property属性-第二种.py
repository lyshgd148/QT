# property 可以简化获取数据的流程
# 高内聚，低耦合


class Goods:
    def __init__(self):
        self.o_p = 100
        self.dis = 0.8

    def get_price(self):
        result = self.o_p * self.dis
        return result

    def set_price(self, value):
        self.o_p = value

    def del_price(self):
        del self.o_p

    price = property(get_price, set_price, del_price)


obj = Goods
print(obj.price)
obj.price = 250
print(obj.price)
del obj.price
# print(obj.price)
