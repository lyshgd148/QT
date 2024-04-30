import cv2
import numpy as np

image = cv2.imread("./picture/1.jpg")


def process_image(image, arr):
    image_ = image[arr[0]:arr[1], arr[2]:arr[3], 0:3]
    image_ = cv2.cvtColor(image_, cv2.COLOR_BGR2GRAY)
    _, image_ = cv2.threshold(image_, 170, 255, cv2.THRESH_BINARY_INV)
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


fianl_process(image, [174, 238, 94, 980])
fianl_process(image, [354, 424, 93, 967])
fianl_process(image, [357, 410, 1005, 1073])
fianl_process(image, [542, 595, 0, 61])
fianl_process(image, [530, 595, 96, 968])

cv2.imwrite('./picture/1_.jpg', image)
cv2.imshow("Color Detection Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
