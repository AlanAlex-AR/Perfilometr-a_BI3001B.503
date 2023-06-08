import numpy as np
import cv2 as cv
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt

def patterns(img1, img2,Ind):
    # Calcular la diferencia absoluta entre las imágenes
    print(np.shape(img1))
    Sec= img1[Ind[:, 0], Ind[:, 1]]
    diff = np.abs(img1 - img2)
    print(np.shape(Sec))
    

    # Aplicar umbralización para resaltar las diferencias
    threshold = 20  # Ajustar el umbral según sea necesario
    _, binary_diff = cv.threshold(diff, threshold, 255, cv.THRESH_BINARY)

    # Calcular el porcentaje de píxeles diferentes
    total_pixels = np.size(Sec)
    different_pixels = np.count_nonzero(binary_diff [Ind[:, 0], Ind[:, 1]])
    percentage_different = (different_pixels / total_pixels) * 100

    print("Porcentaje de píxeles diferentes:", percentage_different)
    # Asegurarse de que los valores estén en el rango correcto [0, 255]
    binary_diff = np.clip(binary_diff, 0, 255)

    # Convertir la imagen de vuelta a tipo entero
    binary_diff = binary_diff.astype(np.uint8)

    plt.imshow(binary_diff, cmap='gray')
    plt.show()
