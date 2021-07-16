"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 8-2] 사물 영상 중에서 권총 영상 찾기
"""
import cv2
import numpy as np
import glob

img = cv2.imread(filename="../img/pistol.jpg")
cv2.imshow(winname="query", mat=img)

search_dir = "../img/101_ObjectCategories"


def img2hash(img):
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(src=gray, dsize=(16, 16))
    avg = gray.mean()
    bi = 1 * (gray > avg)
    return bi


def hamming_distance(a, b):
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    distance = (a != b).sum()
    return distance


query_hash = img2hash(img=img)

img_path = glob.glob(search_dir + "/**/*.jpg")

for path in img_path:
    img = cv2.imread(filename=path)
    cv2.imshow(winname="searching...", mat=img)
    cv2.waitKey(1)
    a_hash = img2hash(img=img)
    dst = hamming_distance(a=query_hash, b=a_hash)
    if dst / 256 < 0.25:
        print(path, dst / 256)
        cv2.imshow(winname=path, mat=img)

cv2.destroyWindow(winname="searching...")
cv2.waitKey()
cv2.destroyAllWindows()
