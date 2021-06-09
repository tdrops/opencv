"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

이미지 일부를 삼각형 대응 방법으로 변형
"""


import cv2
import numpy as np


img = cv2.imread(filename="./img/taekwonv1.jpg")

pts1 = np.float32([[188,14],[85,202],[294,216]])  # 변경전 대응점
pts2 = np.float32([[128,40],[85,307],[306,167]])  # 변경후 대응점

x1,y1,w1,h1 = cv2.boundingRect(points=pts1)  # 위 삼각형의 최소,최대 x,y로 사각형 구하기
x2,y2,w2,h2 = cv2.boundingRect(points=pts2)

roi1 = img[y1:y1+h1,x1:x1+w1]  # 변경할 영역 잘라냄
roi2 = img[y2:y2+h2,x2:x2+w2]

pts1_0 = np.float32([[188-x1,14-y1],[85-x1,202-y1],[294-x1,216-y1]])  # 변경 대응점을 roi 기준으로 변경
pts2_0 = np.float32([[128-x2,40-y2],[85-x2,307-y2],[306-x2,167-y2]])

matrix = cv2.getAffineTransform(src=pts1_0, dst=pts2_0)  # 대응 행렬 구함
warped = cv2.warpAffine(src=roi1, M=matrix, dsize=(w2,h2))  # roi1에 행렬 반영

mask = np.zeros(shape=(h2,w2), dtype=np.uint8)  # roi2 크리로 마스크 만듬
mask = cv2.fillConvexPoly(img=mask, points=np.int32(pts2_0), color=(255,255,255))  # 변경후 대응점 모양으로 잘라내기 위한 마스크

warped_masked = cv2.bitwise_and(src1=warped, src2=warped, mask=mask)  # 변경된 값을 마스크 모양대로 잘라냄
roi2_not_mask = cv2.bitwise_and(src1=roi2, src2=roi2, mask=cv2.bitwise_not(src=mask))  # roi2를 마스크 외부 값만 잘나냄

roi2_not_mask = roi2_not_mask + warped_masked  # 이미지 2개를 합침
img[y2:y2+h2,x2:x2+w2] = roi2_not_mask  # 합친 이미지를 roi2영역에 반영

cv2.imshow(winname="img", mat=img)

cv2.waitKey()
cv2.destroyAllWindows()
