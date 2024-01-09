import cv2
import numpy as np

#import gambar
img = cv2.imread("examples/images/blueRed.png")

# convert to HSV
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# masking warna merah
lower_bound = np.array([0, 0, 0]) #lower bound merah
upper_bound = np.array([10, 255, 255]) #upper bound merah
mask = cv2.inRange(img_HSV, lower_bound, upper_bound)
img_masked = cv2.bitwise_and(img, img, mask=mask)

# tampilkan gambar
cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Result", img_masked)

cv2.waitKey(0)
cv2.destroyAllWindows()