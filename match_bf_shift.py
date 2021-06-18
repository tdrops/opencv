"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

bfmatcher.match - 대응점 표시
"""
import cv2
import numpy as np


img1 = cv2.imread(filename="./img/taekwonv1.jpg")
img2 = cv2.imread(filename="./img/figures.jpg")
gray1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kpt1,desc1 = sift.detectAndCompute(gray1, None)
kpt2,desc2 = sift.detectAndCompute(gray2, None)
bfmatcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bfmatcher.match(desc1, desc2)
result = cv2.drawMatches(img1=img1, keypoints1=kpt1, img2=img2, keypoints2=kpt2, matches1to2=matches, outImg=None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow(winname="result", mat=result)
cv2.waitKey()
cv2.destroyAllWindows()
