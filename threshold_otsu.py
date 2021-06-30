"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-11] 오츠의 알고리즘을 적용한 스레시홀드
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/scaned_paper.jpg", flags=cv2.IMREAD_GRAYSCALE)

_,th1 = cv2.threshold(src=img, thresh=130, maxval=255, type=cv2.THRESH_BINARY)
_,th2 = cv2.threshold(src=img, thresh=-1, maxval=255, type=cv2.THRESH_BINARY|cv2.THRESH_OTSU)

cv2.imshow(winname="threshold", mat=np.hstack((img,th1,th2)))
cv2.waitKey()
cv2.destroyAllWindows()
