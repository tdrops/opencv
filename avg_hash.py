"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-1] 권총을 평균 해시로 변환
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/pistol.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

gray = cv2.resize(src=gray, dsize=(16, 16))

avg = gray.mean()

bin = 1 * (gray > avg)
print(bin)

cv2.imshow(winname="original", mat=img)
cv2.waitKey()
