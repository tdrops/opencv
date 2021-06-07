"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

2개의 기준점으로 이미지에 원근감 부여
"""

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(filename="./img/fish.jpg")

h, w = img.shape[:2]  # 높이, 폭 구하기

pts1 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])  # 기준점1
pts2 = np.float32([[100, 50], [w - 100, 50], [10, h - 50], [w - 10, h - 50]])  # 기준점2

matrix = cv2.getPerspectiveTransform(src=pts1, dst=pts2)  # 행렬 구하기
result = cv2.warpPerspective(src=img, M=matrix, dsize=(w, h))  # 행렬 반영

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)

cv2.waitKey()
cv2.destroyAllWindows()
