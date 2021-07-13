"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-6] 미분 커널로 경계 검출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/sudoku.jpg")

gx_kernel = np.array([[-1,1]])
gy_kernel = np.array([[-1],[1]])

edge_gx = cv2.filter2D(src=img, ddepth=-1, kernel=gx_kernel)
edge_gy = cv2.filter2D(src=img, ddepth=-1, kernel=gy_kernel)

cv2.imshow(winname="ori/edge_gx/edge_gy", mat=np.hstack((img,edge_gx,edge_gy)))
cv2.waitKey()
cv2.destroyAllWindows()
