# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:08:47 2023

@author: Alberto Aguiar
"""

import numpy as np

# Parámetros de la distribución normal
media = 0  # Media de la distribución
desviacion = 1  # Desviación estándar de la distribución
tamano_muestra = 10  # Tamaño de la muestra

# Generación de la muestra utilizando la distribución normal
muestra = np.random.normal(media, desviacion, tamano_muestra)

# Imprimir la muestra generada
print("Muestra generada:")
print(muestra)
