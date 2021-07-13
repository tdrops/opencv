"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-16] 모폴로지 그레이디언트
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/morphological.png")

k = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))

gradient = cv2.morphologyEx(src=img, op=cv2.MORPH_GRADIENT, kernel=k)

cv2.imshow(winname="ori/gradient", mat=np.hstack((img,gradient)))
cv2.waitKey()
cv2.destroyAllWindows()
