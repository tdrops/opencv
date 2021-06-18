"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

blob.detect, param - key points 찾기, param 적용
"""
import cv2
import numpy as np


img = cv2.imread(filename="./img/house.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
param = cv2.SimpleBlobDetector_Params()

param.minThreshold = 10
param.maxThreshold = 240
param.thresholdStep = 5

param.filterByArea = True
param.minArea = 200

param.filterByColor = False
param.filterByConvexity = False
param.filterByInertia = False
param.filterByCircularity = False

blob = cv2.SimpleBlobDetector_create(parameters=param)
keypoints = blob.detect(gray)
img = cv2.drawKeypoints(image=img, keypoints=keypoints, outImage=None, color=None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow(winname="param", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
