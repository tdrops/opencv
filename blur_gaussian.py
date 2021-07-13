"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-3] 가우시안 블러
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/gaussian_noise.jpg")

k1 = np.array([[1,2,1],
               [2,4,2],
               [1,2,1]])/16
blur1 = cv2.filter2D(src=img, ddepth=-1, kernel=k1)

k2 = cv2.getGaussianKernel(ksize=3, sigma=0)
blur2 = cv2.filter2D(src=img, ddepth=-1, kernel=k2*k2.T)

blur3 = cv2.GaussianBlur(src=img, ksize=(3,3), sigmaX=0)

print(f"k1:\n{k1}")
print(f"k2:\n{k2}")
print(f"k2.T:\n{k2.T}")
print(f"k2*k2.T:\n{k2*k2.T}")

cv2.imshow(winname="blur1/2/3", mat=np.hstack((blur1,blur2,blur3)))
cv2.waitKey()
cv2.destroyAllWindows()
