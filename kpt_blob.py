"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

blob.detect - key points 찾기
"""
import cv2
import numpy as np


img = cv2.imread(filename="./img/house.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
blob = cv2.SimpleBlobDetector_create()
keypoints = blob.detect(gray)
img = cv2.drawKeypoints(image=img, keypoints=keypoints, outImage=None, color=(0,0,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow(winname="blob", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
