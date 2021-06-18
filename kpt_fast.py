"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

fast.detect - key point 찾기
"""
import cv2
import numpy as np


img = cv2.imread(filename="./img/house.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
fast = cv2.FastFeatureDetector_create()
keypoints = fast.detect(gray, None)
img = cv2.drawKeypoints(image=img, keypoints=keypoints, outImage=None)
cv2.imshow(winname="Fast", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
