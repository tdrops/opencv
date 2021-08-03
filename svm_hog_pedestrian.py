"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-12] HOG-SVM 보행자 검출
"""
import cv2

hogdef = cv2.HOGDescriptor()
hogdef.setSVMDetector(_svmdetector=cv2.HOGDescriptor_getDefaultPeopleDetector())

hogdaim = cv2.HOGDescriptor((48,96), (16,16), (8,8), (8,8), 9)
hogdaim.setSVMDetector(_svmdetector=cv2.HOGDescriptor_getDaimlerPeopleDetector())

cap = cv2.VideoCapture("../img/walking.avi")
mode = True

while cap.isOpened():
    ret, img = cap.read()
    if ret:
        if mode:
            found, _ = hogdef.detectMultiScale(img=img)
            for (x,y,w,h) in found:
                cv2.rectangle(img=img, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,255))
        else:
            found, _ = hogdaim.detectMultiScale(img=img)
            for (x,y,w,h) in found:
                cv2.rectangle(img=img, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0))

        cv2.putText(img=img, text="Detector:Default" if mode else "Detector:Daimler", org=(10,50), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0,255,0))
        cv2.imshow(winname="frame", mat=img)
        key = cv2.waitKey(delay=1)
        if key == 27:
            break
        elif key == ord(" "):
            mode = not mode
    else:
        break

cap.release()
cv2.destroyAllWindows()
