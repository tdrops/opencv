"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

tophat, blackhat
"""



import cv2
import numpy as np


img = cv2.imread(filename="./img/moon_gray.jpg")

k = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(9,9))
tophat = cv2.morphologyEx(src=img, op=cv2.MORPH_TOPHAT, kernel=k)
blackhat = cv2.morphologyEx(src=img, op=cv2.MORPH_BLACKHAT, kernel=k)

cv2.imshow(winname="tophat / blackhat", mat=np.hstack([img, tophat, blackhat]))

cv2.waitKey()
cv2.destroyAllWindows()
