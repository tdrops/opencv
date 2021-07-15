"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 7-16] 평균 이동 세그멘테이션 필터
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/taekwonv1.jpg")


def onChange(x):
    sp = cv2.getTrackbarPos(trackbarname="sp", winname="img")
    sr = cv2.getTrackbarPos(trackbarname="sr", winname="img")
    lv = cv2.getTrackbarPos(trackbarname="lv", winname="img")

    mean = cv2.pyrMeanShiftFiltering(src=img, sp=sp, sr=sr, dst=None, maxLevel=lv)

    cv2.imshow(winname="img", mat=np.hstack((img,mean)))


cv2.imshow(winname="img", mat=np.hstack((img,img)))

cv2.createTrackbar("sp", "img", 0, 100, onChange)
cv2.createTrackbar("sr", "img", 0, 100, onChange)
cv2.createTrackbar("lv", "img", 0, 5, onChange)
cv2.waitKey()
cv2.destroyAllWindows()
