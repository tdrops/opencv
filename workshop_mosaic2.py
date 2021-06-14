"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

마우스로 선택한 영영 모자익 처리하기
"""



import cv2
import numpy as np


img = cv2.imread("./img/taekwonv1.jpg")
cv2.imshow(winname="original", mat=img)

is_drag = False
x1 = 0
y1 = 0
x2 = 0
y2 = 0


def onMouse(event, x, y, flags, param):
    draw = img.copy()
    global is_drag, x1, y1, x2, y2
    if event == cv2.EVENT_MOUSEMOVE:
        if is_drag:
            x2 = x
            y2 = y
            cv2.rectangle(img=draw, pt1=(x1,y1), pt2=(x2,y2), color=(0,255,0), thickness=1)
            cv2.imshow(winname="original", mat=draw)
    elif event == cv2.EVENT_LBUTTONDOWN:
        is_drag = True
        x1 = x
        y1 = y
        x2 = x
        y2 = y
    elif event == cv2.EVENT_LBUTTONUP:
        is_drag = False
        x2 = x
        y2 = y

        img[y1:y2 + 1, x1:x2 + 1] = cv2.blur(src=img[y1:y2+1,x1:x2+1], ksize=(30,30))
        cv2.imshow(winname="original", mat=img)


cv2.setMouseCallback(window_name="original", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
