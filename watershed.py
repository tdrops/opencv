"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-14] 마우스와 워터세드로 배경 분리
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/taekwonv1.jpg")
rows, cols = img.shape[:2]
img_draw = img.copy()

marker = np.zeros(shape=(rows, cols), dtype=np.int32)
markerId = 1
colors = []
isDragging = False


def onMouse(event, x, y, flags, param):
    global img_draw, isDragging, marker, markerId
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        colors.append((markerId, img[y, x]))
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            marker[y, x] = markerId
            cv2.circle(img=img_draw, center=(x, y), radius=3, color=(0, 0, 255), thickness=-1)
            cv2.imshow(winname="watershed", mat=img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            markerId += 1
    elif event == cv2.EVENT_RBUTTONDOWN:
        # cv2.watershed(image=img, markers=marker)
        img_draw[marker == -1] = (0, 255, 0)
        for mid, color in colors:
            img_draw[marker == mid] = color
            cv2.imshow(winname="watershed", mat=img_draw)


cv2.imshow(winname="watershed", mat=img)
cv2.setMouseCallback(window_name="watershed", on_mouse=onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
