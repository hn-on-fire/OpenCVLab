import cv2
import numpy as np

im = cv2.imread('Resources/lena.jpg', 0)
im = cv2.resize(im, (0, 0), fx=0.4, fy=0.4)
can = cv2.Canny(im, 90, 100, L2gradient=True)
dis = np.hstack([im, can])
cv2.imshow('lena', np.uint8(dis))
cv2.waitKey(0)
cv2.destroyAllWindows()
