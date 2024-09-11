# 从汉诺塔(Hanoi)去理解递归

def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n - 1) + 1


result = hanoi(64)
print(result)