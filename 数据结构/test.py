# import time
#
# t1 = time.time()
# print(t1)
# for i in range(10000000000):
#     pass
# t2 = time.time()
# print((t2 - t1) / 60)
#
# list1 = [1, 2, 3, None]
# print(list1, len(list1))


# def anagramSolution1(s1, s2):
#     sl = list(s2)
#     p1 = 0
#     Ok = True
#     while p1 < len(s1) and Ok:
#         p2 = 0
#         found = False
#         while p2 < len(sl) and not found:
#             if s1[p1] == sl[p2]:
#                 found = True
#             else:
#                 p2 = p2 + 1
#         if found:
#             sl[p2] = None
#         else:
#             Ok = False
#         p1 += 1
#     return Ok
#
#
# print(anagramSolution1('hello', 'helloe'))
#
#
# def anagramSolution2(s1, s2):
#     l1 = list(s1)
#     l2 = list(s2)
#     l1.sort()
#     l2.sort()
#     pos = 1
#     match = True
#     while pos < len(s1) and match:
#         if l1[pos] == l2[pos]:
#             pos += 1
#         else:
#             match = False
#     return match
#
#
# print(anagramSolution2('hello', 'llheoo'))


# def anagramSolution3(s1, s2):
#     c1 = [0] * 26
#     c2 = [0] * 26
#     for i in range(len(s1)):
#         pos = ord(s1[i]) - ord('a')
#         c1[pos] += 1
#     for i in range(len(s2)):
#         pos = ord(s2[i]) - ord('a')
#         c2[pos] += 1
#
#     i = 0
#     Ok = True
#     while i < 26 and Ok == True:
#         if c1[i] == c2[i]:
#             i = i + 1
#         else:
#             Ok = False
#     return Ok
#
#
# print(anagramSolution3('hello', 'llheoo'))


def test1():
    l = []
    for i in range(1000):
        l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))

from timeit import Timer
t1 = Timer("test1()", "from __main__ import test1")
print(t1.timeit(number=1000), '\n')

t2 = Timer("test2()", "from __main__ import test2")
print(t2.timeit(number=1000), '\n')

t3 = Timer("test3()", "from __main__ import test3")
print(t3.timeit(number=1000), '\n')

t4 = Timer("test4()", "from __main__ import test4")
print(t4.timeit(number=1000), '\n')
