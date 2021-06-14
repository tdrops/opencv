"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

pyrUp, pyrDown 4배 확대 축소
"""



import cv2
import numpy as np


img = cv2.imread(filename="./img/girl.jpg")
cv2.imshow(winname="original", mat=img)

result1 = cv2.pyrUp(src=img)
result2 = cv2.pyrDown(src=img)

cv2.imshow(winname="result1", mat=result1)
cv2.imshow(winname="result2", mat=result2)

cv2.waitKey()
cv2.destroyAllWindows()
