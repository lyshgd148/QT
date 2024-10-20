import cv2
import numpy as np
import matplotlib.pyplot as plt

path = './picture/5412.jpg'
kernel = np.ones((9,9), np.uint8)
image = cv2.imread(path)
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
blurred_image = cv2.erode(blurred_image, kernel, iterations=1)
blurred_image = cv2.dilate(blurred_image, kernel, iterations=1)



# 使用Canny边缘检测算法
edges = cv2.Canny(blurred_image, 50, 75)  # 100和200分别是低阈值和高阈值

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 提取边缘点坐标
edge_points = []
for contour in contours:
    for point in contour:
        x, y = point[0]
        edge_points.append((x, y))

plt.figure()
x = [point[0] for point in edge_points]
y = [-point[1]+474 for point in edge_points]
plt.plot(x, y)
plt.axis('equal')
cv2.imshow('Original Image', image)
cv2.imshow('blurred_image', edges)
cv2.waitKey(0)

plt.show()
cv2.destroyAllWindows()
