"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-11] 라플라시안 마스크를 적용한 경계 검출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/sudoku.jpg")

edge = cv2.Laplacian(src=img, ddepth=-1)

cv2.imshow(winname="ori/edge", mat=np.hstack((img,edge)))
cv2.waitKey()
cv2.destroyAllWindows()
