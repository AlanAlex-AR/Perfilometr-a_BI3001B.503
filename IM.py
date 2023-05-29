import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

def lectura(I):
    count=0
    Input_carpeta= "C:/Users/fabia/Downloads/Procesamiento de imagenes\Perfilometr-a_BI3001B.503/Protocolo"
    Names= os.listdir(Input_carpeta)
    if type(I)==str:
        for N in Names:
            if I==N.split(".")[0]: I=count
            count+=1

    image_path= Input_carpeta + "/" + Names[I]
    IMG= cv.imread(image_path)
    assert IMG is not None, "file could not be read, check with os.path.exists()"
    return IMG