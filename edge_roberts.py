import cv2
import numpy as np


img = cv2.imread(filename="./img/sudoku.jpg")

k1 = np.array([[1,0],
               [0,-1]])
k2 = np.array([[1,0],
               [0,-1]])

img2 = cv2.filter2D(src=img, ddepth=-1, kernel=k1)
img3 = cv2.filter2D(src=img, ddepth=-1, kernel=k2)

cv2.imshow(winname="diff", mat=np.hstack([img, img2, img3]))
cv2.waitKey()
cv2.destroyAllWindows()
