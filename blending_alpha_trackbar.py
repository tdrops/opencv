import cv2
import numpy as np


img1 = cv2.imread(filename="../img/man_face.jpg")
img2 = cv2.imread(filename="../img/lion_face.jpg")

cv2.imshow(winname="man_lion", mat=img1)


def onChange(x):
    alpha = x / 100
    add = cv2.addWeighted(src1=img1, alpha=alpha, src2=img2, beta=(1-alpha), gamma=0)
    cv2.imshow(winname="man_lion", mat=add)


cv2.createTrackbar("T", "man_lion", 100, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()
