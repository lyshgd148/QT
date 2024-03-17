# import sys
# import cv2
#
# grays = "@%#*+=-:. "  # 由于控制台是白色背景，所以先密后疏/黑色背景要转置一下
# gs = 10  # 10级灰度
# # grays2 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^.` "
# # gs2 = 67
#
# img = cv2.imread('./test.jpeg', 0)  # 读入灰度图
#
# # 宽（列）和高（行数）
# w = img.shape[1]
# h = img.shape[0]
# ratio = float(w) / h  # 调整长宽比 (**注：此比例为win cmd，ratio需要根据不同终端的字符长宽调整)
#
# scale = w // 150  # 缩放尺度，向下取整，每50个像素取一个 值越小图越小(scale 越大)
#
# for y in range(0, h, int(scale * ratio)):  # 根据缩放长度 遍历高度 y对于h，x对应w
#     for x in range(0, w, scale):  # 根据缩放长度 遍历宽度
#         idx = img[y][x] * gs // 255  # 获取每个点的灰度  根据不同的灰度填写相应的 替换字符
#         if idx == gs:
#             idx = gs - 1
#         sys.stdout.write(grays[idx])  # 写入控制台
#     sys.stdout.write('\n')
#     sys.stdout.flush()
#
#



# import sys
# import os
#
# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')
#
# # 清除控制台输出
# clear_console()
# def set_cursor_position(x, y):
#     sys.stdout.write(f"\033[{y};{x}H")
#
# def print_at_position(x, y, text):
#     set_cursor_position(x, y)
#     sys.stdout.write(text)
#     # set_cursor_position(0, 0)
#
#
# for i in range(1,200,5):
#     for j in range(1,200,10):
#         print_at_position(i, j, ".")
# sys.stdout.flush()



# import sys
# for i in range(200):
#     for j in range(200):
#         sys.stdout.write(".")
#     sys.stdout.write('\n')