"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

contour hierarchy
"""



import cv2
import numpy as np


img = cv2.imread(filename="./img/shapes_donut.png")
img2 = img.copy()

img_gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

ret, img_gray = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

im2,contour1,hierarchy = cv2.findContours(image=img_gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
print(f"len(contour1):{len(contour1)} hierarchy:{hierarchy}")

im2,contour2,hierarchy = cv2.findContours(image=img_gray, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
print(f"len(contour2):{len(contour2)} hierarchy:{hierarchy}")

cv2.drawContours(image=img, contours=contour1, contourIdx=-1, color=(0,255,0), thickness=3)

for idx, cont in enumerate(contour2):
    color = [int(i) for i in np.random.randint(low=0,high=255,size=3)]
    cv2.drawContours(image=img2, contours=contour2, contourIdx=idx, color=color, thickness=3)
    cv2.putText(img=img2, text=str(idx), org=tuple(cont[0][0]), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0,0,255))

cv2.imshow(winname="img", mat=img)
cv2.imshow(winname="img2", mat=img2)
cv2.waitKey()
cv2.destroyAllWindows()
