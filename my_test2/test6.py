import cv2
import numpy as np

image = cv2.imread("./picture/6.jpg")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_color = np.array([0, 198, 170])  # 最低颜色阈值
upper_color = np.array([255, 255, 255])  # 最高颜色阈值

# 创建掩膜（通过阈值化）
mask = cv2.inRange(hsv_image, lower_color, upper_color)
# 对原始图像应用掩膜
result = cv2.bitwise_and(image, image, mask=mask)

kernel1 = np.ones((2, 2), np.uint8)
kernel2 = np.ones((3, 3), np.uint8)
# # 腐蚀操作
result = cv2.erode(result, kernel1, iterations=1)
# # 膨胀操作
result = cv2.dilate(result, kernel2, iterations=1)
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if len(cnt) >= 4:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        print(box)

        cv2.drawContours(result, [box], 0, (0, 255, 0), 2)


def process_image(image, arr):
    image_ = image[arr[0]:arr[1], arr[2]:arr[3], 0:3]
    image_ = cv2.cvtColor(image_, cv2.COLOR_BGR2GRAY)
    _, image_ = cv2.threshold(image_, 125, 255, cv2.THRESH_BINARY_INV)
    return image_


def gray_rgb(image):
    page, lie = image.shape
    image_ = np.zeros((page, lie, 3))
    for i in range(page):
        for j in range(lie):
            image_[i][j][0:3] = image[i, j]
    return image_


def fianl_process(image, arr):
    i_n = process_image(image, arr)
    i_n = gray_rgb(i_n)
    image[arr[0]:arr[1], arr[2]:arr[3], 0:3] = i_n


fianl_process(image, [536, 601, 2, 68])
fianl_process(image, [525, 594, 1002, 1079])
fianl_process(image, [520, 600, 86, 974])
fianl_process(image, [357, 423, 2, 65])
fianl_process(image, [354, 418, 1002, 1079])
fianl_process(image, [349, 422, 87, 975])
fianl_process(image, [175, 243, 2, 65])
fianl_process(image, [173, 240, 1010, 1079])
fianl_process(image, [169, 246, 85, 991])

cv2.imshow("Color Detection Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
