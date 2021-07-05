"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-24] SeamlessClone 으로 합성
"""
import cv2
import numpy as np


img1 = cv2.imread(filename="../img/drawing.jpg")
img2 = cv2.imread(filename="../img/my_hand.jpg")

mask = np.full_like(a=img1, fill_value=255)

h1,w1 = img1.shape[:2]
h2,w2 = img2.shape[:2]
center = (w2//2, h2//2)

normal = cv2.seamlessClone(src=img1, dst=img2, mask=mask, p=center, flags=cv2.NORMAL_CLONE)
mixed = cv2.seamlessClone(src=img1, dst=img2, mask=mask, p=center, flags=cv2.MIXED_CLONE)

cv2.imshow(winname="normal", mat=normal)
cv2.imshow(winname="mixed", mat=mixed)

cv2.waitKey()
cv2.destroyAllWindows()
