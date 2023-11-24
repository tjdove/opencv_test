
import cv2

#print("Hello World!")

img = cv2.imread("assets/beaker.jpg", cv2.IMREAD_COLOR)

#Resize
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

#rotate 
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("assets/beaker2.jpg", img)

cv2.imshow("ThaBeaker", img)
cv2.waitKey(0)
cv2.destroyAllWindows
