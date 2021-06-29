"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-1] 관심 영역 지정
"""
import cv2
import numpy as np


x = 320
y = 150
w = 50
h = 50

img = cv2.imread(filename="../img/sunset.jpg")

roi = img[y:y+h,x:x+w]
cv2.rectangle(img=roi, pt1=(0,0), pt2=(w-1, h-1), color=(0,255,0))
cv2.imshow(winname="img", mat=img)

cv2.waitKey()
cv2.destroyAllWindows()
