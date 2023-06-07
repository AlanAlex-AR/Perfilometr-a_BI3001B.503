import numpy as np
import cv2 as cv
from mpl_toolkits.mplot3d import axes3d
import IM
import Contornos_redimension as Cont
import Contorno_lateral as C_lateral
from matplotlib import pyplot as plt
import Water_Shed as WS
import Graph 
import Metrica

#Lectura de la imagen superior
No=21
img = IM.lectura(No)
Noo=0
Ref= IM.lectura(Noo)


#Aislamiento del objeto principal 
Ais= Cont.Contornos(img)

#Aislamiento de objeto secundario (si aplica)  
T=100
Objetivo1= WS.Water_shed(img, img, Ais,T)
Parcial= cv.cvtColor(Ais,cv.COLOR_BGR2GRAY)
#Obtener 2 treshold
ret, PP = cv.threshold(Parcial, 0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
print(ret)
ret= ret*1.98
#T=209    #185,208,220
Final= WS.Water_shed(img, img, Objetivo1,ret)
#Final,tre= cv.bitwise_and(img,Objetivo)
plt.imshow(Final)
plt.title("Objetivo Aislado")
plt.show()

#Redimensión de la imagen / Gráfico 3D / Métrica 
N0= Graph.Graph(Final)

#Cerebro referencia
print(np.shape(Final))
Sec= cv.bitwise_and(Ref,Final)
plt.imshow(Sec)
plt.show
N1= Graph.Graph(Sec)

#Métrica

IND = np.argwhere(Final > 0)
Metrica.Met(N0,N1,IND)
"""""
#Lectura de la imagen lateral 
No=12
img = IM.lectura(No)
Noo=0
Ref= IM.lectura(Noo)

#Aislamiento del objeto principal 
Ais= C_lateral.Contornos(img)

#Aislamiento de objeto secundario (si aplica)  
T=100
Objetivo1= WS.Water_shed(img, img, Ais,T)
Parcial= cv.cvtColor(Ais,cv.COLOR_BGR2GRAY)
#Obtener 2 treshold
ret, PP = cv.threshold(Parcial, 0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
ret= ret*2.7
print(ret)
Final= WS.Water_shed(img, img, Objetivo1,ret)
#Final,tre= cv.bitwise_and(img,Objetivo)
plt.imshow(Final)
plt.title("Objetivo Aislado")
plt.show()
"""""