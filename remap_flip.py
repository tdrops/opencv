"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

cv2.warpAffine 또는 cv2.remap 로 사진 좌우 상하 뒤집기
"""

import cv2
import numpy as np
import matplotlib.pylab as plt
from time import time

img = cv2.imread("./img/girl.jpg")
h, w = img.shape[:2]  # 높이, 폭 구하기

start_time = time()
matrix = np.float32([[-1, 0, w - 1], [0, -1, h - 1]])
result1 = cv2.warpAffine(src=img, M=matrix, dsize=(w, h))  # 행렬 반영
print(f"cv2.warpAffine로 뒤집기 :{time() - start_time}초")  # 소요 시간 표시

start_time = time()
mapy, mapx = np.indices(dimensions=(h, w), dtype=np.float32)
mapx = -mapx + w - 1
mapy = -mapy + h - 1
result2 = cv2.remap(src=img, map1=mapx, map2=mapy, interpolation=cv2.INTER_LINEAR)  # cv2.remap 을 사용하여 뒤집기 
print(f"cv2.remap로 뒤집기 :{time() - start_time}초")  # 소요 시간 표시

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result1", mat=result1)
cv2.imshow(winname="result2", mat=result2)

cv2.waitKey()
cv2.destroyAllWindows()
