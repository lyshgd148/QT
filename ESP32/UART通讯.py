import time
import cv2
import numpy as np
import json
import serial

# 可以再往多线程上面想想，但现在我要完成任务，就这样吧！
flag = 0
ser = serial.Serial('COM4', 9600)
data_original = list()
time_start = time.time()
time_end = time.time()
while True:
    time_start = time.time()
    if ser.in_waiting > 0:
        flag += 1
        time_end = time.time()
        data = ser.read()
        number = int.from_bytes(data, byteorder='little')
        data_original.append(number)
        if flag % 100 == 0:
            print(number, end='\n')
        else:
            print(number, end=' ')
    if flag == 0:
        if (time_end - time_start) < -10:
            break
    elif flag != 1:
        if (time_end - time_start) < -1:
            break
ser.close()

with open("band.json", "r") as f:
    data_o = json.load(f)


def data_process(o_data):
    data_new = list()
    result = [o_data[i:i + 8] for i in range(0, len(o_data), 8)]
    new = 0

    for num in result:
        n = len(num)
        if n == 8:
            for i in range(7, -1, -1):
                new += num[7 - i] << i
            data_new.append(new)
            new = 0
    return data_new


result = data_process(data_original)
print(result)

result_ = [result[i:i + 100] for i in range(0, len(result), 100)]
if len(result_[-1]) < 100:
    result_ = result_[1:-2]
result_ = np.array(result_)
result_ = result_.astype(np.uint8)


def determine(n_data, data):
    n = len(data)
    m = len(n_data)
    right = 0
    rate = 0
    num = min(m, n)
    for i in range(num):
        if data[i] == n_data[i]:
            right += 1
    if num != 0:
        rate = right / num
    return rate


print(determine(result, data_o), len(result))
cv2.imshow("发送过来的图片", result_)
cv2.waitKey(0)
cv2.destroyAllWindows()
