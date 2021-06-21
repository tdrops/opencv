"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

ORB 로 찾고, BF HAMMING2 knnMatch 2 로 대응시키고 대응 편명도 그리기
"""
import cv2
import numpy as np


img1 = cv2.imread(filename="./img/taekwonv1.jpg")
img2 = cv2.imread(filename="./img/figures.jpg")

gray1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)

detector = cv2.ORB_create()
kp1, des1 = detector.detectAndCompute(gray1, None)
kp2, des2 = detector.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher_create(normType=cv2.NORM_HAMMING2)
matches = matcher.knnMatch(des1, des2, 2)

good_matches = [first for first, second in matches if first.distance < second.distance * 0.75]

src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches])
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches])

mtrx, mask = cv2.findHomography(srcPoints=src_pts, dstPoints=dst_pts)

h, w = img1.shape[:2]
pts = np.float32([[[0,0]], [[0,h-1]], [[w-1,h-1]], [[w-1,0]]])
dst = cv2.perspectiveTransform(src=pts, m=mtrx)

cv2.polylines(img=img2, pts=[np.int32(dst)], isClosed=True, color=(0,255,0), thickness=1)

result = cv2.drawMatches(img1=img1, keypoints1=kp1, img2=img2, keypoints2=kp2, matches1to2=good_matches, outImg=None, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow(winname="result", mat=result)
cv2.waitKey()
cv2.destroyAllWindows()
