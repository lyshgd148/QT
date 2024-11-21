def encrypt(string):
    import math
    num = math.sqrt(len(string))
    if num - int(num) > 0:
        num = int(num) + 1
        for _ in range(num * num - len(string)):
            string += " "
    else:
        num = int(num)

    ls = [[None for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            ls[i][j] = string[i * num + j]
    string = ""
    for i in range(num):
        for j in range(num):
            string += ls[num - 1 - j][i]
    return string


def decrypt(string):
    import math
    num = int(math.sqrt(len(string)))
    ls = [["" for i in range(num)] for j in range(num)]
    strings = ""
    for i in range(num):
        for j in range(num):
            ls[num - 1 - j][i] = string[i * num + j]
    for i in range(num):
        for j in range(num):
            strings += ls[i][j]
    return strings


string = "!HEllo  world!!!"
print(encrypt(string), "*****", decrypt(encrypt(string)))
