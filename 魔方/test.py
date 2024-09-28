import cv2
import numpy as np

img = cv2.imread('./picture/6.jpg')
img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))


HSV=cv2.cvtColor(img ,cv2.COLOR_BGR2HSV)
def getpos(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN: #定义一个鼠标左键按下去的事件
        print(HSV[y,x])

cv2.imshow("imageHSV",HSV)
cv2.imshow('image',img )
cv2.setMouseCallback("imageHSV",getpos)
cv2.waitKey(0)

