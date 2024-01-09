import cv2
import os

output_folder = "examples/video/asJPG"
vidObj = cv2.VideoCapture("examples/video/record.mp4")

# buat folder jika tidak ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

count = 0
success = 1

while success:
    success, image = vidObj.read()

    # cek gambar tidak kosong
    if success:
        image_path = os.path.join(output_folder, "frame%d.jpg" % count)
        cv2.imwrite(image_path, image)
        count += 1
