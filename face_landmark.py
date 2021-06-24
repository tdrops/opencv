"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

얼굴 사진에서 주요점을 찾아 표시함
"""
import cv2
import dlib


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/shape_predictor_68_face_landmarks.dat")

img = cv2.imread(filename="./img/man_face.jpg")
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

faces = detector(gray)

for rect in faces:
    x, y = rect.left(), rect.top()
    w, h = rect.right()-x, rect.bottom()-y

    cv2.rectangle(img=img, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=1)

    shape = predictor(image=gray, box=rect)
    for i in range(68):
        part = shape.part(i)
        cv2.circle(img=img, center=(part.x,part.y), radius=2, color=(0,0,255), thickness=-1)
        cv2.putText(img=img, text=f"{i}", org=(part.x,part.y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.2, color=(255,255,255), thickness=1, lineType=cv2.LINE_AA)

cv2.imshow(winname="img", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()

"""
import cv2
import numpy as np
import dlib


cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/shape_predictor_68_face_landmarks.dat")

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for rect in faces:
        x, y = rect.left(), rect.top()
        w, h = rect.right() - x, rect.bottom() - y

        cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=1)

        shape = predictor(image=gray, box=rect)
        for i in range(68):
            part = shape.part(i)
            cv2.circle(img=img, center=(part.x, part.y), radius=2, color=(0, 0, 255), thickness=-1)
            cv2.putText(img=img, text=f"{i}", org=(part.x, part.y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.2,
                        color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

    cv2.imshow(winname="cam", mat=img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""
