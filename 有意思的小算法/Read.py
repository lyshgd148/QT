f = open('test.txt', 'wb+')
f.write(b'0123456789abcdef')
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))
f.close()
#f.seek()对文件指针进行操作