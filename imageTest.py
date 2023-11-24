
import cv2
import random
#print("Hello World!")

img = cv2.imread("assets/beaker.jpg", cv2.IMREAD_ANYCOLOR)
#print(img[250][400])
#print(img)

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


#print("TEST:")
#print(random.randint(0, 255))

section = img[300:500, 300:500]

print("section:")
print(section.shape)
print("img:")
print(img.shape)

img[100:300, 650:850] = section

cv2.imshow("ThaBeaker", section)
cv2.waitKey(0)
cv2.imshow("ThaBeaker", img)

cv2.waitKey(0)
cv2.destroyAllWindows


