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


img = cv2.imread(filename="../github/opencv/img/taekwonv1.jpg")

pts1 = np.float32([[188,14],[85,202],[294,216]])
pts2 = np.float32([[128,40],[85,307],[306,167]])

x1,y1,w1,h1 = cv2.boundingRect(points=pts1)  # 삼각점을 둘러싸는 사각형의 좌표 구함
x2,y2,w2,h2 = cv2.boundingRect(points=pts2)

roi1 = img[y1:y1+h1,x1:x1+w1]
roi2 = img[y2:y2+h2,x2:x2+w2]

offset1 = np.zeros(shape=(3,2), dtype=np.float32)  # 삼각점을 roi 기준으로 좌표 변경
offset2 = np.zeros(shape=(3,2), dtype=np.float32)

for i in range(3):
    offset1[i][0] = pts1[i][0] - x1
    offset1[i][1] = pts1[i][1] - y1

    offset2[i][0] = pts2[i][0] - x2
    offset2[i][1] = pts2[i][1] - y2

matrix = cv2.getAffineTransform(src=offset1, dst=offset2)  # 매트릭스 구함
warped = cv2.warpAffine(src=roi1, M=matrix, dsize=(w2,h2))  # 매트릭스 반영

mask = np.full(shape=(h2,w2), fill_value=0, dtype=np.uint8)  # warped 부분과 아닌 부분을 잘라내기 위한 mask 생성
cv2.fillConvexPoly(img=mask, points=np.int32(offset2), color=255)
notmask = cv2.bitwise_not(src=mask)

warped_masked = cv2.bitwise_and(src1=warped, src2=warped, mask=mask)  # warped를 mask 모양으로 자르고
roi2_notmasked = cv2.bitwise_and(src1=roi2, src2=roi2, mask=notmask)  # 그렇지 않은 부분을 mask 반대 모양으로 자름

result = roi2_notmasked + warped_masked  # mask 된 이미지의 다른 부분은 0 이므로 더하면 두 이미지를 겹쳐 그린 것이됨

img[y2:y2+h2,x2:x2+w2] = result  # 결과물은 roi2 영역에 반영

cv2.imshow(winname="img", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
