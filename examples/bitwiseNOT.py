import cv2
import numpy as np

# kotak
kotak = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(kotak, (25, 25), (275, 275), 255, -1)
cv2.imshow("Kotak", kotak)


# NOT operation
bitwise_NOT = cv2.bitwise_not(kotak)
cv2.imshow("Bitwise NOT", bitwise_NOT)

cv2.waitKey(0)
cv2.destroyAllWindows()