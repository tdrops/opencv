"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

erode - 침식
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/morph_dot.png")
cv2.imshow(winname="original", mat=img)

k = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))
img2 = cv2.erode(src=img, kernel=k)

cv2.imshow(winname="erode", mat=np.hstack([img,img2]))

cv2.waitKey()
cv2.destroyAllWindows()
