import numpy as np
import cv2

img = cv2.imread('Resources/lena.jpg')
img =cv2.resize(img, (0,0), fx=0.3, fy=0.3)
Z = np.float32(img.reshape((-1,3)))

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4
_, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
labels = labels.reshape((img.shape[:-1]))
reduced = np.uint8(centers)[labels]

result = np.hstack([img, reduced])

cv2.imshow('out', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
