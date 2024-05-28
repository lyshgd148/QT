# 以4x^5+3x^4+2x^3+x^2+x+10为例
def jiuzhao_Algorithm(temp, x):
    n = len(temp)
    result = 0
    for i in range(n - 1):
        result = (result + temp[i]) * x
    result += temp[-1]
    return result


if __name__ == "__main__":
    result = jiuzhao_Algorithm([4, 3, 2, 1, 1, 10], 2)
    print(result)
