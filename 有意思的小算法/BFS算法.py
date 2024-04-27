import cv2
import sys
import copy

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
image_new = copy.deepcopy(image)

# bfs算法 寻找连通域 一种更快速的算法
temp = list()


def bfs(i, j):
    global temp
    if i - 1 >= 0 and image_new[i - 1][j] == 1:
        temp.append((i - 1, j))
        image_new[i - 1][j] = 2
    if j - 1 >= 0 and image_new[i][j - 1] == 1:
        temp.append((i, j - 1))
        image_new[i][j - 1] = 2
    if j + 1 <= len(image[0]) and image_new[i][j + 1] == 1:
        temp.append((i, j + 1))
        image_new[i][j + 1] = 2
    if i + 1 < len(image) and image_new[i + 1][j] == 1:
        temp.append((i + 1, j))
        image_new[i + 1][j] = 2

    if len(temp) !=0:
        i, j = temp.pop(0)
        bfs(i, j)
    else:
        return


num = 0
for i in range(h):
    for j in range(w):
        if image_new[i][j] == 1:
            num += 1
            bfs(i, j)

print(f'图像中的连同区域有{num}个')

# 显示图像
cv2.imshow(' ', image * 255)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 刘雨生 写于2024.4.18
