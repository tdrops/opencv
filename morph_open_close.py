import cv2
"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

open close 연산
"""



import numpy as np


img1 = cv2.imread(filename="./img/morph_dot.png")
img2 = cv2.imread(filename="./img/morph_hole.png")

k = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(5,5))
result1 = cv2.morphologyEx(src=img1, op=cv2.MORPH_OPEN, kernel=k)
result2 = cv2.morphologyEx(src=img2, op=cv2.MORPH_CLOSE, kernel=k)

hstack1 = np.hstack([img1, result1])
hstack2 = np.hstack([img2, result2])

cv2.imshow(winname="open close", mat=np.vstack([hstack1, hstack2]))
cv2.waitKey()
cv2.destroyAllWindows()
