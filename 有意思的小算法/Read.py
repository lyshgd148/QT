f = open('test.txt', 'wb+')
f.write(b'0123456789abcdef')
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))
f.close()
# f.seek(偏移量，1/2/3)对文件指针进行操作
# 0：表示从文件开头开始计算偏移量（起始位置是文件的开头）。
# 1：表示从当前文件指针位置开始计算偏移量（起始位置是当前文件指针的位置）。
# 2：表示从文件末尾开始计算偏移量（起始位置是文件的末尾）。
