import cv2 as cv

img = cv.imread('Resources/sampleImage.jfif')
`img = cv.resize(img,(0,0), fx=2, fy=2)
img = cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
cv.imshow('display', img)
cv.waitKey(0)
cv.destroyAllWindows()
