"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

sift flann - 키포인트 비교
"""
import cv2
import numpy as np


img1 = cv2.imread(filename="./img/taekwonv1.jpg")
img2 = cv2.imread(filename="./img/figures.jpg")

gray1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp1,desc1 = sift.detectAndCompute(gray1, None)
kp2,desc2 = sift.detectAndCompute(gray2, None)

index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)

flannmatcher = cv2.FlannBasedMatcher(index_params, search_params)
matches = flannmatcher.match(queryDescriptors=desc1, trainDescriptors=desc2)
res = cv2.drawMatches(img1=img1, keypoints1=kp1, img2=img2, keypoints2=kp2, matches1to2=matches, outImg=None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow(winname="result", mat=res)
cv2.waitKey()
cv2.destroyAllWindows()
