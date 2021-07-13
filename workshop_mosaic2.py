"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-20] 블러링으로 모자이크 처리 풀이 결과
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/taekwonv1.jpg")

x,y,w,h = cv2.selectROI(windowName="mosaic", img=img, showCrosshair=False)

if w>0 and h>0:
    roi = img[y:y+h,x:x+w]
    blur = cv2.blur(src=roi, ksize=(30,30))
    img[y:y + h, x:x + w] = blur
    cv2.imshow(winname="mosaic", mat=img)
    cv2.waitKey()
    cv2.destroyAllWindows()
