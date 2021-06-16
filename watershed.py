"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

watershed - 색 채워 넣기
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/taekwonv1.jpg")
draw = img.copy()
h,w = img.shape[:2]
marker = np.zeros(shape=(h,w), dtype=np.int32)
cv2.imshow(winname="original", mat=img)

isDragging = False

makerId = 1

colors = []

def onMouse(event, x, y, flags, param):
    global isDragging, makerId, colors

    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        colors.append((makerId,img[y,x]))
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            marker[y,x] = makerId
            cv2.circle(img=draw, center=(x,y), radius=1, color=(0,0,255), thickness=-1)
            cv2.imshow(winname="original", mat=draw)
    elif event == cv2.EVENT_LBUTTONUP:
        isDragging = False
        makerId += 1
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.watershed(image=img, markers=marker)

        draw[marker==-1] = (0,255,0)
        for mid, color in colors:
            draw[marker == mid] = color
        cv2.imshow(winname="original", mat=draw)


cv2.setMouseCallback(window_name="original", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
