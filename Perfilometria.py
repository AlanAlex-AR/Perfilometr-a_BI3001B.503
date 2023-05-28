import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#plt.imshow(thresh,cmap = "gray")
#plt.show() 

<<<<<<< HEAD
img = cv.imread('IMG_3839.jpg')

"""plt. imshow(img)
plt.show()

fig, ax = plt.subplots()
plt.hist(img.ravel(),256,[0,256]);
plt.title("Histograma de la imagen")
ax.set_xlabel("N° Pixel")
ax.set_ylabel("Pixel Value")
plt.show ()"""""

=======
img = cv.imread('IMG_55mm_s_p .jpg')
plt.imshow(img)
plt.show ()
>>>>>>> c08aa8c750dc89169a57bcd9ab71196931555d8d
assert img is not None, "file could not be read, check with os.path.exists()"
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#ret, thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
#ret, thresh = cv.threshold(gray,100,255,cv.THRESH_TOZERO) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
#ret, thresh = cv.threshold(gray,100,255,cv.THRESH_OTSU) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
ret, thresh = cv.threshold(gray,100,255,cv.THRESH_TRIANGLE) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)##


#plt.imshow(thresh,cmap = "gray")
#plt.show() 

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 3)

plt.imshow(opening,cmap = "gray")
plt.title("Reducción de Ruido con tratamiento Morfologico")
plt.show() 

# sure background area
sure_bg = cv.dilate(opening,kernel,iterations=3)

plt.imshow(sure_bg,cmap = "gray")
plt.title("sure_bg Dilatación para asegurar el Background")
plt.show() 

# Finding sure foreground area
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

plt.imshow(dist_transform,cmap = "gray")
plt.title("Trasformación de distancia") # calcula la distancia de cada píxel en una imagen a la región de fondo más cercana,# asigna a cada píxel un valor que representa la distancia euclidiana entre ese píxel y la región de fondo
plt.show() 


plt.imshow(sure_fg,cmap = "gray")
plt.title("sure_fg binarización Asegurado la región de interes")
plt.show() 

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)

plt.imshow(unknown,cmap = "gray")
plt.title("unknown resta de sure_bg y sure_fg")
plt.show() 

plt.imshow(markers,cmap = "gray")
plt.title("markers connect componnents sure_fg")
plt.show() 

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

plt.imshow(markers,cmap = "gray")
plt.title("markers plus 1 ")
plt.show() 
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

plt.imshow(markers,cmap = "gray")
plt.title("markers with unkown == 255 is 0 ")
plt.show() 
markers = cv.watershed(img,markers)

plt.imshow(markers,cmap = "gray")
plt.title("markers watershed ")
plt.show() 
img[markers == -1] = [255,0,0]

plt.imshow(img)
plt.title("outline")
plt.show()



