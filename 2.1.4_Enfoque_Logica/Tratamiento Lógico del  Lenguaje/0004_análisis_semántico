#< -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 08:09:59 2023
@author: 6E1
"""

import numpy as np

# Creamos nuestro diccionario de términos
vocabulario = ['casa', 'colina', 'verde', 'feliz', 'triste']

# Creamos un arreglo de ceros con una longitud igual al tamaño de nuestro diccionario
vector_oracion = np.zeros(len(vocabulario))

# Definimos la oración que queremos analizar
oracion = 'La casa verde me hace feliz'

# Iteramos sobre cada término de nuestra oración
for termino in oracion.split():
    # Si el término está en nuestro diccionario, aumentamos su frecuencia en nuestro vector
    if termino in vocabulario:
        vector_oracion[vocabulario.index(termino)] += 1
# Definimos un vector de pesos que representa la polaridad de cada término en nuestro diccionario
pesos = np.array([0.5, -0.5, 0.75, 1.0, -0.75])

# Calculamos el producto punto entre nuestro vector de oración y nuestros pesos
sentimiento = np.dot(vector_oracion, pesos)

if sentimiento>0:
  print("La oración tiene polaridad positiva de:",sentimiento)
elif sentimiento<0:
  print("La oración tiene polaridad negativa de:",sentimiento)
else:
  print("La oración tiene polaridad neutra")
