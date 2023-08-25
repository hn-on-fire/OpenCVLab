import cv2
import numpy as np


def colorDist(color):
    colors = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (255, 125, 0), (255, 255, 0), (125, 255, 0), (0, 255, 0),
              (0, 255, 255), (0, 0, 255), (255, 0, 255)]
    mini, idx = None, 0
    for c in range(len(colors)):
        col = np.array(colors[c])
        if mini is None or mini > np.linalg.norm(color - col):
            mini, idx = np.linalg.norm(color - col), c
    return colors[idx]


im = cv2.imread('Resources/lena.jpg')
im = cv2.resize(im, (0, 0), fx=.3, fy=0.3)
a = [[(12,0,0)], [(255, 230, 255)]]
x, y, z = im.shape
dis = np.zeros_like(im)
for i in range(x):
    for j in range(y):
        dis[i, j, :] = colorDist(im[i][j])
dis = np.hstack((im, dis))
cv2.imshow('lena', np.uint8(dis))
cv2.waitKey(0)
cv2.destroyAllWindows()
