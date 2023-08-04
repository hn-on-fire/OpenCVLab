import cv2 as cv
img = cv.imread('Resources/img.jpg')
img = cv.rectangle(img,(5,10),(150,180),(255,0,0),1)
cv.imshow('display', img)
cv.waitKey(0)
cv.destroyAllWindows()