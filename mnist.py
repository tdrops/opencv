"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-3] MNIST 손글씨 숫자 이미지셋 공통 모듈
"""
import cv2
import numpy as np

data = None
k = list(range(10))


def load():
    global data

    image = cv2.imread(filename="../img/digits.png")
    gray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)

    cells = [np.hsplit(ary=row, indices_or_sections=100) for row in np.vsplit(ary=gray, indices_or_sections=50)]
    data = np.array(cells)


def getData(reshape=True):
    if data is None:
        load()

    if reshape:
        full = data.reshape(-1, 400).astype(np.float32)
    else:
        full = data

    labels = np.repeat(a=k, repeats=500).reshape(-1, 1)
    return full, labels


def getTrain(reshape=True):
    if data is None:
        load()

    train = data[:, :90]

    if reshape:
        train = train.reshape(-1, 400).astype(np.float32)

    train_labels = np.repeat(a=k, repeats=450).reshape(-1, 1)

    return train, train_labels


def getTest(reshape=True):
    if data is None:
        load()

    test = data[:, 90:100]

    if reshape:
        test = test.reshape(-1, 400).astype(np.float32)

    test_labels = np.repeat(a=k, repeats=50).reshape(-1, 1)

    return test, test_labels


def digit2data(src, reshape=True):
    h, w = src.shape[:2]

    square = src

    if h > w:
        pad = (h - w) // 2
        square = np.zeros(shape=(h, h), dtype=np.uint8)
        square[:, pad:pad + w] = src
    elif h < w:
        pad = (w - h) // 2
        square = np.zeros(shape=(w, w), dtype=np.uint8)
        square[pad:pad + h, :] = src

    px20 = np.zeros(shape=(20, 20), dtype=np.uint8)
    px20[2:18, 2:18] = cv2.resize(src=square, dsize=(16, 16), interpolation=cv2.INTER_AREA)
    if reshape:
        px20 = px20.reshape((1, 400)).astype(np.float32)
    return px20
