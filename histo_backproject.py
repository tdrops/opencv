"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-32] 마우스로 선택한 영역의 물체 배경 제거
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


windowName = "pump_horse"

img = cv2.imread(filename="../img/pump_horse.jpg")
hsv_img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2HSV)
draw = img.copy()


def masking(bp, winname):
    disc = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(5,5))
    cv2.filter2D(src=bp, ddepth=-1, kernel=disc, dst=bp)
    _, mask = cv2.threshold(src=bp, thresh=1, maxval=255, type=cv2.THRESH_BINARY)
    result = cv2.bitwise_and(src1=img, src2=img, mask=mask)
    cv2.imshow(winname=winname, mat=result)


def backProject_manual(hist_roi):
    hist_img = cv2.calcHist(images=[hsv_img], channels=[0,1], mask=None, histSize=[180,256], ranges=[0,180,0,256])
    hist_rate = hist_roi / (hist_img+1)
    h,s,v = cv2.split(m=hsv_img)
    bp = hist_rate[h.ravel(), s.ravel()]
    bp = np.minimum(bp, 1)
    bp = bp.reshape(hsv_img.shape[:2])
    cv2.normalize(src=bp, dst=bp, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    bp = bp.astype(np.uint8)
    masking(bp=bp, winname="manual")


def backProject_cv(hist_roi):
    bp = cv2.calcBackProject(images=[hsv_img], channels=[0,1], hist=hist_roi, ranges=[0,180,0,256], scale=1)
    masking(bp=bp, winname="cv2")


(x,y,w,h) = cv2.selectROI(windowName=windowName, img=img, showCrosshair=False)
if w>0 and h>0:
    roi = draw[y:y+h,x:x+w]
    cv2.rectangle(img=draw, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=1)
    hsv_roi = cv2.cvtColor(src=roi, code=cv2.COLOR_BGR2HSV)
    hist_roi = cv2.calcHist(images=[hsv_roi], channels=[0,1], mask=None, histSize=[180,256], ranges=[0,180,0,256])
    backProject_manual(hist_roi=hist_roi)
    backProject_cv(hist_roi=hist_roi)


cv2.imshow(winname=windowName, mat=draw)
cv2.waitKey()
cv2.destroyAllWindows()
