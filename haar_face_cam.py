"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-16] 카메라로 얼굴과 눈 검출
"""
import cv2

face_cascade = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier("./data/haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.3, minNeighbors=5, minSize=(80, 80))

        for (x, y, w, h) in faces:
            cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
            roi = gray[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(image=roi)
            for i, (ex, ey, ew, eh) in enumerate(eyes):
                if i >= 2:
                    break
                cv2.rectangle(img=img[y:y + h, x:x + w], pt1=(ex, ey), pt2=(ex + ew, ey + eh), color=(255, 0, 0),
                              thickness=2)
        cv2.imshow(winname="face detect", mat=img)
    else:
        break
    if cv2.waitKey(delay=5) == 27:
        break

cv2.destroyAllWindows()
