"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-11] 거리 변환으로 전신 스켈레톤 찾기
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/full_body.jpg", flags=cv2.IMREAD_GRAYSCALE)
ret, th = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

dst = cv2.distanceTransform(src=th, distanceType=cv2.DIST_L2, maskSize=5)

dst = (dst * 255 / (dst.max() - dst.min())).astype(np.uint8)
skeleton = cv2.adaptiveThreshold(src=dst, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 thresholdType=cv2.THRESH_BINARY, blockSize=7, C=-3)

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="dst", mat=dst)
cv2.imshow(winname="skeleton", mat=skeleton)
cv2.waitKey()
cv2.destroyAllWindows()
