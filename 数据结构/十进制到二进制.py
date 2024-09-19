from struct_ import Stack


def divideByN(decNumber, N):
    remstack = Stack()
    digits = "0123456789ABCDEF"
    while decNumber > 0:
        rem = decNumber % N
        remstack.push(rem)
        decNumber = decNumber // N

    srtings = ""
    while not remstack.isEmpty():
        srtings += digits[remstack.pop()]
    return srtings


print(divideByN(233, 16))
