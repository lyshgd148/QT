def recDC(VlueLists, change, Results):
    minCoins = change
    if change in VlueLists:
        Results[change] = 1
        return 1
    elif Results[change] != 0:
        return Results[change]
    else:
        for i in [c for c in VlueLists if change >= c]:
            numCoins = 1 + recDC(VlueLists, change - i, Results)
            if numCoins < minCoins:
                minCoins = numCoins
                Results[change] = minCoins
        return minCoins


print(recDC([1, 5, 10, 25], 63, [0] * 64))
