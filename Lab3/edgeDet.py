import cv2
import numpy as np

im = cv2.imread('Resources/lena.jpg')
im = cv2.resize(im, (0, 0), fx=0.4, fy=0.4)
lap = cv2.Laplacian(im, cv2.CV_64F, (15, 15))
dis = np.hstack([im, lap])
cv2.imshow('lena', np.uint8(dis))
cv2.waitKey(0)
cv2.destroyAllWindows()