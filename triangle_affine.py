"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

2개의 삼각점 대응 방법으로 이미지 일부를 변형해서 원본 이미지에 붙이기
"""


import cv2
import numpy as np
import matplotlib.pylab as plt


pts1 = np.float32([[188,14],[85,202],[294,216]])  # 변형의 기준이 되는 2개의 삼각점
pts2 = np.float32([[128,40],[85,307],[306,167]])

img = cv2.imread(filename="./img/taekwonv1.jpg")
h,w = img.shape[:2]  # 높이, 폭 구함

cv2.imshow(winname="original", mat=img)

matrix = cv2.getAffineTransform(src=pts1, dst=pts2)  # 대응점으로 행렬 구함  
warped = cv2.warpAffine(src=img, M=matrix, dsize=(w,h))  # 원본이미지에 행렬 적용

cv2.imshow(winname="warped", mat=warped)

mask = np.zeros_like(a=img, dtype=np.uint8)
cv2.fillPoly(img=mask, pts=[np.int32(pts2)], color=(255,255,255))  # 두번째 삼각형 모양의 마스크 생성
notmask = cv2.bitwise_not(src=mask)

warped_masked = cv2.bitwise_and(src1=warped, src2=mask)  # 변형한 이미지를 두번째 삼각형 모양으로 잘라냄

cv2.imshow(winname="warped_masked", mat=warped_masked)

img_notmasked = cv2.bitwise_and(src1=img, src2=notmask)  # 원본이미지를 2번째 삼각형 모양의 반전모양으로 잘라냄

result = warped_masked + img_notmasked  # 여백부분이 0 이므로 더하면 원본 이미지에 변형된 이미지가 붙은 모양이됨

cv2.imshow(winname="result", mat=result)

cv2.waitKey()
cv2.destroyAllWindows()
