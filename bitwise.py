"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-18] 비트와이즈 연산
"""
import cv2
import numpy as np


img1 = np.zeros(shape=(200,400), dtype=np.uint8)
img2 = np.zeros(shape=(200,400), dtype=np.uint8)
img1[:,:200] = 255
img2[100:,:] = 255

bitAnd = cv2.bitwise_and(src1=img1, src2=img2)
bitOr = cv2.bitwise_or(src1=img1, src2=img2)
bitXor = cv2.bitwise_xor(src1=img1, src2=img2)
bitNot = cv2.bitwise_not(src=img1)

cv2.imshow(winname="img1", mat=img1)
cv2.imshow(winname="img2", mat=img2)
cv2.imshow(winname="and", mat=bitAnd)
cv2.imshow(winname="or", mat=bitOr)
cv2.imshow(winname="xor", mat=bitXor)
cv2.imshow(winname="not", mat=bitNot)

cv2.waitKey()
cv2.destroyAllWindows()
