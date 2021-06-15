"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

모멘트를 이용한 중심점, 넓이, 둘레길이 구하기
"""



import cv2
import numpy as np


img = cv2.imread(filename="./img/shapes.png")
img_gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
ret, img_gray = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
img2, contours, hierarchy = cv2.findContours(image=img_gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    mmt = cv2.moments(array=c)
    cx = int(mmt["m10"]/mmt["m00"])
    cy = int(mmt["m01"]/mmt["m00"])
    a = mmt["m00"]
    l = cv2.arcLength(curve=c, closed=True)
    cv2.circle(img=img, center=(cx,cy), radius=5, color=(0,255,255), thickness=-1)
    cv2.putText(img=img, text=f"A:{a}", org=(cx,cy), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0,0,255))
    cv2.putText(img=img, text=f"L:{l}", org=tuple(c[0][0]), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0,0,255))

    print(f"Area:{cv2.contourArea(contour=c, oriented=False)}")

cv2.imshow(winname="img", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()

