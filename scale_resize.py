"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-3] cv2.resize()로 확대와 축소
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/fish.jpg")
h,w = img.shape[:2]

result1 = cv2.resize(src=img, dsize=(int(w*0.5),int(h*0.5)), interpolation=cv2.INTER_AREA)
result2 = cv2.resize(src=img, dsize=None, dst=None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result1", mat=result1)
cv2.imshow(winname="result2", mat=result2)
cv2.waitKey()
cv2.destroyAllWindows()
