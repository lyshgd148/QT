import cv2

path = './picture/250.jpg'
image = cv2.imread(path)
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# 使用Canny边缘检测算法
edges = cv2.Canny(blurred_image, 100, 200)  # 100和200分别是低阈值和高阈值
edges2 = cv2.Canny(image, 100, 200)

cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)
cv2.imshow('Canny Edge Detection2', edges2)
cv2.waitKey(0)
cv2.destroyAllWindows()