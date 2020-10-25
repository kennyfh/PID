import cv2 # importamos OpenCV
import numpy as np


"""
Carga una imagen (fotográfica) a color (que tenga mucho contenido de azul, aunque también
otros colores).
"""
img = cv2.imread('ejemplo2.jpg') #Lee la imagen
# cv2.imshow('Prueba', img) #Muestra la imagen
# cv2.waitKey(0) # Espera 
# cv2.destroyAllWindows() # Destruya todas las ventanas que se han abierto

"""
A) Separa los tres canales RGB que componen la imagen
y visualiza cada uno por separado como imágenes 
en escala de grises.
"""
b,g,r = cv2.split(img) # Dividimos la imagen en los tres canales

cv2.imshow('B',b)
cv2.waitKey(0)
"""
cv2.waitkey(x) es una función de enlace de teclado. Su argumento es el tiempo en milisegundos. La función espera milisegundos especificados para cualquier evento de teclado. 
Si presiona cualquier tecla en ese tiempo, el programa continúa. Si se pasa 0, espera indefinidamente una pulsación de tecla.
"""
cv2.imshow('G',g)
cv2.waitKey(0)

cv2.imshow('R',r)
cv2.waitKey(0)

cv2.destroyAllWindows()

"""
Pasa la imagen a color a escala de grises de dos formas: 
usando la fórmula de Y en el modelo YIQ y la de I en el modelo HSI. Explica a qué se deben las diferencias.
"""

## FORMULA Y

y = 0.299 * r + 0.587 * g + 0.114*b
y = y.astype(np.uint8) ##
# print(f"La y es {y}")

cv2.imshow('YIQ', y)
cv2.waitKey(0)
cv2.destroyAllWindows()

## FORMULA I

i = 1 / 3* (r+g+b)
i = i.astype(np.uint8)
cv2.imshow('HSI', i)
cv2.waitKey(0)
cv2.destroyAllWindows()

