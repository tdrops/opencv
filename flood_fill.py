"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

floodFill -  마우스로 색 채우기
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/taekwonv1.jpg")
h,w = img.shape[:2]

mask = np.zeros(shape=(h+2,w+2), dtype=np.uint8)

cv2.imshow(winname="original", mat=img)

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.floodFill(image=img, mask=mask, seedPoint=(x,y), newVal=(255,255,255), loDiff=(10,10,10), upDiff=(10,10,10))
        cv2.imshow(winname="original", mat=img)

cv2.setMouseCallback(window_name="original", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
