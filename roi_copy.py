"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-2] 관심영역 복제 및 새창 띄우기
"""
import cv2
import numpy as np


x = 320
y = 150
w = 50
h = 50

img = cv2.imread(filename="../img/sunset.jpg")

roi = img[y:y+h,x:x+w]
img2 = roi.copy()

img[y:y+h,x+w:x+w+w] = roi

cv2.rectangle(img=img, pt1=(x,y), pt2=(x+w+w,y+h), color=(0,255,0), thickness=1)

cv2.imshow(winname="img", mat=img)
cv2.imshow(winname="img2", mat=img2)
cv2.waitKey()
cv2.destroyAllWindows()
