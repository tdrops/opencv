"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-13] 마우스로 색 채우기
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/taekwonv1.jpg")
rows, cols = img.shape[:2]

mask = np.zeros(shape=(rows + 2, cols + 2), dtype=np.uint8)

newVal = (255, 255, 255)

loDiff, upDiff = (10, 10, 10), (10, 10, 10)
# loDiff, upDiff = (3,3,3), (3,3,3)

cv2.imshow(winname="fill", mat=img)


def onMouse(event, x, y, flags, param):
    global mask, img
    if event == cv2.EVENT_LBUTTONDOWN:
        seed = (x, y)
        cv2.floodFill(image=img, mask=mask, seedPoint=seed, newVal=newVal, loDiff=loDiff, upDiff=upDiff)
        # cv2.floodFill(image=img, mask=mask, seedPoint=seed, newVal=newVal)
        cv2.imshow(winname="fill", mat=img)


cv2.setMouseCallback(window_name="fill", on_mouse=onMouse)

cv2.waitKey()
cv2.destroyAllWindows()
