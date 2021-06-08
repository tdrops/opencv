"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

sin, cos 함수로 이미지 변형하기 - cv2.remap 함수 사용 
"""

import cv2
import numpy as np
import matplotlib.pylab as plt

l = 20  # 주기
amp = 15  # 변형 크기

img = cv2.imread(filename="./img/taekwonv1.jpg")

h, w = img.shape[:2]  # 높이, 폭 구하기

cv2.imshow(winname="original", mat=img)

mapy, mapx = np.indices(dimensions=(h, w), dtype=np.float32)

sinx = mapx + amp * np.sin(mapy / l)
cosy = mapy + amp * np.cos(mapx / l)

img_sinx = cv2.remap(src=img, map1=sinx, map2=mapy, interpolation=cv2.INTER_LINEAR)  # x 반향으로만 변형
img_cosy = cv2.remap(src=img, map1=mapx, map2=cosy, interpolation=cv2.INTER_LINEAR)  # y 방향으로만 변형

img_both = cv2.remap(src=img, map1=sinx, map2=cosy, interpolation=cv2.INTER_LINEAR)  # x,y 모두 변형

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="sinx", mat=img_sinx)
cv2.imshow(winname="cosy", mat=img_cosy)
cv2.imshow(winname="both", mat=img_both)

cv2.waitKey()
cv2.destroyAllWindows()
