# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:03:14 2023

@author: Alberto Aguiar
"""


from random import random

# Definir una función para generar una muestra aleatoria
def generar_muestra():
    if random() < 0.7:
        return 'A'
    else:
        return 'B'

# Generar una muestra
muestra = [generar_muestra() for _ in range(1000)]

# Calcular la probabilidad de obtener 'A' en la muestra
probabilidad_A = muestra.count('A') / len(muestra)
print("Probabilidad de obtener 'A':", probabilidad_A)
