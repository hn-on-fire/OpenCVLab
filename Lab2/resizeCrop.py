import cv2
im = cv2.imread('Resources/sample.jfif')
cv2.imshow('Cropped', im[0:1000, 0:300])
cv2.imshow("Resized", cv2.resize(im, (300, 1000)))
cv2.waitKey(0)
cv2.destroyAllWindows()