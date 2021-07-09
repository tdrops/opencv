"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-5] 회전 변환행렬 구하기
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/fish.jpg")
h,w = img.shape[:2]

m45 = np.float32([[np.cos(45*np.pi/180), -np.sin(45*np.pi/180), w],
                  [np.sin(45*np.pi/180),  np.cos(45*np.pi/180), 0]])
m90 = np.float32([[np.cos(90*np.pi/180), -np.sin(90*np.pi/180), w],
                  [np.sin(90*np.pi/180),  np.cos(90*np.pi/180), 0]])

result1 = cv2.warpAffine(src=img, M=m45, dsize=(w*2,h*2))
result2 = cv2.warpAffine(src=img, M=m90, dsize=(w*2,h*2))

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="result1", mat=result1)
cv2.imshow(winname="result2", mat=result2)
cv2.waitKey()
cv2.destroyAllWindows()
