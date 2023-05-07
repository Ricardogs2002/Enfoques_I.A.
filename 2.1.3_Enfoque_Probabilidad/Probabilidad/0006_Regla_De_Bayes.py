"""
Created on Thu May 4 2023

@author: Adan Alvarez.
"""

# Probabilidad de ser hombre
p_hombre = 0.4

# Probabilidad de ser mujer
p_mujer = 0.6

# Probabilidad de hacer ejercicio dado que es hombre
p_ejercicio_dado_hombre = 0.8

# Probabilidad de hacer ejercicio dado que es mujer
p_ejercicio_dado_mujer = 0.5

# Probabilidad de hacer ejercicio (denominador de la fórmula de Bayes)
p_ejercicio = p_hombre * p_ejercicio_dado_hombre + p_mujer * p_ejercicio_dado_mujer

# Probabilidad de ser hombre dado que hace ejercicio (numerador de la fórmula de Bayes)
p_hombre_dado_ejercicio = p_hombre * p_ejercicio_dado_hombre / p_ejercicio

print("\n\nProbabilidad de que una persona alegida sea hombre y haga ejercicio dado los siguientes datos")
print("\n            Ecuacion de Bayes: P(A | B) = (P(B | A) * P(A)) / P(B)\n\n")

print("                                    Genero                        ")
print("                               /             \                    ")
print("                            H 40%             M 60%               ")
print("                             /                  \                 ")
print("                        Ejercicio?           Ejercicio?           ")
print("                          /    \               /    \             ")
print("                        Sí      No            Si      No          ")
print("                        /         \          /         \          ")
print("                      80%         20%       50%        50%        ")

#El ":.2f" especifica que se deben mostrar dos decimales.
print(f"\n\nLa probabilidad de que la persona seleccionada al azar sea un hombre y que haga ejercicio es {p_hombre_dado_ejercicio*100:.2f}%")
