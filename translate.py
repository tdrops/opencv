"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-1] 평행 이동
"""
import cv2
import numpy as np

dx = 100
dy = 50

img = cv2.imread(filename="../img/fish.jpg")
h, w = img.shape[:2]

matrix = np.float32([[1, 0, dx], [0, 1, dy]])

result = cv2.warpAffine(src=img, M=matrix, dsize=(w + dx, h + dy))
result2 = cv2.warpAffine(src=img, M=matrix, dsize=(w + dx, h + dy), dst=None, flags=cv2.INTER_LINEAR,
                         borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 0, 0))
result3 = cv2.warpAffine(src=img, M=matrix, dsize=(w + dx, h + dy), dst=None, flags=cv2.INTER_LINEAR,
                         borderMode=cv2.BORDER_REFLECT)
cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result", mat=result)
cv2.imshow(winname="result2", mat=result2)
cv2.imshow(winname="result3", mat=result3)
cv2.waitKey()
cv2.destroyAllWindows()
