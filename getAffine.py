"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

2개의 기준점으로 이미지 뒤틀기
"""

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(filename="./img/fish.jpg")

h, w = img.shape[:2]  # 높이, 폭 구하기

pts1 = np.float32([[100, 50], [200, 50], [100, 200]])
pts2 = np.float32([[80, 70], [210, 60], [250, 120]])

matrix = cv2.getAffineTransform(src=pts1, dst=pts2)  # 2점간 대응 행렬 구하기
result = cv2.warpAffine(src=img, M=matrix, dsize=(w*2, h))  # 행렬 적용

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)

cv2.waitKey()
cv2.destroyAllWindows()
