import cv2
import numpy as np

im = cv2.imread('Resources/lena.jpg')
im = cv2.resize(im, (0, 0), fx=0.4, fy=0.4)
blr = cv2.GaussianBlur(src=im, ksize=(15, 15), sigmaX=2)
ker = (1/(15*15))*np.uint8(np.ones(shape=(15,15)))
box = cv2.filter2D(im, cv2.CV_8U, ker)
dis = np.hstack([blr, box])
cv2.imshow('lena', np.uint8(dis))
cv2.waitKey(0)
cv2.destroyAllWindows()