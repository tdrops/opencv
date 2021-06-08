"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

마우스로 선택한 영역을 축소와 확대를 하는 방식으로 모자이크 처리한 효과로 변형
"""


import cv2
import numpy as np
import matplotlib.pylab as plt


rate = 15

img = cv2.imread(filename="./img/taekwonv1.jpg")
draw = img.copy()
cv2.imshow(winname="original", mat=draw)

while True:
    x,y,w,h = cv2.selectROI(windowName="original", img=img)
    if x > 0 and y > 0:
        roi = img[y:y+h,x:x+w]
        roi = cv2.resize(src=roi, dsize=(w//rate, h//rate))
        roi = cv2.resize(src=roi, dsize=(w, h), interpolation=cv2.INTER_AREA)
        img[y:y+h,x:x+w] = roi
        cv2.imshow(winname="original", mat=img)
    else:
        break

# cv2.waitKey()
cv2.destroyAllWindows()
