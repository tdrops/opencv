"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

방사 왜곡 효과 주기
"""


import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread(filename="./img/girl.jpg")
h, w = img.shape[:2]  # 높이, 폭 구하기

mapy, mapx = np.indices(dimensions=(h, w), dtype=np.float32)  # 인덱스 배열 구하기

mapx = 2 * mapx / (w - 1) - 1  # 폭, 높이 2 중심 0,0 의 값으로 변경
mapy = 2 * mapy / (h - 1) - 1

r, theta = cv2.cartToPolar(x=mapx, y=mapy)  # 극좌표로 변경

k1, k2, k3 = 0.5, 0.2, 0.0  # 배럴 왜곡
# k1, k2, k3 = -0.3, 0, 0  # 핀큐션 왜곡
r = r * (1 + k1 * r ** 2 + k2 * r ** 4 + k3 * r ** 6)

mapx, mapy = cv2.polarToCart(magnitude=r, angle=theta)  # 직교 좌표로 원위치 

mapx = (mapx + 1) * (w - 1) / 2  # 좌상단이 0,0 크기 w X h 인 좌표로 원위치
mapy = (mapy + 1) * (h - 1) / 2

result = cv2.remap(src=img, map1=mapx, map2=mapy, interpolation=cv2.INTER_LINEAR)  # 공식을 적용해서 그림

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)
cv2.waitKey()
cv2.destroyAllWindows()
