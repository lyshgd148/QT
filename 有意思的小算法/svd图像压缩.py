import numpy as np
from PIL import Image


def Compress(channel, percent):
    u, s, vt = np.linalg.svd(channel)
    m = u.shape[0]
    n = vt.shape[0]
    rechannel = np.zeros((m, n))
    for k in range(len(s)):
        rechannel = rechannel + s[k] * np.dot(u[:, k].reshape(m, 1), vt[k, :].reshape(1, n))
        if float(k) / len(s) > percent:
            rechannel[rechannel < 0] = 0
            rechannel[rechannel > 255] = 255
    return np.rint(rechannel).astype("uint8")


image = Image.open("./picture/svd.png")
image = np.array(image)
R = image[:, :, 0]
G = image[:, :, 1]
B = image[:, :, 2]

for percent in [0.001, 0.005, 0.01, 0.02, 0.03, 0.05, 0.05, 0.1, 0.2, 0.3, 0.5]:
    rR = Compress(R, percent)
    rG = Compress(G, percent)
    rB = Compress(B, percent)
    reI = np.stack((rR, rG, rB), 2)
    Image.fromarray(reI).save(f"./picture/{percent}svd.png")
    print(percent)
