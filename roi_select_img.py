"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-4] selectROI 로 관심영역 지정 
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/sunset.jpg")
x,y,w,h = cv2.selectROI(windowName="img", img=img, showCrosshair=False)

if w>0 and h>0:
    roi = img[y:y+h,x:x+w]
    cv2.imshow(winname="roi", mat=roi)
    cv2.imwrite(filename="../img/cropped.jpg", img=roi)

cv2.imshow(winname="img", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
