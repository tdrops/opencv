"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-34] 반해골 괴물 얼굴 합성 풀이
"""
import cv2
import numpy as np


overlap_percent = 0.15

img1 = cv2.imread(filename="../img/man_face.jpg")
img2 = cv2.imread(filename="../img/skull.jpg")
h,w = img1.shape[:2]

half = w // 2
width = int(w * overlap_percent//2)

result = img1.copy()
result[:,half:] = img2[:,half:]

# result = result.astype(np.float32)

alpha = 1.0
step = 1/(width*2)
for x in range(half-width,half+width+1,1):
    result[:,x] = img1[:,x]*alpha + img2[:,x]*(1-alpha)
    alpha = alpha - step
    if alpha < 0:
        alpha = 0

# result = result.astype(np.uint8)

cv2.imshow("result", mat=result)
cv2.waitKey()
cv2.destroyAllWindows()
