import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('test.jpeg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# 上下翻转图像
img = img1[::-1]
plt.figure('picture1')
plt.imshow(img, cmap='gray')

plt.figure('picture2')
plt.imshow(img1, cmap='jet', origin='upper')
plt.colorbar()

plt.figure('3D')
x = np.arange(img.shape[1])
y = np.arange(img.shape[0])
x, y = np.meshgrid(x, y)
ax3d = plt.axes(projection='3d')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
ax3d.plot_wireframe(x, y, img)

# 显示
plt.show()
