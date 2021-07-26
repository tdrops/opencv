"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-20] knnMatch 함수로부터 좋은 매칭점 찾기
"""
import cv2
import numpy as np

img1 = cv2.imread(filename="../img/taekwonv1.jpg")
img2 = cv2.imread(filename="../img/figures.jpg")
gray1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)

detector = cv2.ORB_create()
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING)

matches = matcher.knnMatch(queryDescriptors=desc1, trainDescriptors=desc2, k=2)

ratio = 0.75
good_matechs = [first for first,second in matches if first.distance < second.distance * ratio]

res = cv2.drawMatches(img1=img1, keypoints1=kp1, img2=img2, keypoints2=kp2, matches1to2=good_matechs, outImg=None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow(winname="result", mat=res)
cv2.waitKey()
cv2.destroyAllWindows()
