import numpy as np
import cv2 as cv
from mpl_toolkits.mplot3d import axes3d
import IM
import Contornos_redimension as Cont
from matplotlib import pyplot as plt
import Water_Shed as WS
import Graph 

#Lectura de la imagen 
No=31
img = IM.lectura(No)
Noo=0
Ref= IM.lectura(Noo)


#Aislamiento del objeto principal 
Ais= Cont.Contornos(img)

#Aislamiento de objeto secundario (si aplica)
T=160   
Objetivo1= WS.Water_shed(img, img, Ais,T)
T=209    #185,208,220
Objetivo= WS.Water_shed(img, img, Objetivo1,T)
Final= cv.bitwise_and(img,Objetivo)
plt.imshow(Final)
plt.title("Objetivo Aislado")
plt.show()

#Redimensión de la imagen / Gráfico 3D / Métrica 
Graph.Graph(Final)

#Cerebro referencia
print(np.shape(Objetivo))
Sec= cv.bitwise_and(Ref,Objetivo)
plt.imshow(Sec)
plt.show
Graph.Graph(Sec)


