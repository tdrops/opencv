"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 4-29] 컬러 이미지에 대한 이퀄라이즈 적용
"""
import cv2
import numpy as np

img = cv2.imread(filename="../img/yate.jpg")
img_yuv = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2YUV)

# img_yuv[:,:,0] = cv2.equalizeHist(src=img_yuv[:,:,0])
img_yuv[:, :, 0] = cv2.equalizeHist(src=img_yuv[:, :, 0])

img2 = cv2.cvtColor(src=img_yuv, code=cv2.COLOR_YUV2BGR)

cv2.imshow(winname="img:img2", mat=np.hstack((img, img2)))
cv2.waitKey()
cv2.destroyAllWindows()
