import numpy as np
import cv2
import math

picture_data = {0: 4932 - 100, 1: 10610 - 100, 2: 15578 - 100,
                3: 20679 - 100, 4: 25538 - 100, 5: 30044 - 100,
                6: 34995 - 100, 7: 40170 - 100, 8: 45012 - 100,
                9: 50000 - 100}

learn_rate = 0.01
w_1 = np.random.uniform(-np.sqrt(6 / 800), np.sqrt(6 / 800), size=(784, 16))
u = np.zeros(16)
b_1 = np.array([0 for _ in range(16)])
w_2 = np.random.uniform(-np.sqrt(6 / 32), np.sqrt(6 / 32), size=(16, 16))
v = np.zeros(16)
b_2 = np.array([0 for _ in range(16)])
w_3 = np.random.uniform(-np.sqrt(6 / 17), np.sqrt(6 / 17), size=(16, 10))
b_3 = np.array([0 for _ in range(10)])
y = np.zeros(10)

w_1_new = np.zeros((784, 16))
b_1_new = np.zeros(16)
w_2_new = np.zeros((16, 16))
b_2_new = np.zeros(16)
w_3_new = np.zeros((16, 10))
b_3_new = np.zeros(10)


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


def renew_b_3(y_real):
    global b_3_new
    b_3_new = 2 * (y - y_real) * y * (1 - y)


def renew_w_3(v_):
    global w_3_new
    vec16x1 = np.reshape(v_, (16, 1))
    vec1x10 = np.reshape(b_3_new, (1, 10))
    w_3_new = np.dot(vec16x1, vec1x10)


def renew_b_2(v_):
    global b_2_new
    v_matrix = [[v_[i] * (1 - v_[i]) if i == j else 0 for j in range(16)] for i in range(16)]
    v_matrix = np.array(v_matrix)
    temp = np.dot(v_matrix, w_3)
    vec10x1 = np.reshape(b_3_new, (10, 1))
    temp = np.dot(temp, vec10x1)
    b_2_new = np.reshape(temp, 16)


def renew_w_2():
    pass


data = get_data('./picture/0/1.jpg')
get_u(data, w_1)
get_v(u, w_2)
get_y(v, w_3)
# print(u, v, y)
renew_b_3(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
renew_w_3(v)
# print(w_3_new.shape)
renew_b_2(v)
# print(b_2_new, b_2_new.shape)
