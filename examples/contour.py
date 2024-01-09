import cv2

# import gambar
img = cv2.imread("examples/images/butterfly.jpg")

# blur
img_blur = cv2.GaussianBlur(img, (5, 5), 100)

# canny edge detection algorithm
canny = cv2.Canny(img_blur, 125, 175)

# contours
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(f"number of contours: {len(contours)}")

# tampilkan gambar
cv2.drawContours(img, contours, -1, (0, 255, 255), 2)
cv2.imshow("Original", img)
cv2.imshow("Result", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()