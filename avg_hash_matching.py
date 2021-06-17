"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

hash로 찾기
"""
import glob

import cv2
import numpy as np


img = cv2.imread(filename="./img/pistol.jpg")


def img2hash(path):
    img = cv2.imread(filename=path)
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(src=gray, dsize=(16,16))
    avg = gray.mean()
    return 1*(gray > avg)


def match(a, b):
    a = a.reshape(1,-1)
    b = b.reshape(1,-1)
    return (a != b).sum()/256


hash1 = img2hash("./img/pistol.jpg")


paths = glob.glob(pathname="./img/101_ObjectCategories/revolver/*.jpg", recursive=True)

for path in paths:
    hash2 = img2hash(path=path)
    mat = match(a=hash1, b=hash2)
    if mat <= 0.25:
        img = cv2.imread(filename=path)
        cv2.putText(img=img, text=f"{mat}", org=(0,0), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0,255,0), thickness=1)
        cv2.imshow(winname=f"{mat}", mat=img)
        cv2.waitKey(1000)
    else:
        print("searching...")

print("finish")

cv2.waitKey()
cv2.destroyAllWindows()
