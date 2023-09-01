import cv2
import numpy as np


def harris(img, threshold=0.6):

    img_cpy = img.copy() # copying image

    img1_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    dx = cv2.Sobel(src=img1_gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)
    dy = cv2.Sobel(src=img1_gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3)
    dx2 = np.square(dx)
    dy2 = np.square(dy)
    dxdy = dx*dy
    g_dx2 = cv2.GaussianBlur(dx2, (3, 3), 2)
    g_dy2 = cv2.GaussianBlur(dy2, (3, 3), 2)
    g_dxdy =  cv2.GaussianBlur(dxdy, (3, 3), 2)
    c = g_dx2*g_dy2 - np.square(g_dxdy) - 0.12*np.square(g_dx2 + g_dy2)
    cv2.normalize(c, c, 0, 1, cv2.NORM_MINMAX)

    loc = np.where(c >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.circle(img_cpy, pt, 3, (0, 0, 255), -1)

    return img_cpy


im = cv2.imread('Resources/chess.jpg')
dis = np.uint8(np.hstack((im, harris(im))))
cv2.imshow("Harris", dis)
cv2.waitKey(0)
cv2.destroyAllWindows()
