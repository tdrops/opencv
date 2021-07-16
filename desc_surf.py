"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-11] SURF로 키 포인트 및 디스크립터 추출
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/house.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create(hessianThreshold=1000, nOctaves=3, nOctaveLayers=True, extended=True)

keypoints, desc = surf.detectAndCompute(gray, None)

img_draw = cv2.drawKeypoints(image=img, keypoints=keypoints, outImage=None,
                             flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow(winname="img_draw", mat=img_draw)
cv2.waitKey()
cv2.destroyAllWindows()
