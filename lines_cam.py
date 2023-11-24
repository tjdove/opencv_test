import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0,0 ), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255,0 ), 5)
    img = cv2.rectangle(img, (100,100), (200, 200), (128, 128, 128), 4)
    img = cv2.circle(img, (300,300), 60, (255, 0, 0), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Hello World', (200,height-10), font, 2,(0,0,0), 2, cv2.LINE_AA)


    #out_image = np.zeros(frame.shape,np.uint8)
    #smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    cv2.imshow("ThaBeaker", img)

    if cv2.waitKey(1)  == ord('q'):
        break


cap.release()




#print(ret)
#print(frame.shape)

#cv2.imshow("ThaBeaker", frame)
#cv2.waitKey(0)
cv2.destroyAllWindows
