"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-9] 바이너리 이미지 만들기
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/gray_gradient.jpg")

th1 = np.zeros_like(img)

th1[img > 127] = 255

ret, th2 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

cv2.imshow(winname="threshold", mat=np.vstack((img,th1,th2)))

cv2.waitKey()
cv2.destroyAllWindows()
