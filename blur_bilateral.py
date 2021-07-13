"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-5] 바이레터럴 필터와 가우시안 필터 비교
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/gaussian_noise.jpg")

blur1 = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0)
blur2 = cv2.bilateralFilter(src=img, d=5, sigmaColor=75, sigmaSpace=75)

cv2.imshow(winname="ori/blur1/blur2", mat=np.hstack((img,blur1,blur2)))
cv2.waitKey()
cv2.destroyAllWindows()
