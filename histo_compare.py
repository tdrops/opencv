"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-33] 히스토그램 비교
"""
import cv2
import numpy as np


img1 = cv2.imread(filename="../img/taekwonv1.jpg")
img2 = cv2.imread(filename="../img/taekwonv2.jpg")
img3 = cv2.imread(filename="../img/taekwonv3.jpg")
img4 = cv2.imread(filename="../img/dr_ochanomizu.jpg")

img1_hsv = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2HSV)
img2_hsv = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2HSV)
img3_hsv = cv2.cvtColor(src=img3, code=cv2.COLOR_BGR2HSV)
img4_hsv = cv2.cvtColor(src=img4, code=cv2.COLOR_BGR2HSV)

hist1 = cv2.calcHist(images=[img1_hsv], channels=[0,1], mask=None, histSize=[180,256], ranges=[0,180,0,256])
cv2.normalize(src=hist1, dst=hist1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist2 = cv2.calcHist(images=[img2_hsv], channels=[0,1], mask=None, histSize=[180,256], ranges=[0,180,0,256])
cv2.normalize(src=hist2, dst=hist2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist3 = cv2.calcHist(images=[img3_hsv], channels=[0,1], mask=None, histSize=[180,256], ranges=[0,180,0,256])
cv2.normalize(src=hist3, dst=hist3, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist4 = cv2.calcHist(images=[img4_hsv], channels=[0,1], mask=None, histSize=[180,256], ranges=[0,180,0,256])
cv2.normalize(src=hist4, dst=hist4, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

ret = cv2.compareHist(H1=hist1, H2=hist1, method=cv2.HISTCMP_CORREL)
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist2, method=cv2.HISTCMP_CORREL)
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist3, method=cv2.HISTCMP_CORREL)
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist4, method=cv2.HISTCMP_CORREL)
print(f"{ret:7.2}")

ret = cv2.compareHist(H1=hist1, H2=hist1, method=cv2.HISTCMP_CHISQR)
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist2, method=cv2.HISTCMP_CHISQR)
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist3, method=cv2.HISTCMP_CHISQR)
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist4, method=cv2.HISTCMP_CHISQR)
print(f"{ret:7.2}")

sum_hist1 = np.sum(hist1)
ret = cv2.compareHist(H1=hist1, H2=hist1, method=cv2.HISTCMP_INTERSECT)
ret = ret / sum_hist1
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist2, method=cv2.HISTCMP_INTERSECT)
ret = ret / sum_hist1
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist3, method=cv2.HISTCMP_INTERSECT)
ret = ret / sum_hist1
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist4, method=cv2.HISTCMP_INTERSECT)
ret = ret / sum_hist1
print(f"{ret:7.2}")

ret = cv2.compareHist(H1=hist1, H2=hist1, method=cv2.HISTCMP_BHATTACHARYYA)
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist2, method=cv2.HISTCMP_BHATTACHARYYA)
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist3, method=cv2.HISTCMP_BHATTACHARYYA)
print(f"{ret:7.2}", end="\t")
ret = cv2.compareHist(H1=hist1, H2=hist4, method=cv2.HISTCMP_BHATTACHARYYA)
print(f"{ret:7.2}")
