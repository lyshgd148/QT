import math


def round_area(r):
    s = r ** 2 * math.pi
    print('半径为{0}的圆面积大约是:{1:.2f}'.format(r, s))


round_area(3.1)
