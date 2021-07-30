"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-31] 파노라마 사진 생성기
"""
import cv2
import numpy as np

imgL = cv2.imread(filename="../img/restaurant1.jpg")
imgR = cv2.imread(filename="../img/restaurant2.jpg")
hl, wl = imgL.shape[:2]
hr, wr = imgR.shape[:2]

grayL = cv2.cvtColor(src=imgL, code=cv2.COLOR_BGR2GRAY)
grayR = cv2.cvtColor(src=imgR, code=cv2.COLOR_BGR2GRAY)

descriptor = cv2.xfeatures2d.SIFT_create()
(kpsL, featuresL) = descriptor.detectAndCompute(grayL, None)
(kpsR, featuresR) = descriptor.detectAndCompute(grayR, None)

matcher = cv2.DescriptorMatcher_create("BruteForce")
matches = matcher.knnMatch(featuresR, featuresL, 2)

good_matches = []
for m in matches:
    if len(m) == 2 and m[0].distance < m[1].distance * 0.75:
        good_matches.append((m[0].trainIdx, m[0].queryIdx))

if len(good_matches) > 4:
    ptsL = np.float32([kpsL[i].pt for (i, _) in good_matches])
    ptsR = np.float32([kpsR[i].pt for (_, i) in good_matches])
    mtrx, status = cv2.findHomography(ptsR, ptsL, cv2.RANSAC, 4.0)

    panorama = cv2.warpPerspective(src=imgR, M=mtrx, dsize=(wr+wl, hr))
    panorama[0:hl, 0:wl] = imgL
else:
    panorama = imgL

cv2.imshow(winname="imgL", mat=imgL)
cv2.imshow(winname="imgR", mat=imgR)
cv2.imshow(winname="panorama", mat=panorama)
cv2.waitKey()
cv2.destroyAllWindows()
