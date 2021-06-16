"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

matchShapes
"""



import cv2
import numpy as np


target = cv2.imread(filename="./img/4star.jpg")
shapes = cv2.imread(filename="./img/shapestomatch.jpg")

target_gray = cv2.cvtColor(src=target, code=cv2.COLOR_BGR2GRAY)
shapes_gray = cv2.cvtColor(src=shapes, code=cv2.COLOR_BGR2GRAY)

ret, target_gray = cv2.threshold(src=target_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
ret, shapes_gray = cv2.threshold(src=shapes_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

_,ctr_target,_ = cv2.findContours(image=target_gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
_,ctr_shapes,_ = cv2.findContours(image=shapes_gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

matches = []
for ctr in ctr_shapes:
    match = cv2.matchShapes(contour1=ctr_target[0], contour2=ctr, method=cv2.CONTOURS_MATCH_I2, parameter=0.0)
    matches.append((match, ctr))
    cv2.putText(img=shapes, text=f"{match}", org=tuple(ctr[0][0]), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0,0,255), thickness=1)

matches.sort(key=lambda x: x[0])
cv2.drawContours(image=shapes, contours=[matches[0][1]], contourIdx=-1, color=(0,255,0), thickness=1)
cv2.imshow(winname="target", mat=target)
cv2.imshow(winname="shapes", mat=shapes)
cv2.waitKey()
cv2.destroyAllWindows()


