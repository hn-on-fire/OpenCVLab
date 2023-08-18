import cv2
import numpy as np

im = cv2.imread('Resources/lena.jpg')
im = cv2.resize(im, (0, 0), fx=0.4, fy=0.4)
blr = cv2.GaussianBlur(src=im, ksize=(0, 0), sigmaX=2)
sh = cv2.addWeighted(im, 2.5, blr, -1.5, 0)
dis = np.hstack([im, sh])
cv2.imshow('lena', np.uint8(dis))
cv2.waitKey(0)
cv2.destroyAllWindows()
