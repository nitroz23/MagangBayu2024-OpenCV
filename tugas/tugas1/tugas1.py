import cv2
import numpy as np

img = cv2.imread("tugas/tugas1/tugas1.png")

lowerBound = np.array([60, 90, 60], dtype=np.uint8)
upperBound = np.array([173, 255, 109], dtype=np.uint8)

mask = cv2.inRange(img, lowerBound, upperBound)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)

    if area > 1500:
        color = (0, 0, 255)  
        thickness = 2
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)

cv2.imshow("Bounding Box", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
