# import library OpenCV
import cv2

# membaca gambar dalam file
img = cv2.imread("examples/images/home.jpg")

# print(img.shape)
h, w, c = img.shape


# image[top:bottom, left:right]
cropped_img = img[250:384, 300:512]

resized_img = cv2.resize(img, (int(w/2), int(h/2)))

cv2.imshow("Gambar", img)
cv2.imshow("Cropped", cropped_img)
cv2.imshow("Resized", resized_img)

cv2.waitKey(0) #menunggu key-press
cv2.destroyAllWindows() #menutup semua window

