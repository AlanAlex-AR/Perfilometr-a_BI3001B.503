import cv2
import numpy as np
import matplotlib.pyplot as plt
import IM

# Cargar las dos imágenes en escala de grises

No=32
image1 = IM.lectura(No)
Noo=0
image2= IM.lectura(Noo)
imgae1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
imgae2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)


# Normalizar las intensidades en el rango [0, 1]
image1_norm = image1.astype(float) / 255.0
image2_norm = image2.astype(float) / 255.0

# Crear el mapa de altura de cada imagen
height_map1 = image1_norm * 255.0
height_map2 = image2_norm * 255.0

# Comparar los mapas de altura visualmente
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(height_map1, cmap='gray')
axs[0].set_title('Imagen 1')
axs[0].axis('off')

axs[1].imshow(height_map2, cmap='gray')
axs[1].set_title('Imagen 2')
axs[1].axis('off')

plt.show()
