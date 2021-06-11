"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

Canny를 사용한 경계 검출
"""


import cv2
import numpy as np

img = cv2.imread(filename="./img/sudoku.jpg")

img2 = cv2.Canny(image=img, threshold1=100, threshold2=200)

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="canny", mat=img2)
cv2.waitKey()
cv2.destroyAllWindows()
