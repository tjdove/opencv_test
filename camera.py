import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out_image = np.zeros(frame.shape,np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    out_image [:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    out_image [height//2:, :width//2] = smaller_frame
    out_image [:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    out_image [height//2:, width//2:] = smaller_frame

    cv2.imshow("ThaBeaker", out_image)

    if cv2.waitKey(1)  == ord('q'):
        break


cap.release()




#print(ret)
#print(frame.shape)

#cv2.imshow("ThaBeaker", frame)
#cv2.waitKey(0)
cv2.destroyAllWindows
