# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:38:56 2023

@author: Alberto Aguiar
"""

import nltk

# Definir una gramática CFG
gramatica = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'el' | 'un'
    N -> 'perro' | 'gato'
    V -> 'persigue' | 'salta'
""")

# Crear un analizador de la gramática CFG
analizador = nltk.ChartParser(gramatica)

# Frase de entrada para analizar
frase = "el perro persigue un gato"

# Tokenizar la frase en una lista de palabras
palabras = nltk.word_tokenize(frase)

# Analizar la frase utilizando el analizador de la gramática
for arbol in analizador.parse(palabras):
    print(arbol)
    arbol.pretty_print()
