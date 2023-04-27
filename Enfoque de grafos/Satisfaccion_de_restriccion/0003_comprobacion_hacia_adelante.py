# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:00:00 2023

@author: 6E1
"""

import numpy as np
# Comprobación hacia adelante / forward checking
# Matriz de adyacencia que representa el mapa
# Cada fila representa una región y cada columna indica si hay una 
# frontera entre esa región y la región correspondiente
# La diagonal principal se establece en 0 para evitar contar una región 
# como adyacente a sí misma
# Se crea una matriz de adyacencia de 7x7
# Las letras representan las regiones y las filas y columnas representan 
# si hay una frontera entre las regiones correspondientes
adyacencia = np.array([
    [0, 1, 0, 1, 0, 0, 0],  #A
    [1, 0, 1, 1, 0, 0, 0],  #B
    [0, 1, 0, 0, 0, 1, 0],  #C
    [1, 1, 0, 0, 1, 0, 1],  #D
    [0, 0, 0, 1, 0, 1, 1],  #E
    [0, 0, 1, 0, 1, 0, 1],  #F
    [0, 0, 0, 1, 1, 1, 0]   #G
])  #A  B  C  D  E  F  G

# Se establece el número de regiones en el mapa
num_regiones = adyacencia.shape[0]

# Se definen los colores disponibles para colorear las regiones
colores = ['Rojo', 'Azul', 'Verde', 'Amarillo']

# Se define la función de "forward checking" para encontrar una solución de coloreo
def forward_checking(coloring, zona_incolora):
    # Si no quedan zonas sin colorear, se ha encontrado una solución
    if not zona_incolora:
        return True
    # Se selecciona la siguiente zona sin colorear para intentar pintarla
    # con cada color disponible
    region = zona_incolora[0]
    for color in colores:
        # Si el color actual es consistente con los colores de las regiones
        # adyacentes, se colorea la región actual
        if is_value_consistent(region, color, coloring):
            coloring[region] = color
            # Se crea una nueva lista de regiones sin colorear, sin la región actual
            new_uncolored_regions = [r for r in zona_incolora if r != region]
            # Se llama recursivamente a la función "forward_checking" con la 
            # nueva configuración de coloreo y las regiones sin colorear
            # Si se encuentra una solución, se retorna "True"
            if forward_checking(coloring, new_uncolored_regions):
                return True
            # Si no se encuentra una solución, se vuelve a dejar la región sin colorear
            coloring[region] = None
    # Si no se encontró una solución con ninguno de los colores, se retorna "False"
    return False
# Esta función comprueba si el color asignado a una región es consistente con
# los colores asignados a las regiones adyacentes.
# Recibe como entrada la región, el color a asignar y la asignación de colores
# actual (coloring).
def is_value_consistent(region, color, coloring):
    # Se itera a través de las regiones adyacentes a la región dada.
    # Se utiliza la matriz de adyacencia para determinar si hay una frontera
    # entre la región dada y cada región adyacente.
    # Si hay una frontera y la región adyacente ya tiene asignado el color a
    # asignar, entonces el color no es consistente.
    for i, adyacente in enumerate(adyacencia[region]):
        if adyacente == 1 and coloring[i] == color:
            return False
    # Si se han comprobado todas las regiones adyacentes y no se ha encontrado
    # ninguna que tenga el color a asignar, entonces el color es consistente.
    return True

# Se crea una lista con el valor None (sin color asignado) para cada una de las
# regiones del mapa
coloring = [None] * num_regiones

# Se llama a la función forward_checking con el coloring inicial y una lista de 
# regiones sin color asignado
# Si se encuentra una solución, la función devuelve True y se imprime la
# asignación de colores para cada región
# En caso contrario, se imprime un mensaje indicando que no se encontró solución.
if forward_checking(coloring, list(range(num_regiones))):
    print("Solución encontrada:")
    for i, color in enumerate(coloring):
        print(f"Región {i+1}: {color}")
else:
    print("No se encontró solución.")
