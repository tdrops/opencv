"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

사진에서 haarcascade 로 얼굴과 눈 인식
"""
import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("./data/haarcascade_eye.xml")

img = cv2.imread(filename="./img/children.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(image=gray)

for (x,y,w,h) in faces:
    cv2.rectangle(img=img, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=1)
    roi = img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(image=roi)

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img=img[y:y+h,x:x+w], pt1=(ex,ey), pt2=(ex+ew,ey+eh), color=(255,0,0), thickness=1)

cv2.imshow(winname="img", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
