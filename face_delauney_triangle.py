import cv2
import numpy as np
import dlib


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../data/shape/shape_predictor_68_face_landmarks.dat")

img = cv2.imread(filename="./img/man_face.jpg")
h,w = img.shape[:2]
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

rects = faces = detector(gray)


points = []
for rect in rects:
    shape = predictor(image=gray, box=rect)
    for i in range(68):
        part = shape.part[i]
        points.append((part.x, part.y))

subdiv = cv2.Subdiv2D((0,0,w,h))
subdiv.insert(points)
triangleList = subdiv.getTriangleList()

h, w = img.shape[:2]
for t in triangleList:
    pts = t.reshpae(-1,2).astype(np.int32)
    if (pts<0).sum() or (pts[:0]>w).sum() or (pts[:,1]>h).sum():
        continue
    cv2.polylines(img, [pts], True, (255.255,255), 1, cv2.LINE_AA)
cv2.imshow(winname="img", mat=img)
cv2.waitKey()
