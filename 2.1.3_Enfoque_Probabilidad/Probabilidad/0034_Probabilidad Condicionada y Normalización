# Probabilidad condicionada
"""
La probabilidad condicionada es la probabilidad de que ocurra un evento A, dada cierta información o evidencia de que ha ocurrido otro evento B. 
Se denota como P(A|B), donde "P" representa la probabilidad y el símbolo "|" significa "dado que".
La probabilidad condicionada se calcula utilizando la fórmula:
P(A|B) = P(A and B) / P(B)
donde P(A and B) es la probabilidad de que ambos eventos A y B ocurran simultáneamente, y P(B) es la probabilidad de que ocurra el evento B.
"""
# Calcula la probabilidad de obtener un 6 al lanzar un dado de 6 caras, sabiendo que el resultado es un número par.

# número de caras del dado
n_caras = 6

# número de resultados pares
n_pares = n_caras // 2

# número de resultados que son 6 y pares
n_6_y_pares = 1

# probabilidad de obtener un número par
prob_pares = n_pares / n_caras

# probabilidad de obtener un 6 y un número par
prob_6_y_pares = n_6_y_pares / n_caras

# probabilidad de obtener un 6, dado que el resultado es un número par
prob_6_cond_pares = prob_6_y_pares / prob_pares

print("La probabilidad de obtener un 6, dado que el resultado es un número par, es:", prob_6_cond_pares)

# Normalización
"""
La probabilidad normalizada se refiere a la escala de las probabilidades de tal manera que su suma sea igual a 1. 
Esto se hace para que se puedan interpretar como probabilidades relativas,
donde la suma de todas las probabilidades es 1 y representa la totalidad de las posibles ocurrencias de los eventos.
"""
# Normaliza una lista de probabilidades para que sumen 1.

# lista de probabilidades
probs = [0.2, 0.3, 0.1, 0.4]

# suma de las probabilidades
sum_probs = sum(probs)

# normalización de las probabilidades
norm_probs = [p / sum_probs for p in probs]

print("Lista de probabilidades original:", probs)
print("Lista de probabilidades normalizada:", norm_probs)
