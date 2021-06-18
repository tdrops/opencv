"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

ORB FlannMatcher - 대응점 찾기
"""
import cv2
import numpy as np

img1 = cv2.imread(filename="./img/taekwonv1.jpg")
img2 = cv2.imread(filename="./img/figures.jpg")

gray1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp1, desc1 = orb.detectAndCompute(gray1, None)
kp2, desc2 = orb.detectAndCompute(gray2, None)

index_params = dict(algorithm=6, table_number=6, key_size=12, multi_probe_level=1)
search_params = dict(checks=32)
flannmatcher = cv2.FlannBasedMatcher(index_params, search_params)
matches = flannmatcher.match(desc1, desc2)
result = cv2.drawMatches(img1=img1, keypoints1=kp1, img2=img2, keypoints2=kp2, matches1to2=matches, outImg=None,
                         flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow(winname="result", mat=result)
cv2.waitKey()
cv2.destroyAllWindows()
