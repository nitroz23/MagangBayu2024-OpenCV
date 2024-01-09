# import library OpenCV
import cv2

# membaca webcam
cap = cv2.VideoCapture(0)


while True:
    # baca tiap frame dari kamera
    ret, frame = cap.read()

    if not ret: break

    cv2.imshow('WEBCAM', frame) # menampilkan frame

    # menutup window dengan menekan tombol 'esc'
    if cv2.waitKey(1) == 27: break

cap.release() # menutup video
cv2.destroyAllWindows() # menutup semua window