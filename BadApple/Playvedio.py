import numpy as np
import cv2
Num=0


while Num<=6473:
    Num+=1
    frame = cv2.imread(f"./picture/{Num}.jpg")
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame=frame[2:476, 107:743]
    kernel = np.ones((7, 7), np.uint8)
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    image = cv2.erode(frame, kernel, iterations=1)
    image = cv2.dilate(image, kernel, iterations=1)

    # 使用Canny边缘检测算法
    edges = cv2.Canny(image, 50, 125)  # 100和200分别是低阈值和高阈值

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f'{Num}'
    org = (50, 50)  # 文本左下角的坐标
    fontScale = 0.8
    color = (255, 0, 0)  # 字体颜色，这里为蓝色
    thickness = 2  # 字体粗细

    image_with_text = cv2.putText(edges, text, org, font, fontScale, color, thickness, cv2.LINE_AA)


    cv2.imshow('image', edges)

    k = cv2.waitKey(10)
    if (k & 0xff == ord('q')):
        break

cv2.destroyAllWindows()