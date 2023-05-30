from mpl_toolkits.mplot3d import axes3d
import numpy as np
import cv2 as cv
import IM
from matplotlib import pyplot as plt



img=cv.imread("b.JPG")


plt.imshow(img)
#plt.show()



assert img is not None, "file could not be read, check with os.path.exists()"
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#ret, thresh = cv.threshold(gray,60,255,cv.THRESH_BINARY_INV) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
#ret, thresh = cv.threshold(gray,100,255,cv.THRESH_TOZERO) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
ret, thresh = cv.threshold(gray,150,255,cv.THRESH_OTSU) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
#ret, thresh = cv.threshold(gray,100,255,cv.THRESH_TRIANGLE) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)##
print(np.shape(gray))
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.plot(gray)
plt.show()

"""""
plt.imshow(gray,cmap = "gray")
#plt.show() 

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 3)

plt.imshow(opening,cmap = "gray")
plt.title("Reducción de Ruido con tratamiento Morfologico")
#plt.show() 

# sure background area
sure_bg = cv.dilate(opening,kernel,iterations=3)

plt.imshow(sure_bg,cmap = "gray")
plt.title("sure_bg Dilatación para asegurar el Background")
#plt.show() 

edged= cv.Canny(gray,30,200)
contornos, jerarquia = cv.findContours(edged,cv.RETR_CCOMP,cv.CHAIN_APPROX_SIMPLE)
#print(contornos)
cv.drawContours(img,contornos[1],-1,(0,0,255),2) 
cv.imshow('Contours',img)
cv.waitKey(0)
cv.destroyAllWindows()

"""
