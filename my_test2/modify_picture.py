import cv2
import numpy as np
import copy


# for i in range(1, 7):
#     image = cv2.imread(f'./picture/{i}.jpg')
#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


def process_picture(image):
    image_ = copy.deepcopy(image)


if __name__ == '__main__':
    image = cv2.imread(f'./picture/6.jpg')

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY_INV)
    process_picture(image)

    image_original = cv2.imread(f'./picture/6.jpg')

    # cv2.imshow('Image_original', image_original)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(image)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
