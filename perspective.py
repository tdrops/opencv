import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(filename="./img/fish.jpg")

h, w = img.shape[:2]

pts1 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
pts2 = np.float32([[100, 50], [w - 100, 50], [10, h - 50], [w - 10, h - 50]])

matrix = cv2.getPerspectiveTransform(src=pts1, dst=pts2)
result = cv2.warpPerspective(src=img, M=matrix, dsize=(w, h))

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)

cv2.waitKey()
cv2.destroyAllWindows()
