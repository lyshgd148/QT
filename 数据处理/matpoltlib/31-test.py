import cv2
import numpy as np
from scipy.signal import convolve2d

kernel = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [1, 0, -1]])

kernel1 = np.array([[1, 0, -1],
                    [2, 0, -2],
                    [1, 0, -1]])

# kernel = kernel[::-1, ::-1]

img = cv2.imread('test.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray1 = convolve2d(gray, kernel, 'same')
gray2 = convolve2d(gray, kernel1, 'same')
gray=(gray1+gray2)/2

# 归一化处理
gray = (gray - np.min(gray)) / (np.max(gray) - np.min(gray)) * 255
gray = np.round(gray).astype(np.uint8)



# gray = (gray - np.min(gray)) / (np.max(gray) - np.min(gray)) * 255
# gray = np.round(gray).astype(np.uint8)

print(gray)
cv2.imshow('Gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
