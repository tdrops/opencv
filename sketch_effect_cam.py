import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    if ret:
        pass
    else:
        break

cap.release()
cv2.destroyAllWindows()
