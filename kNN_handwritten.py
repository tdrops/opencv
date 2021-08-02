"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-8] 손글씨 숫자 인식
"""
import cv2
import numpy as np
import mnist

train, train_labels = mnist.getTrain()

knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

image = cv2.imread("../img/4027.png")
cv2.imshow(winname="image", mat=image)
cv2.waitKey(delay=0)

gray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)
_, gray = cv2.threshold(src=gray, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)

img, contours, _ = cv2.findContours(image=gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    (x, y, w, h) = cv2.boundingRect(points=c)

    if w >= 5 and h >= 25:
        roi = gray[y:y + h, x:x + w]
        cv2.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=1)

        data = mnist.digit2data(src=roi)

        ret, result, neighbors, dist = knn.findNearest(data, k=1)
        cv2.putText(img=image, text="%d" % ret, org=(x, y + 155), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=2,
                    color=(255, 0, 0), thickness=2)
        cv2.imshow(winname="image", mat=image)
        cv2.waitKey()
cv2.destroyAllWindows()
