import cv2
import numpy as np

image = cv2.imread("./picture/7.jpg")


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


fianl_process(image, [323, 395, 0, 96])
fianl_process(image, [319, 390, 116, 1005])
fianl_process(image, [310, 376, 1027, 1078])
fianl_process(image, [508, 580, 0, 95])
fianl_process(image, [500, 570, 122, 1001])
fianl_process(image, [490, 550, 1037, 1078])
fianl_process(image, [690, 760, 0, 90])
fianl_process(image, [675, 745, 124, 1014])
fianl_process(image, [666, 734, 1045, 1078])

cv2.imwrite('./picture/7_.jpg', image)
cv2.imshow("Color Detection Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
