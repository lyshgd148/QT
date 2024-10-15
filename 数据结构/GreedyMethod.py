def GreedyMethod(money):
    # 贪心策略
    value = []
    if money <= 0:
        return 0, []
    elif money >= 100:
        money -= 100
        value.append(100)
    elif 50 <= money < 100:
        money -= 50
        value.append(50)
    elif 20 <= money < 50:
        money -= 20
        value.append(20)
    elif 10 <= money < 20:
        money -= 10
        value.append(10)
    elif 5 <= money < 10:
        money -= 5
        value.append(5)
    elif 1 <= money < 5:
        money -= 1
        value.append(1)
    num, zhi = GreedyMethod(money)
    return 1 + num, value + zhi


print(GreedyMethod(14))
