import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def Water_shed(img,MM,Ais,T):
    Ais= cv.cvtColor(Ais,cv.COLOR_BGR2GRAY)
    #plt.imshow(Ais, cmap="gray")
    #plt.show()
    ret, Ais = cv.threshold(Ais, T,255,cv.THRESH_BINARY) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    #plt.imshow(Ais, cmap="gray")
    #plt.title("Binarización")
    #plt.show()
    kernel = np.ones((3,3),np.uint8)
    Ais = cv.morphologyEx(Ais,cv.MORPH_OPEN,kernel, iterations = 3)
    AiS = cv.erode(Ais,kernel,iterations=3)

    # Finding sure foreground area
    dist_transform = cv.distanceTransform(Ais,cv.DIST_L2,5)
    ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    #plt.imshow(dist_transform,cmap = "gray")
    #plt.title("Trasformación de distancia") # calcula la distancia de cada píxel en una imagen a la región de fondo más cercana,# asigna a cada píxel un valor que representa la distancia euclidiana entre ese píxel y la región de fondo
    #plt.show() 


    #plt.imshow(sure_fg,cmap = "gray")
    #plt.title("sure_fg binarización Asegurado la región de interes")
    #plt.show() 

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(Ais,sure_fg)# Marker labelling
    ret, markers = cv.connectedComponents(sure_fg)

    #plt.imshow(unknown,cmap = "gray")
    #plt.title("unknown resta de sure_bg y sure_fg")
    #plt.show() 

    #plt.imshow(markers,cmap = "gray")
    #plt.title("markers connect componnents sure_fg")
    #plt.show() 

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1

    #plt.imshow(markers,cmap = "gray")
    #plt.title("markers plus 1 ")
    #plt.show() 

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    #plt.imshow(markers,cmap = "gray")
    #plt.title("markers with unkown == 255 is 0 ")
    #plt.show() 
    markers = cv.watershed(img,markers)

    #plt.imshow(markers,cmap = "gray")
    #plt.title("markers watershed ")
    #plt.show() 

    img[markers == 1] = [0,0,0]

    #plt.imshow(img,cmap = "gray")
    #plt.title("Objetivo Aislado")
    #plt.show() 
    

    return img






