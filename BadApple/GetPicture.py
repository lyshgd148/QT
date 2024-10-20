import numpy as np
import cv2

cap = cv2.VideoCapture('./video/1.mp4')
Num=0

while(cap.isOpened()):
    Num+=1
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    cv2.imwrite(f"./picture/{Num}.jpg", frame)
    k = cv2.waitKey(20)
    if (k & 0xff == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()