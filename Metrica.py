import numpy as np
import cv2 as cv
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt


def Met(Obj,Ref,Ind,OBJ,REF,Area):
    #Comparativo= Ref-Obj
    #plt.imshow(Comparativo)
    #plt.show()
    Reales_Falsos=0
    Falsos_positivos=0
    real=np.count_nonzero(Obj > 0)
    Total=np.size(Obj)
    print(real)
    Medidas_pixel= 282 #Pixeles por mm
    Medida_total= (Area*Medidas_pixel)
    Falso=Total-Medida_total
    if real<Medida_total:
        Falsos_positivos= Medida_total-real
        print("Falsos positivos", Falsos_positivos)
    else:
        Reales_Falso= real-Medida_total
        print("Positivos falso", Reales_Falso)
    
    
   

    mean, std_dev = cv.meanStdDev(Obj)
    Obj[Obj< std_dev] = 0
    Ajuste= np.round(std_dev*2)
    #Obj[Obj> std_dev]-= (std_dev*2)
    mask = np.where(Obj, 1, 0)
    Obj= Obj-(Ajuste * mask)
    
    print("Ref", std_dev)
    #print(np.shape(Ind))
    Comparativo = np.zeros_like(Obj)
    # Convertir la imagen de vuelta a tipo entero
    # Comparativo = Comparativo.astype(np.uint8)

    Comparativo[Ref <= Obj] = 0
    Comparativo[Ref > Obj]  = 1
    
    #print(min(Comparativo))
    #print(max(Comparativo))
    seccion_comparacion = Comparativo[Ind[:, 0], Ind[:, 1]]
    porcentaje = (np.sum(seccion_comparacion > 0) / len(Ind)) * 100
    print("Estimación de superficie de contacto", porcentaje)

    #Otras métricas
    correlation_matrix = np.corrcoef(Ref, Obj)
    correlation = correlation_matrix[0, 1]
    print("Coeficiente de correlación de pearson", correlation)
    print(np.shape(seccion_comparacion))
    absolute_diff = np.abs(Ref - Obj)
    mad = np.mean(absolute_diff)
    print ("Mad", mad)

    mse = np.mean((Ref - Obj) ** 2)
    rmse = np.sqrt(mse)
    print ("RMSE", rmse)

    plt.imshow(Comparativo, cmap='gray')
    plt.title("Estimación de los puntos de contacto")
    plt.show()
    return Obj

    

    