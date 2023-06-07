import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def rugo(img,ref):
    # Calcular la matriz de co-ocurrencia de niveles de gris para ambas imágenes
    img= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ref= cv.cvtColor(ref,cv.COLOR_BGR2GRAY)

    laplacian1 = cv.Laplacian(ref, cv.CV_64F)
    laplacian2 = cv.Laplacian(img, cv.CV_64F)

    # Normalizar los valores de los operadores Laplacianos a un rango de 0 a 255
    laplacian1_normalized = cv.normalize(laplacian1, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    laplacian2_normalized = cv.normalize(laplacian2, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

    # Calcular la diferencia absoluta entre los mapas de rugosidades
    diferencia_rugosidades = cv.absdiff(laplacian1_normalized, laplacian2_normalized)

    # Aplicar umbralización para identificar las diferencias significativas en rugosidades
    umbral = 50  # Umbral para la detección de diferencias significativas en rugosidades
    diferencias_significativas = np.where(diferencia_rugosidades > umbral, 255, 0).astype(np.uint8)
    L1 = np.where(laplacian1_normalized > umbral, 255, 0).astype(np.uint8)
    L2 = np.where(laplacian2_normalized > umbral, 255, 0).astype(np.uint8)

    cv.imshow('Diferencias en Rugosidades', diferencias_significativas)


