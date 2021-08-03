"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 9-14] BOW-SVM 으로 비행기와 모터사이클 인식
"""
import cv2
import numpy as np

categories = ['airplanes', 'Motorbikes']
dict_file = "./plane_bike_train.npy"
svm_model_file = "./plane_bike_svm.xml"

imgs = ['../img/aircraft.jpg','../img/jetstar.jpg', '../img/motorcycle.jpg', '../img/motorbike.jpg']

detector = cv2.xfeatures2d.SIFT_create()

bowextractor = cv2.BOWImgDescriptorExtractor(detector, cv2.BFMatcher(cv2.NORM_L2))
bowextractor.setVocabulary(np.load(dict_file))

svm = cv2.ml.SVM_load(svm_model_file)

for i, path in enumerate(imgs):
    img = cv2.imread(filename=path)
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    hist = bowextractor.compute(image=gray, keypoints=detector.detect(gray))

    ret, result = svm.predict(hist)

    name = categories[int(result[0][0])]
    txt, base = cv2.getTextSize(text=name, fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, thickness=3)
    x,y = 10, 50
    cv2.rectangle(img=img, pt1=(x,y-base-txt[1]), pt2=(x+txt[0],y+txt[1]), color=(30,30,30), thickness=-1)
    cv2.putText(img=img, text=name, org=(x,y), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow(path, img)

cv2.waitKey(delay=0)
cv2.destroyAllWindows()
