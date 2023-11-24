import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#hsv - hue/saturation/brightness

    #BGR_color = np.array([[[255,0,0]]])
    #cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    cv2.imshow("ThaBeaker", img)

    if cv2.waitKey(1)  == ord('q'):
        break


cap.release()
cv2.destroyAllWindows

