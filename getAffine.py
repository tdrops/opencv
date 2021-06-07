import cv2
import numpy as np
import matplotlib.pylab as plt


img = cv2.imread(filename="./img/fish.jpg")
cv2.imshow(winname="original", mat=img)

cv2.waitKey()
cv2.destroyAllWindows()
