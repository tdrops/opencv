"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-12] 적응형 스레시홀드 적용
"""
import cv2
import numpy as np


img = cv2.imread(filename="../img/sudoku.png", flags=cv2.IMREAD_GRAYSCALE)
_, th1 = cv2.threshold(src=img, thresh=-1, maxval=255, type=cv2.THRESH_BINARY|cv2.THRESH_OTSU)
th2 = cv2.adaptiveThreshold(src=img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=9, C=5)
th3 = cv2.adaptiveThreshold(src=img, maxValue=233, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=9, C=5)

cv2.imshow(winname="threshold", mat=np.hstack((img,th1,th2,th3)))
cv2.waitKey()
cv2.destroyAllWindows()
