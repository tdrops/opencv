"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

digits.png 를 읽어 들이고 이미지를 20X20으로 변경하는 함수
"""
import cv2
import numpy as np

data = None
k = list(range(10))


def load():
    global data
    image = cv2.imread(filename="./img/digits.png")
    gray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
    return np.array(cells)


def getData(reshape=True):
    if data is None:
        load()
    if reshape:
        full = data.reshape(-1, 400).astype(np.float32)
    else:
        full = data

    labels = np.repeat(k, 500).reshape(-1, 1)
    return (full, labels)


def getTrain(reshape=True):
    if data is None:
        load()
    train = data[:, :90]
    if reshape:
        train.reshape(-1, 400).astype(np.float32)

    train_labels = np.repeat(k, 450).reshape(-1, 1)
    return (train, train_labels)


def getTest(reshape=True):
    if data is None:
        load()
    test = data[:, 90:100]
    if reshape:
        test.reshpae(-1, 400).astype(np.float32)

    test_labels = np.repeat(k, 50).reshape(-1, 1)
    return (test, test_labels)


def digit2data(src, reshape=True):
    h, w = src.shape[:2]
    if h == w:
        square = src
    elif h > w:
        pad = (h - w) // 2
        square = np.zeros(shape=(h, h), dtype=np.uint8)
        square[:, pad:pad + w] = src
    elif h < w:
        pad = (w - h) // 2
        square = np.zeros(w, w, dtype=np.uint8)
        square[pad:pad + h, :] = src

    px20 = np.zeros(shape=(20, 20), dtype=np.uint8)
    px20[2:2 + 16, 2:2 + 16] = square.resize(new_shape=(16, 16))
    if reshape:
        px20 = px20.reshape(shape=(1, 400)).astype(np.float32)
    return px20
