import numpy as np
import cv2 as cv
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt

def Met(Obj,Ref,Ind):
    #Comparativo= Ref-Obj
    #plt.imshow(Comparativo)
    #plt.show()
    print(np.shape(Ind))
    Comparativo = np.zeros_like(Obj)
    # Convertir la imagen de vuelta a tipo entero
    #Comparativo = Comparativo.astype(np.uint8)

    Comparativo[Ref <= Obj] = 0
    Comparativo[Ref > Obj] = 1
    
    #print(min(Comparativo))
    #print(max(Comparativo))
    seccion_comparacion = Comparativo[Ind[:, 0], Ind[:, 1]]
    porcentaje = (np.sum(seccion_comparacion > 0) / len(Ind)) * 100
    print(porcentaje)

    plt.imshow(Comparativo, cmap='gray')
    plt.title("Puntos de contacto")
    plt.show()

    

    