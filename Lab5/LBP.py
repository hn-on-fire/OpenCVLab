import cv2
import numpy as np
im = cv2.imread('Resources/lena.jpg')
im=cv2.resize(im, (0, 0), fx=0.4, fy=0.4)
im_g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


def mask(mat):
    mat_cp = np.where(mat > mat[1][1], 1, 0)
    p = [[2**0, 2**1, 2**2], [2**7, 0, 2**3], [2**6, 2**5, 2**4]]
    try:
        return np.sum(np.multiply(mat_cp, p))
    except ValueError:
        print(p, mat)


lbp = np.zeros_like(im_g)
for i in range(1, im_g.shape[0]-1):
    for j in range(1, im_g.shape[1] - 1):
        lbp[i][j] = mask(im_g[i-1:i+2, j-1:j+2])
dis = np.uint8(np.hstack((im_g, lbp)))
cv2.imshow('LBP', dis)
cv2.waitKey(0)
cv2.destroyAllWindows()
