"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

중앙의 동그란 영역의 이미지를 확대/축소
"""

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(filename="./img/taekwonv1.jpg")
h, w = img.shape[:2]  # 높이, 폭 구하기

exp = 0.5  # 배율
scale = 1  # 변형을 적용할 범위

mapy, mapx = np.indices(dimensions=(h, w), dtype=np.float32)  # 인덱스 배열 구하기

mapx = 2 * mapx / (w - 1) - 1  # 중심을 원점으로 변경
mapy = 2 * mapy / (h - 1) - 1

r, theta = cv2.cartToPolar(x=mapx, y=mapy)  # 극좌표로 변경

r[r < scale] = r[r < scale] ** 0.6  # 중심으로 부터의 거리 조정(확대 / 축소)

mapx, mapy = cv2.polarToCart(magnitude=r, angle=theta)  # 직교좌표로 원위치

# mapx = (mapx / (w-1) + 1) / 2
# mapy = (mapy / (w-1) + 1) / 2

mapx = (mapx + 1) * (w - 1) / 2  # 중심 원위치
mapy = (mapy + 1) * (h - 1) / 2

result = cv2.remap(src=img, map1=mapx, map2=mapy, interpolation=cv2.INTER_LINEAR)  # 공식이 반영된 상태로 그림

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)

cv2.waitKey()
cv2.destroyAllWindows()
