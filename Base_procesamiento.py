# Autor: Fabian

### Descripcion 
    # Generar el analisis de perfilometria de una imagen superficial y lateral de un material sobre un objeto

# Componentes requeridos 
#Inicio del programa 
# Importar librerias de matplotlib 
# Importar liberiras de OpenCV 

import os
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
import Rugosidades
import PP_prueba

def process(self):
    #Lectura de la imagen superior
    No=3   #Numero de imagen de la carpeta 
    img = IM.lectura(No)    
    Noo=0  #Numero de la imagen de referencia en la carpeta
    Ref= IM.lectura(Noo)
    Area=2500  #Area del objeto a analizar en mm^2


    #Aislamiento del objeto principal (Cerebro)
    Ais= Cont.Contornos(img)

    #Aislamiento de objeto secundario (Objetivo a analizar)
    T=130
    Objetivo1= WS.Water_shed(img, img, Ais,T)
    Parcial= cv.cvtColor(Ais,cv.COLOR_BGR2GRAY)
    #Obtener 2 treshold
    ret, PP = cv.threshold(Parcial, 0,255,cv.THRESH_TOZERO+cv.THRESH_OTSU) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    print(ret)
    ret= ret*2.0

    #Objetivo secundario aislado
    Final= WS.Water_shed(img, img, Objetivo1,ret)


    #Redimension de la imagen / Grafico 3D / Metrica 
    R1= Graph.Graph(Final)

    #Cerebro referencia
    #print(np.shape(Final))
    Sec= cv.bitwise_and(Ref,Final)
    #plt.imshow(Sec)
    #plt.show
    N1= Graph.Graph(Sec)

    # Metricas de comparativa 
    IND = np.argwhere(Final > 0)
    R2=Metrica.Met(R1,N1,IND, Final, Sec, Area)


    # Nombre de la carpeta
    nombre_carpeta = 'Resultados'

    # Crear la carpeta
    os.makedirs(nombre_carpeta, exist_ok=True)

    # Ruta y nombre de la imagen1
    ruta_imagen1= os.path.join(nombre_carpeta, 'analisis1F.jpg')

    # Ruta y nombre de la imagen2
    ruta_imagen2= os.path.join(nombre_carpeta, 'analisis2F.jpg')

    self.R1= cv.applyColorMap(R1, cv.COLORMAP_JET)
    self.R2= R2*255

    cv.imwrite(ruta_imagen1, R1)
    cv.imwrite(ruta_imagen2, R2)




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