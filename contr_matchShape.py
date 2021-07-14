"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-7] 도형 매칭으로 비슷한 도형 찾기
"""
import cv2
import numpy as np

target = cv2.imread(filename="../img/4star.jpg")
shapes = cv2.imread(filename="../img/shapestomatch.jpg")

target_gray = cv2.cvtColor(src=target, code=cv2.COLOR_BGR2GRAY)
shapes_gray = cv2.cvtColor(src=shapes, code=cv2.COLOR_BGR2GRAY)

ret, target_th = cv2.threshold(src=target_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
ret, shapes_th = cv2.threshold(src=shapes_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

im, target_cntrs, hierarchy = cv2.findContours(image=target_th, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
im, shapes_cntrs, hierarchy = cv2.findContours(image=shapes_th, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

matchs = []
for contr in shapes_cntrs:
    match = cv2.matchShapes(contour1=target_cntrs[0], contour2=contr, method=cv2.CONTOURS_MATCH_I2, parameter=0.0)
    matchs.append((match, contr))
    cv2.putText(img=shapes, text="%.2f"%match, org=tuple(contr[0][0]), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0,0,255), thickness=1)

matchs.sort(key=lambda x: x[0])

cv2.drawContours(image=shapes, contours=[matchs[0][1]], contourIdx=-1, color=(0,255,0), thickness=1)
cv2.imshow(winname="target", mat=target)
cv2.imshow(winname="shapes", mat=shapes)
cv2.waitKey()
cv2.destroyAllWindows()
