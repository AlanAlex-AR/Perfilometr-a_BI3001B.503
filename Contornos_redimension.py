from mpl_toolkits.mplot3d import axes3d
import numpy as np
import cv2 as cv
import IM
from matplotlib import pyplot as plt



I=32
img = IM.lectura(I)
#img=cv.imread("b.JPG")

plt.imshow(img)
#plt.show()

assert img is not None, "file could not be read, check with os.path.exists()"
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#ret, thresh = cv.threshold(gray,60,255,cv.THRESH_BINARY_INV) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
#ret, thresh = cv.threshold(gray,100,255,cv.THRESH_TOZERO) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
ret, thresh = cv.threshold(gray,150,255,cv.THRESH_OTSU) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
#ret, thresh = cv.threshold(gray,100,255,cv.THRESH_TRIANGLE) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)##

# Obtener las dimensiones de la imagen
alto,ancho = np.shape(gray)
alto1=alto*0.039
ancho1=ancho*0.04
gray1=gray*0.2

# Crear una cuadrícula de coordenadas para el objeto 3D
x = np.linspace(0, ancho1 - 1, ancho, )
y = np.linspace(0, alto1 - 1, alto,)
X, Y = np.meshgrid(x, y)

# Obtener la altura de cada píxel / 
altura = gray1 - 5

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar el objeto 3D
ax.plot_surface(X, Y, altura, cmap='gray', linewidth=0)

# Configurar los límites de los ejes
ax.set_xlim([0, ancho1 - 1])
ax.set_ylim([0, alto1 - 1])
ax.set_zlim([0, 255*0.25])  # Intervalo de intensidad, ajusta según tus necesidades
ax.set_xlabel("Eje x (mm)")
ax.set_ylabel("Eje y (mm)")
ax.set_zlabel("Eje z (mm)")

# Mostrar el gráfico
plt.show()





# fake data

plt.imshow(gray,cmap = "gray")
plt.title("Imagen en escala de grises")
plt.show() 

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
H= cv.drawContours(img,contornos[1],-1,(0,0,255),2) 
print(H)
plt.show ()


