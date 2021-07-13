"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 6-19] 라플라시안 피라미드로 연상 복원
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/taekwonv1.jpg")

smaller = cv2.pyrDown(src=img)
bigger = cv2.pyrUp(src=smaller)

laplacian = img - bigger

laplacian = cv2.subtract(src1=img, src2=bigger)

restored = bigger + laplacian

cv2.imshow(winname="ori/laplacian/bigger/restored", mat=np.hstack((img,laplacian,bigger,restored)))
cv2.waitKey()
cv2.destroyAllWindows()
