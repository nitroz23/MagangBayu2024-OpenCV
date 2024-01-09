# import library OpenCV
import cv2

# membaca gambar dalam file
img = cv2.imread("examples/images/home.jpg")

# BGR to RGB
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR to HSV
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original", img)
cv2.imshow("RGB", img_RGB)
cv2.imshow("HSV", img_HSV)

cv2.waitKey(0)
cv2.destroyAllWindows()