"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

orb.detectAndCompute - key poinsts 찾기
"""
import cv2
import numpy as np


img = cv2.imread(filename="./img/house.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create()
keypoints1, desc1 = orb.detectAndCompute(img, None)
keypoints2, desc2 = orb.detectAndCompute(gray, None)
img_draw1 = cv2.drawKeypoints(image=img, keypoints=keypoints1, outImage=None, color=None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img_draw2 = cv2.drawKeypoints(image=img, keypoints=keypoints2, outImage=None, color=None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow(winname="orb", mat=np.hstack((img_draw1,img_draw2)))
cv2.waitKey()
cv2.destroyAllWindows()
