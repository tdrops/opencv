"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-5] BGR, BGRA, Alpha 채널 
"""
import cv2
import numpy as np


filename = "../img/opencv_logo.png"
img = cv2.imread(filename=filename)

bgr = cv2.imread(filename=filename, flags=cv2.IMREAD_COLOR)

bgra = cv2.imread(filename=filename, flags=cv2.IMREAD_UNCHANGED)

cv2.imshow(winname="img", mat=img)
cv2.imshow(winname="bgr", mat=bgr)
cv2.imshow(winname="bgra", mat=bgra)
cv2.imshow(winname="a", mat=bgra[:,:,3])

cv2.waitKey()
cv2.destroyAllWindows()
