import cv2
import sys

sys.setrecursionlimit(20000)  # 限制递归次数
# 图像的读取，二分割
image = cv2.imread('./test.png')
h, w, c = image.shape
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, image = cv2.threshold(gray_image, 127, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 转化为0和1
temp0 = image == 0
temp1 = image == 1
image[temp1] = 2
image[temp1] = 0
image[temp0] = 1
image_new = image


# dfs算法 寻找连通域 非常简单
def dfs(i, j):
    if i < 0 or j < 0 or i > h - 1 or j > w - 1 or image_new[i][j] != 1:
        return
    image_new[i][j] = 2
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

num = 0
for i in range(h):
    for j in range(w):
        if image_new[i][j] == 1:
            num += 1
            dfs(i, j)

print(f'图像中的连同区域有{num}个')

# 显示图像
cv2.imshow(' ', image * 255)
cv2.waitKey(0)
cv2.destroyAllWindows()
                            #刘雨生 写于2024.4.18
