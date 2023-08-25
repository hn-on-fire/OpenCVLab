import numpy as np
import cv2

img = cv2.imread('Resources/lena.jpg')
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
print(lines)
for r_theta in lines:
    arr = np.array(r_theta[0], dtype=np.float64)
    r, theta = arr
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * r
    y0 = b * r
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv2.imshow('lena', np.uint8(img))
cv2.waitKey(0)
cv2.destroyAllWindows()

