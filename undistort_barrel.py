"""
opencv

출처

제목: 파이썬으로 만드는 OpenCV 프로젝트
저자: 이세우
출판: 프로그래밍인사이트
"""
"""
요약

[예제 5-14 방사 왜곡 효과]
"""
import cv2
import numpy as np

img = np.full(shape=(300,400,3), fill_value=255, dtype=np.uint8)
img[::10,:,:] = 0
img[:,::10,:] = 0
height,width = img.shape[:2]

# k1,k2,p1,p2 = 0.001,0,0,0
k1,k2,p1,p2 = -0.0005,0,0,0
disCoeff = np.float32([k1,k2,p1,p2])

fx,fy = 10,10
cx,cy = width/2, height/2
camMtx = np.float32([[fx,0,cx],[0,fy,cy],[0,0,1]])

dst = cv2.undistort(src=img, cameraMatrix=camMtx, distCoeffs=disCoeff)

cv2.imshow(winname="original", mat=img)
cv2.imshow(winname="dst", mat=dst)
cv2.waitKey()
cv2.destroyAllWindows()
