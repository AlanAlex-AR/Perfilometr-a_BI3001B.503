from mpl_toolkits.mplot3d import axes3d
import numpy as np
import cv2 as cv
import IM
from matplotlib import pyplot as plt


# Obtener las dimensiones de la imagen
def 
    alto,ancho = np.shape(gray)
    alto1=alto*0.039
    ancho1=ancho*0.04
    gray1=gray*0.2

    # Crear una cuadrícula de coordenadas para el objeto 3D
    x = np.linspace(0, ancho1 - 1, ancho, )
    y = np.linspace(0, alto1 - 1, alto,)
    X, Y = np.meshgrid(x, y)

    # Obtener la altura de cada píxel / 
    altura = gray1 - 10

    # Crear la figura y los ejes 3D
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')

    # Graficar el objeto 3D
    #ax.plot_surface(X, Y, altura, cmap='gray', linewidth=0)

    # Configurar los límites de los ejes
    #ax.set_xlim([0, ancho1 - 1])
    #ax.set_ylim([0, alto1 - 1])
    #ax.set_zlim([0, 255*0.25])  # Intervalo de intensidad, ajusta según tus necesidades
    #ax.set_xlabel("Eje x (mm)")
    #ax.set_ylabel("Eje y (mm)")
    #ax.set_zlabel("Eje z (mm)")

    # Mostrar el gráfico
    #plt.show()
