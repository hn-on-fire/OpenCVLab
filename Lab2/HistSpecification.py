import numpy as np
from skimage import exposure
import cv2
im = cv2.imread('Resources/sample.jfif')
print(im.shape)
ref = cv2.imread('Resources/ref.jfif')
ref = cv2.resize(ref, dsize=(1328, 747), interpolation=cv2.INTER_CUBIC)
print(ref.shape)
matched = exposure.match_histograms(im, ref, channel_axis=True)

ou = np.vstack((im, ref, matched))
ou = cv2.resize(ou, (0,0), fx=1, fy=0.4)
cv2.imshow('Histogram Equalization', ou)
cv2.waitKey(0)
cv2.destroyAllWindows()
