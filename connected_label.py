"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

connectedComponents - 연결 요소 레이블링
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/shapes_donut.png")
img2 = np.zeros_like(a=img)
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(src=gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
cnt, labels = cv2.connectedComponents(image=th)

for i in range(cnt):
    img2[labels == i] = [int(j) for j in np.random.randint(low=0, high=255, size=3)]

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="img2", mat=img2)
cv2.waitKey()
cv2.destroyAllWindows()
