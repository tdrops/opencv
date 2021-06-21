"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

orb 로 찾고 bf norm_hamming 으로 연결하고 distance 짧은 것만 골라내기
"""
import cv2
import numpy as np

img1 = cv2.imread(filename="./img/taekwonv1.jpg")
img2 = cv2.imread(filename="./img/figures.jpg")

gray1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)

detector = cv2.ORB_create()
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

bfmatcher = cv2.BFMatcher_create(normType=cv2.NORM_HAMMING, crossCheck=True)
matches = bfmatcher.match(desc1, desc2)

matches = sorted(matches, key=lambda x:x.distance)

min_distance = matches[0].distance
max_distance = matches[-1].distance

ratio = 0.2

good_thresh = (max_distance-min_distance)*ratio + min_distance

good_matches = [m for m in matches if m.distance < good_thresh]

result = cv2.drawMatches(img1=img1, keypoints1=kp1, img2=img2, keypoints2=kp2, matches1to2=good_matches, outImg=None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow(winname="result", mat=result)
cv2.waitKey()
cv2.destroyAllWindows()
