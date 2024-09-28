
import cv2
import numpy as np


class GetColor:
    def __init__(self):
        self.path=["./picture/1.jpg","./picture/2.jpg","./picture/3.jpg","./picture/4.jpg","./picture/5.jpg","./picture/6.jpg"]
        self.colors=[]


    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                self.image_copy = self.image.copy()
                cv2.rectangle(self.image_copy, (self.ix, self.iy), (x, y), (0, 255, 0), 2)
                cv2.imshow('image', self.image_copy)

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            cv2.rectangle(self.image, (self.ix, self.iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', self.image)

            w, h = abs(self.ix - x), abs(self.iy - y)
            roi = self.image[min(self.iy, y):min(self.iy, y) + h, min(self.ix, x):min(self.ix, x) + w]
            roi = cv2.resize(roi, (300, 300))
            self.getColor(roi)
            cv2.imshow('ROI', roi)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def getColor(self,imgOutput1):
        imgOutput1 = cv2.resize(imgOutput1, (300, 300))
        width, height = 300, 300  # 设定图片大小
        yellow_min = np.array([10, 200, 140])
        yellow_max = np.array([50, 255, 240])
        red_min = np.array([0, 150, 90])
        red_max = np.array([10, 255, 145])
        blue_min = np.array([100, 60, 40])
        blue_max = np.array([130, 220, 110])
        white_min = np.array([6, 7, 130])
        white_max = np.array([50, 40, 200])
        orange_min = np.array([0, 50, 170])
        orange_max = np.array([20, 255, 255])
        green_min = np.array([40, 130, 100])
        green_max = np.array([80, 210, 180])
        color=[]


        for i in range(3):
            temp = []
            for j in range(3):
                y_start = i * width // 3
                y_end = (i + 1) * width // 3
                x_start = j * width // 3
                x_end = (j + 1) * width // 3
                pic = imgOutput1[y_start:y_end, x_start:x_end]
                hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
                mask_red = cv2.inRange(hsv, red_min, red_max)
                red_bili = cv2.countNonZero(mask_red) / (pic.size / 3)
                mask_yellow = cv2.inRange(hsv, yellow_min, yellow_max)
                yellow_bili = cv2.countNonZero(mask_yellow) / (pic.size / 3)
                mask_blue = cv2.inRange(hsv, blue_min, blue_max)
                blue_bili = cv2.countNonZero(mask_blue) / (pic.size / 3)
                mask_white = cv2.inRange(hsv, white_min, white_max)
                white_bili = cv2.countNonZero(mask_white) / (pic.size / 3)
                mask_orange = cv2.inRange(hsv, orange_min, orange_max)
                orange_bili = cv2.countNonZero(mask_orange) / (pic.size / 3)
                mask_green = cv2.inRange(hsv, green_min, green_max)
                green_bili = cv2.countNonZero(mask_green) / (pic.size / 3)
                if red_bili >= 0.2:
                    print(f"第{self.k+1}张图第" + str(3 * i + j + 1) + "个格子:红")
                    temp.append("红")
                elif yellow_bili >= 0.2:
                    print(f"第{self.k+1}张图第" + str(3 * i + j + 1) + "个格子:黄")
                    temp.append("黄")
                elif blue_bili >= 0.2:
                    print(f"第{self.k+1}张图第" + str(3 * i + j + 1) + "个格子:蓝")
                    temp.append("蓝")
                elif white_bili >= 0.2:
                    print(f"第{self.k+1}张图第" + str(3 * i + j + 1) + "个格子:白")
                    temp.append("白")
                elif orange_bili >= 0.2:
                    print(f"第{self.k+1}张图第" + str(3 * i + j + 1) + "个格子:橙")
                    temp.append("橙")
                elif green_bili >= 0.2:
                    print(f"第{self.k+1}张图第" + str(3 * i + j + 1) + "个格子:绿")
                    temp.append("绿")
                else:
                    print(f"第{self.k+1}张图第" + str(3 * i + j + 1) + "个格子:空")
                    temp.append("空")
            color.append(temp)
        self.colors.append(color)

    def Oneprocess(self,path):
        self.drawing = False
        self.ix, self.iy = -1, -1
        self.image = cv2.imread(path)
        self.image = cv2.resize(self.image, (self.image.shape[1] // 2, self.image.shape[0] // 2))
        self.image_copy = self.image.copy()
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.draw_rectangle)

        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def run(self):
        for k in range(6):
            self.k=k
            self.Oneprocess(self.path[k])
        return self.colors



drawer = GetColor()
color=drawer.run()
print(color)