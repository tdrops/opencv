"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

dlib 로 얼굴 68개 주요점 구해서 삼각형으로 연결
"""
import cv2
import numpy as np
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/shape_predictor_68_face_landmarks.dat")

img = cv2.imread(filename="./img/man_face.jpg")
h, w = img.shape[:2]
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

rects = faces = detector(gray)

points = []
for rect in rects:
    shape = predictor(image=gray, box=rect)
    for i in range(68):
        part = shape.part(i)
        points.append((part.x, part.y))

x, y, w, h = cv2.boundingRect(np.float32(points))
subdiv = cv2.Subdiv2D((x, y, x + w, y + h))

# subdiv = cv2.Subdiv2D((0,0,w,h))
subdiv.insert(points)
triangleList = subdiv.getTriangleList()

h, w = img.shape[:2]
for t in triangleList:
    pts = t.reshape(-1, 2).astype(np.int32)
    if (pts < 0).sum() or (pts[:, 0] > w).sum() or (pts[:, 1] > h).sum():
        continue
    cv2.polylines(img, [pts], True, (255, 255, 255), 1, cv2.LINE_AA)
cv2.imshow(winname="img", mat=img)
cv2.waitKey()

"""
import cv2
import numpy as np
import dlib


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./data/shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    h, w = img.shape[:2]
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    rects = faces = detector(gray)

    points = []
    for rect in rects:
        shape = predictor(image=gray, box=rect)
        for i in range(68):
            part = shape.part(i)
            points.append((part.x, part.y))

    # x, y, w, h = cv2.boundingRect(np.float32(points))
    # subdiv = cv2.Subdiv2D((x, y, x + w, y + h))

    subdiv = cv2.Subdiv2D((0,0,w,h))
    subdiv.insert(points)
    triangleList = subdiv.getTriangleList()

    h, w = img.shape[:2]
    for t in triangleList:
        pts = t.reshape(-1, 2).astype(np.int32)
        if (pts < 0).sum() or (pts[:, 0] > w).sum() or (pts[:, 1] > h).sum():
            continue
        cv2.polylines(img, [pts], True, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow(winname="cam", mat=img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""
