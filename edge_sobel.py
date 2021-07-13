"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-9] 소벨 마스크를 적용한 경계 검출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/sudoku.jpg")

gx_k = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
gy_k = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

edge_gx = cv2.filter2D(src=img, ddepth=-1, kernel=gx_k)
edge_gy = cv2.filter2D(src=img, ddepth=-1, kernel=gy_k)

sobelx = cv2.Sobel(src=img, ddepth=-1, dx=1, dy=0, ksize=3)
sobely = cv2.Sobel(src=img, ddepth=-1, dx=0, dy=1, ksize=3)

cv2.imshow(winname="ori/gx/gy/ori/sobelx/sobley", mat=np.vstack((np.hstack((img,edge_gx,edge_gy,edge_gx+edge_gy)),
                                                                 np.hstack((img,sobelx,sobely,sobelx+sobely)))))
cv2.waitKey()
cv2.destroyAllWindows()
