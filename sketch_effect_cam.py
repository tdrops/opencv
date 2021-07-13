import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    if ret:
        img2, img3 = cv2.pencilSketch(src=img)
        img2 = cv2.cvtColor(src=img2, code=cv2.COLOR_GRAY2BGR)
        img4 = cv2.stylization(src=img)
        img5 = cv2.detailEnhance(src=img)
        img6 = cv2.edgePreservingFilter(src=img)

        cv2.imshow(winname="sketch effect", mat=np.vstack((np.hstack((img,img2,img3)),np.hstack((img4,img5,img6)))))
        if cv2.waitKey(1) & 0xff == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
