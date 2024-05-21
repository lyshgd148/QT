import json
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

learn_rate = 0.055
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


def renew_w_3():
    global w_3_new
    vec16x1 = np.reshape(v, (16, 1))
    vec1x10 = np.reshape(b_3_new, (1, 10))
    w_3_new = np.dot(vec16x1, vec1x10)


v_matrix = np.zeros((16, 16))


def renew_b_2():
    global b_2_new, v_matrix
    temp = [[v[i] * (1 - v[i]) if i == j else 0 for j in range(16)] for i in range(16)]
    v_matrix = np.array(temp)
    temp = np.dot(v_matrix, w_3)
    vec10x1 = np.reshape(b_3_new, (10, 1))
    temp = np.dot(temp, vec10x1)
    b_2_new = np.reshape(temp, 16)


def renew_w_2():
    global w_2_new
    vec16x1 = np.reshape(u, (16, 1))
    vec1x10 = np.reshape(b_3_new, (1, 10))
    vec16x16 = np.transpose(w_3)
    temp = np.dot(vec16x1, vec1x10)
    temp = np.dot(temp, vec16x16)
    temp = np.dot(temp, v_matrix)
    w_2_new = np.reshape(temp, (16, 16))


u_matrix = np.zeros((16, 16))


def renew_b_1():
    global b_1_new, u_matrix
    temp = [[u[i] * (1 - u[i]) if i == j else 0 for j in range(16)] for i in range(16)]
    u_matrix = np.array(temp)
    vec1x10 = np.reshape(b_3_new, (1, 10))
    vec16x16_1 = np.transpose(w_3)
    vec16x16_2 = np.transpose(w_2)
    temp = np.dot(vec1x10, vec16x16_1)
    temp = np.dot(temp, v_matrix)
    temp = np.dot(temp, vec16x16_2)
    temp = np.dot(temp, u_matrix)
    b_1_new = np.reshape(temp, 16)


def renew_w_1(data_):
    global w_1_new
    vec784x1 = np.reshape(data_, (784, 1))
    vec1x16 = np.reshape(b_1_new, (1, 16))
    temp = np.dot(vec784x1, vec1x16)
    w_1_new = temp


if __name__ == "__main__":
    picture_train_start = {0: 1, 1: 4933, 2: 10611,
                           3: 15579, 4: 20680, 5: 25539,
                           6: 30045, 7: 34996, 8: 40171,
                           9: 45013}
    picture_train_end = {0: 1 + 4000, 1: 4933 + 4000, 2: 10611 + 4000,
                         3: 15579 + 4000, 4: 20680 + 4000, 5: 25539 + 4000,
                         6: 30045 + 4000, 7: 34996 + 4000, 8: 40171 + 4000,
                         9: 45013 + 4000}

    picture_test_start = {0: 4932 - 99, 1: 10610 - 99, 2: 15578 - 99,
                          3: 20679 - 99, 4: 25538 - 99, 5: 30044 - 99,
                          6: 34995 - 99, 7: 40170 - 99, 8: 45012 - 99,
                          9: 50000 - 99}
    picture_test_end = {0: 4932, 1: 10610, 2: 15578,
                        3: 20679, 4: 25538, 5: 30044,
                        6: 34995, 7: 40170, 8: 45012,
                        9: 50000}
    right = 0
    time = 0
    loss = list()

    for i in range(41000):
        num = i % 10
        if picture_train_start[num] <= picture_train_end[num]:
            data = get_data(f'./picture/{num}/{picture_train_start[num]}.jpg')
            picture_train_start[num] += 1

            y_real = np.array([0.999 if j == num else 0.001 for j in range(10)])
            get_u(data, w_1)
            get_v(u, w_2)
            get_y(v, w_3)
            renew_b_3(y_real)
            renew_w_3()
            renew_b_2()
            renew_w_2()
            renew_b_1()
            renew_w_1(data)
            b_3 = b_3 - learn_rate * b_3_new
            b_2 = b_2 - learn_rate * b_2_new
            b_1 = b_1 - learn_rate * b_1_new
            w_3 = w_3 - learn_rate * w_3_new
            w_2 = w_2 - learn_rate * w_2_new
            w_1 = w_1 - learn_rate * w_1_new

            tt = np.sum((y - y_real) ** 2)
            loss.append(tt)
            time += 1
            print(f"第——{time}——轮训练")

    for i in range(1000):
        num = i % 10
        if picture_test_start[num] <= picture_test_end[num]:
            data = get_data(f'./picture/verification/{picture_test_start[num]}.jpg')
            picture_test_start[num] += 1
            get_u(data, w_1)
            get_v(u, w_2)
            get_y(v, w_3)
            index = np.argmax(y)
            if index == num:
                print(f"{picture_train_start[num]}.jpg", num)
                right += 1

    print(f'准确率:{right / 1000}')

    with open('./w_1.json', 'w') as f:
        hh = w_1.tolist()
        json.dump(hh, f)
    with open('./w_2.json', 'w') as f:
        hh = w_2.tolist()
        json.dump(hh, f)
    with open('./w_3.json', 'w') as f:
        hh = w_3.tolist()
        json.dump(hh, f)
    with open('./b_1.json', 'w') as f:
        hh = b_1.tolist()
        json.dump(hh, f)
    with open('./b_2.json', 'w') as f:
        hh = b_2.tolist()
        json.dump(hh, f)
    with open('./b_3.json', 'w') as f:
        hh = b_3.tolist()
        json.dump(hh, f)

    plt.plot(np.arange(1, 40011), loss)
    plt.show()
