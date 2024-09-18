# 定义栈

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Stack1(list):

    def isEmpty(self):
        return self == []

    def push(self, item):
        self.append(item)

    def peek(self):
        return self[- 1]

    def size(self):
        return len(self)

    def __repr__(self):
        l = len(self) * 7
        s = "|" + "-" * l + ")\n|"
        for i in self:
            s+="| %-5s" %i
        s+="\n|"+"-"*l+")"
        return  s


