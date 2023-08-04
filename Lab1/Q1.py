import cv2 as cv
img = cv.imread('Resources/img.jpg')
cv.imshow('display', img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('Lab1/imageCopy.jpg', img)
