"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

소벨 필터
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/sudoku.jpg")

k1 = np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])
k2 = np.array([[-1,-2,-1],
               [0,0,0],
               [1,2,1]])

img2 = cv2.filter2D(src=img, ddepth=-1, kernel=k1)
img3 = cv2.filter2D(src=img, ddepth=-1, kernel=k2)

img4 = cv2.Sobel(src=img, ddepth=-1, dx=1, dy=0, ksize=3)
img5 = cv2.Sobel(src=img, ddepth=-1, dx=0, dy=1, ksize=3)

hstack1 = np.hstack([img,img2,img3,img2+img3])
hstack2 = np.hstack([img,img4,img5,img4+img5])

cv2.imshow(winname="sobel", mat=np.vstack([hstack1,hstack2]))
cv2.waitKey()
cv2.destroyAllWindows()
