from mpl_toolkits.mplot3d import axes3d
import numpy as np
import cv2 as cv
import IM
from matplotlib import pyplot as plt

def Contornos(img):

    plt.imshow (img)
    plt.title("Imagen a Analizar")
    plt.show()

    fig, ax = plt.subplots()
    plt.hist(img.ravel(),256,[0,256]);
    plt.title("Histograma de la imagen")
    ax.set_xlabel("N° Pixel")
    ax.set_ylabel("Pixel Value")
    plt.show ()

    assert img is not None, "file could not be read, check with os.path.exists()"
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #ret, thresh = cv.threshold(gray,60,255,cv.THRESH_BINARY_INV) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    #ret, thresh = cv.threshold(gray,100,255,cv.THRESH_TOZERO) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    ret, thresh = cv.threshold(gray,150,255,cv.THRESH_OTSU) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    #ret, thresh = cv.threshold(gray,100,255,cv.THRESH_TRIANGLE) #0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)##

    plt.imshow(gray,cmap = "gray")
    plt.title("Imagen en escala de grises")
    plt.show() 

    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 3)

    #plt.imshow(opening,cmap = "gray")
    #plt.title("Reducción de Ruido con tratamiento Morfologico")
    #plt.show() 

    # sure background area
    sure_bg = cv.dilate(opening,kernel,iterations=3)

    #plt.imshow(sure_bg,cmap = "gray")
    #plt.title("sure_bg Dilatación para asegurar el Background")
    #plt.show() 

    edged= cv.Canny(gray,30,200)
    contornos, jerarquia = cv.findContours(sure_bg,cv.RETR_CCOMP,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img,contornos,-1,(255,255,255),2) 
    mask = np.zeros(img.shape, dtype=np.uint8)

    for contour in contornos:
        area = cv.contourArea(contour)
        area_min = 10000  # Área mínima del objeto deseado 
        if area_min <= area:
            cv.drawContours(mask, [contour], 0, (255,255,255), -1)

    result = cv.bitwise_and(img, mask)

    plt.imshow(mask)
    plt.title("Máscara del objeto")
    plt.show()

    plt.imshow(result)
    plt.title("Objeto Aislado")
    plt.show()
    return result



