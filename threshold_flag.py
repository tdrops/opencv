"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-10] 스레시홀딩 플래그 실습
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/gray_gradient.jpg")

_, th1 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
_, th2 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_TOZERO_INV)

# _, th6 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_OTSU)
# _, th7 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_MASK)
# _, th8 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_TRIANGLE)

cv2.imshow(winname="threshold", mat=np.vstack((img,th1,th2,th3,th4,th5)))
cv2.waitKey()
cv2.destroyAllWindows()
