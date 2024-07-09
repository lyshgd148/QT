def Next(s):
    n = len(s)
    temp = list()
    temp.append(0)
    for i in range(1, n):
        if s[temp[i - 1]] == s[i]:
            temp.append(temp[i - 1] + 1)
        else:
            if s[temp[temp[i - 1] - 1]] == s[i]:
                temp.append(temp[temp[i - 1] - 1] + 1)
            else:
                temp.append(0)
    return temp


def Kmp(S, s, nxt, i=0, j=0):
    global result
    if s[j] == S[i]:
        i += 1
        j += 1
    else:
        if j == 0:
            i += 1
        else:
            j = nxt[j - 1]
    if j == len(s):
        j = 0
        result.append(i - len(s))
    if i == len(S):
        return
    Kmp(S, s, nxt, i, j)


result = list()
S = " 人工智能1 hahhahah你阿斯3和你法术懂嗯嗯太有 意思了，人工智能2 可哈 看了。  多借 口11232dadfasfda达 人工智资能4 到！@！#@人工智能3萨达dasd1"
s = "人工智能"
nxt = Next(s)
Kmp(S, s, nxt)
print(result)

n = len(s)
m = len(S)
for i in range(len(result)):  # 将匹配到的字符串打印下来，并且多打印一个，便于判断
    if (result[i] + n) < m:
        print(S[result[i]:result[i] + n + 1])
    else:
        print(S[result[i]:result[i] + n])
