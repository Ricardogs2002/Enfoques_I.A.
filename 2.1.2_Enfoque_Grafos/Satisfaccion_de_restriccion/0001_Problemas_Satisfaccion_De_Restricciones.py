

import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import random
import numpy as np

# Definir mapa de países adyacentes en un diccionario
mapa = {
    'Mexico': ['USA', 'Guatemala', 'Belize'],
    'USA': ['Canada', 'Mexico'],
    'Canada': ['USA'],
    'Guatemala': ['Mexico', 'Belize', 'El Salvador', 'Honduras'],
    'Belize': ['Mexico', 'Guatemala'],
    'El Salvador': ['Guatemala', 'Honduras'],
    'Honduras': ['Guatemala', 'El Salvador', 'Nicaragua'],
    'Nicaragua': ['Honduras', 'Costa Rica'],
}

# Definir colores disponibles en una lista de python
colores = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

# Inicializar asignacion de colores en un diccionario vacio
asignaciones = {}

# Colorear cada país
for pais in mapa:
    # Crea un conjunto de pythonpara los colores prohibidos
    prohibidos = set()

    for vecino in mapa[pais]:
        # Comprueba si la region adyacente ya tiene el color, si es asi, lo agrega a prohibidos
        if vecino in asignaciones:
            prohibidos.add(asignaciones[vecino])

    # Se crea un diccionario de contadores de colores inicializados en cero y aumenta cada vez que se utilice ese color
    conteos = {c: 0 for c in colores}
    for color in asignaciones.values():
        #Si el color esta en uso, incrementa su contador
        conteos[color] += 1
    #Crea otra lista para ordenar los colores de menor a mayor uso
    opciones = sorted(colores, key=lambda c: conteos[c])
    color = None
    for c in opciones:
        if c not in prohibidos:
            #recorre nuevamente todos los colores y si no esta en uso, lo asigna a la variable colores
            color = c
            break

    #Si no encuentra el color crea uno nuevo aleatoriamente
    if color is None:
        color = random.choice(colores)
    #Asigna el color a la region
    asignaciones[pais] = color

    # Mostrar asignación de colores actual en la terminal
    print(pais + ': ' + color)

# Crea una figura y un par de ejes cartesianos
fig, ax = plt.subplots()
for pais, xy in zip(mapa.keys(), [(1, 1), (3, 1), (5, 1), (2, 2), (4, 2), (3, 3), (2, 4), (4, 4)]): #Asigna las cordenadas de cada uno de los hexagonos
    # Obtiene el color asignado en el diccionario para cada pais
    color = asignaciones[pais]
    # crea un hexágono regular con las coordenadas xy, con seis vértices y un radio que lo hace adecuado para encajar perfectamente con sus vecinos.
    # El borde del hexágono está dibujado en negro y el interior se llena con el color asignado.
    hexagono = RegularPolygon(xy, numVertices=6, radius=1/np.sqrt(3), ec='black', fc=color)
    #agrega el hexágono al gráfico.
    ax.add_patch(hexagono)
    #Agrega el texto al centro del hexagono con las cordenadas guardadas anteriormente en la variable xy como los centros
    # ha y va son parámetros de la función annotate()
    ax.annotate(pais, xy, ha='center', va='center')

#establece que los ejes x e y tengan la misma escala
plt.axis('scaled')
plt.show()  # Mostrar ventana hasta que el usuario la cierre
