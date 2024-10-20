import cv2

Num = 1
while Num <= 6473:
    Num += 1
    path = f'./picture/{Num}.jpg'
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = gray[2:476, 107:743]
    cv2.imwrite(f"./picture/{Num}.jpg", gray)
