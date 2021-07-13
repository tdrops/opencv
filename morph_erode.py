"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-13] 침식 연산
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/morph_dot.png")

k = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))
erosion = cv2.erode(src=img, kernel=k)

cv2.imshow(winname="ori/erode", mat=np.hstack((img,erosion)))
cv2.waitKey()
cv2.destroyAllWindows()
