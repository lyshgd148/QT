import cv2
import wave
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []


def getXY(path):
    global x, y
    kernel = np.ones((7, 7), np.uint8)
    image = cv2.imread(path)
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    blurred_image = cv2.erode(blurred_image, kernel, iterations=1)
    blurred_image = cv2.dilate(blurred_image, kernel, iterations=1)
    edges = cv2.Canny(blurred_image, 50, 125)  # 100和200分别是低阈值和高阈值

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        for point in contour:
            x_, y_ = point[0]
            y_ = -y_ + 474
            x.append(x_)
            y.append(y_)


def getvedio():
    for i in range(1, 6474):
        print(i)
        path = f"./picture/{i}.jpg"
        getXY(path)


left = [i / 636 for i in x]
right = [i / 474 for i in y]
left = np.array(left)
right = np.array(right)
with wave.open("./BadApple.wav", 'w') as f:
    f.setnchannels(2)  # 设置为双声道
    f.setsampwidth(2)  # 设置采样宽度为 2 字节（16位）
    f.setframerate(44100)  # 设置采样率

    # 将左右声道数据合并为双声道数据
    data = np.zeros((len(left), 2), dtype=np.int16)
    data[:, 0] = (left * 32767).astype(np.int16)
    data[:, 1] = (right * 32767).astype(np.int16)
    f.writeframes(data.tobytes())

plt.figure()
getvedio()
xx = np.arange(len(x))
print(len(x) / 44000)
plt.plot(xx, x, "r")
# plt.plot(xx, y, "blue")
plt.show()
