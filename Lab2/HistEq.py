import numpy as np
import cv2
im = cv2.imread('Resources/sample.jpg', 0)
equ = cv2.equalizeHist(im)
ou = np.hstack((im, equ))
cv2.imshow('Histogram Equalization', ou)
cv2.waitKey(0)
cv2.destroyAllWindows()
