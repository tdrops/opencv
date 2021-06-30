"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-19] bitwise_and 연산으로 마스킹하기
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/girl.jpg")
mask = np.zeros_like(img)
cv2.circle(img=mask, center=(150,140), radius=100, color=(255,255,255), thickness=-1)

bitAnd = cv2.bitwise_and(src1=img, src2=mask)

cv2.imshow(winname="bit_mask", mat=np.hstack((img,mask,bitAnd)))
cv2.waitKey()
cv2.destroyAllWindows()
