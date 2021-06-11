"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

가우시안 필터로 촛점 흐리기
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/gaussian_noise.jpg")

k1 = np.array([[1,2,1],
               [2,4,2],
               [1,2,1]])/16

img2 = cv2.filter2D(src=img, ddepth=-1, kernel=k1)

k2 = cv2.getGaussianKernel(ksize=3, sigma=0)
img3 = cv2.filter2D(src=img, ddepth=-1, kernel=k2*k2.T)

img4 = cv2.GaussianBlur(src=img, ksize=(3,3), sigmaX=0)

cv2.imshow(winname="gaussian blur", mat=np.hstack([img,img2,img3,img4]))
cv2.waitKey()
cv2.destroyAllWindows()
