import cv2
import numpy as np

image = cv2.imread("./picture/2.jpg")


def process_image(image, arr,value=220,type=cv2.THRESH_BINARY_INV):
    image_ = image[arr[0]:arr[1], arr[2]:arr[3], 0:3]
    image_ = cv2.cvtColor(image_, cv2.COLOR_BGR2GRAY)
    _, image_ = cv2.threshold(image_, value, 255, type)
    return image_


def gray_rgb(image):
    page, lie = image.shape
    image_ = np.zeros((page, lie, 3))
    for i in range(page):
        for j in range(lie):
            image_[i][j][0:3] = image[i, j]
    return image_


def fianl_process(image, arr,value=220,type=cv2.THRESH_BINARY_INV):
    i_n = process_image(image, arr,value,type)
    i_n = gray_rgb(i_n)
    image[arr[0]:arr[1], arr[2]:arr[3], 0:3] = i_n


fianl_process(image, [34, 79, 6, 454])
fianl_process(image, [36, 72, 490, 1073])
fianl_process(image, [139, 178, 10, 448])
fianl_process(image, [129, 176, 485, 1072])
fianl_process(image, [263, 311, 12, 452])
fianl_process(image, [244, 305, 487, 1074])
fianl_process(image, [427, 504, 5, 453])
fianl_process(image, [388, 483, 488, 1075],155,cv2.THRESH_BINARY)
fianl_process(image, [655, 773, 0, 446])
fianl_process(image, [618, 737, 488, 1077])


cv2.imwrite('./picture/2_.jpg', image)
cv2.imshow("Color Detection Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
