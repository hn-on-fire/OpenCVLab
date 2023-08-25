import cv2
import numpy as np

im = cv2.imread('Resources/box.jpg', 0)
im = cv2.resize(im, (0, 0), fx=.3, fy=0.3)
ret, tr = cv2.threshold(im, 144, 255, cv2.THRESH_BINARY)
ret2, tr2 = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
dis = np.hstack((im, tr, tr2))
cv2.imshow('lena', np.uint8(dis))
cv2.waitKey(0)
cv2.destroyAllWindows()
