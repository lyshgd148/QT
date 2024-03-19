import struct


def fast_inverse_square_root(number):
    x2 = number * 0.5
    y = number
    i = struct.unpack('I', struct.pack('f', y))[0]
    i = 0x5f3759df - (i >> 1)
    y = struct.unpack('f', struct.pack('I', i))[0]
    y = y * (1.5 - (x2 * y * y))
    return y


print(fast_inverse_square_root(9))  ### WTF 这段代码太吊了！！雷神3优化同款算法！！！



#####留个小坑 是否可以作出其函数图像！！
