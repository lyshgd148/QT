from struct_ import Stack


def match(left, right):
    left_ls = ['(', '[', '{']
    right_ls = [')', ']', '}']
    if left_ls.index(left) == right_ls.index(right):
        return True
    else:
        return False


def parChecker(symbolSring):
    s = Stack()
    bal = True
    index = 0

    while index < len(symbolSring) and bal:
        if symbolSring[index] in "([{":
            s.push(symbolSring[index])
            # print(symbolSring[index])
        else:
            if s.isEmpty():
                bal = False
                return bal
            else:
                symbol = s.pop()
                if match(symbol, symbolSring[index]):
                    pass
                else:
                    return False
        index += 1

    if s.isEmpty():
        return True
    else:
        return False


print(parChecker("(((()()()()()()()()()()())))"))
print(parChecker("(([)]())"))
