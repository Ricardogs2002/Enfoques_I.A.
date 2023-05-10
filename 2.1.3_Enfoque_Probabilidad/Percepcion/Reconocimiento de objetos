import cv2

# Cargar el clasificador Haar pre-entrenado para detectar rostros
clasificador_rostros = cv2.CascadeClassifier('ruta_del_clasificador.xml')

# Cargar la imagen de entrada
imagen = cv2.imread('ruta_de_la_imagen')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar rostros en la imagen utilizando el clasificador Haar
rostros = clasificador_rostros.detectMultiScale(imagen_gris, scaleFactor=1.1, minNeighbors=5)

# Dibujar rectángulos alrededor de los rostros detectados en la imagen
for (x, y, w, h) in rostros:
    cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar la imagen con los rostros detectados
cv2.imshow('Imagen con rostros detectados', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
El reconocimiento de objetos en la inteligencia artificial 
es una técnica que permite que una máquina sea capaz de identificar y 
clasificar objetos en imágenes o videos. Esta técnica es utilizada 
en una amplia variedad de aplicaciones, desde la automatización 
industrial hasta la seguridad y vigilancia.
"""
