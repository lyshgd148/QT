import os


def transform(num):
    Snum = str(num)
    if num < 100:
        byte = int(Snum, 16)
        low = bytes([int('0', 16)])
        byte = bytes([byte])
        byte = byte + low
    else:
        high = bytes([int(str(num // 100), 16)])
        low = bytes([int(str(num % 100), 16)])
        byte = low + high
    return byte


dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir, 'test.bin'), 'wb') as f:
    for i in range(256):
        f.write(transform(i))

"""
var = int('199', 16)
print(var.to_bytes(2, 'little'), type(var))
"""

