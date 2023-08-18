import cv2
import numpy as np

im = cv2.imread('Resources/lena.jpg', 0)
im = cv2.resize(im, (0, 0), fx=0.4, fy=0.4)
blr = cv2.GaussianBlur(src=im, ksize=(0, 0), sigmaX=2)
sX = cv2.Sobel(src=blr, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)
sY = cv2.Sobel(src=blr, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3)
sh = cv2.addWeighted(sX, 0.5, sY, 0.5, 0)
dis = np.hstack([im, sh])
cv2.imshow('lena', np.uint8(dis))
cv2.waitKey(0)
cv2.destroyAllWindows()
