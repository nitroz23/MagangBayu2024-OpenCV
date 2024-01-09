import cv2
import numpy as np

# kotak
kotak = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(kotak, (25, 25), (275, 275), 255, -1)
cv2.imshow("Kotak", kotak)

# lingkaran
lingkaran = np.zeros((300, 300), dtype="uint8")
cv2.circle(lingkaran, (150, 150), 150, 255, -1)
cv2.imshow("Lingkaran", lingkaran)

# OR operation
bitwise_OR = cv2.bitwise_or(kotak, lingkaran)
cv2.imshow("Bitwise OR", bitwise_OR)

cv2.waitKey(0)
cv2.destroyAllWindows()