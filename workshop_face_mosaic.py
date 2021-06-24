"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

haar 로 얼굴 영역 좌표를 구하고 축소 확대로 모자이크 효과 내기
"""
import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image=gray)

    for (x,y,w,h) in faces:
        roi = img[y:y+h,x:x+w]
        roi = cv2.resize(src=roi, dsize=(w//15,h//15))
        roi = cv2.resize(src=roi, dsize=(w,h))
        img[y:y+h,x:x+w] = roi
    cv2.imshow(winname="img", mat=img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
