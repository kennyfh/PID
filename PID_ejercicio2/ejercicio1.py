import cv2
import matplotlib.pyplot as plt
import numpy as np

#######################
img = cv2.imread("ejemplo2.jpg",0)
rows, colums = img.shape # filas # columnas
cv2.imshow("hist",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#A)
def histograma():
    img2 = cv2.calcHist([img], [0], None, [256], [0, 256])  # calcula histograma
    plt.xlabel('Gray Level') #editamos etiquetas para los ejes x e y
    plt.ylabel('Pixel Count')
    plt.plot(img2)  # monto la gráfica
    plt.show() #la mostramos
    



histograma()