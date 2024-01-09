import cv2
import numpy as np

# import gambar
img = cv2.imread("examples/images/butterfly.jpg")

# blur
img_blur = cv2.GaussianBlur(img, (5, 5), 100)

# tampilkan gambar
cv2.imshow("Original", img)
cv2.imshow("Result", img_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()