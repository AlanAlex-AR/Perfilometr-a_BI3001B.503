import numpy as np
import cv2 as cv
from mpl_toolkits.mplot3d import axes3d
import IM
import Contornos_redimension as Cont
from matplotlib import pyplot as plt
import Water_Shed as WS

#Lectura de la imagen 
No=32
img = IM.lectura(No)


#Aislamiento del objeto principal 
Ais= Cont.Contornos(img)

#Aislamiento de objeto secundario (si aplica)
Objetivo= WS.Water_shed(img, img, Ais)

#Redimensión de la imagen / Gráfico 3D / Métrica 

