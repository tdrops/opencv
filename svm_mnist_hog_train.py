"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

숫자 기울기를 바로잡고 HOG 로 읽고 SVM으로 훈련하여 손으로 쓴 숫자 인식
"""
import cv2
import numpy as np
import mnist
import time


affine_flag = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR

def deskew(img):
    m = cv2.moments(array=img)
    if abs(m["mu02"]) < 1e-2:
        return img.copy()
    skew = m["mu11"]/m["mu02"]
    M = np.float32([[1, skew, -0.5*20*skew], [0,1,0]])
    img = cv2.warpAffine(src=img, M=M, dsize=(20,20), flags=affine_flag)
    return img


winSize = (20,20)
blockSize = (10,10)
blockStride = (5,5)
cellSize = (5,5)
nbins = 9
hogDesc = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins)

if __name__ == "__main__":
    train_data, train_label = mnist.getTrain(reshape=False)
    test_data, test_label = mnist.getTest(reshape=False)

    deskewed = [list(map(deskew, row)) for row in train_data]
    hogdata = [list(map(hogDesc.compute, row)) for row in deskewed]

    train_data = np.float32(hogdata)

    train_data = train_data.reshape(-1, train_data.shape[2])

    svm = cv2.ml.SVM_create()
    startT = time.time()
    svm.trainAuto(train_data, cv2.ml.ROW_SAMPLE, train_label)
    endT = time.time()-startT
    print(f"{endT}초 소요")
    svm.save("./svm_mnist.xml")

    deskewed = [list(map(deskew, row)) for row in test_data]
    hogdata = [list(map(hogDesc.compute, row)) for row in deskewed]

    test_data = np.float32(hogdata)

    test_data = test_data.reshape(-1, test_data.shape[2])

    ret, result = svm.predict(test_data)

    correct = (result == test_label).sum()
    print(correct*100.0/result.size)
