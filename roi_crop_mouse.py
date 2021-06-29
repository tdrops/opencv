"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-3] 마우스로 관심영역 지정
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/sunset.jpg")
cv2.imshow(winname="img", mat=img)

x1 = 0
y1 = 0
x2 = 0
y2 = 0

clicked = False

def onMouse(event, x, y, flags, param):
    global x1, y1, x2, y2, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
        clicked = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if clicked:
            draw = img.copy()
            cv2.rectangle(img=draw, pt1=(x1,y1), pt2=(x,y), color=(0,255,0), thickness=1)
            cv2.imshow(winname="img", mat=draw)
    elif event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        clicked = False
        if x1<x2 and y1<y2:
            roi = img[y1:y2+1,x1:x2+1]
            cv2.imshow(winname="roi", mat=roi)



cv2.setMouseCallback(window_name="img", on_mouse=onMouse)


cv2.waitKey()
cv2.destroyAllWindows()
