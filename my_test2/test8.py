import cv2
import numpy as np

image = cv2.imread("./picture/8.jpg")


def process_image(image, arr):
    image_ = image[arr[0]:arr[1], arr[2]:arr[3], 0:3]
    image_ = cv2.cvtColor(image_, cv2.COLOR_BGR2GRAY)
    _, image_ = cv2.threshold(image_, 45, 255, cv2.THRESH_BINARY)
    return image_


def gray_rgb(image):
    page, lie = image.shape
    image_ = np.zeros((page, lie, 3))
    for i in range(page):
        for j in range(lie):
            image_[i][j][0:3] = image[i, j]
    return image_


def fianl_process(image, arr):
    i_n = process_image(image, arr)
    i_n = gray_rgb(i_n)
    image[arr[0]:arr[1], arr[2]:arr[3], 0:3] = i_n


fianl_process(image, [21, 807, 19, 83])
fianl_process(image, [25, 805, 185, 240])
fianl_process(image, [23, 802, 337, 400])
fianl_process(image, [30, 797, 490, 555])
fianl_process(image, [33, 798, 643, 701])
fianl_process(image, [30, 800, 800, 860])
fianl_process(image, [31, 800, 956, 1016])

cv2.imwrite('./picture/8_.jpg', image)
cv2.imshow("Color Detection Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
