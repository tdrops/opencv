"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

Laplacian 을 사용한 경계 검출
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/sudoku.jpg")
img2 = cv2.Laplacian(src=img, ddepth=-1)

cv2.imshow(winname="laplacian", mat=np.hstack([img,img2]))
cv2.waitKey()
cv2.destroyAllWindows()
