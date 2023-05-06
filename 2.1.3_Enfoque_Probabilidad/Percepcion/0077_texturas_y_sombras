import cv2

# Cargar las imágenes de textura y sombra desde el archivo
img_textura = cv2.imread('textura.jpg')  # cargar la imagen de textura desde un archivo
img_sombra = cv2.imread('sombras.jpg')  # cargar la imagen de sombra desde un archivo

# Convertir a escala de grises para facilitar el procesamiento
gray_textura = cv2.cvtColor(img_textura, cv2.COLOR_BGR2GRAY)  # convertir la imagen de textura a escala de grises
gray_sombra = cv2.cvtColor(img_sombra, cv2.COLOR_BGR2GRAY)  # convertir la imagen de sombra a escala de grises

# Crear un kernel para suavizar la imagen y mejorar el resultado del filtro
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # crear un kernel para suavizar la imagen y mejorar el resultado del filtro

# Aplicar filtro de textura mediante operaciones morfológicas
texture = cv2.morphologyEx(gray_textura, cv2.MORPH_TOPHAT, kernel)  # aplicar filtro de textura mediante operaciones morfológicas

# Aplicar filtro de sombra mediante operaciones morfológicas
shadows = cv2.morphologyEx(gray_sombra, cv2.MORPH_GRADIENT, kernel)  # aplicar filtro de sombra mediante operaciones morfológicas

# Mostrar los resultados
cv2.imshow('Textura original', img_textura)  # mostrar la imagen de textura original
cv2.imshow('Textura con filtro', texture)  # mostrar la imagen de textura con el filtro aplicado
cv2.imshow('Sombra original', img_sombra)  # mostrar la imagen de sombra original
cv2.imshow('Sombra con filtro', shadows)  # mostrar la imagen de sombra con el filtro aplicado


cv2.waitKey(0) 
cv2.destroyAllWindows()  
