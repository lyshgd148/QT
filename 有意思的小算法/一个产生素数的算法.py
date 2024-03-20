# 产生一个 <N 的所有素数

# def Prime(n):
#     prime_list = list(range(1, n + 1))
#     for i in range(2, n // 2 + 1):
#         for j in prime_list:
#             if j % i == 0 and j != i:
#                 prime_list.remove(j)
#     return prime_list
#
#
# with open('prime.txt', 'w') as f:
#     list1 = Prime(100000)
#     n = 1
#     for i in list1:
#         if n % 10 == 0:
#             f.write(str(i) + '\n')
#         else:
#             f.write(str(i) + ',')
#         n += 1

# 哈哈先生成10w个简单测试一下,牛逼


# 产生素数的改进算法 ,开根算法极大的减少了运算量
# import math
#
#
# def Prime(n):
#     prime_list = list(range(1, n + 1))
#     for i in range(2, int(math.sqrt(n)) + 1):
#         for j in prime_list:
#             if j % i == 0 and j != i:
#                 prime_list.remove(j)
#     return prime_list
#
#
# with open('prime.txt', 'w') as f:
#     list1 = Prime(1000000)
#     n = 1
#     for i in list1:
#         if n % 20 == 0:
#             f.write(str(i) + '\n')
#         else:
#             f.write(str(i) + ',')
#         n += 1


# 算法再改进 我靠这算法的效率简直就是超级加倍！！！
import math


def Prime(n):
    prime_list = [2]
    for i in range(3, n + 1):
        flag = True  # 增加一个变量用于判断是否为质数
        if i % 2 != 0:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    flag = False
                    break  # 跳出内部循环
        else:
            flag = False
        if flag:
            prime_list.append(i)
    return prime_list


with open('prime.txt', 'w') as f:
    list1 = Prime(100000000)
    n = 1
    for i in list1:
        if n % 20 == 0:
            f.write(str(i) + '\n')
        else:
            f.write(str(i) + ',')
        n += 1
 