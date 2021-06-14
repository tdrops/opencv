"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

laplacian 외곽선 검출
"""



import cv2
import numpy as np


img = cv2.imread(filename="./img/taekwonv1.jpg")
smaller = cv2.pyrDown(src=img)
bigger = cv2.pyrUp(src=smaller)
laplacian = cv2.subtract(src1=img, src2=bigger)
restored = laplacian + bigger

cv2.imshow(winname="laplacian", mat=np.hstack([img, bigger, laplacian, restored]))

cv2.waitKey()
cv2.destroyAllWindows()
