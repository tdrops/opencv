"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

bilateralFilter 사용 - 노이즈는 줄이고 경계는 유지
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/girl.jpg")

img2 = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0)
img3 = cv2.bilateralFilter(src=img, d=5, sigmaColor=75, sigmaSpace=75)

cv2.imshow(winname="blur", mat=np.hstack([img, img2, img3]))
cv2.waitKey()
cv2.destroyAllWindows()
