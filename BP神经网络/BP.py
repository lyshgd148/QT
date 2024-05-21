import json
import numpy as np
import cv2
import math

with open('w_1.json') as f:
    w_1 = json.load(f)
    w_1 = np.array(w_1)

with open('w_2.json') as f:
    w_2 = json.load(f)
    w_2 = np.array(w_2)

with open('w_3.json') as f:
    w_3 = json.load(f)
    w_3 = np.array(w_3)

with open('b_1.json') as f:
    b_1 = json.load(f)
    b_1 = np.array(b_1)

with open('b_2.json') as f:
    b_2 = json.load(f)
    b_2 = np.array(b_2)

with open('b_3.json') as f:
    b_3 = json.load(f)
    b_3 = np.array(b_3)

y = np.zeros(10)
u = np.zeros(16)
v = np.zeros(16)


def get_data(path):
    image = cv2.imread(path)
    image = image / 255
    image = image[:, :, 0]
    image = image.flatten()
    return image


def sigmog(x):
    data = 1 / (1 + math.e ** (-x))
    return data


def get_u(x, w):
    global u
    for i in range(16):
        num = np.dot(x, w[:, i])
        num += b_1[i]
        num = sigmog(num)
        u[i] = num


def get_v(u_, w):
    global v
    for i in range(16):
        num = np.dot(u_, w[:, i])
        num += b_2[i]
        num = sigmog(num)
        v[i] = num


def get_y(v_, w):
    global y
    for i in range(10):
        num = np.dot(v_, w[:, i])
        num += b_3[i]
        num = sigmog(num)
        y[i] = num


if __name__ == "__main__":
    # data = get_data('./picture/verification/10511.jpg')
    data = get_data('./9.jpg')
    get_u(data, w_1)
    get_v(u, w_2)
    get_y(v, w_3)
    index = np.argmax(y)
    print(f'图片是{index}')
