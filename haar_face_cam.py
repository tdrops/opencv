"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

haar 로 캠의 얼굴, 눈 인식
"""
import cv2


face_cascade = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("./data/haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image=gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(img=img, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=1)
        roi = gray[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(image=roi)

        for i, (ex,ey,ew,eh) in enumerate(eyes):
            if i >= 2:
                break
            cv2.rectangle(img=img[y:y+h,x:x+w], pt1=(ex,ey), pt2=(ex+ew,ey+ew), color=(255,0,0), thickness=1)

    cv2.imshow(winname="cam", mat=img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()
