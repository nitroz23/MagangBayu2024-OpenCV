# import library OpenCV
import cv2

# membaca gambar dalam file
img = cv2.imread("examples/images/home.jpg")

# keluarkan output ke dalam window bernama "Gambar"
# dengan gambar yang telah dibaca
cv2.imshow("Gambar", img)

cv2.waitKey(0) #menunggu key-press
cv2.destroyAllWindows() #menutup semua window