import cv2
import matplotlib.pyplot as plt
image = cv2.imread('IMG_3772.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

plt.imshow(gray)
plt.show ()