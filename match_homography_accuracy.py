"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-22] RANSAC 원근 변환 근사 계산으로 나쁜 매칭 제거
"""
import cv2
import numpy as np

img1 = cv2.imread(filename="../img/taekwonv1.jpg")
img2 = cv2.imread(filename="../img/figures2.jpg")
gray1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)

detector = cv2.ORB_create()
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = matcher.match(queryDescriptors=desc1, trainDescriptors=desc2)

matches = sorted(matches, key=lambda x: x.distance)

res1 = cv2.drawMatches(img1=img1, keypoints1=kp1, img2=img2, keypoints2=kp2, matches1to2=matches, outImg=None,
                       flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

src_pts = np.float32([kp1[m.queryIdx].pt for m in matches])
dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches])

mtrx, mask = cv2.findHomography(srcPoints=src_pts, dstPoints=dst_pts, method=cv2.RANSAC, ransacReprojThreshold=5.0)
h, w = img1.shape[:2]
pts = np.float32([[[0, 0]], [[0, h - 1]], [[w - 1, h - 1]], [[w - 1, 0]]])
dst = cv2.perspectiveTransform(src=pts, m=mtrx)
img2 = cv2.polylines(img=img2, pts=[np.int32(dst)], isClosed=True, color=255, thickness=3, lineType=cv2.LINE_AA)

matchesMask = mask.ravel().tolist()
res2 = cv2.drawMatches(img1=img1, keypoints1=kp1, img2=img2, keypoints2=kp2, matches1to2=matches, outImg=None,
                       matchesMask=matchesMask, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

accuracy = float(mask.sum()) / mask.size

cv2.imshow(winname="result1", mat=res1)
cv2.imshow(winname="result2", mat=res2)
cv2.waitKey()
cv2.destroyAllWindows()
