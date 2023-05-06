# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 08:09:59 2023
@author: 6E1
"""
import numpy as np

# Función que determina si un animal tiene alas y pico (es un ave)
def ave(animal):
    return np.logical_and(animal["alas"], animal["pico"])

# Función que determina si un animal tiene aletas y vive en el agua (es un pez)
def pez(animal):
    return np.logical_and(animal["aletas"], animal["agua"])

# Función que determina si un animal no es un ave ni un pez (es un mamífero)
def mamifero(animal):
    return not ave(animal) and not pez(animal)

# Función que determina si un animal es un ave por defecto (asumiendo que es un mamífero si no hay evidencia en contrario)
def ave_por_defecto(animal):
    return np.logical_or(mamifero(animal), ave(animal))

# Creamos tres animales con diferentes características
Tucán = {"alas": True, "pico": True, "aletas": False, "agua": False}
Atún = {"alas": False, "pico": False, "aletas": True, "agua": True}
Ornitorrinco = {"alas": False, "pico": True, "aletas": False, "agua": True}

# Verificamos si cada animal es un ave, un pez o un mamífero por defecto
print("El tucán es un ave por defecto: ", ave_por_defecto(Tucán))
print("El atún es un pez por defecto: ", not ave_por_defecto(Atún))
print("El ornitorrinco es un mamífero por defecto: ", mamifero(Ornitorrinco))
