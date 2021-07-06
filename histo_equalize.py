"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-28] 그레이 스케일 이퀄라이드 적용
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/yate.jpg", flags=cv2.IMREAD_GRAYSCALE)
h, w = img.shape[:2]
print(f"h:{h} w:{w} h*w:{h * w}")

hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

cdf = hist.cumsum()  # 누적 구하기

print(f"cdf.min():{cdf.min()}")
print(f"cdf.max():{cdf.max()}")

cdf = np.uint8((cdf - cdf.min()) / (cdf.max() - cdf.min()) * 255)  # 0~255 사이 값으로 변경

img2 = cdf[img]  # cdf 에서 img 값으로 인덱싱

img3 = cv2.equalizeHist(img)

cv2.imshow(winname="img:img2:img3", mat=np.hstack((img, img2, img3)))
cv2.waitKey()
cv2.destroyAllWindows()
