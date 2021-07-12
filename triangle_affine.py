"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-9] 삼각형 어핀 변환
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/taekwonv1.jpg")

pts1 = np.float32([[188,14],[85,202],[294,216]])
pts2 = np.float32([[128,40],[85,307],[306,167]])

x1,y1,w1,h1 = cv2.boundingRect(pts1)
x2,y2,w2,h2 = cv2.boundingRect(pts2)

roi1 = img[y1:y1+h1,x1:x1+w1]
roi2 = img[y2:y2+h2,x2:x2+w2]

offset1 = np.zeros(shape=(3,2), dtype=np.float32)
offset2 = np.zeros(shape=(3,2), dtype=np.float32)

for i in range(3):
    offset1[i][0] = pts1[i][0] - x1
    offset1[i][1] = pts1[i][1] - y1

    offset2[i][0] = pts2[i][0] - x2
    offset2[i][1] = pts2[i][1] - y2

mtrx = cv2.getAffineTransform(src=offset1, dst=offset2)
warped = cv2.warpAffine(src=roi1, M=mtrx, dsize=(w2,h2), dst=None, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)

mask = np.zeros(shape=(h2,w2), dtype=np.uint8)
mask = cv2.fillConvexPoly(img=mask, points=np.int32(offset2), color=255)
mask_not = cv2.bitwise_not(src=mask)

result1 = cv2.bitwise_and(src1=warped, src2=warped, mask=mask)
result2 = cv2.bitwise_and(src1=roi2, src2=roi2, mask=mask_not)

img[y2:y2+h2,x2:x2+w2] = result1 + result2

cv2.imshow(winname="affine", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
