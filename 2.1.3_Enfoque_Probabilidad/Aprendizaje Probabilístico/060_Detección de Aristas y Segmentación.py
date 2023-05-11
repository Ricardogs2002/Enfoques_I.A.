import cv2
#import numpy as np

def do_canny(image, low_threshold, high_threshold):
    """
    Aplica la detección de bordes de Canny a una imagen con 
    los umbrales especificados.
    """
    return cv2.Canny(image, low_threshold, high_threshold)

def on_trackbar(val):
    """
    Callback para el evento onChange del trackbar. Actualiza 
    los umbrales de la detección de bordes de Canny.
    """
    low_threshold = cv2.getTrackbarPos('low_threshold', 'Canny')
    high_threshold = cv2.getTrackbarPos('high_threshold', 'Canny')
    canny = do_canny(img, low_threshold, high_threshold)
    cv2.imshow('Canny', canny)

# Carga la imagen
img = cv2.imread('manos2.jpg', cv2.IMREAD_GRAYSCALE)

# Crea la ventana y el trackbar
cv2.namedWindow('Canny')
cv2.createTrackbar('low_threshold', 'Canny', 0, 255, on_trackbar)
cv2.createTrackbar('high_threshold', 'Canny', 0, 255, on_trackbar)

# Aplica Canny por primera vez
on_trackbar(0)

# Espera a que se presione ESC para cerrar la ventana
while True:
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()
