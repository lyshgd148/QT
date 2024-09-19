from struct_ import Deque


def palchecker(aString):
    chardeque = Deque()
    Equal = True

    for i in aString:
        chardeque.addRear(i)

    while chardeque.size() > 1 and Equal:
        last = chardeque.removeRear()
        first = chardeque.removeFront()

        if last != first:
            return False

    return Equal


print(palchecker("qweew"))
