"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-15] 모자이크 처리 풀이 결과
"""
import cv2
import numpy as np

img = cv2.imread("../img/taekwonv1.jpg")
draw = img.copy()

cv2.imshow(winname="draw", mat=draw)

x,y,w,h = cv2.selectROI(windowName="draw", img=draw, showCrosshair=False)

if w and h:
    roi = img[y:y+h,x:x+w]
    roi = cv2.resize(src=roi, dsize=(w//15,h//15))
    roi = cv2.resize(src=roi, dsize=(w,h), interpolation=cv2.INTER_AREA)
    img[y:y + h, x:x + w] = roi
    cv2.imshow(winname="draw", mat=img)

cv2.waitKey()
cv2.destroyAllWindows()
