"""
Created on Sun May 7 2023

@author: Adan Alvarez
"""

import pygame
import math

# Inicialización de Pygame
pygame.init()

# Definición del tamaño de la ventana
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moviendo figura geométrica")

# Definición de variables, control de fotogramas
clock = pygame.time.Clock()

# Definición de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definición de la figura geométrica movil
rect = pygame.Rect(0, 0, 50, 50) #Tamaño
rect.center = (-50, 200) #Posicion

# Definición de la figura estática central
center_rect = pygame.Rect(175, 175, 50, 50)

# Bucle principal del programa
done = False
while not done:
    # Captura de eventos
    for event in pygame.event.get():   #    Condicional para cerrar el programa
        if event.type == pygame.QUIT:
            done = True

    # Movimiento de la figura geométrica
    if rect.right < center_rect.left:
        rect.move_ip(5, 0)               #A partir de la izquierda de la ventana mueve la figura a la derecha
    elif center_rect.colliderect(rect):  # Devuelve TRUE si los puntos se superponen
        rect.move_ip(0, -5)              # Mueve la figura hacia arriba cuando coliciona
    elif rect.right < size[0]:
        rect.move_ip(5, 0)               # Continua el recorrido hasta el final de la ventana

    # Dibujado de la pantalla
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, WHITE, center_rect)
    pygame.display.flip()

    # Control de FPS
    clock.tick(20)

# Cierre de Pygame
pygame.quit()

