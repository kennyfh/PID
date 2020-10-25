import cv2
import numpy as np

"""
Cargados imágenes en escala de grises de 256 niveles de gris.
Realiza una “superposición” de ambas imágenes sumándolas.
 Al sumar los niveles de gris, teóricamente se obtendrían valores entre 0 y 510. Averiguacómo está tratando el software usado el rango de valores de salida. Es decir, ¿se han truncado todos los valores mayores de 255? ¿Se han rescalado? A la vista de las respuestas anteriores ¿se ha perdido mucha información? Si es así, ¿cómo se podría mejorar el resultado?

"""
img = cv2.imread('ejemplo3.jpg',0) #960x1920
img2 = cv2.imread('ejemplo.jpg',0) #1080x1920
img2 = cv2.resize(img2, (1920,960))

cv2.imshow('foto1', img)
cv2.waitKey(0)
cv2.imshow('foto2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = img/2
img2 = img2/2
print(f"La imagen 1 es {img}")
print(f"La imagen 2 es {img2}")


superposicion = np.add(img,img2) ## Por el principio de adición de matrices, ambas matrices tienen que tener misma dimensión
superposicion = superposicion.astype(np.uint8) #Convierte la matriz con decimales a numeros enteros para trabajar mejor
print(f"La matriz superposicion es {superposicion}")
print(superposicion)
cv2.imshow('superposicion', superposicion)
cv2.waitKey(0)
cv2.destroyAllWindows()


