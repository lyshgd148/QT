import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('test.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(type(img), img.shape)
# 现在我要更改图片了：
ary = np.array([[0] * 400] * 200)
print(ary.shape)
img[200:400, 200:600] = ary
# 好，我要上下颠倒图像了
img = img[::-1]

# 显示图片方法1:
plt.imshow(img, cmap='jet', origin='upper')
plt.colorbar()
plt.show()

# # 显示图片方法2:
# cv2.imshow('yuyin', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
