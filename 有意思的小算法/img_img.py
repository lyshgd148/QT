import cv2
import numpy as np

img = cv2.imread("test.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = img[::2]
img = img[:, ::2]
img = img[0:500:, 0:500:]
img = np.dot(img, img)
img = img.astype(np.uint8)
print(img)
cv2.imshow('Img_img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
