import numpy as np
import cv2 as cv
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt

def Met(Obj,Ref):
    Comparativo= Ref-Obj
    plt.imshow(Comparativo)
    plt.show()
    
    Comparativo[Comparativo > 0] = 1
    plt.imshow(Comparativo)
    plt.show()
    

    