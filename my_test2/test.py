# import cv2
# import numpy as np
#
# img = cv2.imread("./picture/6.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 50, 150)
#
# contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#
# print(contours)
# for cnt in contours:
#     if len(cnt) >= 4:
#         rect = cv2.minAreaRect(cnt)
#         box = cv2.boxPoints(rect)
#         box = np.int0(box)
#
#         cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
#
# cv2.imshow("Result", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

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

#
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if len(cnt) >= 4:
        rect = cv2.minAreaRect(cnt)
        print(rect)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        cv2.drawContours(result, [box], 0, (0, 255, 0), 2)

# 显示结果图像
cv2.imshow("Color Detection Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
