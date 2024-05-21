import cv2
import numpy as np

path = "9.jpg"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
kernel = np.ones((2, 2), np.uint8)
image = cv2.dilate(image, kernel, iterations=1)
cv2.imwrite(path, image)
print(image.shape)

# m = len(image)
# n = len(image[0])
# print(m / 28, n / 28)
#
# num = 1
# for i in range(0, m // 28):
#     for j in range(n // 28):
#         image_block = image[i * 28:i * 28 + 28, j * 28:j * 28 + 28]
#         cv2.imwrite(f"./picture/{num}.jpg", image_block)
#         num += 1
