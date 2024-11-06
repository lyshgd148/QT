import sys
sys.setrecursionlimit(10000)
def recDC(VlueLists, change, Results, Money):
    minCoins = change
    if change in VlueLists:
        Results[change] = 1
        return 1, [change]
    elif Results[change] != 0:
        temp=Money[change][:]
        return Results[change], temp
    else:
        minMoney = []
        for i in [c for c in VlueLists if change >= c]:
            numCoins, numMoney = recDC(VlueLists, change - i, Results, Money)
            # print(Money,change,i)
            numCoins += 1
            numMoney += [i]
            if numCoins <= minCoins:
                minCoins = numCoins
                Results[change] = minCoins
                minMoney = numMoney
        Money[change] += minMoney
        return minCoins, minMoney #我靠这里不能返回 Money[change] 因为返回给一个变量后 其实是这个变量指向Money[change]


num = 7024
print(recDC([1, 5, 10, 25], num, [0] * (num + 1), [[] for _ in range(num + 1)]))
