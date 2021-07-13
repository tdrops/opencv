"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-12] 캐니 엣지 검출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/sudoku.jpg")
edges = cv2.Canny(image=img, threshold1=100, threshold2=200)

cv2.imshow(winname="origin", mat=img)
cv2.imshow(winname="edges", mat=edges)
cv2.waitKey()
cv2.destroyAllWindows()
