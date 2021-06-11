import cv2
import numpy as np
import matplotlib.pylab as plt


cap = cv2.VideoCapture(0)
if cap:
    if cap.isOpened():
        while True:
            ret, img = cap.read()
            h,w = img.shape[:2]
            print(f"h:{h} w:{w}")
            if ret:
                img2 = img.copy()

                cv2.remap(src=img2[:,:w//2],map1=-map1)


                cv2.imshow(winname="video", mat=np.hstack([img, img2]))
            else:
                break
            if cv2.waitKey(1) != -1:
                break
    else:
        print(f"video open error")
else:
    print(f"video open error")

cap.release()
